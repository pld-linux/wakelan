Summary:	wakelan - send a wake-on-lan packet
Summary(pl):	wakelan - wysyla pakiet WOL
Name:		wakelan
Version:	1.1
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/Network/misc/%{name}-%{version}.tar.gz
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WakeLan sends a properly formatted UDP packet across the network which will
cause a wake-on-lan enabled computer to power on.

%description(pl)
WakeLan wysyla pakiet UDP przez siec ktory powoduje wlaczenie
komputera z WOL

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" ./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/man/man1
install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING
%attr(755,root,root) %{_bindir}/*
%{_prefix}/man/man1/*
