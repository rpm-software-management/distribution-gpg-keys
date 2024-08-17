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

# Use the same algorithm as in github workflow
git_rawhide_release() {
	local REPOSDIR="$(mktemp -d)"
	git clone -q https://src.fedoraproject.org/rpms/fedora-repos.git --depth 1 --branch rawhide "$REPOSDIR" >/dev/null
	awk '$1 == "%global" && $2 == "rawhide_release" { print $3 }' "$REPOSDIR/fedora-repos.spec" && rm -rf "$REPOSDIR"
}

dnf_rawhide_release() {
	PKG_VER=$(dnf --repo=rawhide repoquery -q fedora-gpg-keys)
	echo "${PKG_VER#$PKG}" | cut -d- -f2 | cut -d: -f2
}

VER=$(git_rawhide_release)
echo "Release: $VER"
if ! [ "$VER" -gt 0 ]; then
	echo "Failed to obtain rawhide release"
	exit 1
fi

echo "Current Rawhide is release $VER"

check_path rawhide $VER
check_path rawhide+1 $((VER+1))
check_path rawhide-1 $((VER-1))
check_path rawhide-2 $((VER-2))
