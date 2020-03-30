import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 '
}
url = 'https://ytn.co.kr/_ln/0101_202003301150162102'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

url = soup.find('meta', {'property': 'og:url'}).get('content')
image = soup.find('meta', {'property': 'og:image'}).get('content')
desc = soup.find('meta', {'property': 'og:description'}).get('content')

print(url)
print(image)
print(desc)

article = soup.select_one('div.article_paragraph').text.strip()
# print(article)

words = list(filter(lambda x: len(x) > 2, map(lambda s: s.strip(), re.split('[\s\[\]]', article))))
word_count = {}
for w in words:
    if w in word_count:
        word_count[w] = word_count[w] + 1
    else:
        word_count[w] = 1

rank = list(map(lambda t: t[0], sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]))
# rank = list(sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5])
print(rank)
