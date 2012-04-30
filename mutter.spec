%define gir_major 3.0
%define major 0
%define libname %mklibname %{name} %{major}
%define girname %mklibname %{name}-gir %{gir_major}
%define develname %mklibname -d %{name}

Summary: Mutter window manager
Name: mutter
Version: 3.4.1
Release: 1
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://ftp.gnome.org/pub/gnome/sources/mutter/
Source0: http://ftp.gnome.org/pub/GNOME/sources/mutter/%{name}-%{version}.tar.xz

BuildRequires:	gnome-doc-utils
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
	--disable-schemas-install \
	--disable-scrollkeeper \
	--enable-compile-warnings=no

%make

%install
%makeinstall_std
%find_lang %{name} 

%files -f %{name}.lang
%doc README COPYING NEWS HACKING 
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
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

