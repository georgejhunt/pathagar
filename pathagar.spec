Name:           pathagar
Version:        0
Release:        5

Summary:        Book Server

Group:          Applications/Archiving
License:        GPLv2

URL:            http://wiki.laptop.org
%global         path1        git://github.com/PathagarBooks/pathagar


BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     x86_64
Requires:      yum
Requires:       python
Requires:       mod_wsgi
Requires:       python-setuptools
Requires:       sqlite
Requires:       Django
BuildRequires: git
BuildRequires: python-pip
BuildRequires: python-virtualenv


%description
This package contains the XS repository configuration.

%prep
%setup -q  -c -T


%build
TARGET=/tmp/tree.$$
mkdir -p $TARGET/pathagar

# get the environment set up
virtualenv $TARGET/pathagar

# need place to put the git clone
TFILE=/tmp/pathagargit.$$
mkdir -p $TFILE
cd $TFILE

# git wants to clone into an empty directory
git clone git://github.com/PathagarBooks/pathagar
rm -rf ./pathagar/.git
cp -rp $TFILE/pathagar/* $TARGET/pathagar
rm -rf $TFILE

cd $TARGET/pathagar
$TARGET/pathagar/bin/pip install -r requirements.pip
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/library/
cp -rp $TARGET/pathagar $RPM_BUILD_ROOT/library



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/library/pathagar


%changelog
