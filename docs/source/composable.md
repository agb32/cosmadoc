# Composability

COSMA has two composable systems to allow experimentation with composability, i.e. the ability to define server components within software.

## Liqid system

A Liqid system installed in 2021 has 4 nodes (including a login node) to which both GPU and RAM can be composed upon demand (i.e. a request to cosma-support).

The GPUs are NVIDIA A100-40GB.  There are 3 GPUs which can be configured between the nodes.

To make use of the composed RAM, prefix your commands with `mm`.  For example, `free -h` will show you there is 2TB RAM on the login8b node, while `mm free -h` gives access to the additional composed RAM, and so (depending on configuration) will usually show you that there is 4.5TB RAM available.

## CerIO system

A [CerIO](cerio.md) system installed in 2024 has 8 nodes which share 8 GPUs, allowing servers with up to 8 GPUs to be configured.  Follow the [instructions](cerio.md) to use this system.
