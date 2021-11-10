%global debug_package %{nil}
Name:		{{{ git_name name=example }}}

# We need lead=1.0 because the last tagged version is 1.0.13
Version:	{{{ git_version lead=1.0 }}}
Release:	1%{?dist}
Summary:	This is a simple example to test copr

Group:		Applications/File
License:	GPLv2+
URL:		http://github.com/example
Source0:	{{{ git_dir_pack }}}


%description
Simple example to demonstrate copr's abilites.


%prep
{{{ git_dir_setup_macro }}}


%build
make %{?_smp_mflags}


%install
install -d %{buildroot}%{_sbindir}
cp -a main %{buildroot}%{_sbindir}/main


%files
%doc
%{_sbindir}/main

%changelog
* Sun Feb 18 2018 clime <clime@redhat.com> 1.0.13-1
- disable debuginfo generation (clime@redhat.com)
- add find debuginfo (clime@redhat.com)
- add -g switch (clime@redhat.com)
- empty changelog (clime@redhat.com)
- update (clime@redhat.com)

* Sun Feb 18 2018 clime <clime@redhat.com>
- disable debuginfo generation (clime@redhat.com)
- add find debuginfo (clime@redhat.com)
- add -g switch (clime@redhat.com)
- empty changelog (clime@redhat.com)
- update (clime@redhat.com)

* Sun Feb 18 2018 clime <clime@redhat.com>
- disable debuginfo generation (clime@redhat.com)
- add find debuginfo (clime@redhat.com)
- add -g switch (clime@redhat.com)
- empty changelog (clime@redhat.com)
- update (clime@redhat.com)

* Sun Feb 18 2018 clime <clime@redhat.com>
- disable debuginfo generation (clime@redhat.com)
- add find debuginfo (clime@redhat.com)
- add -g switch (clime@redhat.com)
- empty changelog (clime@redhat.com)
- update (clime@redhat.com)


