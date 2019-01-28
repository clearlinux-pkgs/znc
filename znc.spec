#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5AE420CC0209989E (ktonibud@gmail.com)
#
Name     : znc
Version  : 1.7.2
Release  : 14
URL      : http://znc.in/releases/znc-1.7.2.tar.gz
Source0  : http://znc.in/releases/znc-1.7.2.tar.gz
Source99 : http://znc.in/releases/znc-1.7.2.tar.gz.sig
Summary  : An IRC bouncer with modules & scripts support
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 MIT
Requires: znc-bin = %{version}-%{release}
Requires: znc-data = %{version}-%{release}
Requires: znc-lib = %{version}-%{release}
Requires: znc-license = %{version}-%{release}
Requires: znc-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : grep
BuildRequires : icu4c-dev
BuildRequires : pkgconfig(openssl)
BuildRequires : sed
BuildRequires : zlib-dev
Patch1: manpages.patch

%description
# [![ZNC](https://wiki.znc.in/resources/assets/wiki.png)](https://znc.in) - An advanced IRC bouncer

%package bin
Summary: bin components for the znc package.
Group: Binaries
Requires: znc-data = %{version}-%{release}
Requires: znc-license = %{version}-%{release}
Requires: znc-man = %{version}-%{release}

%description bin
bin components for the znc package.


%package data
Summary: data components for the znc package.
Group: Data

%description data
data components for the znc package.


%package dev
Summary: dev components for the znc package.
Group: Development
Requires: znc-lib = %{version}-%{release}
Requires: znc-bin = %{version}-%{release}
Requires: znc-data = %{version}-%{release}
Provides: znc-devel = %{version}-%{release}

%description dev
dev components for the znc package.


%package lib
Summary: lib components for the znc package.
Group: Libraries
Requires: znc-data = %{version}-%{release}
Requires: znc-license = %{version}-%{release}

%description lib
lib components for the znc package.


%package license
Summary: license components for the znc package.
Group: Default

%description license
license components for the znc package.


%package man
Summary: man components for the znc package.
Group: Default

%description man
man components for the znc package.


%prep
%setup -q -n znc-1.7.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548691136
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1548691136
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/znc
cp LICENSE %{buildroot}/usr/share/package-licenses/znc/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/znc/NOTICE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/znc
/usr/bin/znc-buildmod

