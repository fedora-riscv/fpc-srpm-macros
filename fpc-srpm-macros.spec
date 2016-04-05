Name:           fpc-srpm-macros
Version:        1.0
Release:        1%{?dist}
Summary:        RPM macros needed by packages built with Free Pascal Compiler

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
* Mon Mar 14 2016 Mattia Verga <mattia.verga@tiscali.it> - 1.0-1
- Initial creation with supported architectures
