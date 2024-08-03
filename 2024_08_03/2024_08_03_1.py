import os.path
import os
from datetime import datetime
import random

current_path = os.path.abspath(__name__)  #取得目前檔案路徑
directory_name = os.path.dirname(current_path) #取得目前資料夾路徑
data_path = os.path.join(directory_name,'data') #目前資料夾路徑加上data目錄
print(data_path)
if not os.path.isdir(data_path):
    print("沒有data的目錄，手動建立目錄")
    os.mkdir(data_path)
else:
    print("目錄已建立")

log_path = os.path.join(data_path,'iot.log')
if not os.path.isfile(log_path):
    print("沒有iot.log,建立log檔")
    with open(log_path,mode='w',encoding='utf-8',newline='') as file:
        file.write('時間,濕度,溫度\n')


else:
    print("有log檔")

humidity = str(random.randint(330,820) / 10)
#humidity = str(random.uniform(33.0,82.0))


celsius = str(random.randint(50,400) / 10)
#celsius = str(random.uniform(5.0,40.0))


now = datetime.now()
now_str = now.strftime("%Y-%m-%d %H:%M:%S")

with open(log_path,mode='a',encoding='utf-8',newline='') as file:
    file.write(now_str + ',' + humidity + ',' + celsius +'\n')