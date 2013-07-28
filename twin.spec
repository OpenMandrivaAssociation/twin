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
%defattr(-,root,root)
%{_libdir}/libTutf.so.%{major}*
%{_libdir}/libTw.so.%{twmajor}*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/Tw
%{_includedir}/Tw/*
%dir %{_includedir}/Tutf
%{_includedir}/Tutf/*
%{_libdir}/*.so
%{_libdir}/*.a


%changelog
* Thu Oct 20 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.6.2-3
+ Revision: 705450
- dropped major from devel pkg
  moved module libs to the app pkg

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.2-2mdv2011.0
+ Revision: 615280
- the mass rebuild of 2010.1 packages

* Mon Feb 15 2010 Shlomi Fish <shlomif@mandriva.org> 0.6.2-1mdv2010.1
+ Revision: 506241
- Upgrade twin to version 0.6.2

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.6.0-3mdv2010.0
+ Revision: 445570
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-2mdv2009.0
+ Revision: 269443
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Jun 06 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-1mdv2009.0
+ Revision: 216301
- update to new version 0.6.0
- drop not needed patch
- spec file clean

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - BR gtk-devel & xpm-devel
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel

  + Olivier Thauvin <nanardon@mandriva.org>
    - Import twin



* Mon Nov 01 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.4.6-5mdk
- fix build with new autotools
- add BuildRequires: X11-devel libgtk+-devel libgpm-devel libggi-devel

* Sat Aug 30 2003 Marcel Pol <mpol@gmx.net> 0.4.6-4mdk
- buildrequires bison

* Sun May 25 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.6-3mdk
- distlint again

* Thu May 01 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.6-2mdk
- distlint fix

* Mon Mar 31 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.6-1mdk
- 2.4.6

* Wed Feb 26 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.5-2mdk
- fix configure

* Tue Feb 25 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.5-1mdk
- First mdk package
