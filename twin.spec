# this is the tutf major
%define major 0
# tw major
%define twmajor 4
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define debug_package          %{nil}

Summary:	A text mode Windows Manager
Name:		twin
Version:	0.6.2
Release:	4
License:	GPLv2
Group:		Terminals
Url:		http://sourceforge.net/projects/twin/
Source0:	http://downloads.sourceforge.net/twin/%{name}-%{version}.tar.bz2
Requires:	%{libname} = %{version}-%{release}
BuildRequires:	bison
BuildRequires:	pkgconfig(x11)
BuildRequires:	gtk+-devel
BuildRequires:	gpm-devel
BuildRequires:	libggi-devel
BuildRequires:	xpm-devel
BuildRequires:	libltdl-devel

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

%package -n %{develname}
Summary:	Devellopment files from twin
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname %{name}0 -d}

%description -n %{develname}
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
%makeinstall_std

%files
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/twin/system.*
%{_libdir}/twin/.twenvrc.sh
%{_libdir}/twin/.twinrc
# from libname pkg, these are modules not the twin app
%dir %{_libdir}/twin
%dir %{_libdir}/twin/modules
%{_libdir}/twin/modules/*.so.*
%dir %{_libdir}/twin/modules/HW
%{_libdir}/twin/modules/HW/*.so.*
%{_mandir}/man1/%{name}.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%files -n %{libname}
%{_libdir}/libTutf.so.%{major}*
%{_libdir}/libTw.so.%{twmajor}*

%files -n %{develname}
%dir %{_includedir}/Tw
%{_includedir}/Tw/*
%dir %{_includedir}/Tutf
%{_includedir}/Tutf/*
%{_libdir}/*.so
%{_libdir}/*.a
