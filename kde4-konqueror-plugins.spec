%define		_state		stable
%define		orgname		konq-plugins
Summary:	Konqueror plugins
Summary(pl.UTF-8):	Wtyczki do Konquerora
Name:		kde4-konqueror-plugins
Version:	4.2.3
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/extragear/%{orgname}-%{version}.tar.bz2
# Source0-md5:	4290fa1c92671031aa97c122b09d8c13
URL:		http://www.kde.org/
BuildRequires:	cmake
BuildRequires:	kde4-kdebase-devel >= %{version}
#BuildRequires:	kde4-webkitkde-devel
Requires:	tidy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konqueror plugins.

%description -l pl.UTF-8
Wtyczki do Konquerora.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%find_lang konq-plugins --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f konq-plugins.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fsview
%attr(755,root,root) %{_libdir}/kde4/akregatorkonqfeedicon.so
%attr(755,root,root) %{_libdir}/kde4/autorefresh.so
%attr(755,root,root) %{_libdir}/kde4/adblock.so                                                                                                                                      
%attr(755,root,root) %{_libdir}/kde4/babelfishplugin.so                                                                                                                              
%attr(755,root,root) %{_libdir}/kde4/crashesplugin.so                                                                                                                                
%attr(755,root,root) %{_libdir}/kde4/dirfilterplugin.so                                                                                                                              
%attr(755,root,root) %{_libdir}/kde4/domtreeviewerplugin.so                                                                                                                          
%attr(755,root,root) %{_libdir}/kde4/fsviewpart.so                                                                                                                                   
%attr(755,root,root) %{_libdir}/kde4/khtmlsettingsplugin.so                                                                                                                          
%attr(755,root,root) %{_libdir}/kde4/kimgallery.so                                                                                                                                   
%attr(755,root,root) %{_libdir}/kde4/rellinksplugin.so                                                                                                                               
%attr(755,root,root) %{_libdir}/kde4/uachangerplugin.so                                                                                                                              
%attr(755,root,root) %{_libdir}/kde4/webarchiverplugin.so                                                                                                                            
%attr(755,root,root) %{_libdir}/kde4/minitoolsplugin.so
%attr(755,root,root) %{_libdir}/kde4/searchbarplugin.so
%attr(755,root,root) %{_libdir}/kde4/validatorsplugin.so
%attr(755,root,root) %{_libdir}/kde4/webarchivethumbnail.so

%{_datadir}/apps/dolphinpart/kpartplugins/dirfilterplugin.desktop
%{_datadir}/apps/dolphinpart/kpartplugins/dirfilterplugin.rc

%{_datadir}/apps/dolphinpart/kpartplugins/kimgalleryplugin.desktop
%{_datadir}/apps/dolphinpart/kpartplugins/kimgalleryplugin.rc

%dir %{_datadir}/apps/domtreeviewer
%{_datadir}/apps/domtreeviewer/domtreeviewerui.rc
%dir %{_datadir}/apps/fsview
%{_datadir}/apps/fsview/fsview_part.rc

%{_datadir}/apps/khtml/kpartplugins/autorefresh.desktop
%{_datadir}/apps/khtml/kpartplugins/autorefresh.rc
%{_datadir}/apps/khtml/kpartplugins/crashesplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/crashesplugin.rc
%{_datadir}/apps/khtml/kpartplugins/khtmlsettingsplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/khtmlsettingsplugin.rc
%{_datadir}/apps/khtml/kpartplugins/akregator_konqfeedicon.desktop                                                                                             
%{_datadir}/apps/khtml/kpartplugins/akregator_konqfeedicon.rc                                                                                                  
%{_datadir}/apps/khtml/kpartplugins/plugin_adblock.desktop                                                                                                     
%{_datadir}/apps/khtml/kpartplugins/plugin_adblock.rc                                                                                                          
%{_datadir}/apps/khtml/kpartplugins/minitoolsplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/minitoolsplugin.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_babelfish.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_babelfish.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_domtreeviewer.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_domtreeviewer.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_rellinks.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_rellinks.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_validators.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_validators.rc
%{_datadir}/apps/khtml/kpartplugins/plugin_webarchiver.desktop
%{_datadir}/apps/khtml/kpartplugins/plugin_webarchiver.rc
%{_datadir}/apps/khtml/kpartplugins/uachangerplugin.desktop
%{_datadir}/apps/khtml/kpartplugins/uachangerplugin.rc
%{_datadir}/apps/konqueror/*
%{_datadir}/config.kcfg/validators.kcfg 
%dir %{_datadir}/apps/webkitpart
%dir %{_datadir}/apps/webkitpart/kpartplugins
%{_datadir}/apps/webkitpart/kpartplugins/autorefresh.desktop
%{_datadir}/apps/webkitpart/kpartplugins/autorefresh.rc
%{_datadir}/apps/webkitpart/kpartplugins/crashesplugin.desktop
%{_datadir}/apps/webkitpart/kpartplugins/crashesplugin.rc
%{_datadir}/apps/webkitpart/kpartplugins/plugin_validators.desktop
%{_datadir}/apps/webkitpart/kpartplugins/plugin_validators.rc
%{_datadir}/apps/webkitpart/kpartplugins/uachangerplugin.desktop
%{_datadir}/apps/webkitpart/kpartplugins/uachangerplugin.rc
%{_datadir}/config/translaterc
%{_iconsdir}/hicolor/*/apps/fsview.*
%{_iconsdir}/oxygen/*/actions/babelfish.*
%{_iconsdir}/oxygen/*/actions/cssvalidator.*
%{_iconsdir}/oxygen/*/actions/htmlvalidator.*
%{_iconsdir}/oxygen/*/actions/imagegallery.*
%{_iconsdir}/oxygen/*/actions/validators.*
%{_iconsdir}/oxygen/*/actions/webarchiver.*
%{_datadir}/kde4/services/ServiceMenus/imageconverter.desktop
%{_datadir}/kde4/services/fsview_part.desktop
%{_datadir}/kde4/services/webarchivethumbnail.desktop
/usr/share/apps/akregator/pics/feed.png                                                                                                                       
