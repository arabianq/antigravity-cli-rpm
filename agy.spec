Name:           agy
Version:        1.0.2
Release:        1%{?dist}
Summary:        Google Antigravity CLI

License:        Proprietary
URL:            https://antigravity-cli-auto-updater-974169037036.us-central1.run.app
Source0:        https://storage.googleapis.com/antigravity-public/antigravity-cli/1.0.2-6109799369277440/linux-x64/cli_linux_x64.tar.gz

ExclusiveArch:  x86_64

%description
Antigravity CLI flat native build.

%prep
%setup -q -c

%build
# Pre-compiled binary, nothing to build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 antigravity %{buildroot}%{_bindir}/agy

%files
%{_bindir}/agy

%changelog
* Sun May 24 2026 Antigravity CLI Packager <packager@example.com> - 1.0.2-1
- Initial COPR package for Antigravity CLI
