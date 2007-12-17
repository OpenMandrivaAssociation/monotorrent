%define name monotorrent
%define version 0.2
%define release %mkrel 1

Summary: Bittorrent library for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: MIT
Group: System/Libraries
Url: http://www.monotorrent.com/
BuildArch: noarch
BuildRequires: mono-devel

%description
Monotorrent is an open source bittorrent library.

%prep
%setup -q

%build
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot{%_prefix/lib/pkgconfig,%_datadir}
%makeinstall
#gw noarch
mv %buildroot%_prefix/lib/pkgconfig %buildroot%_datadir

#gw doesn't work yet:
rm -f %buildroot%_bindir/{monotorrent.x,monotorrent-gtk}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO
%dir %_prefix/lib/bitsharp/
%_prefix/lib/bitsharp/*.exe
%_prefix/lib/bitsharp/*.dll
%_datadir/pkgconfig/monotorrent.pc
