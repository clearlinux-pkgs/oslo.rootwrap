#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.rootwrap
Version  : 5.2.0
Release  : 39
URL      : http://tarballs.openstack.org/oslo.rootwrap/oslo.rootwrap-5.2.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.rootwrap/oslo.rootwrap-5.2.0.tar.gz
Summary  : Oslo Rootwrap
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.rootwrap-bin
Requires: oslo.rootwrap-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : debtcollector-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : eventlet-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : funcsigs-python
BuildRequires : hacking
BuildRequires : imagesize-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyrsistent-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
===============================================
oslo.rootwrap -- Escalated Permission Control
===============================================

%package bin
Summary: bin components for the oslo.rootwrap package.
Group: Binaries

%description bin
bin components for the oslo.rootwrap package.


%package python
Summary: python components for the oslo.rootwrap package.
Group: Default
Requires: six-python

%description python
python components for the oslo.rootwrap package.


%prep
%setup -q -n oslo.rootwrap-5.2.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oslo-rootwrap
/usr/bin/oslo-rootwrap-daemon

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
