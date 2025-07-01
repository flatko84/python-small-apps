import urllib.request
from bs4 import BeautifulSoup
import re
import csv
import time

class Scraper:
    """Load and scrape a single page."""

    def __init__(self, url):
        self.url = url
        self.make_request()
        self.get_bs_object()
        self.fields = {}
        self.get_links()
        self.get_images()
        self.get_product_properties()
        self.get_h1()
        self.get_by_class('item_subtitle', 'model')
        
        
    def make_request(self):
        """Make an HTTP request to the URL."""
        try:
            response = urllib.request.urlopen(self.url)
            print(self.url + ' ' + str(response.getcode()))
            if response.getcode() < 200 or response.getcode() >= 300:
                raise Exception
            self.html = response.read()
        except Exception as exception:
            print(exception)
            self.html = ''
        
    def get_bs_object(self):
        self.bs_object = BeautifulSoup(self.html, 'html.parser')
    
    def get_links(self):
        links = [a['href'] for a in self.bs_object.find_all('a', href=True)]
        self.links = links
    
    def get_images(self):
        images = [img["src"] for img in self.bs_object.find_all('img') if 'detail' in img["src"]]
        try:
            self.fields.update({'image': images[0]})
        except:
            print(f"Image not found for {self.url}")
    
    def get_product_properties(self):
        content = self.bs_object.find('div', class_='item_text').find_all('p')
        try:
            for desc in content:
                exploded = str(desc).split(':')
                self.fields.update({self.strip_tags(exploded[0]): self.strip_tags(exploded[1])})
        except:
            print("Probably not a product page.")

    def get_h1(self):
        try:
            h1 = self.bs_object.find('h1')
            self.fields.update({'brand': self.strip_tags(str(h1))})
        except:
            print("Probably not a product page.")

    def get_by_class(self, element_class, name):
        try:
            title = self.bs_object.find('div', class_=element_class)
            self.fields.update({name: self.strip_tags(str(title))})
        except:
            print("Probably not a product page.")
    
    @staticmethod
    def strip_tags(input):
        return re.sub('<[^<]+?>', '', input)

class Crawler:
    """Use BFS to crawl an entire website."""

    def __init__(self, homepage):
        self.homepage = homepage
        self.queue = []
        self.visited = []
        self.fields_header = []
        self.csvfile = open('./table.csv', 'w')
        self.recordswriter = csv.writer(self.csvfile)
        

    def crawl(self):
        """Entry point."""
        self.queue.append(self.homepage)
        while len(self.queue):
            current = self.queue.pop(0)
            page = Scraper(current)
            if 'image' in page.fields.keys() and len(page.fields['image']) and 'view' in current:
                self.write_csv(page.fields)
            for link in page.links:
                if (len(link) > 0 and link[0] == '/'):
                    link = self.homepage + link
                if (link not in self.visited and len(link) > 0 and link[0] != '#' and (link[0] == '/' or link[:len(self.homepage)] == self.homepage)):
                    self.visited.append(link)
                    self.queue.append(link)
            self.update_reports()
            time.sleep(5)

        print(self.visited)

    def update_reports(self):
        """Print reports to a file in real time."""
        with open("./total.txt", "w") as total:
            for url in self.visited:
                total.write(url + "\n")
        with open("./queue.txt", "w") as queue:
            for url in self.queue:
                queue.write(url + "\n")

    def write_csv(self, fields):
        row = []
        for key, value in enumerate(fields):
            row.append(value)

        self.recordswriter.writerow(row)

    
        
#page = Scraper('https://opticlasa.com/products/view/gucci-GG1527S-001-122636')
#print(page.fields)



# instantiate with a hardcoded homepage. Homepage has to be without the trailing slash
crawler = Crawler("https://www.opticlasa.com")
crawler.crawl()
