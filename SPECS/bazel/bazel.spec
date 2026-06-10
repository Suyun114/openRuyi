# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bazel
Version:        9.1.1
Release:        %autorelease
Summary:        Correct, reproducible, and fast builds for everyone
License:        Apache-2.0
URL:            https://bazel.build/
#!RemoteAsset:  sha256:a6f66e26c8f4ca04fa83c796a404eff0544bd78336fbbcd122c9e10cbec4a5d7
Source0:        https://github.com/bazelbuild/bazel/releases/download/%{version}/bazel-%{version}-dist.zip

# Bootstrap via compile.sh; no standard build system
BuildRequires:  java-21-openjdk-devel
BuildRequires:  libarchive
BuildRequires:  python3
BuildRequires:  unzip
BuildRequires:  which
BuildRequires:  zip

%description
Bazel is an open-source build and test tool similar to Make, Maven, and
Gradle. It uses a human-readable, high-level build language. Bazel
supports projects in multiple languages and builds outputs for multiple
platforms. Bazel supports large codebases across multiple repositories,
and large numbers of users.

%prep
%autosetup -c -n %{name}-%{version}

%build
EMBED_LABEL=%{version} \
  EXTRA_BAZEL_ARGS="--tool_java_runtime_version=local_jdk --jobs=1" \
  bash ./compile.sh

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}

# Install bazel wrapper script
install -pm 0755 scripts/packages/bazel.sh %{buildroot}%{_bindir}/bazel

# Install bazel binary
install -pm 0755 output/bazel %{buildroot}%{_bindir}/bazel-real

# Create arch-specific symlink
ln -s bazel-real %{buildroot}%{_bindir}/bazel-%{version}.x-linux-%{_arch}

# Install third_party and tools for embedded tools
cp -r third_party %{buildroot}%{_datadir}/%{name}/
cp -r tools %{buildroot}%{_datadir}/%{name}/

%check

%files
%doc README.md
%license LICENSE
%{_bindir}/bazel
%{_bindir}/bazel-real
%{_bindir}/bazel-%{version}.x-linux-%{_arch}
%{_datadir}/%{name}/

%changelog
%autochangelog
