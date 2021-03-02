import urllib.request
import urllib.parse
from lxml import etree
import time
import json


def handle_request(url, page):
    headers = {
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 87.0.4280.141  Safari / 537.36',
    }
    #拼接url和page进行拼接
    url = url.format(page)
    #print(url)
    request = urllib.request.Request(url=url, headers=headers)
    return request

def parse_content(content):
    #生成对象
    tree=etree.HTML(content)
    #抓取内容
    div_list=tree.xpath('//div[@class="left"]')
    #div_list=tree.xpath('//div[@class="log cate10 auth1"]')
    #遍历div列表
    for odiv in div_list:
        #获取内容
        title=odiv.xpath('.//ul[@class="list-box"]/li/div[@class="content"]//text()')
        title1='\n'.join(title)
        #print(title)
        item={
            '内容':title1
        }
        #将内容添加到列表中
        item_list.append(item)

def main():
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    url = 'http://www.haoduanzi.com/category/?1-{}.html'
    for page in range(start_page, end_page + 1):
        request = handle_request(url, page)
        content=urllib.request.urlopen(request).read().decode()
        #解析内容
        parse_content(content)
        time.sleep(2)
        #写入文件中
        string=json.dumps(item_list,ensure_ascii=False)
        with open('ex1.txt','w',encoding='utf-8') as fp:
            fp.write(string)


if __name__ == '__main__':
    main()
