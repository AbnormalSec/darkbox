""" darkbox curl command """

from .template import Command

import argparse
import urllib.request


class curl(Command):
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = super().get_parser()
        parser.add_argument('url', nargs='?', type=str)
        parser.add_argument('-O', '--output', default=False, type=str)
        return parser
    
    def run(self):
        args = self.get_args()
        url = args['url']

        if not url:
            self.get_parser().print_help()
            return
        
        if not url.startswith('http'):
            url = 'http://' + url
        
        if args['output']:
            urllib.request.urlretrieve(url, args['output'])
            return
        
        response = urllib.request.urlopen(url)
        data = response.read()
        print(data.decode('utf-8'))