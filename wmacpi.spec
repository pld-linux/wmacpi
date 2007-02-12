Summary:	A battery monitor dockapp for ACPI based systems
Summary(pl.UTF-8):	Dokowalny monitor baterii dla systemów opartych o ACPI
Name:		wmacpi
Version:	2.1
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://himi.org/wmacpi/download/%{name}-%{version}.tar.bz2
# Source0-md5:	11fbbcbf31e14f36495b5a945ba778dd
Source1:	%{name}.desktop
URL:		http://himi.org/wmacpi/
BuildRequires:	XFree86-devel
BuildRequires:	libdockapp-devel >= 0.4.0
ExclusiveArch:	%{ix86} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmacpi is a dockapp battery monitor dockapp for ACPI based systems. It
is based on Timecop's wmacpi code and features a proper support for
multiple batteries, support for modern ACPI kernel versions, and other
improvements.

%description -l pl.UTF-8
wmacpi jest dokowalnym monitorem baterii dla systemów opartych o ACPI.
Jest rozwiniętą wersją wmacpi Timecopa i cechuje się prawidłową
obsługą wielu baterii, wsparciem współczesnych wersji ACPI jądra i
innymi udoskonaleniami.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/X11R6/include" \
	LDFLAGS="%{rpmldflags} -L/usr/X11R6/%{_lib} -lX11 -lXpm -lXext -ldockapp"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets,%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/docklets/*
