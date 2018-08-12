""" darkbox wget command """

import argparse
import urllib.request


class wget:
    def __init__(self):
        self.version = '0.0.1'
    
    def get_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--version',
            default=False, action='store_true')
        parser.add_argument('url',
            nargs='?', type=str)
        parser.add_argument('-O', '--output',
            default=False, type=str)
        return parser
    
    def run(self):
        parser = self.get_parser()
        args = vars(parser.parse_args())

        if args['version']:
            print('darkbox {cls} v{version}'.format(
                cls=self.__class__.__name__,
                version=self.version))
            return

        url = args['url']

        if not url:
            print("Error: No URL specified.")
            return
        
        if not url.startswith('http'):
            url = 'http://' + url
        
        if args['output']:
            urllib.request.urlretrieve(url, args['output'])
            return
        
        response = urllib.request.urlopen(url)
        data = response.read()
        print(data.decode('utf-8'))