from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from pandas import DataFrame

url = 'http://www.jwview.com/kj.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
ret = Request(url, headers=headers)
res = urlopen(ret)
contents = res.read()

soup = BeautifulSoup(contents, "html.parser")
print("**************************")

# df_ret = DataFrame(columns=[" 影片名","评分","评价人数","链接 "])

# count =0
tag = soup.find_all('div', class_='txt')
tag.encoding = 'gbk'
print(tag)
