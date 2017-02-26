# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sudo

# >> macros
# << macros

Summary:    Execute some commands as root
Version:    1.8.10p3
Release:    2
Group:      Applications/System
License:    BSD3c
URL:        http://www.sudo.ws/
Source0:    %{name}-%{version}.tar.gz
Source1:    sudo.pamd
Source100:  sudo.yaml
BuildRequires:  pam-devel

%description
Sudo is a command that allows users to execute some commands as root.
The /etc/sudoers file (edited with 'visudo') specifies which users have
access to sudo and which commands they can run. Sudo logs all its
activities to syslogd, so the system administrator can keep an eye on
things. Sudo asks for the password for initializing a check period of a
given time N (where N is defined at installation and is set to 5
minutes by default).


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --libexecdir=%{_libexecdir}/sudo \
    --docdir=%{_docdir}/%{name} \
    --with-noexec=%{_libexecdir}/sudo/sudo_noexec.so \
    --with-pam \
    --with-logfac=auth \
    --with-insults \
    --with-all-insults \
    --with-ignore-dot \
    --with-tty-tickets \
    --enable-shell-sets-home \
    --enable-warnings \
    --with-sudoers-mode=0440 \
    --with-env-editor \
    --with-secure-path=/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/sbin:/usr/sbin:/root/bin

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
install -d -m 755 %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/sudo
install -d -m 755 %{buildroot}%{_localstatedir}/lib/sudo
rm -rf %{buildroot}/usr/share/locale
rm -f %{buildroot}/usr/include/sudo_plugin.h
# << install post

%files
%defattr(-,root,root,-)
# >> files
%doc %{_docdir}/%{name}
%doc %{_mandir}/man?/*
%config(noreplace) %attr(0440,root,root) %{_sysconfdir}/sudoers
%dir %{_sysconfdir}/sudoers.d
%config %{_sysconfdir}/pam.d/sudo
%attr(4755,root,root) %{_bindir}/sudo
%attr(4755,root,root) %{_bindir}/sudoedit
%{_bindir}/sudoreplay
%{_sbindir}/visudo
%{_libexecdir}/sudo
%attr(0700,root,root) %dir %ghost %{_localstatedir}/lib/sudo
# << files
