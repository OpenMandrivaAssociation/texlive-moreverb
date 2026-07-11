%global tl_name moreverb
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3a
Release:	%{tl_revision}.1
Summary:	Extended verbatim
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/moreverb
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moreverb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moreverb.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moreverb.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of verbatim facilities that provide line-numbered verbatim,
verbatim that obeys TAB characters, verbatim input and verbatim output
to file. The package makes use of the LaTeX required verbatim package.
The package is formed from a series of small pieces, and is somewhat
unstructured. The user who looks for thought-through verbatim facilities
is advised to consider using the fancyvrb package in place of moreverb.

