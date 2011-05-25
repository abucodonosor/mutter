%define lib_major 0
%define libname %mklibname %{name} %{lib_major}
%define libnamedev %mklibname -d %{name}
%define api 3.0

Summary: Mutter window manager
Name: mutter
Version: 3.0.2
Release: %mkrel 1
URL: http://ftp.gnome.org/pub/gnome/sources/mutter/
Source0: http://ftp.gnome.org/pub/GNOME/sources/mutter/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: GL-devel
BuildRequires: libice-devel
BuildRequires: libsm-devel
BuildRequires: libx11-devel
BuildRequires: libxcomposite-devel
BuildRequires: libxcursor-devel
BuildRequires: libxdamage-devel
BuildRequires: libxext-devel
BuildRequires: libxfixes-devel
BuildRequires: libxinerama-devel
BuildRequires: libxrandr-devel
BuildRequires: libxrender-devel
BuildRequires: atk-devel
BuildRequires: gtk+3.0-devel
BuildRequires: clutter-devel
BuildRequires: libGConf2-devel GConf2
BuildRequires: gobject-introspection-devel
BuildRequires: startup-notification-devel
BuildRequires: intltool gnome-doc-utils
BuildRequires: zenity
Requires: %{libname} = %{version}
Requires: GConf2 zenity

%description
Mutter is a simple window manager that integrates nicely with 
GNOME 2.

%package -n %{libname}
Summary:        Libraries for Mutter
Group:          System/Libraries
Obsoletes:	%{_lib}mutter-private0 < %{version}

%description -n %{libname}
This package contains libraries used by Mutter.

%package -n %{libnamedev}
Summary:        Libraries and include files with Mutter
Group:          Development/GNOME and GTK+
Requires:       %name = %{version}
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d %{name}-private 0
Obsoletes:	%{_lib}mutter-private-devel < %{version}

%description -n %{libnamedev}
This package provides the necessary development libraries and include 
files to allow you to develop with Mutter.


%prep
%setup -q

%build
%configure2_5x --disable-static --disable-schemas-install --disable-scrollkeeper --enable-compile-warnings=no
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std

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
%{_libdir}/*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*
%_libdir/%name/Meta-%api.gir
