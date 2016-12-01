Name:		distribution-gpg-keys
Version:	1.9
Release:	1%{?dist}
Summary:	GPG keys of various Linux distributions

License:	CC0
URL:		https://github.com/xsuchy/distribution-gpg-keys
# Sources can be obtained by
# git clone git://github.com/xsuchy/distribution-gpg-keys.git
# cd distribution-gpg-keys
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

%if 0%{?fedora} > 0
Suggests:	ubu-keyring
Suggests:	debian-keyring
Suggests:	archlinux-keyrings
Suggests:   %{name}-copr
%endif

%description
GPG keys used by various Linux distributions to sign packages.

%package copr
Summary: GPG keys for Copr projects
BuildArch: noarch

%description copr
GPG keys used by Copr projects.

%prep
%setup -q


%build
#nothing to do here


%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp -a keys/* %{buildroot}%{_datadir}/%{name}/


%files
%license LICENSE
%doc README.md SOURCES.md
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/copr

%files copr
%license LICENSE
%{_datadir}/%{name}/copr

%changelog
* Thu Dec 01 2016 Miroslav Suchý <msuchy@redhat.com> 1.9-1
- add new copr keys
- add Fedora 26 keys
- add more CentOS 7 keys (aarch64, debug, SIGs, testing)

* Mon Oct 24 2016 Miroslav Suchý <miroslav@suchy.cz> 1.8-1
- update copr gpg keys
- README.md: Indicate what keys are actually included
- add rpmfusion F19 keys
- add note how to verify gpg key using fingerprint
- RPMFusion add fedora-20 and fedora-21 keys
- RPMFusion add rpmfusion el-7 keys
- RPMFusion add fedora-25 keys
- use symbol links .
- Add a crucial information to README.md

* Mon Sep 12 2016 Miroslav Suchý <msuchy@redhat.com> 1.7-1
- do not use weak deps on rhel

* Mon Sep 12 2016 Miroslav Suchý <msuchy@redhat.com> 1.6-1
- Rename mageia pubkey to RPM-GPG-KEY-Mageia

* Mon Aug 08 2016 Miroslav Suchý <msuchy@redhat.com> 1.5-1
- move copr keys to subpackage
- update copr gpg keys
- add RPM-GPG-KEY-CentOS-SIG-AltArch-7-ppc64le
- add F25 keys

* Mon Mar 14 2016 Miroslav Suchý <msuchy@redhat.com> 1.4-1
- update SOURCES
- update copr gpg keys
- add mageia gpg keys

* Tue Feb 02 2016 Miroslav Suchý <msuchy@redhat.com> 1.3-1
- add copr keys
- added obsolete gpg keys
- document from where those keys can be originally obtained
- suggest installations of other keyrings
- do not include email in changelog items

* Fri Oct 16 2015 Miroslav Suchý <msuchy@redhat.com> 1.2-1
- document how to do release
- change license to CC-0

* Thu Oct 15 2015 Miroslav Suchý <msuchy@redhat.com> 1.1-1
- initial package



