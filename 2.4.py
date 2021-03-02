import urllib.request
import urllib.parse
from lxml import etree
import time
import os

def handle_request(url, page):
    # 由于第一个url和后面不一样
    if page == 1:
        url = url.format('S')
    else:
        url = url.format('index_' + str(page))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36e Gecko) Chrome / 87.0.4280.141  Safari / 537.36',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


# 解析内容，下载图片
def parse_content(content):
    tree = etree.HTML(content)
    image_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')

    #print(image_list)
    #print(len(image_list))
    #遍历列表，依次下载图片
    for image_src in image_list:
        image_src='http:'+image_src
        download_image(image_src)

def download_image(image_src):
    dirpath='pic'
    #创建一个文件夹
    if os.path.exists(dirpath):
        os.mkdir(dirpath)

    #文件名
    filename=os.path.basename(image_src)
    #图片路径
    filepath=os.path.join(dirpath,filename)
    #发送请求,保存图片
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36e Gecko) Chrome / 87.0.4280.141  Safari / 537.36',
    }
    request = urllib.request.Request(url=image_src, headers=headers)
    response = urllib.request.urlopen(request)
    with open(filepath,'wb') as fp:
        fp.write(response.read())



def main():
    url = 'https://sc.chinaz.com/tupian/index_2.html'
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page, end_page + 1):
        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)
        time.sleep(2)


if __name__ == '__main__':
    main()
