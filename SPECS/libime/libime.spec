# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libime
Version:        1.1.14
Release:        %autorelease
Summary:        Library to support generic input method implementation
License:        LGPL-2.1-or-later AND MIT AND BSD-3-Clause
URL:            https://github.com/fcitx/libime
#!RemoteAsset:  sha256:fb5a0b8305a4d3187684b6a8aade0f86b9206b828acc8486ed6c436e9a23259f
Source0:        https://download.fcitx-im.org/fcitx5/libime/libime-%{version}_dict.tar.zst
BuildSystem:    cmake

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

Requires:       %{name}-data

%description
This is a library to support generic input method implementation.

%package        data
Summary:        Data files of %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    data
The %{name}-data package provides shared data for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel

%description    devel
Development files for %{name}.

%files
%license LICENSES/LGPL-2.1-or-later.txt
%{_bindir}/%{name}_*
%{_libdir}/libIMECore.so.*
%{_libdir}/libIMEPinyin.so.*
%{_libdir}/libIMETable.so.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*

%files data
%{_datadir}/%{name}/

%files devel
%{_includedir}/LibIME/
%{_libdir}/cmake/LibIME*
%{_libdir}/libIMECore.so
%{_libdir}/libIMEPinyin.so
%{_libdir}/libIMETable.so

%changelog
%autochangelog
