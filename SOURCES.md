# Where those keys were obtained

## Centos keys

https://www.centos.org/keys/

## Fedora & Epel keys

https://getfedora.org/en/keys/

## Mageia

http://mirrors.kernel.org/mageia/distrib/cauldron/x86_64/media/core/release/media_info/pubkey

## Copr

cd keys/copr && ../../copr-gpg-download.py --isolate-files

## Red Hat

https://access.redhat.com/security/team/key

## RpmFusion

http://rpmfusion.org/keys
https://pkgs.rpmfusion.org/cgit/free/rpmfusion-free-release.git/tree/
https://pkgs.rpmfusion.org/cgit/nonfree/rpmfusion-nonfree-release.git/tree/

## Adobe

https://get.adobe.com/cz/flashplayer/

## CalcForge

https://www.calcforge.org/RPM-GPG-KEY-calcforge

## Dell

http://linux.dell.com/repo/hardware/dsu/public.key

## Dropbox

https://linux.dropbox.com/fedora/rpm-public-key.asc

## Google

https://dl-ssl.google.com/linux/linux_signing_key.pub

## JPackage

http://www.jpackage.org/jpackage.asc

## PostgreSQL RPM Building Project

https://apt.postgresql.org/pub/repos/yum/

## Remi's repositories

https://git.remirepo.net/cgit/rpms/remi-release.git/plain/RPM-GPG-KEY-remi
https://git.remirepo.net/cgit/rpms/remi-release.git/plain/RPM-GPG-KEY-remi2017
https://git.remirepo.net/cgit/rpms/remi-release.git/plain/RPM-GPG-KEY-remi2018

## Skype

https://repo.skype.com/data/SKYPE-GPG-KEY

## UnitedRPMs

https://github.com/UnitedRPMs/unitedrpms/blob/master/URPMS-GPG-PUBLICKEY-Fedora-24

## VirtualBox

https://www.virtualbox.org/download/oracle_vbox.asc

## How to verify the GPG key

Run `gpg --with-fingerprint key_file` and compare the output with fingerprints on pages above.

## TODO

Add more gpg keys from this list https://rpmfusion.org/FedoraThirdPartyRepos
