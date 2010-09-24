Summary:	wakelan - send a wake-on-lan packet
Summary(pl.UTF-8):	wakelan - wysyła pakiet WOL
Name:		wakelan
Version:	1.1
Release:	5
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/misc/%{name}-%{version}.tar.gz
# Source0-md5:	4a3a31d874967cd6ac761b7d4323e0d5
Patch0:		%{name}-build.patch
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WakeLan sends a properly formatted UDP packet across the network which
will cause a wake-on-lan enabled computer to power on.

%description -l pl.UTF-8
WakeLan wysyła pakiet UDP przez sieć, który powoduje włączenie
komputera z WOL.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
