Name:           cockpit-leapp
Version:        0.1.0
Release:        1%{?dist}
Summary:        Leapp in-place upgrade Cockpit UI

License:        LGPLv2+
URL:            https://github.com/oamg/cockpit-leapp
Source0:        cockpit-leapp-%{version}.tar.gz

BuildArch:      noarch

Requires:       cockpit
Requires:       leapp leapp-repository

%description
Leapp in-place upgrade Cockpit UI

%prep
%setup -q -n cockpit-leapp-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/cockpit/leapp
cp -r public/* %{buildroot}/%{_datadir}/cockpit/leapp

%files
%license LICENSE.txt
%{_datadir}/cockpit/leapp

%changelog
