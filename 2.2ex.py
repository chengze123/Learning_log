from lxml import etree

# 生成对象
tree = etree.parse('test.html')
# print(tree)
#ret = tree.xpath('//div[@id="div1"]/ul/li')
#ret2=tree.xpath('//div[@id="div1"]/ol/li[2]/text()')
ret3=tree.xpath('//div[@id="div1"]/ol/li[last()]/a/@href')
ret4=tree.xpath('//div[@id="div1"]/ul/li[@class="qing" and @name="error"]')
ret5=tree.xpath('//div[@id="div2"]/b[contains(@class,"l")]')
ret6=tree.xpath('//b[contains(@class,"l")]')
ret7=tree.xpath('//li[contains(text(),"爱")]/text()')
ret8=tree.xpath('//li[starts-with(@class,"qi")]/text()')
ret9=tree.xpath('//div[@id="div3"]')
string1= ret9[0].xpath('string(.)')
#print(ret[0].text)
#print(string1.replace('\n','').replace('\t',''))
print(string1)