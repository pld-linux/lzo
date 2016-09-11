Summary:	LZO - a real-time data compression library
Summary(pl.UTF-8):	LZO - biblioteka kompresji danych w czasie rzeczywistym
Name:		lzo
Version:	2.09
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.oberhumer.com/opensource/lzo/download/%{name}-%{version}.tar.gz
# Source0-md5:	c7ffc9a103afe2d1bba0b015e7aa887f
URL:		http://www.oberhumer.com/opensource/lzo/
BuildRequires:	autoconf >= 2.67
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	libtool >= 2:2.0
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

%description -l pl.UTF-8
LZO jest przenośną biblioteką do bezstratnej kompresji danych,
napisaną w ANSI C. Zaimplementowano w niej kilka algorytmów uzyskując
następującą funkcjonalność:
- dekompresja jest prosta i *bardzo* szybka
- dekompresja nie zużywa dodatkowej pamięci
- kompresja jest całkiem szybka
- kompresja wymaga 64kB pamięci
- pozwala zwiększyć kompresję zmniejszając szybkość kompresji, przy
  czym szybkość dekompresji pozostaje niezmieniona
- zawiera poziomy kompresji do generowania prekompresowanych danych,
  osiągające całkiem dobry stopień kompresji
- istnieje poziom kompresji wymagający przy kompresowaniu jedynie 8kB
  pamięci
- obsługuje kompresję nakładającą i 'in-place'
- algorytm nadaje się do bezpiecznego wykorzystania w środowisku
  wielowątkowym
- algorytm jest bezstratny

%package devel
Summary:	LZO header files
Summary(pl.UTF-8):	Pliki nagłówkowe LZO
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LZO.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla LZO.

%package static
Summary:	LZO static library
Summary(pl.UTF-8):	Statyczna biblioteka LZO
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
LZO static library.

%description static -l pl.UTF-8
Biblioteka statyczna LZO.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README THANKS doc/LZO.FAQ doc/LZO.TXT
%attr(755,root,root) %{_libdir}/liblzo2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblzo2.so.2

%files devel
%defattr(644,root,root,755)
%doc doc/LZOAPI.TXT
%attr(755,root,root) %{_libdir}/liblzo2.so
%{_libdir}/liblzo2.la
%{_includedir}/lzo

%files static
%defattr(644,root,root,755)
%{_libdir}/liblzo2.a
