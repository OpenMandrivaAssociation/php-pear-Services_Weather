%define		_class		Services
%define		_subclass	Weather
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.4.7
Release:	2
Summary:	An interface to various online weather-services
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Services_Weather/
Source0:	http://download.pear.php.net/package/Services_Weather-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-pear-Cache >= 1.5.3
Requires:	php-pear-DB >= 1.4
Requires:	php-pear-HTTP_Request >= 1.2
Requires:	php-pear-SOAP >= 0.7.5
Requires:	php-pear-XML_Serializer >= 0.8
Requires:	php-pear-Net_FTP
BuildArch:	noarch
BuildRequires:	php-pear


%description
Services_Weather searches for given locations and retrieves current
weather data and, dependent on the used service, also forecasts. Up to
now, GlobalWeather from CapeScience, a XML service from weather.com
and METAR from noaa.gov are supported. Further services will get
included, if they become available, have a usable API and are properly
documented.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

cd %{upstream_name}-%{version}
sed 's#/usr/local/bin/php#/usr/bin/php#' buildMetarDB.php >> tmp
mv -f tmp buildMetarDB.php

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages
install -m 644 Weather.php  %{buildroot}%{_datadir}/pear/Services/
install -m 644 buildMetarDB.php  %{buildroot}%{_datadir}/pear/Services/
install -m 644 Weather/*.php %{buildroot}%{_datadir}/pear/Services/Weather/

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%doc %{upstream_name}-%{version}/images
%{_datadir}/pear/Services/buildMetarDB.php
%{_datadir}/pear/packages/%{upstream_name}.xml
%{_datadir}/pear/Services/Weather/*
%{_datadir}/pear/Services/Weather.php



%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.5-9mdv2012.0
+ Revision: 741810
- fix major breakage by careless packager

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.5-8
+ Revision: 667640
- mass rebuild

* Tue Aug 03 2010 Thomas Spuhler <tspuhler@mandriva.org> 1.4.5-7mdv2011.0
+ Revision: 565241
- Increased release for rebuild

* Tue Mar 16 2010 Thomas Spuhler <tspuhler@mandriva.org> 1.4.5-6mdv2010.1
+ Revision: 520659
- added Requires: php-pear-Net_FTP
  fixed SPEC file so buildMetarDB.php gets installed

* Thu Feb 18 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.4.5-5mdv2010.1
+ Revision: 507870
- bump release

* Thu Feb 18 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.4.5-3mdv2010.1
+ Revision: 507866
- Hopfuly fix #57093

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.5-1mdv2010.1
+ Revision: 489156
- update to new version 1.4.5

* Tue Nov 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.4-3mdv2010.1
+ Revision: 467083
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4.4-2mdv2010.0
+ Revision: 426668
- rebuild

* Sun Mar 22 2009 Funda Wang <fwang@mandriva.org> 1.4.4-1mdv2009.1
+ Revision: 360161
- new version 1.4.4

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-2mdv2009.1
+ Revision: 321900
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-1mdv2009.0
+ Revision: 272595
- 1.4.3

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.4.2-3mdv2009.0
+ Revision: 224880
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-2mdv2008.1
+ Revision: 178537
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-1mdv2008.0
+ Revision: 15750
- 1.4.2


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-1mdv2007.0
+ Revision: 82644
- Import php-pear-Services_Weather

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-1mdk
- 1.4.0

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-1mdk
- 1.3.2
- fix spec file to conform with the others

* Thu Jan 20 2005 Pascal Terjan <pterjan@mandrake.org> 1.3.1-1mdk
- First mdk package


