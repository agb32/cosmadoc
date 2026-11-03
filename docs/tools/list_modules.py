#!/usr/bin/env python3
"""Generate the list of COSMA modules as a Markdown page.

Run on a COSMA login node from a clean shell, and commit the result:

    module purge
    python3 docs/tools/list_modules.py > docs/source/modulelist.md

As well as listing the modules, the script finds which compiler and MPI
modules each library can be used with.  It reads the build directories that
the modulefiles use, then loads each combination to check that it works, so
only combinations that load are shown.  This takes about a minute.
"""
import collections
import concurrent.futures
import datetime
import glob
import html
import os
import re
import subprocess

MODULEFILES = "/cosma/local/Modules/modulefiles"
SECTIONS = {
    "compilers": "Compilers",
    "mpi": "MPI",
    "libraries": "Libraries",
    "tools": "Tools",
    "MAD": "Large memory node tools",
}
# The second file sets the COSMA module path, in case this runs outside a login shell.
INIT = ("source /etc/profile.d/modules.sh; "
        "source /etc/profile.d/cosma-local-modules.sh >/dev/null 2>&1; "
        "module purge >/dev/null 2>&1; ")
TOKEN = re.compile(r"^(?P<name>[^\s(<]+)(?:\((?P<tags>[^)]*)\))?")
# Build directory names, as used by module_utils.tcl on COSMA.
COMP_DIR = re.compile(r"^([a-zA-Z]+)_([0-9.a-z-]+)$")
MPI_DIR = re.compile(r"^([a-zA-Z]+)_([0-9.a-z-]+)_([a-zA-Z_0-9]+mpi)_([0-9.a-z-]+)$")
ONEAPI = ["compiler-rt", "tbb", "compiler"]


def run(script):
    return subprocess.run(["bash", "-c", INIT + script], capture_output=True,
                          text=True, check=False)


def module_avail(extra=""):
    """Return {section: {name: (versions, default)}} from `module -t avail`."""
    out = run(f"{extra}module -t avail 2>&1").stdout
    data = collections.defaultdict(dict)
    section = None
    for line in out.splitlines():
        if line.endswith(":") and line.startswith("/"):
            section = line[:-1].rstrip("/").rsplit("/", 1)[-1]
            continue
        match = TOKEN.match(line.strip())
        if not match or section is None:
            continue
        path = match.group("name").split("/")
        name = path[0]
        version = "/".join(path[1:])
        versions, default = data[section].get(name, ([], None))
        if version:
            versions.append(version)
        if "default" in (match.group("tags") or ""):
            default = version
        data[section][name] = (versions, default)
    return data


def compiler_options(comp, version):
    """Possible commands to load a compiler, for a build directory's compiler."""
    module = f"{comp}_comp/{version}"
    if comp == "intel":
        return [[module], [module] + ONEAPI]
    return [[module]]


def mpi_options(kind, version, comp, comp_version):
    """Possible commands to load an MPI, for a build directory's MPI."""
    name = "openmpi" if kind == "ompi" else kind
    options = [[f"{name}/{version}"]]
    if kind == "intel_mpi" and comp == "intel" and version == comp_version:
        options.insert(0, ["mpi"])
    return options


def parse_modulefiles(sections):
    """Find modules that need a compiler or an MPI, and their build directories."""
    needs = {}
    for section in sections:
        for path in sorted(glob.glob(f"{MODULEFILES}/{section}/*/*")):
            name, version = path.split("/")[-2:]
            if version.endswith("~") or version.startswith("."):
                continue
            try:
                text = open(path, errors="replace").read()
            except OSError:
                continue
            if "CheckCompiler" not in text:
                continue
            match = re.search(r"set\s+basedir\s+(\S+)", text)
            if not match:
                continue
            basedir = match.group(1).replace("${name}", name).replace("$name", name)
            builds = [os.path.basename(os.path.dirname(p))
                      for p in glob.glob(os.path.join(basedir, "*", version))]
            needs[(name, version)] = ("CheckMPI" in text, builds)
    return needs


def candidates(name, version, uses_mpi, builds):
    """Yield (compiler, mpi, commands) to try for each build directory."""
    for build in sorted(builds):
        match = (MPI_DIR if uses_mpi else COMP_DIR).match(build)
        if not match:
            continue
        comp, comp_version = match.group(1), match.group(2)
        comp_cmds = compiler_options(comp, comp_version)
        if uses_mpi:
            kind, mpi_version = match.group(3), match.group(4)
            mpi_cmds = mpi_options(kind, mpi_version, comp, comp_version)
        else:
            mpi_cmds = [[]]
        tries = [c + m + [f"{name}/{version}"] for c in comp_cmds for m in mpi_cmds]
        yield build, tries


def works(commands, target):
    """True if every module in the command loads, including the target."""
    script = " ".join(f"module load {c} >/dev/null 2>&1;" for c in commands)
    loaded = " && ".join(f"module is-loaded {c}" for c in commands)
    return run(f"{script} {loaded}").returncode == 0