%files data
%defattr(-,root,root,-)
/usr/share/znc/modules/blockuser/tmpl/blockuser_WebadminUser.tmpl
/usr/share/znc/modules/cert/tmpl/index.tmpl
/usr/share/znc/modules/certauth/tmpl/index.tmpl
/usr/share/znc/modules/lastseen/tmpl/index.tmpl
/usr/share/znc/modules/lastseen/tmpl/lastseen_WebadminUser.tmpl
/usr/share/znc/modules/listsockets/tmpl/index.tmpl
/usr/share/znc/modules/notes/files/trash.gif
/usr/share/znc/modules/notes/tmpl/index.tmpl
/usr/share/znc/modules/perform/tmpl/index.tmpl
/usr/share/znc/modules/q/tmpl/index.tmpl
/usr/share/znc/modules/samplewebapi/tmpl/index.tmpl
/usr/share/znc/modules/sasl/tmpl/index.tmpl
/usr/share/znc/modules/send_raw/files/select.js
/usr/share/znc/modules/send_raw/tmpl/index.tmpl
/usr/share/znc/modules/stickychan/tmpl/index.tmpl
/usr/share/znc/modules/stickychan/tmpl/stickychan_WebadminChan.tmpl
/usr/share/znc/modules/webadmin/files/webadmin.css
/usr/share/znc/modules/webadmin/files/webadmin.js
/usr/share/znc/modules/webadmin/tmpl/add_edit_chan.tmpl
/usr/share/znc/modules/webadmin/tmpl/add_edit_network.tmpl
/usr/share/znc/modules/webadmin/tmpl/add_edit_user.tmpl
/usr/share/znc/modules/webadmin/tmpl/del_network.tmpl
/usr/share/znc/modules/webadmin/tmpl/del_user.tmpl
/usr/share/znc/modules/webadmin/tmpl/encoding_settings.tmpl
/usr/share/znc/modules/webadmin/tmpl/index.tmpl
/usr/share/znc/modules/webadmin/tmpl/listusers.tmpl
/usr/share/znc/modules/webadmin/tmpl/settings.tmpl
/usr/share/znc/modules/webadmin/tmpl/traffic.tmpl
/usr/share/znc/webskins/_default_/pub/External.png
/usr/share/znc/webskins/_default_/pub/_default_.css
/usr/share/znc/webskins/_default_/pub/favicon.ico
/usr/share/znc/webskins/_default_/pub/global.css
/usr/share/znc/webskins/_default_/pub/jquery-1.11.2.js
/usr/share/znc/webskins/_default_/pub/jquery-1.11.2.min.js
/usr/share/znc/webskins/_default_/pub/jquery-ui-sortable.1.11.4.css
/usr/share/znc/webskins/_default_/pub/jquery-ui-sortable.1.11.4.js
/usr/share/znc/webskins/_default_/pub/jquery-ui-sortable.1.11.4.min.css
/usr/share/znc/webskins/_default_/pub/jquery-ui-sortable.1.11.4.min.js
/usr/share/znc/webskins/_default_/pub/robots.txt
/usr/share/znc/webskins/_default_/pub/selectize-0.12.1.css
/usr/share/znc/webskins/_default_/pub/selectize-standalone-0.12.1.js
/usr/share/znc/webskins/_default_/pub/selectize-standalone-0.12.1.min.js
/usr/share/znc/webskins/_default_/tmpl/Banner.tmpl
/usr/share/znc/webskins/_default_/tmpl/BaseHeader.tmpl
/usr/share/znc/webskins/_default_/tmpl/BreadCrumbs.tmpl
/usr/share/znc/webskins/_default_/tmpl/DocType.tmpl
/usr/share/znc/webskins/_default_/tmpl/Error.tmpl
/usr/share/znc/webskins/_default_/tmpl/ExtraHeader.tmpl
/usr/share/znc/webskins/_default_/tmpl/Footer.tmpl
/usr/share/znc/webskins/_default_/tmpl/FooterTag.tmpl
/usr/share/znc/webskins/_default_/tmpl/Header.tmpl
/usr/share/znc/webskins/_default_/tmpl/InfoBar.tmpl
/usr/share/znc/webskins/_default_/tmpl/LoginBar.tmpl
/usr/share/znc/webskins/_default_/tmpl/LowerBanner.tmpl
/usr/share/znc/webskins/_default_/tmpl/Menu.tmpl
/usr/share/znc/webskins/_default_/tmpl/MessageBar.tmpl
/usr/share/znc/webskins/_default_/tmpl/Options.tmpl
/usr/share/znc/webskins/_default_/tmpl/_csrf_check.tmpl
/usr/share/znc/webskins/_default_/tmpl/index.tmpl
/usr/share/znc/webskins/dark-clouds/pub/clouds-header.jpg
/usr/share/znc/webskins/dark-clouds/pub/dark-clouds.css
/usr/share/znc/webskins/dark-clouds/pub/favicon.ico
/usr/share/znc/webskins/dark-clouds/tmpl/Banner.tmpl
/usr/share/znc/webskins/dark-clouds/tmpl/FooterTag.tmpl
/usr/share/znc/webskins/dark-clouds/tmpl/Header.tmpl
/usr/share/znc/webskins/dark-clouds/tmpl/LowerBanner.tmpl
/usr/share/znc/webskins/forest/pub/favicon.ico
/usr/share/znc/webskins/forest/pub/forest-header.png
/usr/share/znc/webskins/forest/pub/forest.css
/usr/share/znc/webskins/forest/tmpl/Banner.tmpl
/usr/share/znc/webskins/forest/tmpl/FooterTag.tmpl
/usr/share/znc/webskins/forest/tmpl/Header.tmpl
/usr/share/znc/webskins/forest/tmpl/LowerBanner.tmpl
/usr/share/znc/webskins/ice/pub/favicon.ico
/usr/share/znc/webskins/ice/pub/ice.css
/usr/share/znc/webskins/ice/pub/linkbg.jpg
/usr/share/znc/webskins/ice/pub/pagebg.gif
/usr/share/znc/webskins/ice/tmpl/FooterTag.tmpl
/usr/share/znc/webskins/ice/tmpl/Header.tmpl

