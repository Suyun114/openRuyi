# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname llguidance

Name:           python-%{srcname}
Version:        1.7.5
Release:        %autorelease
Summary:        Bindings for the Low-level Guidance (llguidance) Rust library
License:        MIT
URL:            https://pypi.org/project/llguidance/
VCS:            git:https://github.com/microsoft/llguidance
#!RemoteAsset:  sha256:afaa8f979708cd546c762f06a4fe4748e5ef7f06ed45875dabe7db8f07b73645
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(huggingface-hub)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(transformers)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(anyhow-1/default) >= 1.0.95
BuildRequires:  crate(bytemuck-1/default) >= 1.21.0
BuildRequires:  crate(llguidance-1/default) >= 1.7.5
BuildRequires:  crate(pyo3-0.28/abi3-py39) >= 0.28.2
BuildRequires:  crate(pyo3-0.28/anyhow) >= 0.28.2
BuildRequires:  crate(pyo3-0.28/default) >= 0.28.2
BuildRequires:  crate(pyo3-0.28/extension-module) >= 0.28.2
BuildRequires:  crate(rayon-1/default) >= 1.10.0
BuildRequires:  crate(serde-1/default) >= 1.0.217
BuildRequires:  crate(serde-1/derive) >= 1.0.217
BuildRequires:  crate(serde-json-1/default) >= 1.0.138
BuildRequires:  crate(toktrie-hf-tokenizers-1/default) >= 1.7.5
BuildRequires:  crate(toktrie-tiktoken-1/default) >= 1.7.5

# TODO: llama_cpp not yet packaged
# mlx is Apple-specific
BuildOption(check):  -e "llguidance.llamacpp" -e "llguidance.mlx"

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Low-level Guidance (llguidance) is a Rust library providing fast
structured outputs for LLM inference and guidance.

%prep
%autosetup -n %{srcname}-%{version} -a 0
%rust_setup_registry
rm -f Cargo.lock

# Remove wasm feature and instant dependency from parser crate (not needed on Linux)
sed -i '/^wasm = .*dep:instant/d' parser/Cargo.toml
sed -i '/^instant = { version = "0.1.13", optional = true }/d' parser/Cargo.toml
%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
