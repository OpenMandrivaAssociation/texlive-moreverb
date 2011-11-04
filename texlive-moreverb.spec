# revision 22126
# category Package
# catalog-ctan /macros/latex/contrib/moreverb
# catalog-date 2011-04-18 22:03:09 +0200
# catalog-license lppl
# catalog-version 2.3a
Name:		texlive-moreverb
Version:	2.3a
Release:	1
Summary:	Extended verbatim
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/moreverb
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moreverb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moreverb.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moreverb.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A collection of verbatim facilities that provide line-numbered
verbatim, verbatim that obey's TAB characters, verbatim input
and verbatim output to file. The package makes use of the LaTeX
required verbatim package. The package formed from a series of
small pieces, and is somewhat unstructured. The user who looks
for thought-through verbatim facilities is advised to consider
using the fancyvrb package in place of moreverb.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/moreverb/moreverb.sty
%doc %{_texmfdistdir}/doc/latex/moreverb/README
%doc %{_texmfdistdir}/doc/latex/moreverb/moreverb.pdf
#- source
%doc %{_texmfdistdir}/source/latex/moreverb/moreverb.dtx
%doc %{_texmfdistdir}/source/latex/moreverb/moreverb.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
