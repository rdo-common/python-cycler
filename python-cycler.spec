%global srcname cycler
%global sum Cycle through lists in various ways (used by matplotlib)
%global desc General purpose library used by matplotlib to cycle through lists for colors,\
marker styles, etc

Name:           python-%{srcname}
Version:        0.10.0
Release:        2%{?dist}
Summary:        %{sum}

License:        BSD
Source0:        https://github.com/matplotlib/cycler/archive/v%{version}/%{name}-%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
URL:            https://github.com/matplotlib/cycler.git

BuildArch:      noarch

%description
%{desc}

%package -n python2-%{srcname}
Summary:        %{sum}
Requires:       python-six
BuildRequires:  python2-devel python-six python-setuptools python-nose

%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{desc}


%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       python3-six
BuildRequires:  python3-devel python3-six python3-setuptools python3-nose

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{srcname}
%doc README.rst
%license LICENSE
%{python2_sitelib}/*

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*

%changelog
* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.10.0-2
- Rebuild for Python 3.6

* Mon Aug 29 2016 Neal Becker <nbecker@nbecker2> - 0.10.0-1
- Update to 0.10.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Neal Becker <ndbecker2@gmail.com> - 0.9.0-6
- Add BR python-nose

* Sun Nov 15 2015 Neal Becker <ndbecker2@gmail.com> - 0.9.0-5
- rebuild for py3.5

* Fri Nov  6 2015 Neal Becker <ndbecker2@gmail.com> - 0.9.0-3
- fix license

* Fri Oct 30 2015 Neal Becker <ndbecker2@gmail.com> - 0.9.0-1
- init

