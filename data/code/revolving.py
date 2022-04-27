import numpy as np
import matplotlib.pyplot as plt
import sys



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
print("<td align='center'>" + str(zandaka) + "</th>")
print("<td align='center'>" + str(nenritsu) + "</th>")
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
    print("<td align='center'>" + str(i+1) + "</td>")
    print("<td align='center'>" + str(hensai) + "</td>")
    print("<td align='center'>" + str(tesuu) + "</td>")
    print("<td align='center'>" + str(zandaka) + "</td>")
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
y = total
z = total_hensai
q = wariai
w = [zandaka_0 for j in range(len(x))]
r = [total[len(total)-1] for d in range(len(x))]
yoko = [(1+i) for i in range(len(x))]
# tate = [1 for i in range(month)]


print("<th>" + str("総手数料") + "</th>")
print("</tr>")
print("<tr>")
print("<td align='center'>" + str(goukei) + "</td>")
print("<td align='center'>" + str(total[len(total)-1] - zandaka_0) + "</td>")
print("</tr>")
print("</table>")

# print("TOTAL CHARGE: " + str(total[len(total)-1] - zandaka_0))

fig = plt.figure()
# plt.bar(yoko, y) # この場合のplot関数の第一引数xは、x軸に対応し、第二引数のyがy軸にあたります。
plt.plot(yoko, y) # この場合のplot関数の第一引数xは、x軸に対応し、第二引数のyがy軸にあたります。
plt.plot(yoko, w)
plt.plot(yoko, r)
# plt.plot(64, tate)
# plt.plot(tate)

print(total)
for i in range(len(total)):
    if (total[i] > zandaka_0):
        print(total[i])
        plt.plot(i, total[i], marker='o', markersize=10)
        plt.text(i, total[i], "(" + str(i) + ", " + str(total[i]) + ")")
        # plt.scatter(i, total[i], c='k', s=5)
        break


fig.savefig("./img.png")
print("<img src='./img.png'>")
# plt.plot(y, label="fdsafdas") # この場合のplot関数の第一引数xは、x軸に対応し、第二引数のyがy軸にあたります。
plt.legend()
# plt.show()
