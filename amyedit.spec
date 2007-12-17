%define name	amyedit
%define version	1.0
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	A lightweight editor for LaTeX files
Version: 	%{version}
Release: 	%{release}

Source:		http://kent.dl.sourceforge.net/sourceforge/amyedit/%{name}-%{version}.tar.bz2
URL:		http://amyedit.sourceforge.net/
License:	GPL
Group:		Publishing
BuildRequires:	perl(XML::Parser)
BuildRequires:	gtkmm2.4-devel
BuildRequires:	aspell-devel
BuildRequires:  gtksourceview-devel

%description
AmyEdit is a LaTeX editor written to allow users to easily create LaTeX
documents in a simple, user friendly enviroment. Its main requirement is that
it remains lightweight whilst still having a large number of useful features.

AmyEdit is being designed to run on a fairly old laptop, (a P300 with 64 MB of
RAM), running gedit on this is painfully slow, even after the 30 second
startup time has elapsed.

%prep
%setup -q

%build
aclocal
autoreconf
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="editors_section.png" needs="x11" title="AmyEdit" longtitle="Lightweight LaTeX editor" section="Office/Publishing" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=AmyEdit
Comment=Lightweight LaTeX editor
Exec=%{_bindir}/%{name}
Icon=editors_section
Terminal=false
Type=Application
Categories=GNOME;GTK;X-MandrivaLinux-Office-Publishing;Graphics;Office;Viewer;
EOF

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*
%{_menudir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop

