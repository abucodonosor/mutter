%define lib_major 0
%define libname %mklibname %{name}-private %{lib_major}
%define libnamedev %mklibname -d %{name}-private
%define startup_notification_version 0.4
%define api 2.29

Summary: Mutter window manager
Name: mutter
Version: 2.29.1
Release: %mkrel 4
URL: http://ftp.gnome.org/pub/gnome/sources/mutter/
Source0: http://ftp.gnome.org/pub/GNOME/sources/mutter/%{name}-%{version}.tar.bz2
# (fc) 2.29.1-3mdv improves damage performance (GIT)
Patch0: mutter-2.29.1-damages-performance.patch
# (fc) 2.29.1-3mdv fix flashes when windows are created (GIT)
Patch1: mutter-2.29.1-fix-flashes.patch
# (fc) 2.30.1-2mdv ensure text is local encoded for Zenity (GNOME bug #617536)
Patch2: mutter-2.29.1-local-encoding-for-zenity.patch
# (fc) 2.29.1-4mdv prevent possible DOS with too much damage events (GIT)
Patch3: mutter-2.29.1-fix-damages-dos.patch

License: GPLv2+
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: zenity
BuildRequires: libglade2.0-devel
BuildRequires: libGConf2-devel >= 1.1.9
BuildRequires: startup-notification-devel >= %{startup_notification_version}
BuildRequires: libcanberra-devel
BuildRequires: libgtop2.0-devel
BuildRequires: libxinerama-devel
BuildRequires: libxcomposite-devel
BuildRequires: libxdamage-devel
BuildRequires: libxtst-devel
BuildRequires: libmesaglu-devel
BuildRequires: GConf2
BuildRequires: zenity
BuildRequires: intltool
BuildRequires: gnome-doc-utils
BuildRequires: libcanberra-devel
BuildRequires: gobject-introspection-devel gir-repository
BuildRequires: clutter-devel >= 1.2
BuildRequires: gnome-common libtool
Requires:		%{libname} = %{version}

%description
Mutter is a simple window manager that integrates nicely with 
GNOME 2.

%package -n %{libname}
Summary:        Libraries for Mutter
Group:          System/Libraries

%description -n %{libname}
This package contains libraries used by Mutter.

%package -n %{libnamedev}
Summary:        Libraries and include files with Mutter
Group:          Development/GNOME and GTK+
Requires:       %name = %{version}
Requires:		%{libname} = %{version}
Provides:		%{name}-devel = %{version}-%{release}
Provides:		lib%{name}-private-devel = %{version}-%{release}
Obsoletes: %mklibname -d %{name}-private 0

%description -n %{libnamedev}
This package provides the necessary development libraries and include 
files to allow you to develop with Mutter.


%prep
%setup -q
%patch0 -p1 -b .damages-performance
%patch1 -p1 -b .fix-flashes
%patch2 -p1 -b .local-encoding
%patch3 -p1 -b .damage-dos


%build
%configure2_5x 
#parallel build is broken
make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %{name} 

%clean
rm -rf $RPM_BUILD_ROOT

%define schemas %name

%preun
%preun_uninstall_gconf_schemas %{schemas}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING NEWS HACKING 
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_datadir}/applications/%name.desktop
%{_datadir}/gnome/wm-properties/%name-wm.desktop
%{_datadir}/%name
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/default.so
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{lib_major}*
%_libdir/%name/Meta-%api.typelib

%files -n %{libnamedev}
%defattr(-,root,root)
%doc ChangeLog
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*
%_libdir/%name/Meta-%api.gir

