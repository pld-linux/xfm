Summary:	An X Window System based file manager
Summary(id):	File manager yang berbasiskan X Window System
Summary(is):	Skráastjóri fyrir X gluggakerfið
Summary(pl):	Menad¿er plików pod X Window System
Summary(sk):	Správca súborov pre systém X Window
Summary(zh_CN):	»ùÓÚ X Window ÏµÍ³µÄÎÄ¼þ¹ÜÀíÆ÷¡£
Name:		xfm
Version:	1.3.2
Release:	13
License:	Freeware
Group:		X11/Applications
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.gz
Source1:	%{name}.wmconfig
Patch0:		%{name}-1.3.2-nobr.patch
Patch1:		%{name}-1.3.2-flags.patch
Patch2:		%{name}-1.3.2-string.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
xfm is a file manager for the X Window System. xfm supports moving
around the directory tree, multiple windows, moving/copying/deleting
files, and launching programs.

%description -l id
xfm adalah file manager untuk X Window System. xfm bisa digunakan
untuk berpindah-pindah direktori, mendukung beberapa window, memindahkan/
mengcopy/menghapus file, dan menjalankan program.

%description -l is
xfm er skráastjóri fyrir X gluggakerfið. Með xfm er hægt að flakka um
skráarkefið, opna marga glugga samtímis, flytja/afrita/þurrka út skrár
og ræsa forrit.

%description -l pl
xfm to menad¿er plików pod X Window System. Obs³uguje przechodzenie po
drzewie katalogów, wiele okienek, przenoszenie/kopiowanie/kasowanie
plików oraz uruchamianie programów.

%description -l sk
xfm je správca súborov pre systém X Window. xfm podporuje pohybovanie sa
po adresárovej ¹truktúre, viacero okien, presúvanie/kopírovanie/mazanie
súborov a spú¹tanie programov.

%description -l zh_CN
xfm ÊÇÓÃÓÚ X Window ÏµÍ³µÄÎÄ¼þ¹ÜÀíÆ÷¡£Xfm Ö§³ÖÄ¿Â¼Ê÷¼äÒÆ¶¯¡¢¶à¸ö´°¿Ú¡¢
#~ "ÒÆ¶¯/¸´ÖÆ/É¾³ýÎÄ¼þºÍÆô¶¯³ÌÐò¡£

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
%{__make} Makefiles
%{__make} RPM_OPT_FLAGS="%{rpmcflags}" \
	XFMLIBDIR=%{_datadir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT \
	XFMLIBDIR=%{_datadir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/xfm

gzip -9nf MANIFEST COPYING ChangeLog README README-1.2

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
%{_mandir}/man1/xfm.1x*
%{_mandir}/man1/xfmtype.1x*
