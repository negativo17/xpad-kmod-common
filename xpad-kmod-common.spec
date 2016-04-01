%global debug_package %{nil}

Name:           xpad-kmod-common
Version:        4.1
Release:        1%{?dist}
Summary:        Common files for the X-Box gamepad driver (SteamOS variant)
License:        GPLv2+
URL:            http://store.steampowered.com/steamos/
BuildArch:      noarch

Source0:        https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/plain/COPYING

%description
Common files for the X-Box gamepad driver with specific patches made by Valve
for SteamOS.

%prep
%setup -q -T -c -n %{name}-%{version}
cp %{SOURCE0} .

%install
mkdir -p %{buildroot}%{_sysconfdir}/depmod.d
echo "override xpad * extra/xpad" > %{buildroot}%{_sysconfdir}/depmod.d/xpad.conf

%files
%doc COPYING
%{_sysconfdir}/depmod.d/xpad.conf

%changelog
* Sat Nov 14 2015 Simone Caronni <negativo17@gmail.com> - 4.1-1
- Update to version from 4.1 branch (SteamOS 2.x).

* Wed Jul 08 2015 Simone Caronni <negativo17@gmail.com> - 0.2-1
- Rebase to brewmaster 3.18 kernel.
- Drop integrated patches.

* Wed Oct 01 2014 Simone Caronni <negativo17@gmail.com> - 0.1-2
- Use directly SteamOS kernel source, remove patches:
  https://github.com/ValveSoftware/steamos_kernel/commits/alchemist-3.10/drivers/input/joystick/xpad.c

* Thu May 29 2014 Simone Caronni <negativo17@gmail.com> - 0.1-1
- First build.
