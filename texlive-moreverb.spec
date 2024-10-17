Name:		texlive-moreverb
Version:	22126
Release:	2
Summary:	Extended verbatim
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/moreverb
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moreverb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moreverb.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moreverb.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of verbatim facilities that provide line-numbered
verbatim, verbatim that obey's TAB characters, verbatim input
and verbatim output to file. The package makes use of the LaTeX
required verbatim package. The package formed from a series of
small pieces, and is somewhat unstructured. The user who looks
for thought-through verbatim facilities is advised to consider
using the fancyvrb package in place of moreverb.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/moreverb/moreverb.sty
%doc %{_texmfdistdir}/doc/latex/moreverb/README
%doc %{_texmfdistdir}/doc/latex/moreverb/moreverb.pdf
#- source
%doc %{_texmfdistdir}/source/latex/moreverb/moreverb.dtx
%doc %{_texmfdistdir}/source/latex/moreverb/moreverb.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
