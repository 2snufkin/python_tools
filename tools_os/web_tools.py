import urllib
from bs4 import BeautifulSoup
import requests


def get_html(address):
    response = urllib.urlopen(address)
    return response.read()


def get_all_links(page):
    r = requests.get(page)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        print(link.get('href'))

