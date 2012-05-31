%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           juju
Version:        0.5
Release:        1.bzr531%{?dist}
Summary:        next generation service orchestration system

Group:          System Environment/Orchestration
License:        GNU Affero GPL v3
URL:            https://launchpad.net/juju
# bzr export -r 531 juju-0.5-bzr531.tar.gz lp:juju
Source0:        %{name}-%{version}-bzr531.tar.gz

BuildArch:      noarch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  python-devel
Requires:       python-txaws
Requires:       python-twisted
Requires:       python-txzookeeper
Requires:       python-oauth
Requires:       pydot
Requires:       PyYAML
Requires:       zookeeper


%description
Juju is a next generation service orchestration framework. It has been
likened to APT for the cloud.  With Juju, different authors are able to
create service formulas, called charms, independently, and make those
services coordinate their communication and configuration through a simple
protocol.

%prep
%setup -q -n %{name}-%{version}-bzr531


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O2 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc COPYING README
%{python_sitelib}/*
%{_bindir}/juju
%{_bindir}/juju-*
%{_bindir}/relation-*
%{_bindir}/*-port
%{_bindir}/unit-get
%{_bindir}/config-get


%changelog
* Thu May 31 2012 Francisco Souza <f@souza.cc> - 0.5-1.bzr531
- Initial packaging
