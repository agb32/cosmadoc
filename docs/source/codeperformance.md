# Code performance

Optimising and profiling HPC codes is key to performance, and getting the most science per kWhr.

COSMA includes many tools to help with this, and regular training activities related to these.

The [SHAREing project](https://shareing-dri.github.io/assessment) also offers a code assessment service allowing users to submit their codes for assessment, so that potential easy performance gains can be identified.

Please fill out the form and submit your code!

The following tools are available on COSMA for profiling/benchmarking/etc.  

Here is a summarized table for performance tools:

| Category | Tool | Description | Documentation | Tutorial |
|---|---|---|---|---|
| Compiler Analysis | **Intel Advisor** | Analyses vectorisation, threading design.| [Product docs](https://www.intel.com/content/www/us/en/developer/tools/oneapi/advisor.html) | [Get Started guide](https://www.intel.com/content/www/us/en/docs/advisor/get-started-guide/current/overview.html) |
| Compiler Analysis | **Intel VTune Profiler** | Hotspot analysis, memory access patterns, threading efficiency and I/O. | [Product docs](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html) | [Get Started guide](https://www.intel.com/content/www/us/en/docs/vtune-profiler/get-started-guide/current/overview.html) |
| Compiler Analysis | **AMD uProf** | AMD's profiling suite. | [Product page](https://www.amd.com/en/developer/uprof.html) | [User Guide & docs](https://www.amd.com/en/developer/uprof.html#documentation) |
| Compiler  Analysis | **LIKWID** | Command-line tools (`likwid-perfctr`, `likwid-topology`, `likwid-pin`, etc.) for reading hardware performance counters and controlling thread/process affinity. | [GitHub repository](https://github.com/RRZE-HPC/likwid) | [Wiki: tutorials & examples](https://github.com/RRZE-HPC/likwid/wiki) |
| Compiler Analysis | **gperftools** | Google's lightweight performance analysis tool. | [GitHub repository](https://github.com/gperftools/gperftools) | [CPU Profiler tutorial](https://gperftools.github.io/gperftools/cpuprofile.html) |
| Compiler Analysis | **OProfile** | Sampling profiler for Linux that can profile code. | [Project site](https://oprofile.sourceforge.io/) | [Documentation & guides](https://oprofile.sourceforge.io/docs/) |
| Debugging and Correctness | **Linaro Forge (Allinea)** | The DDT parallel debugger and MAP profiler for MPI/OpenMP/CUDA codes. | [Product site](https://www.linaroforge.com/) | [Documentation & tutorials](https://www.linaroforge.com/documentation/) |
| Debugging and Correctness | **Intel Inspector** | Dynamic analysis tool that detects memory errors and threading errors. | [Product docs](https://www.intel.com/content/www/us/en/developer/tools/oneapi/inspector.html) | [Get Started guide](https://www.intel.com/content/www/us/en/docs/inspector/get-started-guide/current/overview.html) |
| Debugging and Correctness | **Valgrind** | Memcheck tool finds memory errors while Cachegrind/Callgrind profile cache and branch behaviour. | [Project site](https://valgrind.org/) | [Quick Start guide](https://valgrind.org/docs/manual/quick-start.html) |
| Debugging and Correctness | **MUST** | Runtime correctness checker for MPI applications, catching deadlocks, datatype mismatches, resource leaks. | [VI-HPS tool page](https://www.vi-hps.org/tools/must.html) | [VI-HPS hands-on course material](https://www.vi-hps.org/training/course-material/index.html) |
| Tracing and Visualisation | **Score-P** | Generates the profiles and OTF2 traces by tools like Vampir and Scalasca. | [Project page](https://www.vi-hps.org/projects/score-p) | [VI-HPS hands-on course material](https://www.vi-hps.org/training/course-material/index.html) |
| Tracing and Visualisation | **Vampir** | Interactive trace-visualisation tool for exploring event traces at any level of detail. | [Product site](https://vampir.eu/) | [User Manual (tutorial chapters)](https://tu-dresden.de/zih/forschung/ressourcen/dateien/projekte/vampir/dateien/Vampir-User-Manual.pdf?lang=en) |
| I/O Profiling | **Darshan** | I/O characterisation tool that captures POSIX, MPI-IO and HDF5 I/O behaviours. | [Project site](https://www.mcs.anl.gov/research/projects/darshan/) | [Runtime & usage guide](https://www.mcs.anl.gov/research/projects/darshan/docs/darshan3-runtime.html) |

## Advisor
 
The Intel Advisor tool analyses vectorization.

## Allinea

The Linaro (was Allinea, was ARM) FORGE and MAP tools. 

## Darshan

## gperftools

## Inspector

The Intel Inspector tool.

## Likwid

## Must

## Oprofile

## Scorep

## Uprof

## Valgrind

## Vampir

## Vtune

The Intel Vtune tool
