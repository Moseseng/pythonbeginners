import requests
from bs4 import BeautifulSoup

url = "https://www.udemy.com"

req = requests.get(url).text

sup = BeautifulSoup(req, 'html.parser')

print(sup)










         
         