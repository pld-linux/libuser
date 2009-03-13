Summary:	A user and group account administration library
Summary(pl.UTF-8):	Biblioteka do administrowania kontami użytkowników i grup
Name:		libuser
Version:	0.56.6
Release:	3
License:	LGPL v2+
Group:		Applications/System
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	74bd4ad52d81ccf67a8f6cd110add809
Patch0:		%{name}-selinux.patch
BuildRequires:	cyrus-sasl-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libselinux-devel
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	python-devel
BuildRequires:	sgml-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libuser library implements a standardized interface for
manipulating and administering user and group accounts. The library
uses pluggable back-ends to interface to its data sources.

Sample applications modeled after those included with the shadow
password suite are included.

%description -l pl.UTF-8
Biblioteka libuser implementuje ustandaryzowany interfejs do
manipulowania i administrowania kontami użytkowników i grup.
Wykorzystuje system wtyczek backendów współpracujących ze źródłami
danych.

Do pakietu dołączone są przykładowe aplikacje korzystające z
biblioteki, opracowane na podstawie odpowiedników z pakietu shadow.

%package devel
Summary:	Files needed for developing applications which use libuser
Summary(pl.UTF-8):	Pliki do tworzenia aplikacji wykorzystujących libuser
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel

%description devel
The libuser-devel package contains header and other files useful for
developing applications with libuser.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe i inne przydatne do tworzenia
aplikacji wykorzystujących bibliotekę libuser.

%package -n python-libuser
Summary:	Python bindings for the libuser library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki libuser
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-libuser
This package contains the Python bindings for the libuser library,
which provides a Python API for manipulating and administering user
and group accounts.

%description -n python-libuser -l pl.UTF-8
Ten pakiet zawiera wiązania Pythona do biblioteki libuser. Udostępnia
pythonowe API do manipulowania i administrowania kontami użytkowników
i grup.

%prep
%setup -q
%patch0 -p0

%build
%configure \
	--with-selinux \
	--with-ldap \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la
rm $RPM_BUILD_ROOT%{py_sitedir}/*.la

%find_lang %{name}

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO docs/*.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libuser.conf
%attr(755,root,root) %{_bindir}/lchfn
%attr(755,root,root) %{_bindir}/lchsh
%attr(755,root,root) %{_libdir}/libuser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuser.so.1
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libuser_files.so
%{_libdir}/%{name}/libuser_ldap.so
%{_libdir}/%{name}/libuser_shadow.so
%attr(755,root,root) %{_sbindir}/lchage
%attr(755,root,root) %{_sbindir}/lgroupadd
%attr(755,root,root) %{_sbindir}/lgroupdel
%attr(755,root,root) %{_sbindir}/lgroupmod
%attr(755,root,root) %{_sbindir}/lid
%attr(755,root,root) %{_sbindir}/lnewusers
%attr(755,root,root) %{_sbindir}/lpasswd
%attr(755,root,root) %{_sbindir}/luseradd
%attr(755,root,root) %{_sbindir}/luserdel
%attr(755,root,root) %{_sbindir}/lusermod
%{_mandir}/man1/lchage.1*
%{_mandir}/man1/lchfn.1*
%{_mandir}/man1/lchsh.1*
%{_mandir}/man1/lgroupadd.1*
%{_mandir}/man1/lgroupdel.1*
%{_mandir}/man1/lgroupmod.1*
%{_mandir}/man1/lid.1*
%{_mandir}/man1/lnewusers.1*
%{_mandir}/man1/lpasswd.1*
%{_mandir}/man1/luseradd.1*
%{_mandir}/man1/luserdel.1*
%{_mandir}/man1/lusermod.1*
%{_mandir}/man5/libuser.conf.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libuser.so
%{_libdir}/libuser.la
%{_includedir}/libuser
%{_pkgconfigdir}/libuser.pc
%{_gtkdocdir}/libuser

%files -n python-libuser
%defattr(644,root,root,755)
%doc python/modules.txt
%attr(755,root,root) %{py_sitedir}/libusermodule.so
