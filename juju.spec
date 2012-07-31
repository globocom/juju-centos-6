%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           juju
Version:        0.5
Release:        5.bzr561%{?dist}
Summary:        next generation service orchestration system

Group:          System Environment/Orchestration
License:        GNU Affero GPL v3
URL:            https://launchpad.net/juju
# bzr export -r 561 juju-0.5-bzr561.tar.gz lp:juju
Source0:        %{name}-%{version}-bzr561.tar.gz

# CentOSCloudInit class
Patch0:         juju-0.5-cloudinit.patch

BuildArch:      noarch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  python-devel
Requires:       python-argparse
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
%setup -q -n %{name}-%{version}-bzr561
%patch0 -p1


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O2 --skip-build --root $RPM_BUILD_ROOT
install -p -D -m 755 misc/bash_completion.d/juju %{buildroot}/etc/bash_completion.d/juju


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
/etc/bash_completion.d/juju


%changelog
* Mon Jul 30 2012 Francisco Souza <f@souza.cc> - 0.5-4.bzr561
- Updated juju package to revision 561
* Mon Jun 04 2012 Francisco Souza <f@souza.cc> - 0.5-3.bzr531
- Added bash completion
* Fri Jun 01 2012 Francisco Souza <f@souza.cc> - 0.5-2.bzr531
- Fix requirements (added python-argparse)
* Thu May 31 2012 Francisco Souza <f@souza.cc> - 0.5-1.bzr531
- Initial packaging
