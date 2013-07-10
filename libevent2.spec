Name:           libevent2
Summary:        An event notification library for event-driven network servers.
Version:        2.0.21
Source:         %sf_download/levent/libevent/libevent-2.0/libevent-%version-stable.tar.gz
URL:            http://monkey.org/~provos/libevent/
Group:          System/Libraries
Release:        1
License:        GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%package -n libevent2-devel
Summary: Development libevent library, its header files and documentation
Group: Development/C
Requires: libevent2 = %version-%release
Provides: libevent2-devel = %version-%release

%description
An event notification library for event-driven network servers.

%description -n libevent2-devel
This package contains the header files, documentation, examples and
development library for use in developing applications that use the
libevent library.

%prep
%setup -q -n libevent-%version-stable

%build

./configure --prefix=%{_prefix} \
        --libdir=%{_libdir}     \
        --mandir=%{_mandir}     \
        --docdir=%_docdir       \
        --disable-static

make

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/libevent*.la

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root)
%_libdir/*
%_bindir/*

%files -n libevent2-devel
%_includedir/*

%changelog
* Thu Jul 11 2013 - TrungTM
- bump to 2.0.21
