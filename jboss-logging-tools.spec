%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Beta1
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logging-tools
Version:          1.2.0
Release:          0.1%{namedreltag}.0%{?dist}
Summary:          JBoss Logging I18n Annotation Processor
License:          LGPLv2+
URL:              https://github.com/jboss-logging/jboss-logging-tools
Source0:          https://github.com/jboss-logging/jboss-logging-tools/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    testng
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    jboss-parent
BuildRequires:    jboss-logging
BuildRequires:    jboss-logmanager
BuildRequires:    jdeparser

%description
This pacakge contains JBoss Logging I18n Annotation Processor

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-logging-tools-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Sep 09 2013 Marek Goldmann <mgoldman@redhat.com> - 1.2.0-0.1.Beta1
- Upstream release 1.2.0.Beta1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Marek Goldmann <mgoldman@redhat.com> - 1.1.0-1
- Upstream release 1.1.0.Final
- Using new guidelines

* Fri Feb 22 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.2-1
- Upstream release 1.0.2.Final

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.0-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.0-3
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 16 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Upstream release 1.0.0.Final

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.2.CR4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-0.1.CR4
- Upstream release 1.0.0.CR4

* Sun Oct 02 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-0.1.CR1
- Upstream release 1.0.0.CR1

* Thu Aug 04 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-0.1.Beta7
- Initial packaging

