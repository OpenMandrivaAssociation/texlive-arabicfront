%global tl_name arabicfront
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Frontmatter with arabic page numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/arabicfront
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabicfront.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabicfront.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package modifies the definitions of \frontmatter and \mainmatter so
that page numbering starts in arabic style from the front matter while
preserving the rest of the original definitions. For it to work,
\pagenumbering has to be inside these macros--most of classes do that,
but there are exceptions like memoir.

