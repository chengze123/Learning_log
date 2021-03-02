import requests
from lxml import etree
import urllib.parse
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
url = "https://www.aqistudy.cn/historydata/"
response = requests.get(url, headers=headers)
text = response.content.decode('utf-8')
html = etree.HTML(text)
city_set = list()
citys = html.xpath("//div[@class='all']/div/ul")
for city in citys:
    messages = city.xpath(".//li")
    for message in messages:
        city_name = message.xpath(".//a/text()")
        city_name = "".join(city_name)
        # print(city_name)
        city_set.append(city_name)
print(city_set)

