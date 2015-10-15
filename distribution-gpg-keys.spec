Name:		distribution-gpg-keys
Version:	1.0
Release:	1%{?dist}
Summary:	Keys of various Linux distributions

License:	GPLv2
URL:		https://github.com/xsuchy/distribution-gpg-keys
# Sources can be obtained by
# git clone git://github.com/xsuchy/distribution-gpg-keys.git
# cd distribution-gpg-keys
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

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


