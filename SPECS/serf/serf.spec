# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           serf
Version:        1.3.10
Release:        %autorelease
Summary:        High-performance asynchronous HTTP client library
License:        Apache-2.0
URL:            https://serf.apache.org/
VCS:            git:https://github.com/apache/serf.git
#!RemoteAsset:  sha256:be81ef08baa2516ecda76a77adf7def7bc3227eeb578b9a33b45f7b41dc064e6
Source0:        https://archive.apache.org/dist/serf/serf-%{version}.tar.bz2
# BuildSystem:  No supported build system (uses SCons)

BuildRequires:  scons
BuildRequires:  pkgconfig(apr-1)
BuildRequires:  pkgconfig(apr-util-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
Apache Serf is a high-performance, asynchronous HTTP client library
built on top of the Apache Portable Runtime (APR). It multiplexes
connections, running read/write communication asynchronously to
provide high performance operation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and development libraries
needed for building applications that use the serf library.

%prep
%setup -q -n %{name}-%{version}

%build
scons %{?_smp_mflags} \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    APR=%{_prefix} \
    APU=%{_prefix} \
    OPENSSL=%{_prefix} \
    ZLIB=%{_prefix}

%install
scons install --install-sandbox=%{buildroot} PREFIX=%{_prefix}
rm -f %{buildroot}%{_libdir}/libserf-1.a

# Test code incompatible with GCC 14
%check

%files
%license LICENSE NOTICE
%{_libdir}/libserf-1.so.*

%files devel
%{_includedir}/serf-1
%{_libdir}/libserf-1.so
%{_libdir}/pkgconfig/serf-1.pc

%changelog
%autochangelog
