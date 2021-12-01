from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def Covidnotify(title,message):
    notification.notify(title=title, message=message,app_name='Corona notification',
    app_icon=r'C:\Users\Nirankar Singh\OneDrive\Desktop\IPL-master\covid-test.ico', 
    timeout=10)

r=requests.get('https://prsindia.org/covid-19/cases')
data=r.text
soup=BeautifulSoup(data,"html.parser")
datalist=''
for tr in soup.findAll('tr'):
        datalist+=tr.getText('\n')
datalist=datalist.split('\n')
datalist=datalist[11:]
# print(datalist)
statelist=[]
a=5
c=0
for _ in range(36):
    statelist.append(datalist[c:a])
    c=a
    a+=5
# print(statelist)
states=['Bihar','Delhi','Tamil Nadu','Andhra Pradesh','Kerala','Chhattisgarh','Karnataka',
        'Rajasthan']
while True:
    for state in statelist:
        if state[0] in states:
            message=f'Total_cases : {state[1]}\nActive_cases : {state[2]}\nCured : {state[3]}\nDeath : {int(state[1])-int(state[2])-int(state[3])} '
            Covidnotify(f'Covid Cases in {state[0]} ',message)
            time.sleep(3)
    time.sleep(60)
