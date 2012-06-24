Summary:	LZO -- a real-time data compression library
Summary(pl):	LZO -- biblioteka kompresji danych w czasie rzeczywistym
Name:		lzo
Version:	1.07
Release:	4
Group:		Libraries
License:	GPL
Source0:	http://wildsau.idv.uni-linz.ac.at/mfx/download/lzo/%{name}-%{version}.tar.gz
URL:		http://wildsau.idv.uni-linz.ac.at/mfx/lzo.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LZO is a portable lossless data compression library written in ANSI C.
It implements a number of algorithms with the following features:
- Decompression is simple and *very* fast.
- Requires no memory for decompression.
- Compression is pretty fast.
- Requires 64 kB of memory for compression.
- Allows you to dial up extra compression at a speed cost in the
  compressor. The speed of the decompressor is not reduced.
- Includes compression levels for generating pre-compressed data which
  achieve a quite competitive compression ratio.
- There is also a compression level which needs only 8 kB for
  compression.
- Supports overlapping compression and in-place decompression.
- Algorithm is thread safe.
- Algorithm is lossless.

%description -l pl
LZO jest przeno�n� bibliotek� do bezstratnej kompresji danych,
napisan� w ANZI C. Zaimplementowano w niej kilka algorytm�w 
uzyskuj�c nast�puj�c� funkcjonalno��:

- dekompresja jest prosta i *bardzo* szybka
- dekompresja nie zu�ywa dodatkowej pami�ci
- kompresja jest ca�kiem szybka
- kompresja wymaga 64kb pami�ci
- pozwala zwi�kszy� kompresj� zmniejszaj�c szybko�� kompresji, przy czym
  szybko�� dekompresji pozostaje niezmieniona
- zawiera poziomy kompresji do generowania prekompresowanych danych,
  osi�gaj�ce ca�kiem dobry stopie� kompresji
- istnieje poziom kompresji wymagaj�cy przy kompresowaniu jedynie 8kb pami�ci
- obs�uguje kompresj� nak�adaj�c� i 'in-place'
- algorytm nadaje si� do bezpiecznego wykorzystania w �rodowisku wielow�tkowym
- algorytm jest bezstratny

%package devel
Summary:	LZO -- a real-time data compression library
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for LZO.

%description devel -l pl
Pliki nag��wkowe dla LZO

%package static
Summary:	LZO static library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
LZO static library.

%description static -l pl
Biblioteki statyczne dla LZO

%prep
%setup  -q
%build
%configure2_13 \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
