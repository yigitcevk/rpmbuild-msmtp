Name:		msmtp
Version:	1.8.7
Release:	1%{?dist}
Summary:	msmtp rpm packaging task

License:	GPL-3.0
URL:		https://marlam.de/msmtp/releases/%{name}
Source0:	%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	make  
Requires:       bash

%description
The long-tail description for msmtp

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make
make install
mkdir -p %{buildroot}/usr/local/bin
cp -r /tmp/%{name}-%{version} %{buildroot}/usr/local/bin


%files
/usr/local/bin/%{name}-%{version}
