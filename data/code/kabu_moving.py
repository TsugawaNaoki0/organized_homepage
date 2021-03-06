import csv
import numpy as np
import matplotlib.pyplot as plt
# https://jp.investing.com/equities/

#csvファイルを指定
# MyPath = 'dummy.csv'
MyPath = '6501_past.csv'

stock_data = []
#csvファイルを読み込み
rows = []
with open(MyPath) as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

for i in range(len(rows)):
    # print(rows[i])
    stock_data.append(rows[i])
    # print("<br><br>")

x = np.arange(0, len(stock_data), 1) #-5から5まで0.1区切りで配列を作る
x = list(x)

for i in range(1, len(stock_data)):
    # print(stock_data[i][1])
    for k in range(1, 5):
        stock_data[i][k] = float(stock_data[i][k].replace(",", ""))

stock_data.reverse()

for i in range(len(stock_data)):
    print(stock_data[i])
    print("<br>")

y = []
for i in range(len(stock_data)-1):
    y.append(stock_data[i][1])
    # print(stock_data[i][1])

z = []
for i in range(len(stock_data)-1):
    z.append(stock_data[i][2])
    # print(stock_data[i][2])

w = []
for i in range(len(stock_data)-1):
    w.append(stock_data[i][3])
    # print(stock_data[i][3])

v = []
for i in range(len(stock_data)-1):
    v.append(stock_data[i][4])
    # print(stock_data[i][4])

# print(len(stock_data))
x = [0+i for i in range(1, len(stock_data))]
plt.plot(x, y)
plt.plot(x, z)
plt.plot(x, w)
plt.plot(x, v)
plt.title(stock_data[0][0].replace("年", "/").replace("月", "/").replace("日", "/") + " --> " + stock_data[len(stock_data)-2][0].replace("年", "/").replace("月", "/").replace("日", "/"))
plt.show()# print(rows[1])




"""
# csvモジュールを使ってCSVファイルから1行ずつ読み込む
import csv

filename = 'personal_infomation.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)
# 出力結果：
#['年', '地域コード', '地域', '総人口']
#['1920年', '00000', '全国', '55963053']
# …… 省略 ……
#['2010年', '00000', '全国', '128057352']
#['2020年', '00000', '全国', '126226568']
"""
"""
# タブ区切りの文字を読み込む
filename = 'tabdelimiteddata.tsv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f, delimiter='\t')
    for row in csvreader:
        print(row)  # 出力結果は省略
"""

"""
# CSVファイルの内容を1つのリストにまとめる
filename = 'personal_infomation.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader]  # 各年のデータを要素とするリスト
    #content = []
    #for row in csvreader:
    #    content.append(row)

print(content)
# 出力結果：
#[['年', '地域コード', '地域', '総人口'], ['1920年', '00000', '全国',
# '55963053'], …… , ['2010年', '00000', '全国', '128057352'], ['2020年',
# '00000', '全国', '126226568']]

# 特定の列のデータ型を変換する
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)  # 見出し行は別扱い
    content = [[row[0], row[1], row[2], int(row[3])] for row in csvreader]

content.insert(0, header)  # 最後にリストの先頭に見出し行を挿入
print(content)
# 出力結果：
#[['年', '地域コード', '地域', '総人口'], ['1920年', '00000', '全国',
# 55963053], …… , ['2010年', '00000', '全国', 128057352], ['2020年',
# '00000', '全国', 126226568]]

# 数値フィールド以外はシングルクオートで囲まれていることを指示して
# 数値フィールドの値を全て浮動小数点数値に自動的に変換
filename = 'sample.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f, quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
    for row in csvreader:
        print(row)
# 出力結果
# ['年', '地域コード', '地域', '総人口']
# ['1920年', '00000', '全国', 55963053.0]
# …… 省略 ……
# ['2010年', '00000', '全国', 128057352.0]
# ['2020年', '00000', '全国', 126226568.0]

# CSVファイルの内容から辞書形式のデータを作成
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.DictReader(f)
    content = [row for row in csvreader]

print(content[0])
# 出力結果：
#{'年': '1920年', '地域コード': '00000', '地域': '全国', '総人口': '55963053'}
"""

"""
import csv
import pprint

with open('./personal_infomation.csv') as f:
    aaa = f.read()
    print(aaa)
    print(type(aaa))

bbb = eval(aaa)

print(bbb)
"""

"""
import csv                                 #csvモジュールをインポートする。

##########
#csvファイルからしていの列のデータを抽出してリスト化。
#第1引数にcsvファイルのパスを指定して、実行するとリストが作成されるプログラム
#########
def read_csv(file_path):
    csv_file = open(file_path)              # csvファイルを開く
    csv_reader = csv.reader(csv_file)       # 開いたcsvファイルからreaderオブジェクトを生成

    date_list = []                          # 抽出するデータを格納する空のリストを作る。
    temperature_list = []

    for row in csv_reader:                  # readerオブジェクトをループしてデータ抽出。
        if csv_reader.line_num == 1:        # ヘッダー行はスキップする。
            continue                        # Trueになる1行目はなにもしない。
        date_list.append(row[0])            # row行目の日時データをdate_listに格納する。
        temperature_list.append(row[1])     # row行目の気温データをdate_listに格納する。

    csv_file.close()                        # csvファイルを閉じる。
    return date_list, temperature_list      # 作成した２つのリスト(date_list, temperature_listを返す。）

if __name__ == '__main__':
    # file_path = '読み込みたいcsvファイルがあるフルパス'    #csvファイルの保存先をフルパス指定
    file_path = './dummy.csv'    #csvファイルの保存先をフルパス指定
    result = read_csv(file_path)
    print(result)

"""
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import time

import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv



url = "https://hogehoge.tk/personal/generator/"
# url = "https://kabuoji3.com/stock/6501/2019/"
# URLを指定する
html = urllib.request.urlopen(url)
# URLを開く
soup = BeautifulSoup(html, "html.parser")
# BeautifulSoup で開く
# HTMLからニュース一覧に使用しているaタグを絞りこんでいく
news_tag = soup.select("tr")
# news_tag = soup.select(".newsFeed_item_date") ###
# news_tag_2 = soup.select(".newsFeed_item")
# print (news_tag)

for i in range(len(news_tag)):
    news_tag[i] = str(news_tag[i]).replace("<div class=\"tr\">", "").replace("</div>", "")
    # news_tag[i] = str(news_tag[i]).replace("<div class=\"newsFeed_item_date\">", "").replace("</div>", "")
    # print(news_tag[i])
# return news_tag


print("kldjshafkljsahdflkahs")
print()
print()
print()
print()
print()
print()
print()
print()
for i in range(len(news_tag)):
    print(news_tag[i])
"""
