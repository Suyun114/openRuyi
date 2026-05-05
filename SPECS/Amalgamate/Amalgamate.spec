# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 22cc20dbee8782eb4c4aa09025a647291a94fd75

Name:           Amalgamate
Version:        0+git20120420.22cc20d
Release:        %autorelease
Summary:        C/C++ source amalgamation tool
License:        MIT
URL:            https://github.com/vinniefalco/Amalgamate
#!RemoteAsset:  sha256:f3840e0c1564a024608709c9b6621877f2b403c31c880bc094db67cc048ef8d9
Source0:        https://github.com/vinniefalco/Amalgamate/archive/%{commit}.tar.gz

%description
Amalgamate is a tool for creating an amalgamation from C and C++ sources,
combining multiple source files into a single file for easier distribution.

%prep
%setup -q -n Amalgamate-%{commit}

%build
%{__cxx} %{build_cxxflags} %{build_ldflags} -o amalgamate Amalgamate.cpp juce_core_amalgam.cpp

%install
mkdir -p %{buildroot}%{_bindir}
install -pm0755 amalgamate %{buildroot}%{_bindir}/

%files
%doc CHANGES README.md
%license LICENSE
%{_bindir}/amalgamate

%changelog
%autochangelog
