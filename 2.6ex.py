# def func():
# lst1 = ['武汉', '郑州', '杭州', '成都']
# lst2 = ['热干面', '胡辣汤', '小笼包', '串串']
# ield from lst1
# yield from lst2

# g = func()
# for i in range(8):
# print(next(g))

# l1 = []
# for i in range(1, 11):
# l1.append(i)
# print(l1)
# l1=[i for i in range(1,11)]
# print(l1)

# l1 = [i * i for i in range(1, 11)]
# l1 = [i ** 2 for i in range(1, 11)]
# print(l1)
# ******第二个******
# l3 = [j for j in range(1, 101) if j % 2 == 0]
# print(l3)
# l5=[j for j in range(2, 102,2) ]
# print(l5)
# ******第三个******
# l4 = [f'python{k}期' for k in range(1, 101)]
# print(l4)


#l1 = ['barry', 'ab', 'alex', 'wusir', 'xo']

# print([i.upper() for i in l1 if len(i) >= 3])
#names = [['Tom', 'Morty', 'RealMorty', 'Jefferson', 'Andrew', 'Wesley'],
         #['Alice', 'Jennifer', 'Sherry', 'Wendy', 'Alice', 'Jill']]
#l1 = []
#for i in names:
    #or name in i:
        #if name.count('e')==2:
            #l1.append(name.upper())
            #print(l1)

#列表生成式写,循环套循环
#print([name.upper() for i in names for name in i if name.count('e')==2])

#字典推导式
#l1=['Jay','JJ','mEET']
#l2=['周杰伦','林俊杰','元宝']
#dic={l2[i]:l1[i] for i in range(len(l1))}
#print(dic)

#print({i for i in range(1,11)})
#def func(a,b):
    #return a+b
#构建匿名函数
#func1=lambda a,b: a+b
#print(func1(1,7))

#def  func2(a,b):
    #if a>b:
      #c=a
	#else:
     #c=b
#func3=lambda i:(i[0],i[2],i[5])
#print(func3([22,33,44,55,66,77,88]))
#**********************************
l1=[]
def make_average(new_value):
    l1.append(new_value)
    total=sum(l1)
    #return total/len(l1)
    average=total/len(l1)
    return average
print(make_average(10000))
print(make_average(15000))
print(make_average(8000))