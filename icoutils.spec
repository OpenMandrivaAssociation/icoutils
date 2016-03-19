Summary:	Extract and convert bitmaps from Windows icon and cursor files
Name:		icoutils
Version:	0.31.0
Release:	5
Source0:	http://savannah.nongnu.org/download/icoutils/%{name}-%{version}.tar.bz2
License:	GPLv3+
Group:		Graphics
URL:		http://www.nongnu.org/icoutils/
BuildRequires:	pkgconfig(libpng)
BuildRequires:	perl(Carp)

%description
The icoutils are a set of program for extracting and converting
bitmaps from Microsoft Windows icon and cursor files. These files
usually have the extension .ico or .cur, but they can also be
embedded in executables and libraries (.dll-files). (Such embedded
files are referred to as resources.)

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std
install -m755 extresso/extresso extresso/genresscript %{buildroot}%{_bindir}
install -m644 extresso/extresso.1 extresso/genresscript.1 %{buildroot}%{_mandir}/man1

%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS ChangeLog NEWS TODO
%{_bindir}/*
%{_mandir}/man1/*
