# vim: sw=4:ts=4:et


%define relabel_files() \
restorecon -R /usr/bin/FAHClient; \

%define selinux_policyver 3.13.1-266

Name:   fah_selinux
Version:	1.0
Release:	1%{?dist}
Summary:	SELinux policy module for fah

Group:	System Environment/Base		
License:	GPLv2+	
# This is an example. You will need to change it.
URL:		http://HOSTNAME
Source0:	fah.pp
Source1:	fah.if
Source2:	fah_selinux.8


Requires: policycoreutils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils
Requires(postun): policycoreutils
Requires(post): fahclient
BuildArch: noarch

%description
This package installs and sets up the  SELinux policy security module for fah.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man8/fah_selinux.8
install -d %{buildroot}/etc/selinux/targeted/contexts/users/


%post
semodule -n -i %{_datadir}/selinux/packages/fah.pp
semanage port -a -t fah_port_t -p tcp 36330
semanage port -a -t fah_port_t -p tcp 7396
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files

fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semanage port -d -p tcp 36330
    semanage port -d -p tcp 7396
    semodule -n -r fah
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       %relabel_files

    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/fah.pp
%{_datadir}/selinux/devel/include/contrib/fah.if
%{_mandir}/man8/fah_selinux.8.*


%changelog
* Thu Apr  9 2020 YOUR NAME <YOUR@EMAILADDRESS> 1.0-1
- Initial version

