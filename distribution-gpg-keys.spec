Name:		distribution-gpg-keys
Version:	1.4
Release:	1%{?dist}
Summary:	Keys of various Linux distributions

License:	CC0
URL:		https://github.com/xsuchy/distribution-gpg-keys
# Sources can be obtained by
# git clone git://github.com/xsuchy/distribution-gpg-keys.git
# cd distribution-gpg-keys
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

Suggests:	ubu-keyring
Suggests:	debian-keyring
Suggests:	archlinux-keyrings

%description
GPG keys used by various Linux distributions to sign packages.

%prep
%setup -q


%build


%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp -a keys/* %{buildroot}%{_datadir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_datadir}/%{name}

%changelog
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



