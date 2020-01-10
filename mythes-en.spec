Name: mythes-en
Summary: English thesaurus
Version: 3.0
Release: 13%{?dist}
Source: http://www.danielnaber.de/wn2ooo/wn2ooo20050723.tgz
Group: Applications/Text
URL: http://www.danielnaber.de/wn2ooo/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python, perl, wordnet = %{version}
License: MIT and Public Domain and (GPL+ or Artistic)
BuildArch: noarch
Requires: mythes

%description
English thesaurus.

%prep
%setup -q -c %{name}-%{version}

%build
export WNHOME=%{_datadir}/wordnet-%{version}
python wn2ooo/wn2ooo.py > th_en_US_v2.dat
cat th_en_US_v2.dat | perl wn2ooo/th_gen_idx.pl > th_en_US_v2.idx


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_en_US_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
en_US_aliases="en_AG en_AU en_BS en_BW en_BZ en_CA en_DK en_GB en_GH en_IE en_IN en_JM en_MW en_NA en_NG en_NZ en_PH en_SG en_TT en_ZA en_ZM en_ZW"
for lang in $en_US_aliases; do
        ln -s th_en_US_v2.idx "th_"$lang"_v2.idx"
        ln -s th_en_US_v2.dat "th_"$lang"_v2.dat"
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc wn2ooo/LICENSE_th_gen_idx.txt wn2ooo/README.txt
%{_datadir}/mythes/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.0-13
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 12 2012 Caolán McNamara <caolanm@redhat.com> - 3.0-10
- add some aliases

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 07 2010 Caolán McNamara <caolanm@redhat.com> - 3.0-7
- clarify licence of tools

* Sat Apr 03 2010 Caolán McNamara <caolanm@redhat.com> - 3.0-6
- mythes now owns /usr/share/mythes

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Caolán McNamara <caolanm@redhat.com> - 3.0-4
- extend coverage

* Wed Jun 10 2009 Caolán McNamara <caolanm@redhat.com> - 3.0-3
- rebuild against wordnet package

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 28 2007 Caolán McNamara <caolanm@redhat.com> - 3.0-1
- initial version
