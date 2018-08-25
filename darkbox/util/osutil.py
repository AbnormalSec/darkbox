""" darkbox.util.osutil """

import platform


def get_platform():
    plat = platform.system()
    if plat == 'Darwin':
        plat_monk = 'mac'
    elif plat == 'Windows':
        plat_monk = 'win'
    elif plat == 'Linux':
        plat_monk = 'nix'
    else:
        plat_monk = 'unk'
    return plat_monk


def get_distro():
    """
    From platform.py:
    _supported_dists = (
        'SuSE', 'debian', 'fedora', 'redhat', 'centos',
        'mandrake', 'mandriva', 'rocks', 'slackware', 'yellowdog', 'gentoo',
        'UnitedLinux', 'turbolinux', 'arch', 'mageia')
    """
    distro = platform.linux_distribution()
    return distro