%files dev
%defattr(-,root,root,-)
/usr/include/znc/Buffer.h
/usr/include/znc/Chan.h
/usr/include/znc/Client.h
/usr/include/znc/Config.h
/usr/include/znc/Csocket.h
/usr/include/znc/ExecSock.h
/usr/include/znc/FileUtils.h
/usr/include/znc/HTTPSock.h
/usr/include/znc/IRCNetwork.h
/usr/include/znc/IRCSock.h
/usr/include/znc/Listener.h
/usr/include/znc/MD5.h
/usr/include/znc/Message.h
/usr/include/znc/Modules.h
/usr/include/znc/Nick.h
/usr/include/znc/Query.h
/usr/include/znc/SHA256.h
/usr/include/znc/SSLVerifyHost.h
/usr/include/znc/Server.h
/usr/include/znc/Socket.h
/usr/include/znc/Template.h
/usr/include/znc/Threads.h
/usr/include/znc/Translation.h
/usr/include/znc/User.h
/usr/include/znc/Utils.h
/usr/include/znc/WebModules.h
/usr/include/znc/ZNCDebug.h
/usr/include/znc/ZNCString.h
/usr/include/znc/defines.h
/usr/include/znc/main.h
/usr/include/znc/version.h
/usr/include/znc/znc.h
/usr/include/znc/zncconfig.h
/usr/lib64/pkgconfig/znc.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/znc/admindebug.so
/usr/lib64/znc/adminlog.so
/usr/lib64/znc/alias.so
/usr/lib64/znc/autoattach.so
/usr/lib64/znc/autocycle.so
/usr/lib64/znc/autoop.so
/usr/lib64/znc/autoreply.so
/usr/lib64/znc/autovoice.so
/usr/lib64/znc/awaynick.so
/usr/lib64/znc/awaystore.so
/usr/lib64/znc/block_motd.so
/usr/lib64/znc/blockuser.so
/usr/lib64/znc/bouncedcc.so
/usr/lib64/znc/buffextras.so
/usr/lib64/znc/cert.so
/usr/lib64/znc/certauth.so
/usr/lib64/znc/chansaver.so
/usr/lib64/znc/clearbufferonmsg.so
/usr/lib64/znc/clientnotify.so
/usr/lib64/znc/controlpanel.so
/usr/lib64/znc/crypt.so
/usr/lib64/znc/ctcpflood.so
/usr/lib64/znc/dcc.so
/usr/lib64/znc/disconkick.so
/usr/lib64/znc/fail2ban.so
/usr/lib64/znc/flooddetach.so
/usr/lib64/znc/identfile.so
/usr/lib64/znc/imapauth.so
/usr/lib64/znc/keepnick.so
/usr/lib64/znc/kickrejoin.so
/usr/lib64/znc/lastseen.so
/usr/lib64/znc/listsockets.so
/usr/lib64/znc/log.so
/usr/lib64/znc/missingmotd.so
/usr/lib64/znc/modules_online.so
/usr/lib64/znc/nickserv.so
/usr/lib64/znc/notes.so
/usr/lib64/znc/notify_connect.so
/usr/lib64/znc/partyline.so
/usr/lib64/znc/perform.so
/usr/lib64/znc/q.so
/usr/lib64/znc/raw.so
/usr/lib64/znc/route_replies.so
/usr/lib64/znc/sample.so
/usr/lib64/znc/samplewebapi.so
/usr/lib64/znc/sasl.so
/usr/lib64/znc/savebuff.so
/usr/lib64/znc/schat.so
/usr/lib64/znc/send_raw.so
/usr/lib64/znc/shell.so
/usr/lib64/znc/simple_away.so
/usr/lib64/znc/stickychan.so
/usr/lib64/znc/stripcontrols.so
/usr/lib64/znc/watch.so
/usr/lib64/znc/webadmin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/znc/LICENSE
/usr/share/package-licenses/znc/NOTICE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/znc-buildmod.1
/usr/share/man/man1/znc.1
