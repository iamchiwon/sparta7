import requests
from bs4 import BeautifulSoup

# [1] WANNABE / ITZY

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 '
}
url = 'https://www.genie.co.kr/chart/top200'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

charts = soup.select('tr.list')
for chart in charts:
    rank = chart.select_one('td.number').text.strip().split(' ')[0].strip()
    title = chart.select_one('a.title').text.strip()
    artist = chart.select_one('a.artist').text.strip()

    # [1] WANNABE / ITZY
    song = '[{}] {} / {}'.format(rank, title, artist)
    print(song)

