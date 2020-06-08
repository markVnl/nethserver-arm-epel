# actually this is a noarch only applicable to armhfp
%global debug_package %{nil}

Summary:       NethServer YUM epel repo configuration
Name:          nethserver-arm-epel
Version:       7
Release:       2%{?dist}
License:       GPL
ExclusiveArch: armv7hl
Source:        %{name}-%{version}.tar.gz
URL:           %{url_prefix}/%{name}

BuildRequires: nethserver-devtools
Provides:      epel-release = %{version}%{release}

%description
NethServer YUM epel repository configuration for armhfp


%prep
%setup

%build
%{makedocs}
#perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING


%changelog

* Mon Jun 08 2020 Mark Verlinde <mark.verlinde@gmail.com> - 7-2
- Workaround for NethServer/arm-dev#41;
  Revisit if upstream (CentOs) moves on this isseu

* Thu Dec 13 2018 Mark Verlinde <mark.verlinde@gmail.com> - 7-1
- Initial build
