%define oname oa-core

Name:       rubygem-%{oname}
Version:    0.0.5
Release:    2
Summary:    HTTP Basic strategies for OmniAuth
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/intridea/omniauth
Source0:    %{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Suggests:   rubygem(rake)
Suggests:   rubygem(mg) >= 0.0.8
Suggests:   rubygem(rspec) >= 1.3.0
Suggests:   rubygem(webmock) >= 1.3.4
Suggests:   rubygem(rack-test) >= 0.5.4
Suggests:   rubygem(json) >= 1.4.3
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
HTTP Basic strategies for OmniAuth.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGELOG.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE.rdoc
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Mon Dec 20 2010 Rémy Clouard <shikamaru@mandriva.org> 0.0.5-1mdv2011.0
+ Revision: 623511
- import rubygem-oa-core

