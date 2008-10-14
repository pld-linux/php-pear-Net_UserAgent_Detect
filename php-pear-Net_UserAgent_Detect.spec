%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	UserAgent
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Detect

Summary:	%{_pearname} - determines the Web browser
Summary(pl.UTF-8):	%{_pearname} - identyfikuje przeglądarkę
Name:		php-pear-%{_pearname}
Version:	2.5.0
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1844b4d0b133c6a606dc018d20059d01
URL:		http://pear.php.net/package/Net_UserAgent_Detect/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net_UserAgent object does a number of tests on an HTTP User-Agent
string. The results of these tests are available via methods of the
object. This module is based upon the JavaScript browser detection
code available at
http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html.
This module had many influences from the lib/Browser.php code in
version 1.3 of Horde.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Obiekt Net_UserAgent wykonuje wiele testów na polu User-Agent z
nagłówka HTTP. Wyniki tych testów są dostępne poprzez metody obiektu.
Ten moduł został stworzony na podstawie kodu do wykrywania
przeglądarek z poziomu JavaScriptu, dostępnego pod adresem
http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html.
Ten moduł ma także wiele wpływów z kodu lib/Browser.php z Horde w
wersji 1.3.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/Detect
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
