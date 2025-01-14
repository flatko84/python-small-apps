import urllib.request
from bs4 import BeautifulSoup

class Crawler:

    # I find it interesting how properties are set in a class
    def __init__(self, homepage):
        self.homepage = homepage
        self.queue = []
        self.visited = []

    # entry point
    def crawl(self):
        self.queue.append(self.homepage)
        while len(self.queue):
            current = self.queue.pop(0)
            html = self.make_request(current)
            links = self.get_links(html)
            for link in links:
                if (len(link) > 0 and link[0] == '/'):
                    link = self.homepage + link
                if (link not in self.visited and len(link) > 0 and link[0] != '#' and (link[0] == '/' or link[:len(self.homepage)] == self.homepage)):
                    self.visited.append(link)
                    self.queue.append(link)
            self.update_reports()
        print(self.visited)

    # real-time tracking of the queue and the total visited urls. Mesmerizing when open in VS Code :)
    def update_reports(self):
        total = open("./total.txt", "w")
        queue = open("./queue.txt", "w")
        for url in self.visited:
            total.write(url + "\n")
        for url in self.queue:
            queue.write(url + "\n")

    # make HTTP request, exception when response code not in range 200-299
    def make_request(self, url):
        try:
            response = urllib.request.urlopen(url)
            print(url + ' ' + str(response.getcode()))
            if response.getcode() < 200 or response.getcode() >= 300:
                print(url + ' error code ' + response.getcode())
                return ''
            return response.read()
        except Exception as exception:
            print(exception)
            return ''

    # use external package to get all links. Learning BeautifulSoup is not a priority for now, I've asked ChatGPT how to get all links
    def get_links(self, html):
        soup = BeautifulSoup(html, 'html.parser') # ChatGPT
        links = [a['href'] for a in soup.find_all('a', href=True)] # ChatGPT, this is an interesting approach, I'll take a look at it
        return links

# instantiate with a hardcoded homepage. Homepage has to be without the trailing slash
crawler = Crawler("https://www.suse.com")
crawler.crawl()