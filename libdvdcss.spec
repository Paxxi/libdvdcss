%define name 	libdvdcss
%define version	1.2.2
%define release	1

%define major  	2
%define libname %{name}%{major}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:        Library for accessing DVDs like block devices with transparent decryption
Source:		%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Libraries
URL:		http://www.videolan.org/libdvdcss/
Packager:	Yves Duret <yduret@mandrakesoft.com>
BuildRoot:	%_tmppath/%name-%version-%release-root
Conflicts:	libdvdcss0.0.1, libdvdcss0.0.2

%description
libdvdcss is a simple library designed for accessing DVDs like a block device
without having to bother about the decryption. The important features are:
 * Portability: currently supported platforms are GNU/Linux, FreeBSD, NetBSD,
   OpenBSD, BSD/OS, BeOS, Windows 95/98, Windows NT/2000, MacOS X, Solaris,
   HP-UX and OS/2.
 * Adaptability: unlike most similar projects, libdvdcss doesn't require the
   region of your drive to be set and will try its best to read from the disc
   even in the case of a region mismatch.
 * Simplicity: a DVD player can be built around the libdvdcss API using no
   more than 4 or 5 library calls.

%package -n %{libname}
Summary:        Library for accessing DVDs like block devices with transparent decryption
Group:          System/Libraries
Provides:       %name = %version-%release

%description -n %{libname}
libdvdcss is a simple library designed for accessing DVDs like a block device
without having to bother about the decryption. The important features are:
 * Portability: currently supported platforms are GNU/Linux, FreeBSD, NetBSD,
   OpenBSD, BSD/OS, BeOS, Windows 95/98, Windows NT/2000, MacOS X, Solaris,
   HP-UX and OS/2.
 * Adaptability: unlike most similar projects, libdvdcss doesn't require the
   region of your drive to be set and will try its best to read from the disc
   even in the case of a region mismatch.
 * Simplicity: a DVD player can be built around the libdvdcss API using no
   more than 4 or 5 library calls.

%package -n %{libname}-devel
Summary:        Development tools for programs which will use the %{name} library
Group:          Development/C
Requires:	%{libname} = %version-%release
Provides:       %{name}-devel = %version-%release
 
%description -n %{libname}-devel
The %{name}-devel package includes the header files and static libraries
necessary for developing programs which will manipulate DVDs files using
the %{name} library.
 
If you are going to develop programs which will manipulate DVDs, you
should install %{name}-devel.  You'll also need to have the %{name}
package installed.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%clean
rm -rf %buildroot

%post -n %{libname} -p /sbin/ldconfig
 
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc ChangeLog COPYING
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*

%changelog
* Sat Aug 10 2002 Samuel Hocevar <sam@zoy.org> 1.2.2-1
- new upstream release
- even more fixes for the disc/drive region mismatch problem

* Sun Jun 02 2002 Samuel Hocevar <sam@zoy.org> 1.2.1-1
- new upstream release
- fix for a crash on disc/drive region mismatch

* Mon May 20 2002 Samuel Hocevar <sam@zoy.org> 1.2.0-1
- new upstream release
- weird libxalf dependency is gone

* Sun Apr 07 2002 Yves Duret <yduret@mandrakesoft.com> 1.1.1-2plf
- major version is 2 (aka guillaume sux).
- spec clean up: do not rm in %prep, %%buildroot, %%makeinstall_std, %%provides %%version-%%release
- added doc in devel
- sync with cvs's one (%%description,%%files, conflicts).
- fix url

* Sat Apr 06 2002 Guillaume Rousse <rousse@ccr.jussieu.fr> 1.1.1-1plf
- 1.1.1

* Wed Jan 30 2002 Guillaume Rousse <rousse@ccr.jussieu.fr> 1.0.0-3plf 
- new plf extension

* Wed Dec 05 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0.0-3mdk
- removed conflict

* Tue Dec 04 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0.0-2mdk
- contributed to PLF by Yves Duret <yduret@mandrakesoft.com>
- Conflicts: libdvdcss-ogle
- more doc files
- no doc file for devel package

* Fri Nov 30 2001 Yves Duret <yduret@mandrakesoft.com> 1.0.0-1mdk
- version 1.0.0

* Thu Aug 23 2001 Yves Duret <yduret@mandrakesoft.com> 0.0.3-1mdk
- version 0.0.3

* Mon Aug 13 2001 Yves Duret <yduret@mandrakesoft.com> 0.0.2-1mdk
- version 0.0.2

* Tue Jun 19 2001 Yves Duret <yduret@mandrakesoft.com> 0.0.1-1mdk
- first release and first mdk release
