#-*- coding: utf-8 -*-
import tweepy
import pymysql
from konlpy.tag import Twitter

# astomusic 트윗 app
auth = tweepy.OAuthHandler("lnxAnwy8TTyknuqgE2F6yMYG9", "hmQJZBcZSVcO9l93FAjjazZqHxAt0x3sMFYQlYm2LDpIxEXD98")
auth.set_access_token("53275469-VIy3G3etiqG7NrqdGi7qjgHVcH6ve93eAewkWec0W", "QZZsJFlZEsFvdoXZJpD8UX7Nzn3Qnc9dj6scavMISrSjQ")

api = tweepy.API(auth)
##konlpy의 twitter 형태소 분석기 사용
twitter = Twitter()

##connection 연결
conn = pymysql.connect(host='107.191.52.52', unix_socket='/tmp/mysql.sock', user='chok', passwd='znvkd123!@#', db='chok', charset='utf8')
cur = conn.cursor()

mealList = ["짜장면", "탕수육", "짬뽕", "군만두", "팹시", "아이스크림", "부대찌개", "국밥", "콩나물", "두부", "타리미슈", "케이크", "치킨"];

##인코딩 세팅 작업 진행(ex : http://libsora.so/posts/python-hangul/)


# 선릉역 10km 주변 트윗검색
for tweet in tweepy.Cursor(api.search,
                           q="",
                           rpp=100,
                           geocode="37.504525,127.048902,1km",
                           result_type="recent",
                           include_entities=True,
                           lang="ko").items():
    for text in twitter.morphs(tweet.text) :
        for meal in mealList :
            if(meal == text) :
                print("mealName : " + meal)
                print("text : " + tweet.text)
                cur.execute("INSERT INTO test_data VALUES ('%s', '%s')" % (meal, tweet.text))


conn.commit()
conn.close()