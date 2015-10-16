# distribution-gpg-keys

GPG keys used by various Linux distributions to sign packages.

## Keys for

 * centos
 * epel
 * fedora
 * redhat
 * rpmfusion

## Releasing

To get tar.gz:

    dnf install tito
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
