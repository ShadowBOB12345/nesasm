%global		gitcommit	"2b39ec6"

Name:		nesasm
Version:	3.6
Release:	2%{?dist}
Summary:	6502 assembler with specific NES support

License:	MIT
URL:		https://github.com/ClusterM/nesasm
Source0:	https://github.com/ClusterM/nesasm/archive/refs/tags/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make

%description
Just another modification of nesasm. Based on modification by Tim Hentenaar
which is based on modification by Bob Rost which is based on modification
of nesasm 2.51 from MagicKit which is based on 6502 assembler
by J. H. Van Ornum.

%prep
%setup -q 

%build
make %{?_smp_mflags} EXTRA_CFLAGS="%{optflags}" COMMIT="%gitcommit" -C source/


%install
install -pD -m 755 source/%{name} %buildroot%_bindir/%{name}


%files
%doc documentation/*.txt README.md
%_bindir/*

%changelog
* Fri Dec 10 2021 Andrew Clark <andrewclarkii@gmail.com> - 3.6-2
- specfile changes

* Sat Dec 04 2021 Andrew Clark <andrewclarkii@gmail.com> - 3.6-1
- Initial version