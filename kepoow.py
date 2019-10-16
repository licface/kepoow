import argparse
from re import findall
from make_colors import make_colors
import clipboard
import sys
ERROR_MESSAGE = ''

class kepoow(object):
    def __init__(self, url = None):
        super(kepoow, self)
        self.url = url
        
    def generate(self, link):
        if not link[-2:] == "==":
            link += "=="
        if 'https' in link or 'http' in link:
            if 'kepoow' in link:
                url_64 = ''
                url_64 = findall('r(=.*?==)', str(link))
                if len(url_64) > 0:
                    url_64 = url_64[0]
                else:
                    url_64 = ''
                if url_64:
                    url_download = url_64.decode('base64')
                    clipboard.copy(url_download)
                    return url_download
                else:
                    print make_colors("NOT FOUND !", 'lw', 'lr', ['blink'])
                    return False
            else:
                print make_colors('NOT A KEPOOW URL !', 'lw', 'lr', ['blink'])
                ERROR_MESSAGE = 'NOT A KEPOOW URL !'
                return False
        else:
            print make_colors('NOT A VALID URL !', 'lw', 'lr', ['blink'])
            ERROR_MESSAGE = "NOT A VALID URL !"
            return False
        
    def usage(self):
        parser = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter)
        parser.add_argument('URL', help = 'kepoow url, just type "c" for get link from clipboard', action = 'store')
        
        if len(sys.argv) == 1:
            parser.print_help()
        else:
            args = parser.parse_args()
            if args.URL == 'c':
                url = clipboard.paste()
            else:
                url = args.url
            self.generate(url)
            
if __name__ == '__main__':
    c = kepoow()
    c.usage()
                
                
            
        
        