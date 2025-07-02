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
        self.fields = {'url': url}
        self.get_links()
        self.get_images()
        self.get_product_properties()
        self.get_h1()
        self.get_by_class('div', 'item_subtitle', 'model')
        self.get_by_class('span', 'new_price', 'price')
        self.get_by_class('div', 'type_material', 'material')
        
        
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
            print(f"Probably not a product page.")
    
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

    def get_by_class(self, element, element_class, name):
        try:
            title = self.bs_object.find(element, class_=element_class)
            self.fields.update({name: self.strip_tags(str(title))})
        except:
            print("Probably not a product page.")
    
    @staticmethod
    def strip_tags(input):
        return re.sub('<[^<]+?>', '', input)

class Crawler:
    """Use BFS to crawl an entire website."""

    map_fields = {'brand': 'brand',
                  'model': 'model',
                  'price': 'price',
                  'model_size': None,
                  'shape': 'Форма',
                  'frame_material': 'material',
                  'frame_color': 'Цвят на рамката',
                  'image_url': 'image',
                  'link': 'url',
                  'model_type': None,
                  'category_in_dataset': None}

    def __init__(self, homepage, resume = True):
        self.homepage = homepage
        self.queue = []
        self.visited = []
        self.fields_header = []
        self.csvfile = open('./table.csv', 'w', newline='', encoding='utf-8-sig')
        self.recordswriter = csv.writer(self.csvfile, delimiter=";")
        if resume:
            self.resume()
        

    def crawl(self):
        """Entry point."""
        self.queue.append(self.homepage)
        self.recordswriter.writerow(self.map_fields.keys())
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
            time.sleep(10)

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
        """Write results to CSV file."""
        row = []
        for key, value in self.map_fields.items():
            if value in fields.keys() and fields[value]:
                row.append(fields[value])
            else:
                row.append('')
        self.recordswriter.writerow(row)
        self.csvfile.flush()

    def resume(self):
        """Resume last state from the text files."""
        try:
            with open('./queue.txt', 'r') as queue:
                reader = csv.reader(queue)
                for row in reader:
                    if len(row) > 0:
                        self.queue.append(row[0])
            with open('./total.txt', 'r') as total:
                reader = csv.reader(total)
                for row in reader:
                    if len(row) > 0:
                        self.visited.append(row[0])
        except FileNotFoundError:
            print("Nothing to resume. Starting clean.")


# instantiate with a hardcoded homepage. Homepage has to be without the trailing slash
crawler = Crawler("https://www.opticlasa.com")
crawler.crawl()
