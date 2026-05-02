# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname matplotlib

Name:           python-%{srcname}
Version:        3.10.9
Release:        %autorelease
Summary:        Python plotting package
License:        PSF-2.0
URL:            https://matplotlib.org
VCS:            git:https://github.com/matplotlib/matplotlib.git
#!RemoteAsset:  sha256:fd66508e8c6877d98e586654b608a0456db8d7e8a546eb1e2600efd957302358
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(build):  -Csetup-args=--wrap-mode=nodownload -Csetup-args=-Dsystem-freetype=true -Csetup-args=-Dsystem-qhull=true
BuildOption(install):  -l %{srcname} mpl_toolkits pylab +auto -L
# TODO: gtk, Qt, tk, wxPython not yet packaged
# macOS-only, excluded
# nbagg needs ipykernel not yet packaged
# sphinxext needs sphinx not yet packaged
# tests need baseline image data not installed
BuildOption(check):  -e 'matplotlib.backends.backend_gtk*'
BuildOption(check):  -e 'matplotlib.backends.*qt*'
BuildOption(check):  -e 'matplotlib.backends.backend_macosx'
BuildOption(check):  -e 'matplotlib.backends.backend_nbagg'
BuildOption(check):  -e 'matplotlib.backends.backend_tk*'
BuildOption(check):  -e 'matplotlib.backends.backend_wx*'
BuildOption(check):  -e 'matplotlib.sphinxext.*'
BuildOption(check):  -e '*.tests*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(qhull_r)
BuildRequires:  python3dist(pycairo)
BuildRequires:  python3dist(tornado)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(jinja2)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Matplotlib is a comprehensive library for creating static, animated,
and interactive visualizations in Python.

%generate_buildrequires
# Use system library while generating build requires.
%pyproject_buildrequires -p -Csetup-args=--wrap-mode=nodownload -Csetup-args=-Dsystem-freetype=true -Csetup-args=-Dsystem-qhull=true

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
