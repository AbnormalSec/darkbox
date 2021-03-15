"""darkbox.util.osutil"""

import distro
import platform


def get_platform():
    plat = platform.system()
    if plat == 'Darwin':
        return 'mac'
    elif plat == 'Windows':
        return 'win'
    elif plat == 'Linux':
        return 'nix'
    else:
        return 'unk'


def get_distro():
    """
    From platform.py:
    _supported_dists = (
        'SuSE', 'debian', 'fedora', 'redhat', 'centos',
        'mandrake', 'mandriva', 'rocks', 'slackware', 'yellowdog', 'gentoo',
        'UnitedLinux', 'turbolinux', 'arch', 'mageia')
    """
    return distro.linux_distribution(full_distribution_name=False)[0]