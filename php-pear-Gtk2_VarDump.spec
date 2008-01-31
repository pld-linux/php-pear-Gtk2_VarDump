%include	/usr/lib/rpm/macros.php
%define		_class		Gtk2
%define		_subclass	VarDump
%define		_status		beta
%define		_pearname	Gtk2_VarDump

Summary:	%{_pearname} - a simple GUI to examine PHP data trees
Summary(pl.UTF-8):	%{_pearname} - proste GUI do analizy drzew danych PHP
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	23649aad8bc44ce648473a1c70953fc1
URL:		http://pear.php.net/package/Gtk2_VarDump/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(gtk2)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Just a regedit type interface to examine PHP data trees.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Interfejs w stylu regedit do analizy drzew danych PHP.

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
%doc install.log docs/%{_pearname}/docs/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Gtk2/VarDump.php
%{php_pear_dir}/Gtk2/VarDump
