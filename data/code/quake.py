import sys
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv

# url = "https://www.jma.go.jp/bosai/map.html#8/36.386/139.419/&elem=int&contents=earthquake_map"
url = "https://typhoon.yahoo.co.jp/weather/jp/earthquake/"
# URLを指定する
html = urllib.request.urlopen(url)
# URLを開く
# print("@@@@@@@@@")
soup = BeautifulSoup(html, "html.parser")
# BeautifulSoup で開く
# HTMLからニュース一覧に使用しているaタグを絞りこんでいく
# aaa = soup.select("tr")
aaa = soup.select("small")


aaa = list(aaa)

# news_tag = soup.select(".quake-hlHeader") ###
# news_tag = soup.find('div', class_='quake-hlBox') ###
# news_tag = soup.select("table") ###
# news_tag = soup.select(".newsFeed_item_date") ###
# news_tag_2 = soup.select(".newsFeed_item")


# class名がbirdのpタグを検索
# el = soup.find('span', attrs={ 'class': 'quake-hlHeader' })

# タグのテキストを表示
# print(soup)

# soup = str(soup)
# for i in range(len(soup)):
#     print(i)
aaa = aaa[0:7]
aaa = list(aaa)
print(aaa)
print(type(aaa))
print(len(aaa))


for i in range(len(aaa)):
    print(aaa[i])
# print(len(aaa))
# print(soup.find("quake-hlBox"))
#
# bbb = soup.find("quake-hlHeader")
#
# str_sample = soup[bbb:(bbb+1000)]
# print(len(soup))
# print(str_sample)
# print (news_tag)
# print(news_tag)
print()
# print(news_tag)
print()
print()
print()
print()
print()
print()
print()
# for i in range(len(news_tag)):
#     print(news_tag[i])
#     print("@@@@@@@@@@@ @@@@@@@@ @@@@@@@@@@ @@@@@@@@@@@ @@@@@@@@@")
#     print("<br>")


# tag_header = []
#
#
# str_header = list(news_tag[0])
# print(type(str_header))



# print(len(str_header))
# for i in range(len(str_header)):
#     # print(str_header[i])
#     # print("<br>")
#     if (i%2 != 0):
#         tag_header.append(str(str_header[i]).replace("<th class=\"bb-subRankTable__head\" scope=\"col\">", "").replace("</th>", ""))
