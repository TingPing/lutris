all: net.lutris.Lutris.json setuptools-makefile setuptools-bootstrap pyyaml-makefile
	flatpak-builder --force-clean --repo=repo build $<

net.lutris.Lutris.flatpak: all
	flatpak build-bundle repo $@ net.lutris.Lutris
