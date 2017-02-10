Name:           fpc-srpm-macros
Version:        1.1
Release:        2%{?dist}
Summary:        RPM macros needed by packages built with Free Pascal Compiler
# This package only exist in Fedora repositories
# The license is the standard (MIT) specified in
# Fedora Project Contribution Agreement
# and as URL we provide dist-git URL
License:        MIT
URL:            http://pkgs.fedoraproject.org/cgit/rpms/fpc-src-macros.git
Source0:        macros.fpc-srpm
BuildArch:      noarch


%description
This package contains RPM macros needed by packages built with the
Free Pascal Compiler. For example, it makes available a macro that
lists all architectures where fpc is available.

%prep
# nothing to do


%build
# nothing to do


%install
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d
install -p -m 0644 -t %{buildroot}/%{_rpmconfigdir}/macros.d %{SOURCE0}


%files
%{_rpmconfigdir}/macros.d/*



%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Mattia Verga <mattia.verga@tiscali.it> - 1.1-1
- Enable builds on ppc64

* Tue Apr 05 2016 Mattia Verga <mattia.verga@tiscali.it> - 1.0-2
- Added a note to clarify license and URL

* Mon Mar 14 2016 Mattia Verga <mattia.verga@tiscali.it> - 1.0-1
- Initial creation with supported architectures
