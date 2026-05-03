# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname referencing

Name:           python-%{srcname}
Version:        0.37.0
Release:        %autorelease
Summary:        JSON Referencing + Python
License:        MIT
URL:            https://github.com/python-jsonschema/referencing
#!RemoteAsset:  sha256:44aefc3142c5b842538163acb373e24cce6632bd54bdb01b21ad5863489f50d8
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e 'referencing.tests.test_referencing_suite'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
%{summary}.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license COPYING
%doc README.rst

%changelog
%autochangelog
