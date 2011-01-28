Summary:	Library for dealing with deprecated functions
Name:		ruby-deprecated
Version:	2.0.1
Release:	1
License:	Ruby
Source0:	http://rubyforge.org/frs/download.php/40375/deprecated-%{version}.tar.gz
# Source0-md5:	10d0962965ee856c364be2bfe8f1c323
Group:		Development/Languages
URL:		http://deprecated.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small library intended to aid developers working with
deprecated code. The idea comes from the 'D' programming language,
where developers can mark certain code as deprecated, and then
allow/disallow the ability to execute deprecated code.

%prep
%setup -q -n deprecated-%{version}
install %{_datadir}/setup.rb .

%build
ruby setup.rb config --rbdir=%{ruby_rubylibdir} --sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*.rb
