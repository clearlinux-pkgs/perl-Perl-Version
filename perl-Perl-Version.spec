#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Perl-Version
Version  : 1.013.03
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Perl-Version-1.013_03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Perl-Version-1.013_03.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libperl-version-perl/libperl-version-perl_1.013-2.debian.tar.xz
Summary  : 'Parse and manipulate Perl version strings'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Perl-Version-bin = %{version}-%{release}
Requires: perl-Perl-Version-man = %{version}-%{release}
Requires: perl-Perl-Version-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Slurp::Tiny)

%description
=pod
=encoding utf8
=head1 The Perl::Version module
looking at this because you don't know where else to find what you're
looking for. Read this once and you might never have to read one again
for any Perl module.

%package bin
Summary: bin components for the perl-Perl-Version package.
Group: Binaries

%description bin
bin components for the perl-Perl-Version package.


%package dev
Summary: dev components for the perl-Perl-Version package.
Group: Development
Requires: perl-Perl-Version-bin = %{version}-%{release}
Provides: perl-Perl-Version-devel = %{version}-%{release}
Requires: perl-Perl-Version = %{version}-%{release}

%description dev
dev components for the perl-Perl-Version package.


%package man
Summary: man components for the perl-Perl-Version package.
Group: Default

%description man
man components for the perl-Perl-Version package.


%package perl
Summary: perl components for the perl-Perl-Version package.
Group: Default
Requires: perl-Perl-Version = %{version}-%{release}

%description perl
perl components for the perl-Perl-Version package.


%prep
%setup -q -n Perl-Version-1.013_03
cd %{_builddir}
tar xf %{_sourcedir}/libperl-version-perl_1.013-2.debian.tar.xz
cd %{_builddir}/Perl-Version-1.013_03
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Perl-Version-1.013_03/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/perl-reversion

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Perl::Version.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/perl-reversion.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Perl/Version.pm
