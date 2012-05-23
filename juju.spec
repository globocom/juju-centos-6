Name: Juju
Version: 0.5
Release:	1%{?dist}
Summary: next generation service orchestration system

Group/:
License: GNU Affero GPL v3
URL: https://launchpad.net/juju
Source0: http://pypi.python.org/packages/source/j/juju/juju-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: python-devel, gcc
Requires: python-txaws, python-twisted, python-txzookeeper, python-yaml

%description
Juju is a next generation service orchestration framework. It has been
likened to APT for the cloud.  With Juju, different authors are able to
create service formulas, called charms, independently, and make those
services coordinate their communication and configuration through a simple
protocol.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog

