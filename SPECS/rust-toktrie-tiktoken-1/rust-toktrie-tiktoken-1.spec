# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toktrie_tiktoken
%global full_version 1.7.5
%global pkgname toktrie-tiktoken-1

Name:           rust-toktrie-tiktoken-1
Version:        1.7.5
Release:        %autorelease
Summary:        Rust crate "toktrie_tiktoken"
License:        MIT
URL:            https://github.com/guidance-ai/llguidance
#!RemoteAsset:  sha256:d40d6d1a58b9649362611da69ffe12e41b60e30aed3995fc623383eea32c2137
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.95
Requires:       crate(log-0.4/default) >= 0.4.25
Requires:       crate(serde-1/default) >= 1.0.217
Requires:       crate(serde-1/derive) >= 1.0.217
Requires:       crate(serde-json-1/default) >= 1.0.138
Requires:       crate(tiktoken-rs-0.7/default) >= 0.7.0
Requires:       crate(toktrie-1/default) >= 1.7.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "toktrie_tiktoken"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
