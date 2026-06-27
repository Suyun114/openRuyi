# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toktrie_hf_tokenizers
%global full_version 1.7.5
%global pkgname toktrie-hf-tokenizers-1

Name:           rust-toktrie-hf-tokenizers-1
Version:        1.7.5
Release:        %autorelease
Summary:        Rust crate "toktrie_hf_tokenizers"
License:        MIT
URL:            https://github.com/guidance-ai/llguidance
#!RemoteAsset:  sha256:19b4defe24ccadaf7745a4d4bb30cff91bbad7b175c4906fe8e3716b3465a536
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.95
Requires:       crate(log-0.4/default) >= 0.4.25
Requires:       crate(serde-1/default) >= 1.0.217
Requires:       crate(serde-1/derive) >= 1.0.217
Requires:       crate(serde-json-1/default) >= 1.0.138
Requires:       crate(tokenizers-0.21/fancy-regex) >= 0.21.2
Requires:       crate(tokenizers-0.21/unstable-wasm) >= 0.21.2
Requires:       crate(toktrie-1/default) >= 1.7.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "toktrie_hf_tokenizers"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
