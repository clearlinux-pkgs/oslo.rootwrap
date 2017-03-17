#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9069B1335700CDC (infra-root@openstack.org)
#
Name     : oslo.rootwrap
Version  : 5.6.0
Release  : 43
URL      : http://tarballs.openstack.org/oslo.rootwrap/oslo.rootwrap-5.6.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.rootwrap/oslo.rootwrap-5.6.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.rootwrap/oslo.rootwrap-5.6.0.tar.gz.asc
Summary  : Oslo Rootwrap
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.rootwrap-bin
Requires: oslo.rootwrap-python
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/oslo.rootwrap.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package bin
Summary: bin components for the oslo.rootwrap package.
Group: Binaries

%description bin
bin components for the oslo.rootwrap package.


%package python
Summary: python components for the oslo.rootwrap package.
Group: Default

%description python
python components for the oslo.rootwrap package.


%prep
%setup -q -n oslo.rootwrap-5.6.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489784874
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489784874
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oslo-rootwrap
/usr/bin/oslo-rootwrap-daemon

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
