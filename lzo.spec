Summary:	LZO - a real-time data compression library
Summary(pl):	LZO - biblioteka kompresji danych w czasie rzeczywistym
Name:		lzo
Version:	1.08
Release:	4
Group:		Libraries
License:	GPL
Source0:	http://www.oberhumer.com/opensource/lzo/download/%{name}-%{version}.tar.gz
# Source0-md5:	ab94d3da364c7cbd5b78d76f1875b0f6
URL:		http://www.oberhumer.com/opensource/lzo/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6
BuildRequires:	libtool
%ifarch %{x86}
BuildRequires:	nasm
%endif
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
napisan� w ANSI C. Zaimplementowano w niej kilka algorytm�w uzyskuj�c
nast�puj�c� funkcjonalno��:
- dekompresja jest prosta i *bardzo* szybka
- dekompresja nie zu�ywa dodatkowej pami�ci
- kompresja jest ca�kiem szybka
- kompresja wymaga 64kB pami�ci
- pozwala zwi�kszy� kompresj� zmniejszaj�c szybko�� kompresji, przy
  czym szybko�� dekompresji pozostaje niezmieniona
- zawiera poziomy kompresji do generowania prekompresowanych danych,
  osi�gaj�ce ca�kiem dobry stopie� kompresji
- istnieje poziom kompresji wymagaj�cy przy kompresowaniu jedynie 8kB
  pami�ci
- obs�uguje kompresj� nak�adaj�c� i 'in-place'
- algorytm nadaje si� do bezpiecznego wykorzystania w �rodowisku
  wielow�tkowym
- algorytm jest bezstratny

%package devel
Summary:	LZO header files
Summary(pl):	Pliki nag��wkowe LZO
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for LZO.

%description devel -l pl
Pliki nag��wkowe dla LZO.

%package static
Summary:	LZO static library
Summary(pl):	Statyczna biblioteka LZO
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
LZO static library.

%description static -l pl
Biblioteka statyczna LZO.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I acconfig/m4
%{__autoconf}
%{__automake}
%configure \
%ifarch %{x86}
	--enable-asm \
%endif
	--enable-shared

%{__make} CFLAGS_O=""

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README THANKS doc/LZO.FAQ doc/LZO.TXT
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/LZOAPI.TXT
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
