Name:       gdbm
Summary:    GNU Database Routines
Version:    1.8.3
Release:    2
Group:      System/Libraries
License:    GPLv2+ and LGPLv2+
URL:        http://www.gnu.org.ua/software/gdbm
Source0:    http://ftp.gnu.org/pub/gnu/gdbm/gdbm-%{version}.tar.bz2
Patch0:     gdbm-%{version}.dif
Patch1:     gdbm-protoize_dbm_headers.patch
Patch2:     gdbm-prototype_static_functions.patch
Patch3:     gdbm-fix_testprogs.patch
Patch4:     gdbm-destdir.patch
Patch5:     gdbm-stamp.patch
Patch6:     gdbm-aarch64.patch

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

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
%setup -q -n %{name}-%{version}

# gdbm-%{version}.dif
%patch0 -p1
# gdbm-protoize_dbm_headers.patch
%patch1 -p1
# gdbm-prototype_static_functions.patch
%patch2 -p1
# gdbm-fix_testprogs.patch
%patch3 -p1
# gdbm-destdir.patch
%patch4 -p1
# gdbm-stamp.patch
%patch5 -p1
%patch6 -p1

%build
aclocal
autoreconf --force --install
export CFLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack"

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m0644 -t $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
        ChangeLog NEWS README

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_prefix}/%{_lib}/libgdbm.so.3
%{_prefix}/%{_lib}/libgdbm.so.3.0.0

%files devel
%defattr(-,root,root,-)
%{_prefix}/%{_lib}/libgdbm.so
/usr/include/gdbm.h

%files doc
%defattr(-,root,root,-)
%{_infodir}/%{name}*.*
%{_mandir}/man*/*%{name}.*
%{_docdir}/%{name}-%{version}
