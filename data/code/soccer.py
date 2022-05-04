# data_list  12球団
# se_data_list  セリーグ6球団
# pa_data_list  パリーグ6球団

import sys
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv




class mlb_data_class():
    def mlb_data(self):

        url = "https://soccer.yahoo.co.jp/jleague/"

        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        news_tag = soup.select("tr") ###


        tag_data = []

        team_num = 19

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




class jleague_data_class():
    def jleague_data(self):

        url = "https://soccer.yahoo.co.jp/jleague/"

        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        news_tag = soup.select("tr") ###


        tag_data = []

        team_num = 19

        for k in range(team_num):
            str_data = list(news_tag[k])

            for i in range(len(str_data)):

                if (i%2 != 0):

                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--score\">", "").replace("</td>", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--rank\">", "").replace("</td>", "")
                    str_data[i] = str(str_data[i]).replace("<th class=\"sc-tableGame__head sc-tableGame__head--date\" scope=\"col\">", "").replace("</a>\n", "")
                    str_data[i] = str(str_data[i]).replace("<th class=\"sc-tableGame__head sc-tableGame__head--category\" scope=\"col\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<th class=\"sc-tableGame__head sc-tableGame__head--teamHome\" scope=\"col\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<th class=\"sc-tableGame__head sc-tableGame__head--score\" scope=\"col\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<th class=\"sc-tableGame__head sc-tableGame__head--teamAway\" scope=\"col\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<th class=\"sc-tableGame__head sc-tableGame__head--venue\" scope=\"col\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<th class=\"sc-tableGame__head sc-tableGame__head--ticket\" scope=\"col\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"sc-tableGame__data sc-tableGame__data--date\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"sc-tableGame__data sc-tableGame__data--category\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"sc-tableGame__data sc-tableGame__data--team\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"sc-tableGame__data sc-tableGame__data--team\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/30673/info?gk=6\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/30673/info?gk=6\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/30673/info?gk=6\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/30673/info?gk=6\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/30673/info?gk=6\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<span aria-hidden=\"true\" class=\"sc-teamLogo sc-teamLogo--jleague30673\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"sc-tableGame__data sc-tableGame__data--score\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050402\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<div class=\"sc-tableGame__score\">", "").replace("</th>", "")
                    for m in range(30000, 40000):
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_away;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j1/teams/" + str(m) + "/info?gk=6\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_away;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/" + str(m) + "/info?gk=6\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j1/teams/" + str(m) + "/info?gk=6\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/" + str(m) + "/info?gk=6\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_away;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j1/teams/" + str(m) + "/info?gk=68\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_away;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/" + str(m) + "/info?gk=68\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j3/teams/" + str(m) + "/info?gk=68\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j1/teams/" + str(m) + "/info?gk=68\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/" + str(m) + "/info?gk=68\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_away;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j3/teams/" + str(m) + "/info?gk=68\">", "").replace("</th>", "")
                        # print(m)
                    for m in range(100, 300):
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_away;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j1/teams/" + str(m) + "/info?gk=6\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_away;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/" + str(m) + "/info?gk=6\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j1/teams/" + str(m) + "/info?gk=6\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/" + str(m) + "/info?gk=6\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_away;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j1/teams/" + str(m) + "/info?gk=2\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_away;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/" + str(m) + "/info?gk=2\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j1/teams/" + str(m) + "/info?gk=2\">", "").replace("</th>", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/" + str(m) + "/info?gk=2\">", "").replace("</th>", "")
                        # print(m)

                    for m in range(400, 600):
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050" + str(m) + "\">", "").replace("</th>", "")
                        # print(m)



                    str_data[i] = str(str_data[i]).replace("<p class=\"sc-tableGame__scoreDetail\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"sc-tableGame__data sc-tableGame__data--venue\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<td class=\"sc-tableGame__data sc-tableGame__data--ticket\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<p class=\"sc-tableGame__status\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__ticket sc-tableGame__ticket--btn\" data-ylk=\"slk:ticket;\" href=\"/jleague/category/j2/game/2022050403/ticket\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050413\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<span>", "").replace("</span>", "")
                    str_data[i] = str(str_data[i]).replace("<span aria-label=\"hidden\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<span class=\"sc-tableGame__ticket\">", "").replace("</th>", "")

                    for m in range(30000, 32000):
                        str_data[i] = str(str_data[i]).replace("<span aria-hidden=\"true\" class=\"sc-teamLogo sc-teamLogo--jleague" + str(m) + "\">", "")
                    for m in range(100, 300):
                        str_data[i] = str(str_data[i]).replace("<span aria-hidden=\"true\" class=\"sc-teamLogo sc-teamLogo--jleague" + str(m) + "\">", "")
                    for m in range(400, 500):
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__ticket sc-tableGame__ticket--btn\" data-ylk=\"slk:ticket;\" href=\"/jleague/category/j1/game/2022050" + str(m) + "/ticket\">", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__ticket sc-tableGame__ticket--btn\" data-ylk=\"slk:ticket;\" href=\"/jleague/category/j2/game/2022050" + str(m) + "/ticket\">", "")
                        str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__ticket sc-tableGame__ticket--btn\" data-ylk=\"slk:ticket;\" href=\"/jleague/category/j3/game/2022050" + str(m) + "/ticket\">", "")



                    str_data[i] = str(str_data[i]).replace("\n", "")
                    str_data[i] = str(str_data[i]).replace("</div>", "")
                    str_data[i] = str(str_data[i]).replace("</p>", "")
                    str_data[i] = str(str_data[i]).replace("<br>", "")
                    str_data[i] = str(str_data[i]).replace("</br>", "")
                    str_data[i] = str(str_data[i]).replace(" ", "")



                    str_data[i] = str(str_data[i]).replace("<span aria-label=\"hidden\"></span>", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j2/teams/296/info?gk=6\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050400\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050401\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050402\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050403\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050404\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050405\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050406\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050407\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050408\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050409\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__score sc-tableGame__score--hasLink\" data-ylk=\"slk:gm_card;\" href=\"https://soccer.yahoo.co.jp/jleague/game/2022050405\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<th class=\"bb-subRankTable__head\" scope=\"col\">", "").replace("</th>", "")
                    str_data[i] = str(str_data[i]).replace("<a class=\"sc-tableGame__team\" data-ylk=\"slk:tm_home;\" href=\"https://soccer.yahoo.co.jp/jleague/category/j3/teams/31296/info?gk=68\">", "").replace("</th>", "")

                    tag_data.append(str_data[i])


        data_list = [[] for k in range(team_num)]

        num = 0
        for k in range(team_num):
            for i in range(7):
                data_list[k].append(tag_data[num])
                num += 1

        print("<br><br>")
        print("<br><br>")
        print("<br><br>")
        print("<br><br>")
        for i in range(len(data_list)):
            print(str(data_list[i]) + "<br><br>")

        print(type(data_list))

        se_data_list = []
        pa_data_list = []

        for i in range(0, int(team_num/2)):
            se_data_list.append(data_list[i])

        for i in range(int(team_num/2), team_num):
            pa_data_list.append(data_list[i])

        print()
        print()
        print("@@@@@@@@@")
        print("@@@@@@@@@")
        print("@@@@@@@@@")
        print("@@@@@@@@@")
        # print(se_data_list)
        # print("<br><br>")
        # print(tag_data)
        # print(pa_data_list)



league = str(sys.argv[1])

if (league == "CARD"):
    aaa = jleague_data_class()
    bbb = aaa.jleague_data()

elif (league == "MLB"):
    aaa = mlb_data_class()
    bbb = aaa.mlb_data()
