%include	/usr/lib/rpm/macros.php
%define		_class		Gtk2
%define		_subclass	VarDump
%define		_status		beta
%define		_pearname	Gtk2_VarDump

Summary:	%{_pearname} - a simple GUI to examine PHP data trees
Summary(pl):	%{_pearname} - proste GUI do analizy drzew danych PHP
Name:		php-pear-%{_pearname}
Version:	0.0.4
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ad544efaaa77f52d5bd0457f53e824ec
URL:		http://pear.php.net/package/Gtk2_VarDump/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-gtk
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Just a regedit type interface to examine PHP data trees.

In PEAR status of this package is: %{_status}.

%description -l pl
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
%doc install.log docs/%{_pearname}/{examples/Gtk2_VarDump_array.phpw,examples/Gtk2_VarDump_object.phpw,examples/Gtk2_VarDump_string.phpw}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Gtk2/VarDump.php
