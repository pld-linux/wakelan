Summary:	wakelan - send a wake-on-lan packet
Summary(pl):	wakelan - wysy³a pakiet WOL
Name:		wakelan
Version:	1.1
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/misc/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WakeLan sends a properly formatted UDP packet across the network which
will cause a wake-on-lan enabled computer to power on.

%description -l pl
WakeLan wysy³a pakiet UDP przez sieæ, który powoduje w³±czenie
komputera z WOL.

%prep
%setup -q

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
