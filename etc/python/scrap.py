import requests
import bs4


h = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movi=20200303',headers=h)


r = requests.get('https://moviek/rmovie.nhn')

soup = bs4.BeautifulSoup(r.text, 'html.parser')

aTags = soup.select('div.tit3 a')
for a in aTags[:10]:
    print(a.text)