# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-chinese-addons
Version:        5.1.12
Release:        %autorelease
Summary:        Chinese related addon for fcitx5
License:        LGPL-2.1-or-later
URL:            https://github.com/fcitx/fcitx5-chinese-addons
#!RemoteAsset:  sha256:99899bb014d8ffa778657939fb2cf219787cc56eac7cb2f98e5076764d467326
Source0:        https://download.fcitx-im.org/fcitx5/fcitx5-chinese-addons/fcitx5-chinese-addons-%{version}_dict.tar.zst
BuildSystem:    cmake

BuildOption(conf):  -DENABLE_BROWSER=OFF

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fcitx5-lua-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  libime-devel
BuildRequires:  ninja
BuildRequires:  opencc-devel
BuildRequires:  cmake(Qt6)
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Module)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(libcurl)

Requires:       fcitx5-data
Requires:       fcitx5-lua
Requires:       %{name}-data = %{version}-%{release}

%description
This provides pinyin and table input method support for fcitx5.

%package        data
Summary:        Data files of %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       fcitx5-data
Requires:       fcitx5-lua

%description    data
The %{name}-data package provides shared data for %{name}.

%install -a
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%{_bindir}/scel2org5
%{_libdir}/fcitx5/*.so
%{_libdir}/fcitx5/qt6/*.so
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.ChineseAddons.metainfo.xml

%files data
%{_datadir}/fcitx5/addon/*.conf
%{_datadir}/fcitx5/inputmethod/*.conf
%{_datadir}/fcitx5/lua/imeapi/extensions/pinyin.lua
%dir %{_datadir}/fcitx5/pinyin
%{_datadir}/fcitx5/pinyin/*
%dir %{_datadir}/fcitx5/pinyinhelper
%{_datadir}/fcitx5/pinyinhelper/*
%dir %{_datadir}/fcitx5/punctuation
%{_datadir}/fcitx5/punctuation/*
%dir %{_datadir}/fcitx5/chttrans
%{_datadir}/fcitx5/chttrans/*

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%files devel
%{_includedir}/Fcitx5/Module/fcitx-module/*
%{_libdir}/cmake/Fcitx5Module*

%changelog
%autochangelog
