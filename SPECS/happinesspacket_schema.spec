
%global pypi_name happinesspacket_schema

Name:           %{pypi_name}
Version:        0.1.2
Release:        1%{?dist}
Summary:        A schema package for Fedora Happiness Packets

License:        GPLv2+
URL:            https://pagure.io/fedora-commops/fedora-happiness-packets
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  fedora-messaging
BuildRequires:  python3dist(setuptools)

%description
A schema package for Fedora Happiness Packets
 
Requires:       fedora-messaging
Requires:       python3dist(setuptools)

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n %{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%changelog
* Sun May 26 2019 Shraddha Agrawal - 0.1.2-1
- Initial package.
