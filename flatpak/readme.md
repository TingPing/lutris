# TODO

This was just an initial setup, we need to test installing and running real games,
come up with a plan to support system steam probably, get python-eudev actually working, etc.

# Building

```sh
# If missing gnome runtime:
flatpak remote-add --if-not-exists gnome https://sdk.gnome.org/gnome.flatpakrepo
flatpak --user install gnome org.gnome.Platform 3.22
flatpak --user install gnome org.gnome.Sdk 3.22

make
make net.lutris.Lutris.flatpak
```

## Installing

```sh
# If previously installed:
flatpak --user uninstall net.lutris.Lutris
flatpak --user install --bundle ./net.lutris.Lutris.flatpak
flatpak run net.lutris.Lutris
```
