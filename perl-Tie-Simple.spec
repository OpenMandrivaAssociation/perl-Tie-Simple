%define modname	Tie-Simple
%define modver	1.04

Summary:	Create ties without creating full packages
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Tie/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module adds the ability to quickly create new types of tie objects
without creating a complete class. It does so in such a way as to try and
make the programmers life easier when it comes to single-use ties that I
find myself wanting to use from time-to-time.

The 'Tie::Simple' package is actually a front-end to other classes which
really do all the work once tied, but this package does the dwimming to
automatically figure out what you're trying to do.

I've tried to make this as intuitive as possible and dependent on other
bits of Perl where I can to minimize the need for documentation and to make
this extra, extra spiffy.

%prep
%autosetup -n %{modname}-%{modver} -p1

%build
%__perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
%make test

%install
%make_install

%files
%doc META.yml Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

