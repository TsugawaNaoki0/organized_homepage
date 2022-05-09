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

                    for k in range(1, 10):
                        str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/202100" + str(k) + "/top\">", "").replace("</a>\n", "")
                    for k in range(10, 31):
                        str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/mlb/teams/202100" + str(k) + "/top\">", "").replace("</a>\n", "")

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
                    for k in range(1, 13):
                        str_data[i] = str(str_data[i]).replace("<td class=\"bb-subRankTable__data bb-subRankTable__data--team\">\n<a href=\"/npb/teams/" + str(k) + "/top\">", "").replace("</th>", "")
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
        # for i in range(len(data_list)):
        #     print(str(data_list[i]) + "<br><br>")

        se_data_list = []
        pa_data_list = []

        for i in range(0, int(team_num/2)):
            se_data_list.append(data_list[i])
            if (0 < i):
                win_rate = int(int(data_list[i][2]) / (int(data_list[i][2]) + int(data_list[i][3])) * 1000 ) / 1000
                se_data_list[i].append(win_rate)
            elif (i == 0):
                se_data_list[i].append("勝率(切り捨て)")


        for i in range(int(team_num/2), team_num):
            pa_data_list.append(data_list[i])
            if (7 < i):
                win_rate = int(int(data_list[i][2]) / (int(data_list[i][2]) + int(data_list[i][3])) * 1000 ) / 1000
                pa_data_list[i-7].append(win_rate)
            elif (i == 7):
                pa_data_list[i-7].append("勝率(切り捨て)")

        # del pa_data_list[0][7]

        print()
        print()
        # print(se_data_list)
        print("<br><br>")
        # print(tag_data)
        # print(pa_data_list)



        # central league
        print("<table border='1'>")
        print("<tr>")
        for i in range(7):
            print("<th>")
            print(se_data_list[0][i])
            print("</th>")
        print("</tr>")


        for i in range(1, 7):
            print("<tr>")
            for k in range(7):
                print("<td>")
                print(se_data_list[i][k])
                print("</td>")
            print("</tr>")
        print("</table>")

        print("<br><br>")
        print("<br><br>")
        print("<br><br>")

        # pacific league
        print("<table border='1'>")
        print("<tr>")
        for i in range(7):
            print("<th>")
            print(pa_data_list[0][i])
            print("</th>")
        print("</tr>")


        for i in range(1, 7):
            print("<tr>")
            for k in range(7):
                print("<td>")
                print(pa_data_list[i][k])
                print("</td>")
            print("</tr>")
        print("</table>")



league = str(sys.argv[1])

if (league == "NPB"):
    print("<h1>" + league + "</h1>")
    aaa = npb_data_class()
    bbb = aaa.npb_data()

elif (league == "MLB"):
    print("<h1>" + league + "</h1>")
    aaa = mlb_data_class()
    bbb = aaa.mlb_data()
