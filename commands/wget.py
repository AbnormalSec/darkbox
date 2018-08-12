""" darkbox wget command """

import argparse
import urllib.request


class wget:
    def __init__(self):
        version = '0.0.1'
    
    def get_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('url', type=str)
        parser.add_argument('-v', '--version',
            default=False, action='store_true')
        parser.add_argument('-O', '--output',
            default=False, type=str)
        return parser
    
    def run(self):
        parser = self.get_parser()
        args = vars(parser.parse_args())
        if args['version']:
            print('darkbox {} v{}'.format(self.__name__, self.version))
            return

        url = args['url']

        if not url:
            print("Error: No URL specified.")
            return
        
        if not url.startswith('http'):
            print("Error: URL must start with http:// or https://")
            return
        
        if args['output']:
            urllib.request.urlretrieve(url, args['output'])
            return
        
        response = urllib.request.urlopen(url)
        data = response.read()
        print(data.decode('utf-8'))