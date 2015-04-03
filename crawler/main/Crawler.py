#-*- coding: utf-8 -*-
import tweepy

# astomusic 트윗 app
auth = tweepy.OAuthHandler("lnxAnwy8TTyknuqgE2F6yMYG9", "hmQJZBcZSVcO9l93FAjjazZqHxAt0x3sMFYQlYm2LDpIxEXD98")
auth.set_access_token("53275469-VIy3G3etiqG7NrqdGi7qjgHVcH6ve93eAewkWec0W", "QZZsJFlZEsFvdoXZJpD8UX7Nzn3Qnc9dj6scavMISrSjQ")

api = tweepy.API(auth)

# 선릉역 10km 주변 트윗검색
for tweet in tweepy.Cursor(api.search,
                           q="",
                           rpp=100,
                           geocode="37.504525,127.048902,10km",
                           result_type="recent",
                           include_entities=True,
                           lang="ko").items():
    print(tweet.created_at, tweet.text)
