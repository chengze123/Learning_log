import requests
from bs4 import BeautifulSoup
res = requests.get('http://www.jwview.com/jingwei/html/02-10/381329.shtml')
res.encoding = 'gbk'
#print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
#soup.select('title')[0].text
print(soup)