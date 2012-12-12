%define gir_major 3.0
%define major 0
%define libname %mklibname %{name} %{major}
%define girname %mklibname %{name}-gir %{gir_major}
%define develname %mklibname -d %{name}

Summary:	Mutter window manager
Name:		mutter
Version:	3.7.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://ftp.gnome.org/pub/gnome/sources/mutter/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mutter/3.7/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	intltool
BuildRequires:	zenity
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xrender)

Requires: GConf2
Requires: zenity

%description
Mutter is a simple window manager that integrates nicely with 
GNOME 2.

%package -n %{libname}
Summary:	Libraries for Mutter
Group:		System/Libraries
Obsoletes:	%{_lib}mutter-private0 < %{version}

%description -n %{libname}
This package contains libraries used by Mutter.

%package -n %{girname}
Summary: GObject Introspection interface description for %{name}
Group: System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:	Libraries and include files with Mutter
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d %{name}-private 0
Obsoletes:	%{_lib}mutter-private-devel < %{version}

%description -n %{develname}
This package provides the necessary development libraries and include 
files to allow you to develop with Mutter.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper \
	--enable-compile-warnings=no

%make

%install
%makeinstall_std
%find_lang %{name} 

%files -f %{name}.lang
%doc README COPYING NEWS HACKING 
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/GConf/gsettings/mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_datadir}/gnome/wm-properties/%{name}-wm.desktop
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/default.so
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{girname}
%{_libdir}/%{name}/Meta-%{gir_major}.typelib

%files -n %{develname}
%doc ChangeLog
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/%{name}/Meta-%{gir_major}.gir



%changelog
* Tue Nov 13 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.2-1
- update to 3.6.2

* Tue Oct  2 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Mon Apr 30 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.1-1
+ Revision: 794618
- new version 3.4.1

* Mon Mar 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.2-1
+ Revision: 782126
- new version 3.2.2
- cleaned up spec

* Wed May 25 2011 Götz Waschk <waschk@mandriva.org> 3.0.2.1-1
+ Revision: 679083
- update to new version 3.0.2.1

* Wed May 25 2011 Götz Waschk <waschk@mandriva.org> 3.0.2-1
+ Revision: 679071
- update to new version 3.0.2

* Tue Apr 26 2011 Götz Waschk <waschk@mandriva.org> 3.0.1-1
+ Revision: 659246
- update to new version 3.0.1

* Tue Apr 05 2011 Funda Wang <fwang@mandriva.org> 3.0.0-1
+ Revision: 650792
- new version 3.0.0

  + John Balcaen <mikala@mandriva.org>
    - Fix BR for libcanberra-gtk-devel

* Mon Jun 21 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.1-4mdv2011.0
+ Revision: 548403
- Patch3 (GIT): prevent possible DOS with too much damage events

* Tue May 25 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.1-3mdv2010.1
+ Revision: 545988
- Patch2: ensure text is locale encoded for Zenity (GNOME bug 617536)

* Mon May 10 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.1-2mdv2010.1
+ Revision: 544363
- Patch0 (GIT): improves damage performance
- Patch1 (GIT): fix flashes when windows are created

* Fri Mar 19 2010 Götz Waschk <waschk@mandriva.org> 2.29.1-1mdv2010.1
+ Revision: 525203
- new version
- drop patches

* Wed Mar 17 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.0-3mdv2010.1
+ Revision: 524470
- Patch1 (GIT): remove workaround for old intel drivers

* Wed Mar 17 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.0-2mdv2010.1
+ Revision: 524226
- Patch0 (GIT): fix build with latest clutter

* Fri Feb 19 2010 Götz Waschk <waschk@mandriva.org> 2.29.0-1mdv2010.1
+ Revision: 507979
- new version
- new API

* Thu Feb 11 2010 Götz Waschk <waschk@mandriva.org> 2.28.1-0.20100211.1mdv2010.1
+ Revision: 504235
- git snapshot

* Thu Nov 26 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-2mdv2010.1
+ Revision: 470382
- add explicit dep on libmutter

* Thu Oct 08 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 456006
- new version
- update file list

* Wed Sep 16 2009 Götz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 443442
- update to new version 2.27.5

* Sat Sep 05 2009 Götz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 432059
- new version

