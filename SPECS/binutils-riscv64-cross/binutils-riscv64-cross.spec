# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define cross_target riscv64-openruyi-linux

Name:           binutils-riscv64-cross
Summary:        GNU Binutils cross-compiled for RISC-V (riscv64-openruyi-linux)
License:        GFDL-1.3-only AND GPL-3.0-or-later
Version:        2.46.0
Release:        %autorelease
URL:            https://www.gnu.org/software/binutils/
VCS:            git:https://sourceware.org/git/binutils-gdb.git
#!RemoteAsset:  sha256:0f3152632a2a9ce066f20963e9bb40af7cf85b9b6c409ed892fd0676e84ecd12
Source0:        https://ftpmirror.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2
BuildSystem:    autotools

# Backports from Fedora f44 binutils-riscv-testsuite-fixes.patch:
# https://src.fedoraproject.org/rpms/binutils/blob/f44/f/binutils-riscv-testsuite-fixes.patch
# https://src.fedoraproject.org/rpms/binutils/c/f3398aab: allow data-reloc tests when text relocations are rejected
Patch2000:      2000-ld-riscv-data-reloc-allow-textrels-in-tests.patch
# https://src.fedoraproject.org/rpms/binutils/c/a8edbcb: accept signed RISC-V relaxation immediates without full wildcarding
Patch2001:      2001-ld-riscv-relax-tests-accept-signed-immediates.patch
# https://src.fedoraproject.org/rpms/binutils/c/f6c1766: accept layout-dependent RISC-V Zicfilp PLT offsets
Patch2002:      2002-ld-riscv-zicfilp-accept-variable-plt-offset.patch
# https://src.fedoraproject.org/rpms/binutils/c/9e81b24: xfail RISC-V strip test where annotation symbols remain
Patch2003:      2003-binutils-riscv-xfail-strip-annotation-symbol-tests.patch
# openRuyi: default PIE on RISC-V emits this diagnostic before the second
# undefined reference expected by upstream:
# relocation R_RISCV_CALL_PLT against `bar' which may bind externally can not be used when making a shared object; recompile with -fPIC
Patch2004:      2004-ld-elf-dwarf3-accept-riscv-pie-output.patch

BuildOption(build):  -C build-dir

BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  dejagnu
BuildRequires:  flex
# for the testsuite
BuildRequires:  glibc-static
BuildRequires:  texinfo
BuildRequires:  zlib-ng-compat-static
BuildRequires:  pkgconfig(libzstd)

%description
This package provides the GNU Binary Utilities (as, ld, nm, objcopy,
objdump, readelf, strip, ranlib, ar, etc.) configured for cross-compilation
to the riscv64-openruyi-linux target, enabling the building of programs
for openRuyi RISC-V on a non-RISC-V host.

%conf
# FIXME: upstream problem with C23.
mkdir build-dir
cd build-dir
../configure \
      --build=%{_host} \
      --host=%{_host} \
      --target=%{cross_target} \
      --program-prefix=%{cross_target}- \
      --prefix=%{_prefix} \
      --with-bugurl=%{_vendor_bug_url} \
      --with-separate-debug-dir=%{_prefix}/lib/debug \
      --with-pic --with-system-zlib \
      --enable-plugins \
      --enable-threads \
      --disable-gprofng \
      --enable-colored-disassembly \
      --disable-werror


%install
cd build-dir
make DESTDIR=%{buildroot} install-info install
make DESTDIR=%{buildroot} install-bfd install-opcodes
# Remove files that are not target-specific and would conflict with
# native binutils (libraries, headers, info, man pages).
rm -rf %{buildroot}%{_infodir}
rm -rf %{buildroot}%{_mandir}
rm -rf %{buildroot}%{_includedir}
rm -f  %{buildroot}%{_libdir}/lib*
rm -f  %{buildroot}%{_prefix}/lib/lib*
rm -rf %{buildroot}%{_prefix}/lib/bfd-plugins
rm -rf %{buildroot}%{_prefix}/%{_host}
cd ..

%find_lang %{name} --all-name --generate-subpackages

%check
# Drop upstream-known pr19719 tests pending ld/32983.
# https://sourceware.org/bugzilla/show_bug.cgi?id=32983
sed -i '/"pr19719/d' ld/testsuite/ld-elf/shared.exp

cd build-dir

# Keep successful builds quiet, but print concise DejaGnu context on failure.
make RUNTESTFLAGS='TEST_TIMEOUT=600' check || {
  rc=$?
  dejagnu_sum_regex='^(FAIL|XPASS|ERROR|UNRESOLVED):'
  dejagnu_log_regex='^(FAIL|XPASS|ERROR|UNRESOLVED):|^expected:|^actual:|^output is|^returned with:|ld\.messages has'
  echo "===== DejaGnu unexpected results ====="
  find . -name '*.sum' -exec grep -HnE "$dejagnu_sum_regex" {} + || :
  echo "===== DejaGnu failure context ====="
  find . -name '*.log' -exec grep -HnE -C 5 "$dejagnu_log_regex" {} + || :
  exit $rc
}

%files
%defattr(-,root,root)
%{_bindir}/%{cross_target}-*
%dir %{_prefix}/%{cross_target}
%dir %{_prefix}/%{cross_target}/lib
%{_prefix}/%{cross_target}/lib/ldscripts

%changelog
%autochangelog
