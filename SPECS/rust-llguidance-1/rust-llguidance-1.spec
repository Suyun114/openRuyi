# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name llguidance
%global full_version 1.7.5
%global pkgname llguidance-1

Name:           rust-llguidance-1
Version:        1.7.5
Release:        %autorelease
Summary:        Rust crate "llguidance"
License:        MIT
URL:            https://github.com/guidance-ai/llguidance
#!RemoteAsset:  sha256:5baa07a0af9806dc6b051fbaf665362314415c4eaa9471acc47de3a6113b9479
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
# Remove wasm feature and instant dependency (not needed on Linux)
Patch:          2001-remove-wasm-feature.patch

BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.95
Requires:       crate(derivre-0.3/compress) >= 0.3.11
Requires:       crate(indexmap-2/default) >= 2.7.1
Requires:       crate(regex-syntax-0.8/default) >= 0.8.5
Requires:       crate(serde-1/default) >= 1.0.217
Requires:       crate(serde-1/derive) >= 1.0.217
Requires:       crate(serde-json-1/default) >= 1.0.138
Requires:       crate(serde-json-1/preserve-order) >= 1.0.138
Requires:       crate(toktrie-1/default) >= 1.7.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/lark) = %{version}
Provides:       crate(%{pkgname}/logging) = %{version}

%description
Source code for takopackized Rust crate "llguidance"

%package     -n %{name}+ahash
Summary:        Super-fast Structured Outputs - feature "ahash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derivre-0.3/ahash) >= 0.3.11
Requires:       crate(derivre-0.3/compress) >= 0.3.11
Provides:       crate(%{pkgname}/ahash) = %{version}

%description -n %{name}+ahash
This metapackage enables feature "ahash" for the Rust llguidance crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Super-fast Structured Outputs - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ahash) = %{version}
Requires:       crate(%{pkgname}/lark) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
Requires:       crate(%{pkgname}/referencing) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust llguidance crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+generate-header
Summary:        Super-fast Structured Outputs - feature "generate-header"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cbindgen-0.29/default) >= 0.29.0
Provides:       crate(%{pkgname}/generate-header) = %{version}

%description -n %{name}+generate-header
This metapackage enables feature "generate-header" for the Rust llguidance crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jsonschema-validation
Summary:        Super-fast Structured Outputs - feature "jsonschema_validation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jsonschema-0.29) >= 0.29.0
Requires:       crate(lazy-static-1/default) >= 1.5.0
Provides:       crate(%{pkgname}/jsonschema-validation) = %{version}

%description -n %{name}+jsonschema-validation
This metapackage enables feature "jsonschema_validation" for the Rust llguidance crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Super-fast Structured Outputs - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.10.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust llguidance crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+referencing
Summary:        Super-fast Structured Outputs - feature "referencing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(referencing-0.29/default) >= 0.29.0
Provides:       crate(%{pkgname}/referencing) = %{version}

%description -n %{name}+referencing
This metapackage enables feature "referencing" for the Rust llguidance crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm
Summary:        Super-fast Structured Outputs - feature "wasm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(instant-0.1/default) >= 0.1.13
Provides:       crate(%{pkgname}/wasm) = %{version}

%description -n %{name}+wasm
This metapackage enables feature "wasm" for the Rust llguidance crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
