import sys
import datetime




data_in = sys.argv[1]
path = './test/quake_data.txt'

f = open(path, 'r', encoding='UTF-8')
data_before = f.read()

data_in = data_in + "\n" + data_before

f = open(path, 'w')
f.write(data_in)  # 何も書き込まなくてファイルは作成されました
