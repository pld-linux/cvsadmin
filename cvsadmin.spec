Summary:	Utility for cvs managment
Summary(pl):	Narzêdzie do zarz±dzania cvs'em
Name:		cvsadmin
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.cooptel.qc.ca/~limitln/cvsadmin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr

%description
Utility for cvs managment.

%description -l pl
Narzêdzie do zarz±dzania cvs'em.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install src/cvsadmin $RPM_BUILD_ROOT%{_bindir}/cvsadmin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
