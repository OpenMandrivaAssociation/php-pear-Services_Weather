%define	_class	Services
%define	_subclass	Weather
%define	modname	%{_class}_%{_subclass}

Summary:	An interface to various online weather-services
Name:		php-pear-%{modname}
Version:	1.4.7
Release:	4
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Services_Weather/
Source0:	http://download.pear.php.net/package/Services_Weather-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear
Requires:	php-pear-Cache >= 1.5.3
Requires:	php-pear-DB >= 1.4
Requires:	php-pear-HTTP_Request >= 1.2
Requires:	php-pear-SOAP >= 0.7.5
Requires:	php-pear-XML_Serializer >= 0.8
Requires:	php-pear-Net_FTP

%description
Services_Weather searches for given locations and retrieves current
weather data and, dependent on the used service, also forecasts. Up to
now, GlobalWeather from CapeScience, a XML service from weather.com
and METAR from noaa.gov are supported. Further services will get
included, if they become available, have a usable API and are properly
documented.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

cd %{modname}-%{version}
sed 's#/usr/local/bin/php#/usr/bin/php#' buildMetarDB.php >> tmp
mv -f tmp buildMetarDB.php

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages
install -m 644 Weather.php  %{buildroot}%{_datadir}/pear/Services/
install -m 644 buildMetarDB.php  %{buildroot}%{_datadir}/pear/Services/
install -m 644 Weather/*.php %{buildroot}%{_datadir}/pear/Services/Weather/

%files
%doc %{modname}-%{version}/examples
%doc %{modname}-%{version}/images
%{_datadir}/pear/Services/buildMetarDB.php
%{_datadir}/pear/packages/%{modname}.xml
%{_datadir}/pear/Services/Weather/*
%{_datadir}/pear/Services/Weather.php

