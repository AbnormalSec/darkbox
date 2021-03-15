"""darkbox curl command"""

import argparse
import urllib.request

from darkbox.commands.template import Command


class curl(Command):
    """darkbox curl

    transfer a URL

    Designed to be similar to curl by Daniel Stenberg.
    Resource: https://curl.haxx.se
    """

    def __init__(self):
        self.version = '0.1.0'
    
    def get_parser(self):
        parser = super().get_parser(description='darkbox curl')
        parser.add_argument('url', type=str, help='specify URL')
        parser.add_argument('-O', '--output', default=False, type=str,
                            help='Write output to a file')
        return parser
    
    def run(self, args=None):
        args = self.get_args(args)
        url = args['url']
        
        if not url.startswith('http'):
            url = 'http://' + url
        
        if args['output']:
            file_path = args['output']
            try:
                urllib.request.urlretrieve(url, file_path)
            except FileNotFoundError:
                self.file_not_found_error(file_path)
            except IsADirectoryError:
                self.directory_error(file_path)
            return
        
        response = urllib.request.urlopen(url)
        data = response.read()
        print(data.decode('utf-8').rstrip())