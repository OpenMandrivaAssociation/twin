%define major 0
%define libname %mklibname %{name} %{major}
%define libnamedevel %mklibname %{name} %{major} -d

Summary:	A text mode Windows Manager
Name:		twin
Version:	0.6.0
Release:	%mkrel 2
License:	GPLv2
Group:		Terminals
Url:		http://sourceforge.net/projects/twin/
Source0:	http://downloads.sourceforge.net/twin/%{name}-%{version}.tar.bz2
BuildRequires:	bison
BuildRequires:	X11-devel gtk-devel libgpm-devel libggi-devel xpm-devel
BuildRequires:	libltdl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Twin is a text-mode windowing environment:
it draws and manages text windows on a text-mode display,
like X11 does for graphical windows. It has a built-in window manager 
and terminal emulator, and can be used as server for remote clients
in the same style as X11. It can display on Linux console, on X11 
and inside itself. 

%package -n %{libname}
Summary:	Libraries from twin
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
Twin is a text-mode windowing environment.
This package contain shared libraries to run twin.

%package -n %{libnamedevel}
Summary:	Devellopment files from twin
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libnamedevel}
Twin is a text-mode windowing environment.
You need this package to build twin applications.

%prep
%setup -q

%build
%define _disable_ld_no_undefined 1
%configure2_5x \
	--enable--shlibs=yes \
	--enable--modules=yes \
	--enable--unicode=yes \
	--enable--asm=yes

# 0.4.5 don't like %make
make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/twin/system.*
%{_libdir}/twin/.twenvrc.sh
%{_libdir}/twin/.twinrc
%{_mandir}/man1/%{name}.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*
%dir %{_libdir}/twin
%dir %{_libdir}/twin/modules
%{_libdir}/twin/modules/*.so.*
%dir %{_libdir}/twin/modules/HW
%{_libdir}/twin/modules/HW/*.so.*

%files -n %{libnamedevel}
%defattr(-,root,root)
%dir %{_includedir}/Tw
%{_includedir}/Tw/*
%dir %{_includedir}/Tutf
%{_includedir}/Tutf/*
%{_libdir}/*.so
%{_libdir}/*.a
