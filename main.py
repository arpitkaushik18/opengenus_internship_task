from queue import Queue
from spider import Spider
from domain import *
from demo import *
from urllib.request import urlopen
PROJECT_NAME ='opengenus_internship_task'
HOMEPAGE = 'https://www.mysirg.com'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
queue= Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

r=urlopen(HOMEPAGE)
print("Size of Webpage is ",len(r.read())/8,"bytes")

def crawl():
    queued_links= file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links))+' Links in the queue ')
crawl()