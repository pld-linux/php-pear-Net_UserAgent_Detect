%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       UserAgent_Detect
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - determines the Web browser
Summary(pl):	%{_class}_%{_subclass} - identyfikuje przegl±darkê
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net_UserAgent object does a number of tests on an HTTP user agent
string. The results of these tests are available via methods of the
object. This module is based upon the JavaScript browser detection
code available at
http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html.
This module had many influences from the lib/Browser.php code in
version 1.3 of Horde.

%description -l pl

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/UserAgent

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/UserAgent

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/UserAgent
%{php_pear_dir}/%{_class}/UserAgent/*.php
