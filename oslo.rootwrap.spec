#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : oslo.rootwrap
Version  : 5.16.0
Release  : 56
URL      : http://tarballs.openstack.org/oslo.rootwrap/oslo.rootwrap-5.16.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.rootwrap/oslo.rootwrap-5.16.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.rootwrap/oslo.rootwrap-5.16.0.tar.gz.asc
Summary  : Oslo Rootwrap
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.rootwrap-bin = %{version}-%{release}
Requires: oslo.rootwrap-license = %{version}-%{release}
Requires: oslo.rootwrap-python = %{version}-%{release}
Requires: oslo.rootwrap-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : six

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/oslo.rootwrap.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package bin
Summary: bin components for the oslo.rootwrap package.
Group: Binaries
Requires: oslo.rootwrap-license = %{version}-%{release}

%description bin
bin components for the oslo.rootwrap package.


%package license
Summary: license components for the oslo.rootwrap package.
Group: Default

%description license
license components for the oslo.rootwrap package.


%package python
Summary: python components for the oslo.rootwrap package.
Group: Default
Requires: oslo.rootwrap-python3 = %{version}-%{release}

%description python
python components for the oslo.rootwrap package.


%package python3
Summary: python3 components for the oslo.rootwrap package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.rootwrap package.


%prep
%setup -q -n oslo.rootwrap-5.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1558475600
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.rootwrap
cp LICENSE %{buildroot}/usr/share/package-licenses/oslo.rootwrap/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oslo-rootwrap
/usr/bin/oslo-rootwrap-daemon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.rootwrap/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
