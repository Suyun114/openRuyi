# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toktrie
%global full_version 1.7.5
%global pkgname toktrie-1

Name:           rust-toktrie-1
Version:        1.7.5
Release:        %autorelease
Summary:        Rust crate "toktrie"
License:        MIT
URL:            https://github.com/guidance-ai/llguidance
#!RemoteAsset:  sha256:dd0aad1688badacc3a769d7bb38b0f668ef4887bff73aa2d5344d407d8e2f4cb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.95
Requires:       crate(bytemuck-1/default) >= 1.21.0
Requires:       crate(bytemuck-derive-1/default) >= 1.8.1
Requires:       crate(serde-1/default) >= 1.0.217
Requires:       crate(serde-1/derive) >= 1.0.217
Requires:       crate(serde-json-1/default) >= 1.0.138
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "toktrie"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
