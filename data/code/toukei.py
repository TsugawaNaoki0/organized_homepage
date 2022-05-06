
import csv

data_list = [[] for i in range(212)]

with open('./toukei/kanagawa_2018syazyounerai.csv', 'r') as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:
        print(line)
        # data_list[num].append(line)
        data_list[num] = line
        num += 1
        if (len(data_list) <= num):
            break

print()
print()
print()
print(data_list)
for i in range(len(data_list)):
    print(data_list[i])
    # print(i)

location_list = []

num = len(data_list)

for i in range(num):
    location_list.append([data_list[i][0], data_list[i][1], str(data_list[i][4]+data_list[i][5]+data_list[i][6]), data_list[i][7], data_list[i][8], data_list[i][9], data_list[i][10], data_list[i][11]])
    print(i)

for i in range(len(location_list)):
    print(location_list[i])


print(len(location_list))



# num = len(location_list)
# print(num)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
with open('students.csv', 'w', newline='') as student_file:
    writer = csv.writer(student_file)
    # writer.writerow(["RollNo", "Name", "Subject"])
    for num in range(len(location_list)):
        writer.writerow(location_list[num])




# print("<a href='./genba.html' target='_blank'>yahoo!!!</a>")
