Summary:	A battery monitor dockapp for ACPI based systems
Summary(pl):	Dokowalny monitor baterii dla systemów opartych o ACPI
Name:		wmacpi
Version:	2.0
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://himi.org/wmacpi/download/%{name}-%{version}.tar.bz2
# Source0-md5:	73cea5d58607f027fc0213d38ba973c2
# Source0-size:	27912
Source1:	%{name}.desktop
URL:		http://himi.org/wmacpi/
BuildRequires:	XFree86-devel
BuildRequires:	libdockapp >= 0.4.0
ExclusiveArch:	%{ix86} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmacpi is a dockapp battery monitor dockapp for ACPI based systems. It
is based on Timecop's wmacpi code and features a proper support for
multiple batteries, support for modern ACPI kernel versions, and other
improvements.

%description -l pl
wmacpi jest dokowalnym monitorem baterii dla systemów opartych o ACPI.
Jest rozwiniêt± wersj± wmacpi Timecopa i cechuje siê prawid³ow±
obs³ug± wielu baterii, wsparciem wspó³czesnych wersji ACPI j±dra i
innymi udoskonaleniami.

%prep
%setup -q

%build
%{__make}

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
