%global tl_name returntogrid
%global tl_revision 48485

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Semi-automatic grid typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/returntogrid
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/returntogrid.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/returntogrid.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
returntogrid offers a few commands to get something like an simple,
semi-automatic grid typesetting. It does more or less what the existing
gridset package does. The main differences to gridset are that
returntogrid works also with LuaLaTeX and that it has also a command to
do some horizontal movements to get to "tab" positions.

