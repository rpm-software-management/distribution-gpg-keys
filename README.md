# distribution-gpg-keys

GPG keys used by various Linux distributions to sign packages.

## Keys for

 * CentOS
 * EPEL
 * Fedora
 * Red Hat
 * RPM Fusion
 * Mageia
 * COPR repositories

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
