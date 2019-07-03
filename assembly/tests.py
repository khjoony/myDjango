"""
test
"""
#from django.test import TestCase

# Create your tests here.
"""  국회의원 이름 크롤링
import requests
from bs4 import BeautifulSoup as bs

url = 'url'
html = requests.get(url).text
soup = bs(html, 'html.parser')
results = soup.select('a[href*=jsMemPop]')

names = []
for n in results:
    names.append(n.text)

from assembly.models import Member

for name in names:
    Member.objects.create(name = name)
"""
# print('Hello world')
