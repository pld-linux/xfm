Summary: An X Window System based file manager.
Name: xfm
Version: 1.3.2
Release: 13
Copyright: freeware
Group: User Interface/Desktops
Source0: ftp://ftp.x.org/contrib/applications/xfm-1.3.2.tar.gz
Source1: xfm.wmconfig
Patch0: xfm-1.3.2-nobr.patch
Patch1: xfm-1.3.2-flags.patch
Patch2: xfm-1.3.2-string.patch
BuildRoot: /var/tmp/xfm-root

%description
Xfm is a file manager for the X Window System.  Xfm supports moving
around the directory tree, multiple windows, moving/copying/deleting
files, and launching programs.

Install xfm if you would like to use a graphical file manager program.

%prep
%setup -q
%patch0 -p1 -b .nobr
%patch1 -p1 -b .flags
%patch2 -p1 -b .string

%build
xmkmf
make Makefiles
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install install.man
install -m644 $RPM_SOURCE_DIR/xfm.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/xfm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc MANIFEST COPYING ChangeLog README README-1.2
%config /etc/X11/wmconfig/xfm
/usr/X11R6/bin/xfm
/usr/X11R6/bin/xfmtype
/usr/X11R6/bin/xfm.install
%config /usr/X11R6/lib/X11/app-defaults/Xfm
%dir /usr/X11R6/lib/X11/xfm
/usr/X11R6/lib/X11/xfm/dot.xfm
/usr/X11R6/lib/X11/xfm/bitmaps
/usr/X11R6/lib/X11/xfm/pixmaps
/usr/X11R6/man/man1/xfm.1x
/usr/X11R6/man/man1/xfmtype.1x
