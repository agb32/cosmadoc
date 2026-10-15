# Code performance

Optimising and profiling HPC codes is key to performance, and getting the most science per kWhr.

COSMA includes many tools to help with this, and regular training activities related to these.

The [SHAREing project](https://shareing-dri.github.io/assessment) also offers a code assessment service allowing users to submit their codes for assessment, so that potential easy performance gains can be identified.

Please fill out the form and submit your code!

The following tools are available on COSMA for profiling/benchmarking/etc.  

Here is a summarized table for performance tools:

| Tutorial | Description |
|---|---|
| [Intel Advisor](https://www.intel.com/content/www/us/en/docs/advisor/get-started-guide/current/overview.html) | Analyses vectorisation, threading design. |
| [Intel VTune Profiler](https://www.intel.com/content/www/us/en/docs/vtune-profiler/get-started-guide/current/overview.html) | Hotspot analysis, memory access patterns, threading efficiency and I/O. |
| [AMD uProf](https://www.amd.com/en/developer/uprof.html#documentation) | AMD's profiling suite. |
| [LIKWID](https://github.com/RRZE-HPC/likwid/wiki) | Command-line tools (`likwid-perfctr`, `likwid-topology`, `likwid-pin`, etc.) for reading hardware performance counters and controlling thread/process affinity. |
| [gperftools](https://gperftools.github.io/gperftools/cpuprofile.html) | Google's lightweight performance analysis tool. |
| [OProfile](https://oprofile.sourceforge.io/docs/) | Sampling profiler for Linux that can profile code. |
| [Linaro Forge (Allinea)](https://www.linaroforge.com/documentation/) | The DDT parallel debugger and MAP profiler for MPI/OpenMP/CUDA codes. |
| [Intel Inspector](https://www.intel.com/content/www/us/en/docs/inspector/get-started-guide/current/overview.html) | Dynamic analysis tool that detects memory errors and threading errors. |
| [Valgrind](https://valgrind.org/docs/manual/quick-start.html) | Memcheck tool finds memory errors while Cachegrind/Callgrind profile cache and branch behaviour. |
| [MUST](https://www.vi-hps.org/training/course-material/index.html) | Runtime correctness checker for MPI applications, catching deadlocks, datatype mismatches, resource leaks. |
| [Score-P](https://www.vi-hps.org/training/course-material/index.html) | Generates the profiles and OTF2 traces used by tools like Vampir and Scalasca. |
| [Vampir](https://tu-dresden.de/zih/forschung/ressourcen/dateien/projekte/vampir/dateien/Vampir-User-Manual.pdf?lang=en) | Interactive trace-visualisation tool for exploring event traces at any level of detail. |
| [Darshan](https://www.mcs.anl.gov/research/projects/darshan/docs/darshan3-runtime.html) | I/O characterisation tool that captures POSIX, MPI-IO and HDF5 I/O behaviours. |

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
