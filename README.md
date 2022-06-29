# distribution-gpg-keys

GPG keys used by various Linux distributions to sign packages.

## Keys for

 * Amazon Linux
 * Alma Linux
 * COPR repositories
 * CentOS
 * Circle Linux
 * EPEL
 * EuroLinux
 * Fedora
 * Mageia
 * OpenMandriva
 * OpenSuse
 * Oracle Linux
 * Qubes
 * Rocky Linux
 * RosaLinux
 * RPM Fusion
 * Red Hat
 * Navy Linux
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
 * MariaDB
 * MySQL
 * Microsoft
 * PostgreSQL RPM Building Project
 * Remi's
 * Skype
 * VirtualBox
 * Zimbra
 * Zoom


it intentionally does not include keys for Ubuntu as there exists the package `ubu-keyring`, for Debian as there exists the package `debian-keyring`, for ArchLinux as there exists the package `archlinux-keyrings`.

For up to date list of keys see [SOURCES.md](SOURCES.md).

## Storing keys in DNS

If you are owner of the GPG key, you can [generate TYPE 61 DNS records](http://miroslav.suchy.cz/blog/archives/2021/02/13/how_to_generate_openpgp_record_for_dns_type61/index.html) and clients [can verify it using DNSSEC](http://miroslav.suchy.cz/blog/archives/2021/02/11/verify_package_gpg_signature_using_dnssec/index.html) and [Different OpenGPG DNS entries for the same email](http://miroslav.suchy.cz/blog/archives/2021/02/18/different_opengpg_dns_entries_for_the_same_email/index.html).

Here is overview of availability of DNS entries for GPG keys:

| Provider | DNS entry | DNSSEC |
| -------- | --------- | ------ |
| Fedora   | :heavy_check_mark: | :heavy_check_mark: |
| Epel     | :heavy_check_mark: | :heavy_check_mark: |
| Red Hat  | :heavy_check_mark: | :x: |
| CentOS   | requested          | :x: |
| OpenSuse | :heavy_check_mark:          | :heavy_check_mark: |
| RPM Fusion | [requested](https://bugzilla.rpmfusion.org/show_bug.cgi?id=5927)        | :x: |
| Dropbox    | requested        | :x: |
| [Debian 11 bullseye (stable)](https://software.opensuse.org/download.html?project=home%3Aandykimpe%3Adebian-buster&package=distribution-gpg-keys) | :heavy_check_mark:        | :x: |
| Ubuntu LTS [launchpad](https://launchpad.net/~andykimpe/+archive/ubuntu/mock) | :heavy_check_mark:        | :x: |

The keys can be fetched using `resolvectl openpgp EMAIL`. e.g. `resolvectl openpgp security@redhat.com`

## Packaging status
 
![distribution-gpg-keys versions](https://repology.org/badge/vertical-allrepos/distribution-gpg-keys.svg?exclude_unsupported=1&header=distribution-gpg-keys)

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
