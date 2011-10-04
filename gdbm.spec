# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       gdbm
Summary:    GNU Database Routines
Version:    1.8.3
Release:    1
Group:      System/Libraries
License:    GPLv2+ and LGPLv2+
URL:        http://directory.fsf.org/GNU/gdbm.html
Source0:    http://ftp.gnu.org/pub/gnu/gdbm/gdbm-%{version}.tar.bz2
Source100:  gdbm.yaml
Patch0:     gdbm-%{version}.dif
Patch1:     gdbm-protoize_dbm_headers.patch
Patch2:     gdbm-prototype_static_functions.patch
Patch3:     gdbm-fix_testprogs.patch
Patch4:     gdbm-destdir.patch
Patch5:     gdbm-stamp.patch
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
# >> setup
# << setup

%build
# >> build pre
aclocal
autoreconf --force --install
export CFLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack"
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
%make_install

%docs_package
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%doc COPYING
%{_prefix}/%{_lib}/libgdbm.so.3
%{_prefix}/%{_lib}/libgdbm.so.3.0.0
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%{_prefix}/%{_lib}/libgdbm.so
/usr/include/gdbm.h
# << files devel

