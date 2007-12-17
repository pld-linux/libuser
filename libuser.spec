Summary:	A user and group account administration library
Name:		libuser
Version:	0.56.6
Release:	1
License:	LGPL v2+
Group:		Base
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	74bd4ad52d81ccf67a8f6cd110add809
Patch0:		%{name}-0.56.6-selinux.patch
BuildRequires:	cyrus-sasl-devel
BuildRequires:	glib2-devel
BuildRequires:	libselinux-devel
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	popt-devel
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libuser library implements a standardized interface for
manipulating and administering user and group accounts. The library
uses pluggable back-ends to interface to its data sources.

Sample applications modeled after those included with the shadow
password suite are included.

%package devel
Summary:	Files needed for developing applications which use libuser
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel

%description devel
The libuser-devel package contains header files, static libraries, and
other files useful for developing applications with libuser.

%package -n python-libuser
Summary:	Python bindings for the libuser library
Group:		Development/Libraries
Requires:	libuser = %{version}-%{release}

%description -n python-libuser
The libuser-python package contains the Python bindings for the
libuser library, which provides a Python API for manipulating and
administering user and group accounts.

%prep
%setup -q
%patch0 -p0

%build
%configure \
	--with-selinux \
	--with-ldap \
	--with-html-dir=%{_datadir}/gtk-doc/html
%{__make}

%clean
rm -fr $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%post	-p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README TODO docs/*.txt
%config(noreplace) %{_sysconfdir}/libuser.conf

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%exclude %{_libdir}/%{name}/*.la

%files -n python-libuser
%defattr(644,root,root,755)
%doc python/modules.txt
%{py_sitedir}/*.so
%exclude %{py_sitedir}/*.la

%files devel
%defattr(644,root,root,755)
%{_includedir}/libuser
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_pkgconfigdir}/*
%{_datadir}/gtk-doc/html/*
