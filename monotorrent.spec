%define name monotorrent
%define version 0.20
%define release %mkrel 2

Summary: Bittorrent library for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.monotorrent.com/Files/%version/%{name}-%{version}.source.zip
Patch: monotorrent-0.20-pkgconfig.patch
License: MIT
Group: System/Libraries
Url: http://www.monotorrent.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: mono-devel

%description
Monotorrent is an open source bittorrent library.

%prep
%setup -q -c
%patch -p1
chmod +x configure

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
