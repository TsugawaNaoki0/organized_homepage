import sys


# print("af;lkdas;lkdjfda;slkj")
# print(str(sys.argv[1]))
# print("sdfakjdfhfkljsahdfkljas")



try:
    # print(sys.argv[2])
    mansatsu = int(sys.argv[2])
except:
    # print("lk;ahfdl;ksahdfl;kashdfl;kash")
    mansatsu = 1
# if (sys.argv[2] == ""):

if ((int(sys.argv[1]) == 0)):
    shotoku = 0
else:
    shotoku = int(sys.argv[1])



# mansatsu = 1
# if (sys.argv[2] != null):
#     mansatsu = int(sys.argv[2])
# print("所得" + str(shotoku))
# print("<br><br>")
# print("桁変" + str(mansatsu))
# print("<br><br>")


shotoku = shotoku * mansatsu


print("あなたの所得は, " + str(shotoku) + "円です")
print("<br><br>")
print("かかる税率は, ")

shotoku = shotoku / 1000 * 1000
print()

if (shotoku < 1000):
    # print("5%")
    ritsu = 0
    koujyo = 0

elif (1000 <= shotoku and shotoku <= 1949000):
    # print("5%")
    ritsu = 0.05
    koujyo = 0

elif (1950000 <= shotoku and shotoku <=  3299000):
    # print("10%")
    ritsu = 0.10
    koujyo = 97500

elif (3300000 <= shotoku and shotoku <= 6949000):
    # print("20%")
    ritsu = 0.20
    koujyo = 427500

elif (6950000 <= shotoku and shotoku <= 8999000):
    # print("23%")
    ritsu = 0.23
    koujyo = 636000

elif (9000000 <= shotoku and shotoku <= 17999000):
    # print("33%")
    ritsu = 0.33
    koujyo = 1536000

elif (18000000 <= shotoku and shotoku <= 39999000):
    # print("40%")
    ritsu = 0.40
    koujyo = 2796000

elif (40000000 <= shotoku):
    # print("45%")
    ritsu = 0.45
    koujyo = 4796000

print(int(ritsu * 100))
print("％です")
print("<br><br>")
print("<br><br>")
print("控除額は, ")
print(koujyo)
print("円です")
print("<br><br>")
print("<br><br>")
# print(mansatsu)
print()
print()
print()
