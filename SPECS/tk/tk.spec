# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define rrc %{nil}
%define TK_MINOR %(echo %version | cut -c1-3)

Name:           tk
Version:        8.6.16
Release:        %autorelease
Summary:        The Tk GUI Toolkit for Tcl
License:        TCL
URL:            http://www.tcl.tk
VCS:            git:https://github.com/tcltk/tk.git
#!RemoteAsset:  sha256:be9f94d3575d4b3099d84bc3c10de8994df2d7aa405208173c709cc404a7e5fe
Source0:        http://prdownloads.sourceforge.net/tcl/%{name}%{version}%{rrc}-src.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-man-symlinks
BuildOption(conf):  --enable-man-compression=gzip
BuildOption(conf):  --with-tcl=%{_libdir}
BuildOption(build):  -C unix

BuildRequires:  autoconf
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xscrnsaver)

Requires:       tcl%{?_isa} = %{version}

Provides:       wish
Provides:       wish%{TK_MINOR}

%description
Tk is a graphical user interface toolkit that takes the Tcl programming
language to the world of windows, buttons, menus, and other GUI widgets.
It provides standard GUI components and a powerful geometry manager for
creating desktop applications.

%package        devel
Summary:        Header Files and C API Documentation for Tk
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       tcl-devel%{?_isa}
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xft)

%description    devel
This package contains header files and documentation needed for writing
Tk extensions in compiled languages like C, C++, etc., or for
embedding the Tk windowing toolkit in programs written in such languages.

%prep
%setup -q -n %{name}%{version}

%conf -p
cd unix
autoconf -fiv

%check
cd unix
# make test requires an X display, skip by default
%{?_with_check: make test 2>&1 | tee testresults}

%install
make -C unix install \
       INSTALL_ROOT=%{buildroot} TK_LIBRARY=%{_datadir}/tk%{TK_MINOR}
ln -sf wish%{TK_MINOR} %{buildroot}%{_bindir}/wish

chmod 755 %{buildroot}%{_libdir}/libtk%{TK_MINOR}.so

# Install private headers into tk-private (FS#14388, FS#47616)
mkdir -p %{buildroot}%{_includedir}/tk-private
for dir in compat generic generic/ttk unix; do
    install -dm755 %{buildroot}%{_includedir}/tk-private/$dir
    install -m644 $dir/*.h %{buildroot}%{_includedir}/tk-private/$dir/
done

# Remove buildroot traces from tkConfig.sh
sed -i "s|$PWD/unix|%{_libdir}|; s|$PWD|%{_includedir}/tk-private|" %{buildroot}%{_libdir}/tkConfig.sh
sed -i "/^TK_LIB_SPEC=/s/'.*'$//" %{buildroot}%{_libdir}/tkConfig.sh
sed -i "/^Libs.private: /s/ .*$//" %{buildroot}%{_libdir}/pkgconfig/tk.pc

%files
%defattr(-,root,root,755)
%doc README.md license.terms
%doc %{_mandir}/mann
%{_mandir}/man1/*
%{_bindir}/wish*
%{_libdir}/libtk*.so
%{_libdir}/tk%{TK_MINOR}
%{_datadir}/tk%{TK_MINOR}

%files devel
%defattr(-,root,root)
%doc %{_mandir}/man3/*
%{_includedir}/tk.h
%{_includedir}/tkDecls.h
%{_includedir}/tkPlatDecls.h
%{_includedir}/tk-private
%{_libdir}/libtk*.a
%{_libdir}/tkConfig.sh
%{_libdir}/pkgconfig/tk.pc

%changelog
%autochangelog
