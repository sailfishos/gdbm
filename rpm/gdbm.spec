Name:       gdbm
Summary:    GNU Database Routines
Version:    1.18.1
Release:    1
Group:      System/Libraries
License:    GPLv3+ and LGPLv3+
URL:        http://www.gnu.org.ua/software/gdbm
Source0:    %{name}-%{version}.tar.bz2

Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

BuildRequires:    bison
BuildRequires:    flex
BuildRequires:    gettext
BuildRequires:    texinfo

%description
A static and dynamic library for the GNU database routines.

%package devel
Summary:    Include Files and Libraries mandatory for Development
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
Man and info pages for %{name}.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
autoreconf --force --install --verbose
export CFLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack"

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

mkdir -p "%{buildroot}%{_docdir}/%{name}-%{version}"
install -m 0644 -t "%{buildroot}%{_docdir}/%{name}-%{version}" \
        ChangeLog.cvs NOTE-WARNING NEWS README

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING

%{_bindir}/gdbm_dump
%{_bindir}/gdbmtool
%{_bindir}/gdbm_load
%{_libdir}/libgdbm.so.6
%{_libdir}/libgdbm.so.6.0.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/gdbm.h
%{_libdir}/libgdbm.so

%files doc
%defattr(-,root,root,-)
%{_infodir}/*
%{_mandir}/man*/*
%{_docdir}/%{name}-%{version}
