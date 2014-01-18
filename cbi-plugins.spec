%{?_javapackages_macros:%_javapackages_macros}
%global tag cbi-plugins-1.0.5

Name:           cbi-plugins
Version:        1.0.5
Release:        2.0%{?dist}
Summary:        A set of helpers for Eclipse CBI


License:        EPL
URL:            http://git.eclipse.org/c/cbi/org.eclipse.cbi.maven.plugins.git/
Source0:        http://git.eclipse.org/c/cbi/org.eclipse.cbi.maven.plugins.git/snapshot/%{tag}.tar.bz2
BuildArch:      noarch

BuildRequires:  tycho
BuildRequires:  tycho-extras
BuildRequires:  xmvn
Requires:       tycho
Requires:       tycho-extras
Requires:       jpackage-utils

%description
A set of helpers for Eclipse CBI.

%package javadoc

Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%pom_disable_module eclipse-macsigner-plugin
%pom_disable_module eclipse-winsigner-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Nov 13 2013 Alexander Kurtakov <akurtako@redhat.com> 1.0.5-2
- Disable win/mac signers.

* Wed Nov 13 2013 Alexander Kurtakov <akurtako@redhat.com> 1.0.5-1
- Update to latest upstream.

* Mon Sep 30 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.4-1
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.3-1
- Update to latest upstream.

* Thu Mar 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.4.git734d40
- Update to latest upstream.

* Thu Feb 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.3.git120561
- Delete empty line from sources.

* Thu Feb 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.2.git120561
- Review remarks fixed.

* Thu Feb 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.1.git120561
- Initial contribution.
