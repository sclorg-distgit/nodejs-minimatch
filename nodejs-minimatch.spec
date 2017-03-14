%{?scl:%scl_package nodejs-minimatch}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-minimatch
Version:    3.0.2
Release:    2%{?dist}
Summary:    JavaScript glob matcher
License:    ISC
URL:        https://github.com/isaacs/minimatch
Source0:    http://registry.npmjs.org/minimatch/-/minimatch-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Converts glob expressions to JavaScript "RegExp" objects.

%prep
%setup -q -n package

#%nodejs_fixdep lru-cache

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/minimatch
cp -p minimatch.js package.json %{buildroot}%{nodejs_sitelib}/minimatch

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/minimatch
%doc README.md LICENSE

%changelog
* Tue Jan 17 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.2-2
- Bump

* Thu Jul 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.2-1
- Resolves: #1355781

* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.0-4
- Resolves: rhbz#1334856, fixes wrong license

* Wed Apr 06 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.0-3
- Remove legacy dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.0-2
- rebuilt

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 3.0.0-1
- New upstream release

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-1
- New upstream release 1.0.0

* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 0.2.14-1
- New upstream release 0.2.14

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.2.12-3
- replace provides and requires with macro


* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.12-2
- restrict to compatible arches

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.12-1
- update to upstream release 0.2.12

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.11-2
- add macro for EPEL6 dependency generation

Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.2    .11-2
- Add support for software collections

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.11-1
- new upstream release 0.2.11

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.9-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.9-1
- new upstream release 0.2.9
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.4-2
- guard Requires for F17 automatic depedency generation

* Thu Mar 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.4-1
- New upstream release 0.2.4

* Thu Mar 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.2-2
- New upstream release 0.2.4

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.2-1
- new upstream release 0.2.2

* Sat Feb 25 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- new upstream release 0.2.0

* Sun Dec 18 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-2
- add Group to make EL5 happy

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-1
- initial package
