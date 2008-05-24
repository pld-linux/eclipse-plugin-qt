#
# TODO:
# - use our Qt4 libs in libdir?
# - provides Qt4 libs - add no auto prov.?

# Conditional build:
%bcond_without	incall	# don't include all tarballs in .src.rpm
#
%define		need_x86	0
%define		need_x8664	0

%if %{with incall}
%define		need_x86	1
%define		need_x8664	1
%else
%ifarch %{ix86}
%define		need_x86	1
%endif
%ifarch %{x8664}
%define		need_x8664	1
%endif
%endif

Summary:	Qt Eclipse Integration
Summary(pl.UTF-8):	Integracja Qt w Eclipse
Name:		eclipse-plugin-qt
Version:	1.4.0
Release:	0.1
License:	CPL v1.0
Group:		Development/Languages
%if %{need_x86}
Source0:	http://trolltech.com/developer/download/qt-eclipse-integration-linux.x86-%{version}.tar.gz
# Source0-md5:	2bd951a8e08b4dddfd3b44b8b83c0c0c
%endif
%if %{need_x8664}
Source1:	http://trolltech.com/developer/download/qt-eclipse-integration-linux.x86_64-%{version}.tar.gz
# Source1-md5:	a241624ef543b9973e4b25efca8f3041
%endif
URL:		http://trolltech.com/developer/downloads/qt/eclipse-integration-download/
Requires:	eclipse >= 3.3
Requires:	eclipse-plugin-cdt >= 3.1.1
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_libdir}/eclipse

%description
The Qt Eclipse Integration allows programmers to create, build,
debug and run Qt applications from within the Eclipse IDE.
Integrations are available for Qt C++ on top of the Eclipse
C/C++ Development Tooling (CDT) plug-in.

#% description -l pl.UTF-8

%prep
%ifarch %{ix86}
%setup -q -c -T -b0
%endif
%ifarch %{x8664}
%setup -q -c -T -b1
%endif

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -r eclipse/* $RPM_BUILD_ROOT%{_eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_eclipsedir}/features/com.trolltech.qtcpp.feature_%{version}
%{_eclipsedir}/features/com.trolltech.qtcpp.feature_%{version}/*
%{_eclipsedir}/features/com.trolltech.qtcpp.feature_%{version}/.project

%dir %{_eclipsedir}/plugins/com.trolltech.qtcpp.linux.*_*.*.*
%{_eclipsedir}/plugins/com.trolltech.qtcpp.linux.*_*.*.*/.classpath
%{_eclipsedir}/plugins/com.trolltech.qtcpp.linux.*_*.*.*/.project
%dir %{_eclipsedir}/plugins/com.trolltech.qtcpp.linux.*_*.*.*/META-INF
%{_eclipsedir}/plugins/com.trolltech.qtcpp.linux.*_*.*.*/META-INF/MANIFEST.MF
%{_eclipsedir}/plugins/com.trolltech.qtcpp.linux.*_*.*.*/build.properties
%dir %{_eclipsedir}/plugins/com.trolltech.qtcpp.linux.*_*.*.*/lib
%attr(755,root,root) %{_eclipsedir}/plugins/com.trolltech.qtcpp.linux.*_*.*.*/lib/*.so
%attr(755,root,root) %{_eclipsedir}/plugins/com.trolltech.qtcpp.linux.*_*.*.*/lib/*.so.*
%dir %{_eclipsedir}/plugins/com.trolltech.qtcpp.linux.*_*.*.*/src
%{_eclipsedir}/plugins/com.trolltech.qtcpp.linux.*_*.*.*/src/KEEPME

%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}/META-INF
%{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}/META-INF/MANIFEST.MF
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}/bin
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}/bin/com
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}/bin/com/trolltech
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}/bin/com/trolltech/qtcppdesigner
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}/bin/com/trolltech/qtcppdesigner/views
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}/bin/com/trolltech/qtcppdesigner/views/embedded
%{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}/bin/com/trolltech/qtcppdesigner/views/embedded/*
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}/lib
%attr(755,root,root) %{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}/lib/libqtcppdesigner.so
%{_eclipsedir}/plugins/com.trolltech.qtcppdesigner.linux.*_%{version}/plugin.xml

%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesignerplugins.linux.*
%{_eclipsedir}/plugins/com.trolltech.qtcppdesignerplugins.linux.*/.*
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesignerplugins.linux.*/META-INF
%{_eclipsedir}/plugins/com.trolltech.qtcppdesignerplugins.linux.*/META-INF/MANIFEST.MF
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesignerplugins.linux.*/dependentlibs
%{_eclipsedir}/plugins/com.trolltech.qtcppdesignerplugins.linux.*/dependentlibs/*.so
%{_eclipsedir}/plugins/com.trolltech.qtcppdesignerplugins.linux.*/dependentlibs/*.so.*
%{_eclipsedir}/plugins/com.trolltech.qtcppdesignerplugins.linux.*/libqt3supportwidgets.so
%{_eclipsedir}/plugins/com.trolltech.qtcppdesignerplugins.linux.*/libqwebview.so
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppdesignerplugins.linux.*/src
%{_eclipsedir}/plugins/com.trolltech.qtcppdesignerplugins.linux.*/src/KEEPME

%dir %{_eclipsedir}/plugins/com.trolltech.qtcppintegrationhelp.examples_%{version}
%{_eclipsedir}/plugins/com.trolltech.qtcppintegrationhelp.examples_%{version}/.*
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppintegrationhelp.examples_%{version}/AddressBook
%{_eclipsedir}/plugins/com.trolltech.qtcppintegrationhelp.examples_%{version}/AddressBook/*
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppintegrationhelp.examples_%{version}/META-INF
%{_eclipsedir}/plugins/com.trolltech.qtcppintegrationhelp.examples_%{version}/META-INF/MANIFEST.MF
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppintegrationhelp.examples_%{version}/src
%{_eclipsedir}/plugins/com.trolltech.qtcppintegrationhelp.examples_%{version}/src/KEEPME

%dir %{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/META-INF
%{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/META-INF/MANIFEST.MF
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/bin
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/bin/com
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/bin/com/trolltech
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/bin/com/trolltech/qtcppproject
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/bin/com/trolltech/qtcppproject/pages
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/bin/com/trolltech/qtcppproject/pages/embedded
%{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/bin/com/trolltech/qtcppproject/pages/embedded/KEEPME
%{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/bin/com/trolltech/qtcppproject/pages/embedded/*.class
%dir %{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/lib
%attr(755,root,root) %{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/lib/*.so
%{_eclipsedir}/plugins/com.trolltech.qtcppproject.linux.*_%{version}/*.xml

%{_eclipsedir}/plugins/com.trolltech.qt*.jar
