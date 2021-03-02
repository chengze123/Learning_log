#获取一个对象的所有方法dir()
s1='fjdskl'
#print(dir())
l1=[1,2,3]
#print(dir(l1))
#print('__iter__' in dir(s1))
#print('__iter__' in dir(range(2)))
#转化成迭代器 可写成s1.iter()
obj=iter(s1)
#print(obj.__next__())
print(next(obj))#一个next取一个值，多一个next就会报错

