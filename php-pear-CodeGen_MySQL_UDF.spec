%define		_class		CodeGen
%define		_subclass	MySQL_UDF
%define		_status		beta
%define		_pearname	CodeGen_MySQL_UDF
Summary:	%{_pearname} - Tool to generate MySQL UDF extensions from an XML description
Summary(pl.UTF-8):	%{_pearname} - narzędzie do generowania rozszerzeń UDF na podstawie opisu XML
Name:		php-pear-%{_pearname}
Version:	0.9.8
Release:	0.1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a3a2ba01a0d85b2916b29790592e467e
URL:		http://pear.php.net/package/CodeGen_MySQL_UDF/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-CodeGen >= 1.0.4
Requires:	php-pear-CodeGen_MySQL >= 0.9.0
Requires:	php-pear-PEAR >= 1.4.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CodeGen_MySQL_UDF is a code generator for MySQL User Defined Function
(UDF) extensions similar to PECL_Gen for PHP.

It reads in configuration options, function prototypes and code
fragments from an XML description file and generates a complete
ready-to-compile UDF extension.

Preliminary documentation can be found here:
http://talks.php.net/show/UDF_Gen

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
CodeGen_MySQL_UDF to generator kodu dla rozszerzeń zdefiniowanych
przez użytkownika funkcji (User Defined Function - UDF) MySQL zbliżony
do PECL_Gen dla PHP.

Pakiet ten na podstawie opcji konfiguracyjnych, prototypów funkcji i
fragmentów kodu z pliku opisu XML generuje kompletne, gotowe do
skompilowania rozszerzenie UDF.

Dokumentacja do tego pakietu znajduje się pod adresem:
http://talks.php.net/show/UDF_Gen

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
install {./,$RPM_BUILD_ROOT}%{_bindir}/udf-gen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/CodeGen_MySQL_UDF/docs/{examples,manual.html}
%attr(755,root,root) %{_bindir}/udf-gen
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/CodeGen/MySQL/UDF
