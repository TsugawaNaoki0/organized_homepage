import numpy as np
import matplotlib.pyplot as plt
import sys
import graph_maker















tesuu = 0                       # 手数料
zandaka = 2000000                # 残高
zandaka = int(sys.argv[1])



zandaka_0 = zandaka
nenritsu = 0.15                 # 年率
# nenritsu = 0.3375                 # 年率 to_go
year = 365
month = 1                       # 月数
nissu = 25 + (month-1) * 30
# hensai = 1000
hensai = int(sys.argv[2])
goukei = 0

# month = 100
month = int(zandaka / hensai) - 1


total = []
total_tesuu = []
total_hensai = []
wariai = []

# print("<link rel='stylesheet' href='./../../../home.css'>")
print("<table align='left' border='1'>")
print("<tr>")
print("<th>" + str("借入額") + "</th>")
print("<th>" + str("年利") + "</th>")
print("</tr>")
print("<tr>")
print("<td align='center'>" + format(zandaka, ',') + "</th>")
print("<td align='center'>" + format(nenritsu, ',') + "</th>")
print("</tr>")
print("<tr>")
print("<th>" + str("Xヶ月目") + "</th>")
print("<th>" + str("返済額") + "</th>")
print("<th>" + str("手数料") + "</th>")
print("<th>" + str("支払残高") + "</th>")
print("</tr>")


for i in range(month+1):
    tesuu = int(zandaka * nenritsu / 12)
    gan_hensai = hensai * month - tesuu
    # print("手数料: " + str(tesuu))
    print()
    # print("元金の返済額: " + str(gan_hensai))
    zandaka = zandaka - hensai
    # print("Hello !!!!!!!!")
    print("<tr>")
    print("<td align='center'>" + format((i+1), ',') + "</td>")
    print("<td align='center'>" + format(hensai, ',') + "</td>")
    print("<td align='center'>" + format(tesuu, ',') + "</td>")
    print("<td align='center'>" + format(zandaka, ',') + "</td>")
    print("</tr>")

    # print("[MONTH" + str(i+1) + " : " + str(hensai) + "] [CHARGE : " + str(tesuu) + "] [BALANCE : " + str(zandaka) + "] " + "<br><br>")
    # print("[" + str(i+1) + "ヶ月目], 返済額： " + str(hensai) + ", 手数料: " + str(tesuu) + ", 残高: " + str(zandaka))
    goukei += (hensai + tesuu)
    total.append(goukei)
    total_tesuu.append(tesuu)
    total_hensai.append((hensai + tesuu))
    if (zandaka <= 0):
        wariai.append(zandaka_0)
    else:
        wariai.append((goukei / zandaka))


# print("</table>")
print("<br>")

# print("<table>")
print("<tr>")
print("<th>" + str("総支払額") + "<br>")

# print("合計: " + str(goukei))
# print(total)
x = total_tesuu
normal_graph = total
z = total_hensai
q = wariai
zandaka_graph = [zandaka_0 for j in range(len(x))]
total_graph = [total[len(total)-1] for d in range(len(x))]
yoko = [(1+i) for i in range(len(x))]
# tate = [1 for i in range(month)]
# print(yoko)
# print(x)

print("<th>" + str("総手数料") + "</th>")
print("</tr>")
print("<tr>")
print("<td align='center'>" + format(goukei, ',') + "</td>")
print("<td align='center'>" + format((total[len(total)-1] - zandaka_0), ',') + "</td>")
print("</tr>")
print("</table>")

# print("TOTAL CHARGE: " + str(total[len(total)-1] - zandaka_0))

# fig = plt.figure()
# plt.bar(yoko, y) # この場合のplot関数の第一引数xは、x軸に対応し、第二引数のyがy軸にあたります。
# plt.savefig("./img.png")
# fig = plt.figure()

aaa = graph_maker.graph_maker_class()
bbb = aaa.graph_maker(yoko, total, zandaka_0 ,normal_graph, zandaka_graph, total_graph)


print("<img src='./img.png'>")



# print("<img src='./img.png'>")
# plt.plot(y, label="fdsafdas") # この場合のplot関数の第一引数xは、x軸に対応し、第二引数のyがy軸にあたります。
# plt.show()
