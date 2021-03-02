import urllib.request
import urllib.parse
import re

def handle_request(url,page):
    #拼接出指定的url
    url = url +str(page+30) +'.html'
    headers ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56',
    }
    #print(url)
    request= urllib.request.Request(url=url,headers=headers)
    return  request
def get_text(a_href):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56',
    }
    # print(url)
    request = urllib.request.Request(url=a_href, headers=headers)
def parse_content(content):
    #复制链接改成正则开始匹配
    pattern =re.compile(r'<h3><a href="(https://www.lz13.cn/lizhimingyan/\d+\.html)">(.*?)</a></h3>')
    #返回的lt是一个列表，列表中的元素都是元组，元组中第一个元素就是正则中第一个小括号匹配到的内容，元组中第二个元素就是正则
    #中第二个小括号匹配到的内容
    lt = pattern.findall(content)
    print(lt)
    #print(len(lt))
    #获取内容的链接
    for href_title in lt:
        a_href ='http://www.lz13.cn'+href_title[0]
    #获取标题
    title = href_title[-1]
    #向a_href发送请求，获取响应内容
    text = get_text(a_href)
def main():
    url='https://www.lz13.cn/lizhi/lizhimingyan-'
    start_page=int(input('请输入起始页码：'))
    end_page=int(input('请输入结束页码：'))
    for page in range(start_page,end_page +1):
    #根据url和page生成指定的request
       request=handle_request(url,page)
    #发送请求
       content =urllib.request.urlopen(request).read().decode()
    #解析内容
       parse_content(content)


if __name__=='__main__':
    main()