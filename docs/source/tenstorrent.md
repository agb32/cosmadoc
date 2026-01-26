# Tenstorrent QuietBox RISC-V Blackhole node

We have a single Tenstorrent QuietBox node with 4x Blackhole cards.

The host system is a single AMD 8124P 16-core processor with 512GB RAM.

It is a highly capable system for AI inferencing.

## Accessing the Tenstorrent system

To access this system you need to join the do023 project, and then `ssh tenstorrent`.

## Usage of the Tenstorrent system

Most tenstorrent commands start with tt.  To access many of these, you will need to `source /opt/venv/tenstorrent/bin/activate` which makes commands like `tt-smi` available.

To install an updated software stack as a user, you may be able to follow the instructions here (though this may require root access):
[https://docs.tenstorrent.com/getting-started/README.html](https://docs.tenstorrent.com/getting-started/README.html)

Please give any feedback.

