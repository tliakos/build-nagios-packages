Summary:        Nagios monitoriing tools from Jason Hancock
Name:           nagios-plugins-hancock
Version:        %{version}
Release:        1%{?dist}
License:        MIT
Group:          Applications/System
URL:            http://geek.jasonhancock.com
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildRequires: zlib-devel

Requires: perl-JSON
Requires: perl-LWP-Protocol-https
Requires: perl-URI-Encode
Requires: perl-libwww-perl

%description
Nagios monitoring tools from Jason Hancock

%package pnp4nagios
Summary: pnp4nagios configs for Nagios monitoring tools from Jason Hancock
Group: Applications/System

%description pnp4nagios
Nagios monitoriing tools from Jason Hancock

%prep

%build

rm -rf *
export GOPATH=$RPM_BUILD_DIR/go
go get gopkg.in/olivere/elastic.v3
go get github.com/pkg/errors
go get github.com/jasonhancock/go-nagios
go get github.com/jasonhancock/nagios-elk/...
go get github.com/jasonhancock/nagios-graphite/...

for p in nagios-memory nagios-cpu nagios-html-email nagios-puppet nagios-apache nagios-mysql nagios-redis nagios-iops nagios-slack nagios-elasticsearch
do
    wget -q -O $p.tar.gz https://github.com/jasonhancock/$p/archive/master.tar.gz
    mkdir $p
    tar --strip-components=1 -xvzf $p.tar.gz -C $p
done


%install
rm -rf $RPM_BUILD_ROOT

PLUGIN_DIR=$RPM_BUILD_ROOT/usr/lib64/nagios/plugins
PNP_TEMPLATES_DIR=$RPM_BUILD_ROOT/usr/share/nagios/html/pnp4nagios/templates
PNP_CHECK_DIR=$RPM_BUILD_ROOT/etc/pnp4nagios/check_commands

mkdir -p $PLUGIN_DIR
mkdir -p $PNP_TEMPLATES_DIR
mkdir -p $PNP_CHECK_DIR

install -m 0755 */plugins/* $PLUGIN_DIR/
install -m 0644 */pnp4nagios/templates/* $PNP_TEMPLATES_DIR/
install -m 0644 */pnp4nagios/check_commands/* $PNP_CHECK_DIR/
install -m 0755 $RPM_BUILD_DIR/go/bin/check_graphite $PLUGIN_DIR/
install -m 0755 $RPM_BUILD_DIR/go/bin/check_elk_message $PLUGIN_DIR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/lib64/nagios/plugins/*

%files pnp4nagios
/etc/pnp4nagios/check_commands/*
/usr/share/nagios/html/pnp4nagios/templates/*
