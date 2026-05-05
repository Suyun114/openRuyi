# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           subversion
Version:        1.14.5
Release:        %autorelease
Summary:        A Modern Concurrent Version Control System
License:        Apache-2.0
URL:            https://subversion.apache.org/
VCS:            git:https://github.com/apache/subversion.git
#!RemoteAsset:  sha256:e78a29e7766b8b7b354497d08f71a55641abc53675ce1875584781aae35644a1
Source0:        https://downloads.apache.org/subversion/subversion-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --with-apr=%{_prefix}
BuildOption(conf):  --with-apr-util=%{_prefix}
BuildOption(conf):  --with-serf=%{_prefix}
BuildOption(conf):  --with-sasl=%{_prefix}
BuildOption(conf):  --with-libmagic=%{_prefix}
BuildOption(conf):  --with-zlib=%{_prefix}
BuildOption(conf):  --with-lz4=%{_prefix}
BuildOption(conf):  --with-utf8proc=%{_prefix}
BuildOption(conf):  --with-sqlite=%{_prefix}
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-local-library-preloading

BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  pkgconfig(apr-1)
BuildRequires:  pkgconfig(apr-util-1)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(serf-1)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)

Provides:       svn = %{version}-%{release}

%description
Subversion is a concurrent version control system which enables one
or more users to collaborate in developing and maintaining a
hierarchy of files and directories while keeping a history of all
changes. Subversion only stores the differences between versions,
instead of every complete file.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(apr-1)

%description    devel
This package contains the header files and development libraries
needed for building applications that use Subversion.

%install -a
rm -f %{buildroot}%{_libdir}/libsvn*.la
%find_lang %{name}

%check
# gnome-keyring not available; crypto-test requires it
rm -f subversion/tests/libsvn_subr/crypto-test
make check CLEANUP=yes

%files -f %{name}.lang
%license LICENSE NOTICE
%doc BUGS COMMITTERS INSTALL README CHANGES
%{_bindir}/svn*
%{_mandir}/man*/*svn*
%{_libdir}/libsvn_*.so.*

%files devel
%{_includedir}/subversion-1
%{_libdir}/libsvn_*.so
%{_datadir}/pkgconfig/libsvn_*.pc

%changelog
%autochangelog
