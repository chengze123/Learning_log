import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html,'lxml')
    ##使用find_all方法,获取html信息中所有class属性为showtxt的div标签
    ##find_all的第一个参数是获取的标签名,第二个参数class_是标签属性
    ##class在Python中是关键字,所以用class_标识class属性,,避免冲突
    texts = bf.find_all('div',class_ = 'showtxt')
    ##decoude()是为了将texts转变成中文,如果不用这个方法,输出的内容就是一堆编码
    print(texts[0].text.replace('\xa0'*8,'\n\n'))