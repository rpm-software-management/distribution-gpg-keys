# distribution-gpg-keys

GPG keys used by various Linux distributions to sign packages.

## Keys for

 * Amazon Linux
 * COPR repositories
 * CentOS
 * EPEL
 * EuroLinux
 * Fedora
 * Mageia
 * OpenMandriva
 * OpenSuse
 * Oracle Linux
 * Qubes
 * RosaLinux
 * RPM Fusion
 * Red Hat
 * Scientific Linux
 * United RPMs

and for third parties repos:

 * Adobe
 * Brave
 * BlueJeans
 * CalcForge
 * Datto
 * Dell
 * Dropbox
 * Google
 * IUS
 * JPackage
 * Microsoft
 * PostgreSQL RPM Building Project
 * Remi's
 * Skype
 * VirtualBox
 * Zimbra
 * Zoom


it intentionally does not include keys for Ubuntu as there exists the package `ubu-keyring`, for Debian as there exists the package `debian-keyring`, for ArchLinux as there exists the package `archlinux-keyrings`.

For up to date list of keys see [SOURCES.md](SOURCES.md).

## Downstream packaging

If you are going to package this project, then consider packaging Copr keys as subpackage as it is quite big.

This project is available as a package in Fedora, EPEL, openSUSE, archLinux, Mageia, OpenMandriva.

## Releasing

To get tar.gz:

    dnf install tito
    git clone git://github.com/xsuchy/distribution-gpg-keys.git
    cd distribution-gpg-keys
    tito build --tgz

To get SRPM:

    tito build --srpm

To get RPM:

    tito build --rpm

To create new release:

    # do NOT create changelog entries
    git commit
    tito tag
    git push && git push --tags
