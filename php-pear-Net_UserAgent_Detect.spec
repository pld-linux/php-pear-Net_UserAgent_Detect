%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Net_UserAgent_Detect
Summary:	%{_pearname} - determines the Web browser
Summary(pl.UTF-8):	%{_pearname} - identyfikuje przeglądarkę
Name:		php-pear-%{_pearname}
Version:	2.5.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	646e074fd7faa8c14fba12b698ba28c9
URL:		http://pear.php.net/package/Net_UserAgent_Detect/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.1.0
Requires:	php-pear >= 4:1.3-4
Obsoletes:	php-pear-Net_UserAgent_Detect-tests
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
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/UserAgent/Detect.php
%{php_pear_dir}/Net/UserAgent/Detect
