import sys


# str = sys.argv[1]


# print(str)



import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv

url = "https://baseball.yahoo.co.jp/npb/"

# URLを指定する
html = urllib.request.urlopen(url)
# URLを開く
print("@@@@@@@@@")
soup = BeautifulSoup(html, "html.parser")
# BeautifulSoup で開く
# HTMLからニュース一覧に使用しているaタグを絞りこんでいく
# aaa = soup.select(".newsFeed")
news_tag = soup.select("tr") ###
# news_tag = soup.select(".newsFeed_item_date") ###
# news_tag_2 = soup.select(".newsFeed_item")
# print (news_tag)
print(news_tag)
# for i in range(len(news_tag)):
#     news_tag[i] = str(news_tag[i]).replace("<div class=\"bb-subRankTable\">", "").replace("</div>", "")
    # news_tag[i] = str(news_tag[i]).replace("<div class=\"newsFeed_item_date\">", "").replace("</div>", "")
    # print(news_tag[i])
