# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname frontend

Name:           python-%{srcname}
Version:        0.0.3
Release:        %autorelease
Summary:        Develop complex & beautiful UI frontends using Python
License:        GPL-3.0-or-later
URL:            https://github.com/AgarwalPragy/frontend
VCS:            git:https://github.com/AgarwalPragy/frontend.git
#!RemoteAsset:  sha256:cdb5e76a0082b9cd3fa8331dbe44c86f007ab6d07c540551078f60318cd2e019
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

# server.py accesses static/ at import time, not available in buildroot
BuildOption(check):  -e "frontend" -e "frontend.*"

%python_provide python3-%{srcname}

%description
%{summary}.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