def check(item):
    (name, version), build, tries = item
    for commands in tries:
        if works(commands, f"{name}/{version}"):
            return name, version, build, commands
    return name, version, build, None


def find_dependencies(sections):
    """Return {name: {version: [command lists]}} for combinations that load."""
    jobs = []
    needs_mpi = collections.defaultdict(bool)
    for (name, version), (uses_mpi, builds) in parse_modulefiles(sections).items():
        needs_mpi[name] |= uses_mpi
        for build, tries in candidates(name, version, uses_mpi, builds):
            jobs.append(((name, version), build, tries))
    found = collections.defaultdict(lambda: collections.defaultdict(list))
    failed = collections.Counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        for name, version, _, commands in pool.map(check, jobs):
            if commands:
                found[name][version].append(commands)
            else:
                failed[name] += 1
    return found, failed, needs_mpi


def version_key(text):
    return [int(p) if p.isdigit() else p for p in re.split(r"(\d+)", text)]


def write_table(mods, deps, needs_mpi):
    print("| Module | Default | Other versions | Needs |")
    print("| ------ | ------- | -------------- | ----- |")
    for name in sorted(mods, key=str.lower):
        versions, default = mods[name]
        others = [v for v in versions if v != default]
        shown = ", ".join(others[-6:])
        if len(others) > 6:
            shown = f"{len(others) - 6} older, then {shown}"
        need = ""
        if name in deps:
            label = "Compiler and MPI" if needs_mpi[name] else "Compiler"
            need = f'<a href="#dep-{name}">{label}</a>'
        print(f"| `{name}` | {default or ''} | {shown} | {need} |")
    print()


def describe(commands):
    """Split a working command list into compiler, MPI and the full command."""
    target = commands[-1]
    rest = commands[:-1]
    comp = [c for c in rest if c.endswith("_comp") or "_comp/" in c]
    mpi = [c for c in rest if c not in comp and c not in ONEAPI]
    mpi_text = "Intel MPI (`mpi`)" if mpi == ["mpi"] else ", ".join(mpi)
    return (comp[0] if comp else ""), mpi_text, "module load " + " ".join(commands), target


def write_dependencies(deps, failed):
    print("## What to load first\n")
    print("Many libraries can only be loaded after a compiler, and some also need an MPI "
          "module.  Choose a version below to see the combinations that work, and the "
          "command that loads them.  Each combination was tested when this page was "
          "generated.\n")
    for name in sorted(deps, key=str.lower):
        versions = deps[name]
        total = sum(len(v) for v in versions.values())
        print(f'<details id="dep-{name}"><summary><code>{html.escape(name)}</code>: '
              f'{len(versions)} versions, {total} combinations</summary>\n')
        print('<table class="docutils"><thead><tr><th>Version</th><th>Compiler</th><th>MPI</th>'
              "<th>Command</th></tr></thead><tbody>")
        for version in sorted(versions, key=version_key, reverse=True):
            rows = sorted(versions[version], key=lambda c: version_key(" ".join(c)), reverse=True)
            for i, commands in enumerate(rows):
                comp, mpi, command, _ = describe(commands)
                cell = (f'<td rowspan="{len(rows)}"><code>{html.escape(version)}</code></td>'
                        if i == 0 else "")
                print(f"<tr>{cell}<td><code>{html.escape(comp)}</code></td>"
                      f"<td>{html.escape(mpi).replace('`mpi`', '<code>mpi</code>')}</td>"
                      f"<td><code>{html.escape(command)}</code></td></tr>")
        print("</tbody></table>\n")
        if failed.get(name):
            print(f"<p>{failed[name]} older builds could not be loaded with the current "
                  "modules, so they are not shown.</p>\n")
        print("</details>\n")


def main():
    today = datetime.date.today().strftime("%B %Y")
    data = module_avail()
    old = module_avail("module load old-modules >/dev/null 2>&1; ")
    deps, failed, needs_mpi = find_dependencies(SECTIONS)
    total = sum(len(v[0]) or 1 for s in data.values() for v in s.values())
    print("# List of modules\n")
    print(f"This list was generated in {today} and shows {total} modules on the "
          "login nodes.  It can go out of date, so run `module avail` for the "
          "current list, or `module avail NAME` to search.  See "
          "[modules](modules.md) for how to use them.\n")
    print("Where no default is shown, `module load NAME` loads the last version "
          "listed.  The Needs column shows modules that must be loaded after a "
          "compiler or MPI module: follow the link to see which ones.\n")
    print("The list is generated by `docs/tools/list_modules.py`.\n")
    for key, title in SECTIONS.items():
        if key in data:
            print(f"## {title}\n")
            write_table(data[key], deps, needs_mpi)
    write_dependencies(deps, failed)
    extra = sorted({n for s in old.values() for n in s}
                   - {n for s in data.values() for n in s}, key=str.lower)
    print("## Older modules\n")
    print("Retired modules can be used by first running `module load old-modules`, "
          "though they may not work.  This also adds older versions of the modules above, "
          "and these modules:\n")
    print(", ".join(f"`{n}`" for n in extra) + "\n")


if __name__ == "__main__":
    main()
