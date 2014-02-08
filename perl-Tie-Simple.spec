%define upstream_name    Tie-Simple
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Create ties without creating full packages
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch: noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-4mdv2012.0
+ Revision: 765767
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-3
+ Revision: 764292
- rebuilt for perl-5.14.x

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.30.0-2
+ Revision: 656831
- rebuild for updated spec-helper

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 572272
- import perl-Tie-Simple


* Mon Aug 23 2010 cpan2dist 1.03-1mdv
- initial mdv release, generated with cpan2dist
