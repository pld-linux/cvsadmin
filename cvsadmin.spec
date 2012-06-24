Summary:	Utility for cvs managment
Summary(pl):	Narz�dzie do zarz�dzania cvs-em
Name:		cvsadmin
Version:	1.0.3
Release:	2
License:	BSD
Group:		Applications/System
Source0:	http://www.cooptel.qc.ca/~limitln/%{name}-%{version}.tar.gz
# Source0-md5:	2829f202f9079bcaa5aa25452cdb30d6
URL:		http://www.cooptel.qc.ca/~limitln/cvsadmin/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cvsadmin is a simple program to administrate users of a CVS repository. 
It currently allows you to easily:
- add users,
- remove users,
- change users passwords,
- show existing users,
- rename user login,
- change system users.

%description -l pl
Narz�dzie do zarz�dzania u�ytkownikami repozytorium CVS.
Obecnie umo�liwia ono:
- dodanie u�ytkownika,
- usuni�cie u�ytkownika,
- zmian� has�a u�ytkownika,
- przegl�danie listy obecnych u�ytkownik�w,
- zmian� nazwy u�ytkownika,
- zmian� u�ytkownika systemowego.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install man/cvsadmin.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/backend.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
