# tmux Terminal multiplexer 

tmux is a terminal multiplexer. It lets you keep sessions running on COSMA
after you disconnect, and split one terminal into several panes. 

Here are some basic tmux commands to allow you to configure your work environment while you are connecting on COSMA:

    tmux new -s work       # start a named session
    tmux ls                # list sessions
    tmux attach -t work    # reattach after reconnecting
    tmux kill-session -t work

Please note that login nodes may be rebooted, which kills tmux. Check which login node you
were on (`hostname`) before reattaching.

There is a [tmuxsheet](https://tmuxcheatsheet.com) for more information. 