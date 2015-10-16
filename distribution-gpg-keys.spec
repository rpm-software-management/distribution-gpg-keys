Name:		distribution-gpg-keys
Version:	1.2
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
* Fri Oct 16 2015 Miroslav Suchý <msuchy@redhat.com> 1.2-1
- document how to do release
- change license to CC-0

* Thu Oct 15 2015 Miroslav Suchý <msuchy@redhat.com> 1.1-1
- initial package



