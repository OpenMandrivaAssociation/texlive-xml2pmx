Name:		texlive-xml2pmx
Version:	57972
Release:	2
Summary:	Convert MusicXML to PMX and MusiXTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xml2pmx
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xml2pmx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xml2pmx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This program translates MusicXML files to input suitable for
PMX and MusiXTeX processing. This package supports Windows,
MacOS and Linux systems.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/xml2pmx.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/xml2pmx.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
