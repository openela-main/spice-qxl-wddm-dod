%global spice_data_dir  %{_datadir}/spice


Name: spice-qxl-wddm-dod
Version: 0.21
Release: 2%{?dist}
License: ASL 2.0
Summary: A QXL display-only driver for Windows 10 virtual machines.
Group: Virtualization/Management
URL: http://www.spice-space.org

Source0: spice-qxl-wddm-dod.zip
Source1: spice-qxl-wddm-dod-8.1-compatible.zip
Source2: spice-qxl-wddm-dod-0.21-2-spec.zip
Source3: spice-qxl-wddm-dod-0.21-2-sources.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
QXL is a paravirtualized display driver and a part of SPICE project.
This package provides QXL display-only driver for Windows 10 virtual machines.

%prep

%build

%install
rm -rf %{buildroot}
/usr/bin/install -d %{buildroot}%{spice_data_dir}

/usr/bin/unzip %{SOURCE0}
/bin/cp w10/QxlWddmDod_*.msi %{buildroot}%{spice_data_dir}/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{spice_data_dir}/QxlWddmDod_*.msi


%changelog
* Sun Dec  6 2020 Uri Lublin <uril@redhat.com> - 0.21-2
- Fix behavior on rev5 qxl device
  Resolves: rhbz#1851845

* Wed Jun  3 2020 Uri Lublin <uril@redhat.com> - 0.20-1
- Build for 8.3
- Resolves: rhbz#1813149

* Mon Dec 16 2019 Uri Lublin <uril@redhat.com> - 0.19-2
- First build for 8.2
- Resolves: rhbz#1757772

