"""darkbox exip command"""

import argparse
import urllib.request

from darkbox.commands.template import Command


class exip(Command):
    """darkbox exip

    obtain external ip address

    This tool was written by vesche and is unique to the darkbox project.
    """

    def __init__(self):
        self.version = '0.1.0'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox exip')
        return parser
    
    def run(self, args=None):
        args = self.get_args(args)

        exip_sites = [
            'ipinfo.io/ip', 'icanhazip.com', 'ident.me', 'ipecho.net/plain',
            'myexternalip.com/raw', 'wtfismyip.com/text'
        ]
        external_ip = str()
        for url in exip_sites:
            try:
                external_ip = urllib.request.urlopen('http://'+url).read()
            except IOError:
                pass
            if external_ip and (6 < len(external_ip) < 16):
                break

        if external_ip:
            print(external_ip.decode('utf-8').rstrip())
        else:
            print('Error: Could not obtain external IP, no internet access?')