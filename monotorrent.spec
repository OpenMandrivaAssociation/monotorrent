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
Url: https://www.monotorrent.com/
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


%changelog
* Tue Nov 08 2011 Götz Waschk <waschk@mandriva.org> 0.80-2mdv2012.0
+ Revision: 729032
- rebuild

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 0.80-1mdv2011.0
+ Revision: 460836
- new version
- update file list

* Fri Apr 24 2009 Götz Waschk <waschk@mandriva.org> 0.72-1mdv2010.0
+ Revision: 368988
- new version

* Fri Feb 20 2009 Götz Waschk <waschk@mandriva.org> 0.70-1mdv2009.1
+ Revision: 343226
- new version
- new source URL

* Mon Nov 10 2008 Götz Waschk <waschk@mandriva.org> 0.62-1mdv2009.1
+ Revision: 301682
- update to new version 0.62

* Mon Nov 03 2008 Götz Waschk <waschk@mandriva.org> 0.60-1mdv2009.1
+ Revision: 299510
- update to new version 0.60

* Sat Oct 11 2008 Götz Waschk <waschk@mandriva.org> 0.50-1mdv2009.1
+ Revision: 292465
- new version
- update file list

* Sun Jun 22 2008 Götz Waschk <waschk@mandriva.org> 0.40-1mdv2009.0
+ Revision: 227950
- new version

* Wed Apr 30 2008 Götz Waschk <waschk@mandriva.org> 0.30-1mdv2009.0
+ Revision: 199397
- new version
- drop patch
- update file list

* Wed Jan 30 2008 Götz Waschk <waschk@mandriva.org> 0.20-2mdv2008.1
+ Revision: 160154
- fix pkgconfig file

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 0.20-1mdv2008.1
+ Revision: 159156
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 27 2007 Götz Waschk <waschk@mandriva.org> 0.2-1mdv2008.0
+ Revision: 18483
- Import monotorrent



* Thu Apr 26 2007 Götz Waschk <waschk@mandriva.org> 0.2-1mdv2008.0
- initial package
