%define lib_major 0
%define libname %mklibname %{name}-private %{lib_major}
%define libnamedev %mklibname -d %{name}-private
%define startup_notification_version 0.4

Summary: Mutter window manager
Name: mutter
Version: 2.27.1
Release: %mkrel 1
URL: http://ftp.gnome.org/pub/gnome/sources/mutter/
Source0: http://ftp.gnome.org/pub/GNOME/sources/mutter/%{name}-%{version}.tar.bz2
#gw http://bugzilla.gnome.org/show_bug.cgi?id=562106
Patch0: metacity-2.25.55-disable-werror.patch
# (fc) 2.21.3-2mdv enable compositor by default
Patch4: metacity-enable-compositor.patch
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
BuildRequires: clutter-devel >= 0.9.3


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
%patch0 -p1 -b .werror
# don't enable compositor by default, too many drivers are buggy currently
#%patch4 -p1 -b .enable-compositor

#needed by patch 0
autoconf

%build
#needed for gobject-introspection build
%define _disable_ld_as_needed 1
%configure2_5x 
%make

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

%files -n %{libnamedev}
%defattr(-,root,root)
%doc ChangeLog
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*
%_libdir/%name/Meta-2.27.gir
%_libdir/%name/Meta-2.27.typelib