* Sat Aug 29 2009 Götz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 422131
- update to new version 2.27.3

* Wed Aug 12 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-2mdv2010.0
+ Revision: 415264
- move typelib to the library package

* Tue Aug 11 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 414699
- new version
- drop patches
- reenable --as-needed

* Thu Aug 06 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-3mdv2010.0
+ Revision: 410985
- fix for bug #52685

* Thu Jul 30 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-2mdv2010.0
+ Revision: 404615
- fix the patch
- patch for new clutter
- drop patches

* Fri Jul 17 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 396803
- initial package
- drop metacity theme patch
- build without --as-neede
- rename

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 2.27.0-1mdv2010.0
+ Revision: 374234
- new version
- drop patches 5,6

* Wed Apr 15 2009 Frederic Crozat <fcrozat@mandriva.com> 2.26.0-3mdv2009.1
+ Revision: 367437
- Fix default theme for One and Powerpack

* Wed Apr 01 2009 Frederic Crozat <fcrozat@mandriva.com> 2.26.0-2mdv2009.1
+ Revision: 363325
- Add libcanberra-devel as buildrequires
- Update default theme color for Mdv 2009.1
- Patch5 (SVN): fix struts with auto-hidden panel (GNOME bug #572573)
- Patch6 (SVN): use libcanberra to play sound events (GNOME bug #557921)

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356168
- update to new version 2.26.0

* Sun Feb 01 2009 Götz Waschk <waschk@mandriva.org> 2.25.144-1mdv2009.1
+ Revision: 336232
- update to new version 2.25.144

* Sat Dec 27 2008 Götz Waschk <waschk@mandriva.org> 2.25.89-1mdv2009.1
+ Revision: 319930
- new version
- drop patch 5

* Thu Dec 18 2008 Götz Waschk <waschk@mandriva.org> 2.25.55-1mdv2009.1
+ Revision: 315967
- new version
- update patch 0

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 2.25.34-1mdv2009.1
+ Revision: 309097
- update to new version 2.25.34

* Wed Nov 26 2008 Götz Waschk <waschk@mandriva.org> 2.25.13-1mdv2009.1
+ Revision: 306913
- update to new version 2.25.13

* Mon Nov 24 2008 Götz Waschk <waschk@mandriva.org> 2.25.8-1mdv2009.1
+ Revision: 306234
- disable werror to make it build
- depend on zenity
- new version
- update file list

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 2.25.5-2mdv2009.1
+ Revision: 301477
- rebuilt against new libxcb

* Thu Oct 23 2008 Götz Waschk <waschk@mandriva.org> 2.25.5-1mdv2009.1
+ Revision: 296642
- update to new version 2.25.5

* Wed Oct 22 2008 Götz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 296547
- new version
- drop patches 0,1

* Wed Oct 22 2008 Götz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 296387
- fix build deps
- update file list
- new version
- patch to add sources missing from the tarball
- patch to fix linking
- update patch 2

* Tue Oct 14 2008 Götz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 293623
- new version
- update file list

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286846
- new version

* Tue Sep 09 2008 Götz Waschk <waschk@mandriva.org> 2.23.610-1mdv2009.0
+ Revision: 283192
- new version
- update file list

* Wed Sep 03 2008 Götz Waschk <waschk@mandriva.org> 2.23.377-1mdv2009.0
+ Revision: 279925
- new version

* Wed Sep 03 2008 Götz Waschk <waschk@mandriva.org> 2.23.233-1mdv2009.0
+ Revision: 279562
- new version
- update file list

* Tue Aug 26 2008 Frederic Crozat <fcrozat@mandriva.com> 2.23.144-3mdv2009.0
+ Revision: 276236
- Update default theme to Ia Ora Smooth for all distro flavors

* Mon Aug 25 2008 Frederic Crozat <fcrozat@mandriva.com> 2.23.144-2mdv2009.0
+ Revision: 275900
- Patch5 (Fedora): don't move window across workspaces when raising (Mdv bug #25009) (GNOME bug #482354)

* Mon Aug 18 2008 Frederic Crozat <fcrozat@mandriva.com> 2.23.144-1mdv2009.0
+ Revision: 273301
- Release 2.23.144

* Wed Jul 23 2008 Frederic Crozat <fcrozat@mandriva.com> 2.23.55-2mdv2009.0
+ Revision: 242116
- Add xinerama devel libs to BR, ensure Xinerama support is always built

* Mon Jul 14 2008 Götz Waschk <waschk@mandriva.org> 2.23.55-1mdv2009.0
+ Revision: 234435
- new version

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 2.23.34-1mdv2009.0
+ Revision: 231170
- new version
- update license
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 09 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183169
- new version

* Tue Mar 04 2008 Frederic Crozat <fcrozat@mandriva.com> 2.21.21-2mdv2008.1
+ Revision: 178418
- Change theme for download and desktop meta-class, for Mandriva 2008.1

* Thu Feb 28 2008 Götz Waschk <waschk@mandriva.org> 2.21.21-1mdv2008.1
+ Revision: 175974
- new version

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 2.21.13-1mdv2008.1
+ Revision: 165743
- new version

* Mon Feb 04 2008 Götz Waschk <waschk@mandriva.org> 2.21.8-1mdv2008.1
+ Revision: 161960
- new version
- drop patches 5,6

* Fri Feb 01 2008 Frederic Crozat <fcrozat@mandriva.com> 2.21.5-4mdv2008.1
+ Revision: 161162
- Disable compositing for now, too many drivers have still buggy compositing support

  + Götz Waschk <waschk@mandriva.org>
    - remove wonderland theme

* Fri Dec 28 2007 Frederic Crozat <fcrozat@mandriva.com> 2.21.5-3mdv2008.1
+ Revision: 138764
- Patch6 (SVN): fix glitches in compositor (GNOME bug #504876, fix shadows)

* Thu Dec 27 2007 Frederic Crozat <fcrozat@mandriva.com> 2.21.5-2mdv2008.1
+ Revision: 138445
- Patch5 (SVN): use Composite Overlay Window from XComposite >= 0.3

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 19 2007 Götz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 133880
- new version
- drop patch 3

* Wed Dec 19 2007 Frederic Crozat <fcrozat@mandriva.com> 2.21.3-2mdv2008.1
+ Revision: 133820
- Remove source2 and patch3 (no longer used)
- Patch3 (SVN): new compositor code, from Ian Holmes
- Patch4 : enable compositor mode by default

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Götz Waschk <waschk@mandriva.org> 2.21.3-1mdv2008.1
+ Revision: 120712
- new version

* Sun Nov 18 2007 Götz Waschk <waschk@mandriva.org> 2.21.2-1mdv2008.1
+ Revision: 109889
- new version

* Mon Nov 12 2007 Götz Waschk <waschk@mandriva.org> 2.21.1-1mdv2008.1
+ Revision: 108092
- new version
- new version

* Sun Sep 16 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 88438
- new version

* Thu Sep 06 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.55-2mdv2008.0
+ Revision: 81034
- Migrate default theme when upgrading from old distribution

* Tue Aug 07 2007 Götz Waschk <waschk@mandriva.org> 2.19.55-1mdv2008.0
+ Revision: 59865
- update file list
- new version
- drop patch 4
- call intltoolize to fix build

* Thu Aug 02 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.34-2mdv2008.0
+ Revision: 58081
- Patch4: fix kill dialog text with non-UTF8 locale

* Tue Jul 24 2007 Götz Waschk <waschk@mandriva.org> 2.19.34-1mdv2008.0
+ Revision: 54918
- new version
- new devel naming scheme

* Mon Jun 18 2007 Götz Waschk <waschk@mandriva.org> 2.19.21-1mdv2008.0
+ Revision: 40820
- new version

* Mon Jun 11 2007 Götz Waschk <waschk@mandriva.org> 2.19.13-1mdv2008.0
+ Revision: 38000
- new version

* Mon Jun 04 2007 Götz Waschk <waschk@mandriva.org> 2.19.8-1mdv2008.0
+ Revision: 35201
- new version

* Tue Apr 24 2007 Götz Waschk <waschk@mandriva.org> 2.19.5-1mdv2008.0
+ Revision: 17809
- new version

* Wed Apr 18 2007 Götz Waschk <waschk@mandriva.org> 2.19.3-1mdv2008.0
+ Revision: 14423
- new version
- update file list

