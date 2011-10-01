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
