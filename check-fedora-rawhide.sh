#!/bin/sh
#
# Check and update Fedora Rawhide release version
# Requires fedora-repos-rawhide installed

PKG=fedora-gpg-keys

key_path() {
	echo "keys/fedora/RPM-GPG-KEY-fedora-$1-primary"
}

check_path() {
	local NAME="$1"
	local VERSION="$2"

	NAME_PATH="$(key_path $NAME)"
	RELEASE_PATH="$(key_path $VERSION)"

	if [ "$(realpath "$NAME_PATH")" = "$(realpath "$RELEASE_PATH")" ]; then
		echo "Fedora $NAME key is up-to-date"
	else
		rm -f "$NAME_PATH"
		echo "Fedora $NAME key needs change: $RELEASE_PATH"
		ln -vs "$(basename -- "$RELEASE_PATH")" "$NAME_PATH"
	fi
}

PKG_VER=$(dnf --repo=rawhide repoquery -q fedora-gpg-keys)
if [ $? -ne 0 ]; then
	echo "Failed to fetch keys"
	exit 1
fi
VER=$(echo "${PKG_VER#$PKG}" | cut -d- -f2 | cut -d: -f2)

echo "Current Rawhide is release $VER"

check_path rawhide $VER
check_path rawhide+1 $((VER+1))
check_path rawhide-1 $((VER-1))
check_path rawhide-2 $((VER-2))
