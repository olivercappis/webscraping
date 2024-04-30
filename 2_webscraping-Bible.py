import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import ssl

context = ssl._create_unverified_context()





random_chapter = random.randint(1,22)

if random_chapter < 10:
    webpage = f"https://ebible.org/asv/JHN0{random_chapter}.htm"
else:
    webpage = f"https://ebible.org/asv/JHN{random_chapter}.htm"



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req, context=context).read()
soup = BeautifulSoup(webpage, 'html.parser')

page_verses = soup.findAll('div', class_='p')

verse_list = []

for section_verses in page_verses:
    myverses = section_verses.text.split('  ')
    # print(verse_list)


for v in verse_list:
    verse_list.append(v)


myverses = [i for i in myverses if i != ' ']


mychoice = random.choice(myverses)

print(f"chapter: {random_chapter} verse: {mychoice}")






