%define		_class		Services
%define		_subclass	Weather
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.4.5
Release:	%mkrel 3
Summary:	An interface to various online weather-services
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Services_Weather/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-pear-Cache >= 1.5.3
Requires:	php-pear-DB >= 1.4
Requires:	php-pear-HTTP_Request >= 1.2
Requires:	php-pear-SOAP >= 0.7.5
Requires:	php-pear-XML_Serializer >= 0.8
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}
AutoReqProv: 0

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
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages
install -m 644 Weather.php  %{buildroot}%{_datadir}/pear/Services/
install -m 644 Weather/*.php %{buildroot}%{_datadir}/pear/Services/Weather/

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%doc %{upstream_name}-%{version}/images
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
%{_datadir}/pear/Services/Weather/*
