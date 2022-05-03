# data_list  12球団
# se_data_list  セリーグ6球団
# pa_data_list  パリーグ6球団

import sys
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv




class mlb_data_class():
    def mlb_data(self):

        url = "https://baseball.yahoo.co.jp/mlb/"

        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        news_tag = soup.select("tr") ###


        tag_data = []

        team_num = 36

        for k in range(team_num):
            str_data = list(news_tag[k])

            for i in range(len(str_data)):

                if (i%2 != 0):
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--score\">", "").replace("</td>", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--rank\">", "").replace("</td>", "")
                    str_data[i] = str(str_data[i]).replace("<th class=\"bb-subRankTable__head\" scope=\"col\">", "").replace("</th>", "")
                    # str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021000/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021001/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021002/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021003/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021004/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021005/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021006/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021007/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021008/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021009/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021010/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021011/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021012/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021013/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021014/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021015/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021016/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021017/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021018/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021019/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021020/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021021/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021022/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021023/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021024/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021025/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021026/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021027/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021028/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021029/top\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/2021030/top\">", "").replace("</a>\n", "")

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

        for i in range(0, int(team_num/2)):
            se_data_list.append(data_list[i])

        for i in range(int(team_num/2), team_num):
            pa_data_list.append(data_list[i])

        print()
        print()
        print(se_data_list)
        print("<br><br>")
        # print(tag_data)
        print(pa_data_list)




class npb_data_class():
    def npb_data(self):

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

        for i in range(0, int(team_num/2)):
            se_data_list.append(data_list[i])

        for i in range(int(team_num/2), team_num):
            pa_data_list.append(data_list[i])

        print()
        print()
        print(se_data_list)
        print("<br><br>")
        # print(tag_data)
        print(pa_data_list)



league = str(sys.argv[1])

if (league == "NPB"):
    aaa = npb_data_class()
    bbb = aaa.npb_data()

elif (league == "MLB"):
    aaa = mlb_data_class()
    bbb = aaa.mlb_data()
