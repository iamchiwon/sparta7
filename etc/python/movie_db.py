import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta.movies


def scrap_and_insert():
    # URL을 읽어서 HTML를 받아오고,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(data.text, 'html.parser')

    # select를 이용해서, tr들을 불러오기
    movies = soup.select('#old_content > table > tbody > tr')

    # movies (tr들) 의 반복문을 돌리기
    rank = 1
    for movie in movies:
        # movie 안에 a 가 있으면,
        a_tag = movie.select_one('td.title > div > a')
        if a_tag is not None:
            title = a_tag.text
            star = movie.select_one('td.point').text
            print(rank, title, star)
            db.insert_one({'rank': rank, 'title': title, 'score': star})
            rank += 1


def find_and_print():
    all_movies = list(db.find())
    for movie in all_movies:
        print(movie['title'], movie['score'])


def find_avengers_and_print():
    # "어벤져스: 엔드게임" 영화의 평점 출력하기
    movie = db.find_one({'title': '어벤져스: 엔드게임'})
    print(movie['score'])


def find_avengers_score_movies_and_print():
    # "어벤져스: 엔드게임" 영화와 같은 평정의 영화 출력하기
    movie = db.find_one({'title': '어벤져스: 엔드게임'})
    score = movie['score']
    movies = list(db.find({'score': score}))
    for m in movies:
        print(m['title'])


def find_averngers_score_movies_and_update_zero():
    # "어벤져스: 엔드게임" 영화와 같은 평정의 영화들의 평점을 0으로 만들기
    movie = db.find_one({'title': '어벤져스: 엔드게임'})
    score = movie['score']
    db.update_many({'score': score}, {'$set': {'score': 0}})


find_and_print()
