# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rpds_py

Name:           python-rpds-py
Version:        0.30.0
Release:        %autorelease
Summary:        Python bindings to Rust's persistent data structures (rpds)
License:        MIT
URL:            https://github.com/crate-py/rpds
#!RemoteAsset:  sha256:dd8ff7cf90014af0c0f787eea34794ebf6415242ee1d6fa91eaba725cc441e84
Source0:        https://files.pythonhosted.org/packages/source/r/rpds-py/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:ff35e1f1a51cad0757feadb534e1ff3b9bfe2c308f2b10328eba7b7733774f66
Source1:        https://github.com/software-vendor/python-rpds-py-vendor/releases/download/vendor-%{version}/rpds_py-%{version}-vendor.tar.bz2
BuildSystem:    pyproject

BuildOption(prep):  -a1
BuildOption(install):  -l rpds

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  rust
BuildRequires:  python3dist(maturin)

Provides:       python3-rpds-py
%python_provide python3-rpds-py

%description
%{summary}.

%prep -a
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
