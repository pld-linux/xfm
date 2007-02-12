Summary:	An X Window System based file manager
Summary(de.UTF-8):	X-File-Manager
Summary(es.UTF-8):	Administrador de archivos
Summary(fr.UTF-8):	Gestionnaire de fichiers sous X
Summary(id.UTF-8):	File manager yang berbasiskan X Window System
Summary(is.UTF-8):	Skráastjóri fyrir X gluggakerfið
Summary(pl.UTF-8):	Zarządca plików pod X Window System
Summary(pt_BR.UTF-8):	Gerenciador de arquivos
Summary(sk.UTF-8):	Správca súborov pre systém X Window
Summary(tr.UTF-8):	X dosya yöneticisi
Summary(zh_CN.UTF-8):	基于 X Window 系统的文件管理器。
Name:		xfm
Version:	1.3.2
Release:	18
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.gz
# Source0-md5:	e954ca08ef323d4fa0ec1ac01482b6f9
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-1.3.2-nobr.patch
Patch1:		%{name}-1.3.2-flags.patch
Patch2:		%{name}-1.3.2-string.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
xfm is a file manager for the X Window System. xfm supports moving
around the directory tree, multiple windows, moving/copying/deleting
files, and launching programs.

%description -l de.UTF-8
xfm ist ein Datei-Manager für X-Window, der die Manipulation von
Dateien und Verzeichnissen auf intuitive, leicht verständliche Weise
gestattet und außerdem Integration mit anderen Programmen ermöglicht."

%description -l es.UTF-8
xfm es un administrador de archivos para X Window que permite
manipular archivos y directorios de una manera intuitiva y fácil de
entender, así como permite su extensión con otros programas.

%description -l fr.UTF-8
xfm est un gestionnaire de fichiers pour X Window vous permettant de
manipuler des fichiers et des répertoires de façon intuitive et facile
à comprendre, vous pouvez aussi l'étendre avec d'autres programmes.

%description -l id.UTF-8
xfm adalah file manager untuk X Window System. xfm bisa digunakan
untuk berpindah-pindah direktori, mendukung beberapa window,
memindahkan/ mengcopy/menghapus file, dan menjalankan program.

%description -l is.UTF-8
xfm er skráastjóri fyrir X gluggakerfið. Með xfm er hægt að flakka um
skráarkefið, opna marga glugga samtímis, flytja/afrita/þurrka út skrár
og ræsa forrit.

%description -l pl.UTF-8
xfm to program do zarządzania plikami pod X Window System. Obsługuje
chodzenie po drzewie katalogów, wiele okienek, przenoszenie/
/kopiowanie/kasowanie plików oraz uruchamianie programów.

%description -l pt_BR.UTF-8
O xfm é um gerenciador de arquivos para X Window que permite manipular
arquivos e diretórios de uma maneira intuitiva e fácil de entender,
assim como permite sua extensão com outros programas.

%description -l sk.UTF-8
xfm je správca súborov pre systém X Window. xfm podporuje pohybovanie
sa po adresárovej štruktúre, viacero okien,
presúvanie/kopírovanie/mazanie súborov a spúštanie programov.

%description -l tr.UTF-8
xfm yardımıyla dosyaları ve dizinleri kolayca anlaşılabilir bir
arabirim yardımıyla kontrol edebilirsiniz.

%description -l zh_CN.UTF-8
#~ "移动/复制/删除文件和启动程序。
xfm 是用于 X Window 系统的文件管理器。Xfm 支持目录树间移动、多个窗口、

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
%{__make} Makefiles
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}" \
	XFMLIBDIR=%{_datadir}/%{name} \
	LIBDIR="%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	XFMLIBDIR=%{_datadir}/%{name} \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/xfm.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/xfm.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README-1.2 TODO
%attr(755,root,root) %{_bindir}/xfm
%attr(755,root,root) %{_bindir}/xfmtype
%attr(755,root,root) %{_bindir}/xfm.install
%{_appdefsdir}/Xfm
%dir %{_datadir}/xfm
%{_datadir}/xfm/dot.xfm
%{_datadir}/xfm/bitmaps
%{_datadir}/xfm/pixmaps
%{_desktopdir}/xfm.desktop
%{_pixmapsdir}/xfm.png
%{_mandir}/man1/xfm.1x*
%{_mandir}/man1/xfmtype.1x*
