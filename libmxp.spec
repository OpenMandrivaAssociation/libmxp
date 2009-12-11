Summary: Library that parses MXP stream
Name: libmxp
Version: 0.2.4
Release: %mkrel 1
Source0: http://www.kmuddy.com/libmxp/files/%name-%version.tar.gz
License: LGPLv2+
Group: Development/C++
BuildRequires: cmake
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://www.kmuddy.com

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
