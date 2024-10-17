Name:		texlive-returntogrid
Version:	48485
Release:	2
Summary:	Semi-automatic grid typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/returntogrid
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/returntogrid.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/returntogrid.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
returntogrid offers a few commands to get something like an
simple, semi-automatic grid typesetting. It does more or less
what the existing gridset package does. The main differences to
gridset are that returntogrid works also with LuaLaTeX and that
it has also a command to do some horizontal movements to get to
"tab" positions.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/returntogrid
%doc %{_texmfdistdir}/doc/latex/returntogrid

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
