import os
import urllib.request
from html.parser import HTMLParser


class Parser1(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.url = []
        self.is_td = 0
        self.is_first = 1

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.is_td = 1
        if self.is_td == 1 and self.is_first == 1 and tag == 'a':
            self.url.append(attrs[0][1])

    def handle_endtag(self, tag):
        if tag == 'td':
            self.is_td = 0
        if tag == 'table':
            self.is_first = 0


class Parser2(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.link = ''

    @staticmethod
    def _attr(self, attrlist, attrname):
        for attr in attrlist:
            if attr[0] == attrname:
                return attr[1]
        return None

    def handle_starttag(self, tag, attrs):
        if 'http://files.actmi.net' in str(Parser2._attr(self, attrs, 'href')):
            self.link = Parser2._attr(self, attrs, 'href')


data = urllib.request.urlopen('http://actmi.net/downloads/', timeout=10).read()
parser = Parser1()
parser.feed(str(data))
new_url = []


def is_paper(url):
    if 'answers' in url or 'vocab' in url or 'stats' in url:
        return False
    return True


new_url = list(filter(is_paper, parser.url))
new_url = list(map(lambda x: x.strip('.'), new_url))
paper_names = list(map(lambda x: x.strip('./') + '.pdf', new_url))
new_url = list(map(lambda x: 'http://actmi.net/downloads' + x, new_url))

# print(new_url)

download_links = []
for url in new_url:
    data = urllib.request.urlopen(url, timeout=10).read()
    parser = Parser2()
    parser.feed(str(data))
    download_links.append(parser.link)
    print('link parsed: '
          + parser.link)
# print(download_links)
# download_dir = os.getcwd() + '/papers/'
download_dir = os.path.expanduser('~/Downloads/ACT_Papers/')
if not os.path.exists(download_dir):
    os.mkdir(download_dir)
for i in range(len(download_links)):
    file_name = download_dir + paper_names[i]
    try:
        urllib.request.urlretrieve(download_links[i], file_name)
    except:
        print('something wrong happened downloading: ' + file_name)
    else:
        print('successfully downloaded: ' + file_name)
