""" darkbox exip command """

from darkbox.commands.template import Command

import argparse
import urllib.request


class exip(Command):
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox exip')
        return parser
    
    def run(self):
        args = self.get_args()

        exip_sites = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                       'ipecho.net/plain', 'myexternalip.com/raw',
                       'wtfismyip.com/text' ]
        external_ip = ''
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
            print("Error: Could not obtain external IP, no internet access?")