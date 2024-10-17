Summary: Library that parses MXP stream
Name: libmxp
Version: 0.2.4
Release: 3
Source0: http://www.kmuddy.com/libmxp/files/%name-%version.tar.gz
License: LGPLv2+
Group: Development/C++
BuildRequires: cmake
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: https://www.kmuddy.com

%description
Library that parses MXP stream.

%define libname %mklibname mxp 0
%package -n %libname
Summary: Library file for mxp
Group: Development/C++

%description -n %libname
This package contains library files of libmxp.

%define develname %mklibname -d mxp
%package -n %develname
Summary: mxp devellopment files
Group: Development/C++
Requires: %libname = %version
Provides: %name-devel = %version-%release

%description -n %develname
This package contains files need to build applications using libmxp.

%prep
%setup -q -n %name-%version

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.0*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog README* NEWS
%_libdir/*.so
%_includedir/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-2mdv2011.0
+ Revision: 609760
- rebuild

* Fri Dec 11 2009 Funda Wang <fwang@mandriva.org> 0.2.4-1mdv2010.1
+ Revision: 476281
- iBR cmake
- new version 0.2.4

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 0.2.2-2mdv2010.0
+ Revision: 438714
- rebuild

* Sun Dec 07 2008 Funda Wang <fwang@mandriva.org> 0.2.2-1mdv2009.1
+ Revision: 311531
- import libmxp


