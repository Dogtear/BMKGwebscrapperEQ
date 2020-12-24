import requests
import pprint
from bs4 import BeautifulSoup

res = requests.get('https://inatews.bmkg.go.id/light/?act=realtimeev')
html_data = BeautifulSoup(res.text, 'html.parser')

info_table = html_data.select('.table-responsive thead tr')
data_table = html_data.select('.table-responsive tr td')

obj_magi=[]
obj_result=[]

count = 0
for t_data in data_table:
    obj_magi.append(t_data)
    if len(obj_magi) >8:
        # append hasilnya ke 
        obj_result.append({'Status' :obj_magi[0],'Tanggal': obj_magi[1], 'Jam': obj_magi[2],'Lintang': obj_magi[3], 'Bujur': obj_magi[4], 'Kedalaman': obj_magi[5], 'Magnitude': obj_magi[6], 'MT': obj_magi[7], 'Region':obj_magi[8]})
        obj_magi.clear()

print(obj_magi)
pprint.pprint(obj_result)



# pprint.pprint(data_table)


# 