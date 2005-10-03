%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	UserAgent
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Detect

Summary:	%{_pearname} - determines the Web browser
Summary(pl):	%{_pearname} - identyfikuje przegl±darkê
Name:		php-pear-%{_pearname}
Version:	2.1.0
Release:	1.2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fcee7d4da95a31ef9d935edcddbd9687
URL:		http://pear.php.net/package/Net_UserAgent_Detect/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
Obiekt Net_UserAgent wykonuje wiele testów na polu User-Agent z
nag³ówka HTTP. Wyniki tych testów s± dostêpne poprzez metody obiektu.
Ten modu³ zosta³ stworzony na podstawie kodu do wykrywania
przegl±darek z poziomu JavaScriptu, dostêpnego pod adresem
http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html.
Ten modu³ ma tak¿e wiele wp³ywów z kodu lib/Browser.php z Horde w
wersji 1.3.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
