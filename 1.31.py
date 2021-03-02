import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

class ZhilianSpider(object):
    url='http://sou.zhaopin.com/'
    def __init__(self,jl,kw,start_page,end_page):
        #将参数保存为成员属性
        self.jl=jl
        self.kw=kw
        self.start_page=start_page
        self.end_page=end_page

    #爬取程序
    def run(self, end_page=None):
        #循环爬取每一页数据
        for page in range(self.start_page,self.end_page+1):
            request=self.handle_request(page)
            #发送请求获取内容
            content=urllib.request.urlopen(request).read().decode()
            #解析内容
            self.parse_content(content)
    #根据page拼接指定的url，然后生成请求对象。
    def handle_request(self,page):
          data={
              'jl':self.jl,
              'kw':self.kw,
              #由于自己现在打开的url没有P
              #'p':page
          }
          #print(urllib.parse.urlencode(data))
          # #这里一定要有self/类名 要不然会提示未定义
          url_now = self.url+urllib.parse.urlencode(data)
          #print(url_now)
          #构建请求对象
          headers={
              'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 87.0.4280.141  Safari / 537.36',
          }
          request=urllib.request.Request(url=url_now,headers=headers)
          return  request




def main():
    jl=input('请输入工作地点：')
    kw=input('请输入工作关键字：')
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))

    #创建对象，启动爬取程序(封装)
    spider = ZhilianSpider(jl,kw,start_page,end_page)
    spider.run()


if __name__=='__main__':
        main()