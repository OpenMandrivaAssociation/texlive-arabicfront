Name:		texlive-arabicfront
Version:	51474
Release:	2
Summary:	Frontmatter with arabic page numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/arabicfront
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabicfront.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabicfront.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package modifies the definitions of \frontmatter and
\mainmatter so that page numbering starts in arabic style from
the front matter while preserving the rest of the original
definitions. For it to work, \pagenumbering has to be inside
these macros--most of classes do that, but there are exceptions
like memoir.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/arabicfront
%doc %{_texmfdistdir}/doc/latex/arabicfront

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
