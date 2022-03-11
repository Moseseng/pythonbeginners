import requests
from bs4 import BeautifulSoup

import csv

from itertools import zip_longest

job_titlelist = []
vlist = []
loclist = []

skileslist = []

url = "https://wuzzuf.net/search/jobs/?q=Python&a=hpb"

req = requests.get(url).text

cur = BeautifulSoup(req,'lxml')

job_title = cur.find_all("h2" , {"class" :"css-m604qf"})

v = cur.find_all("a" , {"class" :"css-17s97q8"})
loc = cur.find_all("span" , {"class" :"css-5wys0k"})
skiles = cur.find_all("div" , {"class" :"css-y4udm8"})

for i in range(len(job_title)):
    job_titlelist.append(job_title[i].text)
    vlist.append(v[i].text)
    loclist.append(loc[i].text)
    skileslist.append(skiles[i].text)

with open('C:\Users\مكتب المشكاة\Desktop\web\phone\job.csv',"w") as myfile:
    wr = csv.writer(myfile)

    wr.writerow(["job title","company name ", "location", "skills"])

    


