# distribution-gpg-keys

GPG keys used by various Linux distributions to sign packages.

## Keys for

 * COPR repositories
 * CentOS
 * EPEL
 * Fedora
 * Mageia
 * OpenSuse
 * RPM Fusion
 * Red Hat
 * Scientific Linux
 * United RPMs

and for third parties repos:

 * Adobe
 * Brave
 * CalcForge
 * Dell
 * Dropbox
 * Google
 * JPackage
 * Microsoft
 * PostgreSQL RPM Building Project
 * Remi's
 * Skype
 * VirtualBox
 
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
