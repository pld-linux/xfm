Summary:	An X Window System based file manager.
Name:		xfm
Version:	1.3.2
Release:	13
Copyright:	freeware
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.gz
Source1:	xfm.wmconfig
Patch0:		xfm-1.3.2-nobr.patch
Patch1:		xfm-1.3.2-flags.patch
Patch2:		xfm-1.3.2-string.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Xfm is a file manager for the X Window System. Xfm supports moving
around the directory tree, multiple windows, moving/copying/deleting
files, and launching programs.

Install xfm if you would like to use a graphical file manager program.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
make Makefiles
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" \
	XFMLIBDIR=%{_datadir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

make install install.man DESTDIR=$RPM_BUILD_ROOT \
	XFMLIBDIR=%{_datadir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/xfm

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	MANIFEST COPYING ChangeLog README README-1.2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {MANIFEST,COPYING,ChangeLog,README,README-1.2}.gz
%config %{_sysconfdir}/X11/wmconfig/xfm
%attr(755,root,root) %{_bindir}/xfm
%attr(755,root,root) %{_bindir}/xfmtype
%attr(755,root,root) %{_bindir}/xfm.install
%config %{_libdir}/X11/app-defaults/Xfm
%dir %{_datadir}/xfm
%{_datadir}/xfm/dot.xfm
%{_datadir}/xfm/bitmaps
%{_datadir}/xfm/pixmaps
%{_mandir}/man1/xfm.1x.gz
%{_mandir}/man1/xfmtype.1x.gz