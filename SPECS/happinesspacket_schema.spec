# Created by pyp2rpm-3.3.2
%global pypi_name happinesspacket_schema

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        A schema package for Fedora Happiness Packets

License:        GPLv2+
URL:            https://pagure.io/fedora-commops/fedora-happiness-packets
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(fedora-messaging)
BuildRequires:  python3dist(setuptools)

%description
A schema package for Fedora Happiness Packets

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(fedora-messaging)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
A schema package for Fedora Happiness Packets


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Jun 26 2019 Shraddha Agrawal <shraddha.agrawal000@gmail.com> - 1.0.0-1
- Initial package.

