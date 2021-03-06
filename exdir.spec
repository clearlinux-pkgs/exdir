#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : exdir
Version  : 0.4.2
Release  : 2
URL      : https://files.pythonhosted.org/packages/54/f3/05a79114fdec076c922aa79effa4211a4b3ab1ff7ea28017b5ff4a2944ab/exdir-0.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/54/f3/05a79114fdec076c922aa79effa4211a4b3ab1ff7ea28017b5ff4a2944ab/exdir-0.4.2.tar.gz
Summary  : UNKNOWN
Group    : Development/Tools
License  : MIT
Requires: exdir-data = %{version}-%{release}
Requires: exdir-python = %{version}-%{release}
Requires: exdir-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(numpy)
BuildRequires : pypi(ruamel.yaml)
BuildRequires : pypi(six)

%description
[![Build Status](https://travis-ci.org/CINPLA/exdir.svg?branch=dev)](https://travis-ci.org/CINPLA/exdir)
[![Project Status: Active - The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Anaconda-Server Badge](https://anaconda.org/cinpla/exdir/badges/installer/conda.svg)](https://conda.anaconda.org/cinpla)
[![codecov](https://codecov.io/gh/CINPLA/exdir/branch/dev/graph/badge.svg)](https://codecov.io/gh/CINPLA/exdir)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/CINPLA/exdir/dev?filepath=tests%2Fbenchmarks%2Fbenchmarks.ipynb)

%package data
Summary: data components for the exdir package.
Group: Data

%description data
data components for the exdir package.


%package python
Summary: python components for the exdir package.
Group: Default
Requires: exdir-python3 = %{version}-%{release}

%description python
python components for the exdir package.


%package python3
Summary: python3 components for the exdir package.
Group: Default
Requires: python3-core
Provides: pypi(exdir)
Requires: pypi(numpy)
Requires: pypi(ruamel.yaml)
Requires: pypi(six)

%description python3
python3 components for the exdir package.


%prep
%setup -q -n exdir-0.4.2
cd %{_builddir}/exdir-0.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638307310
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mv %{buildroot}/usr/etc %{buildroot}/usr/share
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/etc/jupyter/jupyter_notebook_config.d/exdir.json
/usr/share/etc/jupyter/nbconfig/notebook.d/exdir.json
/usr/share/jupyter/nbextensions/exdir/index.js

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
