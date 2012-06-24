Summary:	An X Window System based file manager
Summary(id):	File manager yang berbasiskan X Window System
Summary(is):	Skr�astj�ri fyrir X gluggakerfi�
Summary(pl):	Zarz�dca plik�w pod X Window System
Summary(sk):	Spr�vca s�borov pre syst�m X Window
Summary(zh_CN):	���� X Window ϵͳ���ļ���������
Name:		xfm
Version:	1.3.2
Release:	15
License:	Freeware
Group:		X11/Applications
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
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
xfm er skr�astj�ri fyrir X gluggakerfi�. Me� xfm er h�gt a� flakka um
skr�arkefi�, opna marga glugga samt�mis, flytja/afrita/�urrka �t skr�r
og r�sa forrit.

%description -l pl
xfm to program do zarz�dzania plikami pod X Window System. Obs�uguje
chodzenie po drzewie katalog�w, wiele okienek, przenoszenie/
/kopiowanie/kasowanie plik�w oraz uruchamianie program�w.

%description -l sk
xfm je spr�vca s�borov pre syst�m X Window. xfm podporuje pohybovanie sa
po adres�rovej �trukt�re, viacero okien, pres�vanie/kop�rovanie/mazanie
s�borov a sp��tanie programov.

%description -l zh_CN
xfm ������ X Window ϵͳ���ļ���������Xfm ֧��Ŀ¼�����ƶ���������ڡ�
#~ "�ƶ�/����/ɾ���ļ�����������

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
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Utilities,%{_pixmapsdir}}

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT \
	XFMLIBDIR=%{_datadir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities/xfm.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/xfm.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc MANIFEST COPYING ChangeLog README README-1.2
%{_applnkdir}/Utilities/xfm.desktop
%{_pixmapsdir}/xfm.png
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
