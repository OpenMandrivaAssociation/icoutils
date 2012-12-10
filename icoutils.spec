%define name icoutils
%define version 0.29.1
%define release %mkrel 3

Summary: Extract and convert bitmaps from Windows icon and cursor files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://savannah.nongnu.org/download/icoutils/%{name}-%{version}.tar.bz2
License: GPLv3+
Group: Graphics
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://www.nongnu.org/icoutils/
Requires: perl
BuildRequires: libpng-devel

%description
The icoutils are a set of program for extracting and converting
bitmaps from Microsoft Windows icon and cursor files. These files
usually have the extension .ico or .cur, but they can also be
embedded in executables and libraries (.dll-files). (Such embedded
files are referred to as resources.)

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
cp extresso/extresso extresso/genresscript %buildroot/%_bindir
cp extresso/extresso.1 extresso/genresscript.1 %buildroot/%_mandir/man1

%find_lang %{name} 

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS TODO
%_bindir/*
%_mandir/man1/*


%changelog
* Sat Oct 01 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.29.1-3mdv2012.0
+ Revision: 702187
- rebuild for new libpng15

* Mon Jul 11 2011 Götz Waschk <waschk@mandriva.org> 0.29.1-2
+ Revision: 689502
- rebuild

* Fri Jul 09 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.29.1-1mdv2011.0
+ Revision: 549895
- new version 0.29.1

* Mon Feb 22 2010 Emmanuel Andry <eandry@mandriva.org> 0.29.0-1mdv2010.1
+ Revision: 509788
- New version 0.29.0

  + Frederik Himpe <fhimpe@mandriva.org>
    - Fix license

* Mon Aug 17 2009 Frederik Himpe <fhimpe@mandriva.org> 0.28.0-1mdv2010.0
+ Revision: 417430
- update to new version 0.28.0

* Wed Jul 01 2009 Götz Waschk <waschk@mandriva.org> 0.27.0-1mdv2010.0
+ Revision: 391167
- update to new version 0.27.0

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.26.0-4mdv2009.0
+ Revision: 240836
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jul 25 2007 Götz Waschk <waschk@mandriva.org> 0.26.0-2mdv2008.0
+ Revision: 55233
- Import icoutils

