# Rocky9 Cluster upgrade

COSMA was reinstalled with Rocky9 in July 2024.

Helpful information should appear here as it becomes available.

In the meantime, please see the [email text](rocky9email) for further details.

## Fixes

### gnome-terminal

If gnome-terminal is refusing to start, please try `dbus-launch gnome-terminal` or alternatively, `xfce4-terminal`.

### x2go

Disable the compositor to get rid of shadows when you move screens around. Find this at:
```
Applications > Settings > Window Manager Tweaks > Compositor
```

The screen lock can also be disabled in:
```
Applications > Settings > Xfce Screensaver > Lock Screen
```
