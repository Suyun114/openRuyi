# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           po4a
Version:        0.74
Release:        %autorelease
Summary:        Tools for helping translation of documentation
License:        GPL-2.0-or-later
URL:            https://po4a.org/
VCS:            git:https://github.com/mquinson/po4a.git
#!RemoteAsset:  sha256:6e390eb7707501a86f2e648d78fddb0d211d1e8699aa1ee201176e9f966a798b
Source0:        https://github.com/mquinson/po4a/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Locale::gettext) >= 1.01
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(SGMLS)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Text::WrapI18N)
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(Unicode::LineBreak)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  docbook-xsl
BuildRequires:  libxslt

%description
po4a (PO for anything) eases the translation of documentation and other
textual content. It converts documentation to PO files for translation,
and then back to the original format from translated PO files.

%prep
%setup -q -n po4a-%{version}

%build
# Replace online docbook.xsl URL with local path for offline build
sed -i 's|http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl|file://%{_datadir}/sgml/docbook/xsl-stylesheets-1.79.2/manpages/docbook.xsl|' Po4aBuilder.pm
LC_ALL=en_US.UTF-8 perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%check
./Build test

%files -f %{name}.files
%doc README* TODO changelog
%{_mandir}/*/man1/po4a*.1*
%{_mandir}/*/man1/msguntypot.1*
%{_mandir}/*/man3/Locale::Po4a::*.3*
%{_mandir}/*/man7/po4a.7*
%{_datadir}/locale/

%changelog
%autochangelog
