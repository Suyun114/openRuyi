# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global major_version 5.5

Name:           lua
Version:        5.5.0
Release:        %autorelease
Summary:        Powerful, efficient, lightweight, embeddable scripting language
License:        MIT
URL:            https://www.lua.org/
VCS:            git:https://github.com/lua/lua.git
#!RemoteAsset:  sha256:57ccc32bbbd005cab75bcc52444052535af691789dba2b9016d5c50640d68b3d
Source0:        https://www.lua.org/ftp/lua-%{version}.tar.gz
#!RemoteAsset:  sha256:5e47bbfad7db2965d69580e918ee64edeb8d8d32de404b8dae9ce5c6d76a1472
Source1:        https://www.lua.org/tests/lua-%{version}-tests.tar.gz
Source2:        luaconf.h
Source3:        mit.txt
Source4:        macros.lua
BuildSystem:    autotools

Patch0:         0001-lua-5.4.6-idsize.patch
Patch1:         0002-lua-5.4.0-beta-autotoolize.patch
Patch2:         0003-lua-5.2.2-configure-linux.patch
Patch3:         0004-lua-5.3.0-configure-compat-module.patch

BuildOption(conf):  --with-readline --with-compat-module
BuildOption(build):  LIBS="-lm -ldl"

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(ncurses)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains development files for %{name}.

%package        help
Summary:        Help files for %{name}

%description    help
%{summary}

%description
Lua is a powerful, efficient, lightweight, embeddable scripting language.
It supports procedural programming, object-oriented programming,
functional programming, data-driven programming, and data description.

%prep
# we need to rename the file within the srcdir before patching,
# autosetup is not usable
%setup -q -a 1
mv src/luaconf.h src/luaconf.h.template.in
%patch 0 -p1 -E -z .autoxxx
%patch 1 -p1 -z .idsize
%patch 2 -p1 -z .configure-linux
%patch 3 -p1 -z .configure-compat-all
# Put proper version in configure.ac, patches hardcodes old versions
sed -i 's|5.3.0|%{version}|g' configure.ac
sed -i 's|5.4.0|%{version}|g' configure.ac
sed -i 's|AC_SUBST(\[MAJOR_VERSION\], \[5.4\])|AC_SUBST([MAJOR_VERSION], [%{major_version}])|g' configure.ac
autoreconf -ifv
cp %{SOURCE3} .

%build -p
sed -i 's|@pkgdatadir@|%{_datadir}|g' src/luaconf.h.template
# hack so that only /usr/bin/lua gets linked with readline as it is the
# only one which needs this and otherwise we get License troubles

%install -a
mv %{buildroot}%{_includedir}/luaconf.h %{buildroot}%{_includedir}/luaconf-%{_arch}.h
mkdir -p %{buildroot}/%{_libdir}/lua/%{major_version}
mkdir -p %{buildroot}/%{_datadir}/lua/%{major_version}
install -p -m 644 %{SOURCE2} %{buildroot}%{_includedir}/luaconf.h
install -Dpm 0644 %{SOURCE4} %{buildroot}/%{_rpmmacrodir}/macros.lua
rm -rf %{buildroot}%{_libdir}/*.a

%files
%defattr(-,root,root)
%license mit.txt
%{_bindir}/lua
%{_bindir}/luac
%dir %{_libdir}/lua
%dir %{_libdir}/lua/%{major_version}
%dir %{_datadir}/lua
%dir %{_datadir}/lua/%{major_version}
%{_libdir}/liblua-%{major_version}.so
%{_libdir}/liblua.so

%files devel
%defattr(-,root,root)
%{_includedir}/l*.h
%{_includedir}/l*.hpp
%{_libdir}/pkgconfig/lua.pc
%{_rpmmacrodir}/macros.lua

%files help
%defattr(-,root,root)
%doc README doc/*.html doc/*.css doc/*.png
%{_mandir}/man1/lua*.1*

%changelog
%autochangelog
