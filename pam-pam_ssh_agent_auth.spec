%define 	modulename pam_ssh_agent_auth
Summary:	PAM module which permits authentication for arbitrary services via ssh-agent
Name:		pam-%{modulename}
Version:	0.9.3
Release:	1
License:	BSD
Group:		Base
Source0:	http://downloads.sourceforge.net/pamsshagentauth/%{modulename}-%{version}.tar.bz2
# Source0-md5:	9872ca1983e566ff5a89c240529e223d
URL:		http://pamsshagentauth.sourceforge.net/
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	/%{_lib}/security

%description
PAM module which permits authentication for arbitrary services via
ssh-agent. Written with sudo in mind, but like any auth PAM module,
can be used for for many purposes.

%prep
%setup -q -n %{modulename}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS
%attr(755,root,root) /%{_lib}/security/%{modulename}.so
%{_mandir}/man8/pam_ssh_agent_auth.8*
