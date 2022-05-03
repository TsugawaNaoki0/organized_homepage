# data_list  12球団
# se_data_list  セリーグ6球団
# pa_data_list  パリーグ6球団

import sys
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv




url = "https://baseball.yahoo.co.jp/npb/"

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
news_tag = soup.select("tr") ###


tag_data = []

team_num = 14

for k in range(team_num):
    str_data = list(news_tag[k])

    for i in range(len(str_data)):

        if (i%2 != 0):
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--score\">", "").replace("</td>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--rank\">", "").replace("</td>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/1/top\">", "").replace("</a>\n", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/2/top\">", "").replace("</th>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/3/top\">", "").replace("</th>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/4/top\">", "").replace("</th>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/5/top\">", "").replace("</th>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/6/top\">", "").replace("</th>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/7/top\">", "").replace("</th>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/8/top\">", "").replace("</th>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/9/top\">", "").replace("</th>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/10/top\">", "").replace("</th>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/11/top\">", "").replace("</th>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/12/top\">", "").replace("</th>", "")
            str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/376/top\">", "").replace("</th>", "")
            str_data[i] = str(str_data[i]).replace("<th class=\"bb-subRankTable__head\" scope=\"col\">", "").replace("</th>", "")

            tag_data.append(str_data[i])


data_list = [[] for k in range(team_num)]

num = 0
for k in range(team_num):
    for i in range(6):
        data_list[k].append(tag_data[num])
        num += 1

print("<br><br>")
print("<br><br>")
print("<br><br>")
print("<br><br>")
for i in range(len(data_list)):
    print(str(data_list[i]) + "<br><br>")

se_data_list = []
pa_data_list = []

for i in range(0, 7):
    se_data_list.append(data_list[i])

for i in range(7, 14):
    pa_data_list.append(data_list[i])

print()
print()
print(se_data_list)
print("<br><br>")
# print(tag_data)
print(pa_data_list)
