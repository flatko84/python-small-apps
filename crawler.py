import urllib.request
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, url):
        self.url = url
        self.queue = []
        self.visited = set()
    def bfs(self):
        while len(self.queue):
            current = self.queue.pop(0)
            html = self.make_request(current)
            links = self.get_links(html)
            for link in links:
                self.queue.append(link)
    def make_request(self):
        return urllib.request.urlopen(self.url).read()
    def get_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links

crawler = Crawler("https://guitar-lessons.eu")
crawler.make_request()