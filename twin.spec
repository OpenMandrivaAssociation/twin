%define name twin 
%define version 0.4.6
%define release %mkrel 5

%define major 0
%define libname %mklibname %name %major
%define libnamedevel %mklibname %name %major -d

Summary: A text mode Windows Manager
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: twin-0.4.6-autoconf-fix.patch.bz2
License: GPL
Group: Terminals
Url: http://linuz.sns.it/~max/twin/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: bison automake1.8
BuildRequires: X11-devel libgtk+-devel libgpm-devel libggi-devel
#Prefix: %{_prefix}

%description
Twin is a text-mode windowing environment:
it draws and manages text windows on a text-mode display,
like X11 does for graphical windows. It has a built-in window manager 
and terminal emulator, and can be used as server for remote clients
in the same style as X11. It can display on Linux console, on X11 
and inside itself. 

%package -n %libname
Summary: Libraries from twin
Group: System/Libraries
Provides: lib%name = %version-%release

%description -n %libname
Twin is a text-mode windowing environment.
This package contain shared libraries to run twin.

%package -n %libnamedevel
Summary: Devellopment files from twin
Group: Development/Other
Requires: %libname = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %libnamedevel
Twin is a text-mode windowing environment.
You need this package to build twin applications

%prep
%setup -q
%patch0 -p1 -b .autoconf

# It stupidly rerun configure on make
perl -pi -e 's|\./configure.*||' Makefile.in

export FORCE_AUTOCONF_2_5=1
aclocal-1.8
autoconf
%configure

%build
# 0.4.5 don't like %make
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/*
%_sbindir/twdm
%_libdir/twin/system.*
%_libdir/twin/.twenvrc.sh
%_libdir/twin/.twinrc
%_mandir/man1/%name.*
%dir %_datadir/%name
%_datadir/%name/*

%files -n %libname
%defattr(-,root,root)
%dir %_libdir/TT
%dir %_libdir/TT/HW
%_libdir/TT/HW/*.so.*
%_libdir/*.so.*
%dir %_libdir/twin
%dir %_libdir/twin/modules
%_libdir/twin/modules/*.so.*
%dir %_libdir/twin/modules/HW
%_libdir/twin/modules/HW/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%dir %_includedir/TT
%_includedir/TT/*
%dir %_includedir/Tutf
%_includedir/Tutf/*
%_libdir/*.so
%_libdir/*.a
%dir %_includedir/Tw
%_includedir/Tw/*
