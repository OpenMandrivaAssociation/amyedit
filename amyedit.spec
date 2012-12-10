Name:		amyedit
Summary:	A lightweight editor for LaTeX files
Version:	1.0
Release:	9
Source:		http://kent.dl.sourceforge.net/sourceforge/amyedit/%{name}-%{version}.tar.bz2
Patch0:		amyedit-1.0-keyfile.patch
Patch1:		amyedit-1.0-signal.patch
Patch2:		amyedit-1.0-fix-build.patch
URL:		http://amyedit.sourceforge.net/
License:	GPLv2
Group:		Publishing
BuildRequires:	perl(XML::Parser)
BuildRequires:	gtkmm2.4-devel
BuildRequires:	aspell-devel
BuildRequires:	intltool
BuildRequires:	gtksourceview1-devel

%description
AmyEdit is a LaTeX editor written to allow users to easily create LaTeX
documents in a simple, user friendly enviroment. Its main requirement is that
it remains lightweight whilst still having a large number of useful features.

AmyEdit is being designed to run on a fairly old laptop, (a P300 with 64 MB of
RAM), running gedit on this is painfully slow, even after the 30 second
startup time has elapsed.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
autoreconf -fi
%configure2_5x
%make
										
%install
%makeinstall_std

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=AmyEdit
Comment=Lightweight LaTeX editor
Exec=%{_bindir}/%{name}
Icon=editors_section
Terminal=false
Type=Application
Categories=GNOME;GTK;Graphics;Office;Viewer;
EOF

#%find_lang %name

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*



%changelog
* Sun Dec 05 2010 Funda Wang <fwang@mandriva.org> 1.0-8mdv2011.0
+ Revision: 610339
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 1.0-7mdv2010.1
+ Revision: 508096
- add gentoo patches to make it build

  + Sandro Cazzaniga <kharec@mandriva.org>
    - fix licence, clean spec

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - import amyedit

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Sep 12 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0-3mdv2007.0
- XDG

* Fri Apr 28 2006 Emmanuel Blindauer <blindauer@mandriva.org> 1.0-2mdk
- missing aclocal

* Wed Mar 15 2006 Austin Acton <austin@mandriva.org> 1.0-1mdk
- initial package
