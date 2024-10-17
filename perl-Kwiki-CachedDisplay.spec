%define upstream_name	 Kwiki-CachedDisplay
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Speed-up Kwiki page display by caching
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Kwiki)
BuildRequires:	perl(Test::Pod::Coverage)
BuildArch:	noarch

%description
This module use pre-generated page upon rendering, so that each successive
page-rendering takes no time in parsing and template-processing. After you
install this plugin, new pages will automatically have pre-generated HTML
copies on disk. HTML copies for old pages will be generated by next time anyone
visit them.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 403375
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.07-3mdv2009.0
+ Revision: 268536
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-2mdv2009.0
+ Revision: 210959
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.07-1mdv2008.0
+ Revision: 20233
- 0.07


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-3mdv2007.0
- Rebuild

* Mon Apr 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-2mdk
- better sources URL
- better buildrequires syntax

* Thu Jan 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdk
- first mandriva release

