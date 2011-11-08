%define name monotorrent
%define version 0.80
%define fver %version
%define release %mkrel 2

Summary: Bittorrent library for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.monsoon-project.org/jaws/data/files/%{name}-%{fver}.tar.gz
License: MIT
Group: System/Libraries
Url: http://www.monotorrent.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: mono-devel

%description
Monotorrent is an open source bittorrent library.

%prep
%setup -q -n %name-%fver

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot{%_prefix/lib/pkgconfig,%_datadir}
%makeinstall_std
#gw noarch
mv %buildroot%_prefix/lib/pkgconfig %buildroot%_datadir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO
%dir %_prefix/lib/monotorrent
%_prefix/lib/monotorrent/MonoTorrent.dll*
%_prefix/lib/monotorrent/MonoTorrent.Dht.dll*
%_datadir/pkgconfig/monotorrent.pc
%_datadir/pkgconfig/monotorrent.dht.pc
