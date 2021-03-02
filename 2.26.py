# def func():
# lst1 = ['卫龙', '老冰棍', '北冰洋', '牛羊配']
# lst2 = ['馒头', '花卷', '豆包', '大饼']
# lst3=['daisy','morty']
# yield from lst1
# yield from lst2
# yield from lst3


# g = func()
# for i in g:
# print(i)

# 给出一个列表, 通过循环, 想列表中添加1~10:
# list=[]
# for i in range(10):
# list.append(i)
# print(i)
# print(list)

# 将10以内所有整数的平方写入列表
# l1 = [i * i for i in range(1, 11)]
# print(l1)
# 100以内所有的偶数写入列表
# l2=[i for i in range(2,100,2)]
# print(l2)
# 从python1期到python100期写入列表lst
# lst = [f'python{i}' for i in range(1,19)]
# print(lst)
# list=[]
# for i in range(1,10):
# list.append(f'python{i}期')
# print(list)

# 这个列表中大于3的元素留下来
# l1 = [4, 3, 2, 6, 5, 5, 7, 8]
# l2 = [i for i in l1 if i > 3]
# print(l2)

#l1 = [i for i in range(1, 31) if i % 3 == 0]
#print(l1)

#l = ['wusir', 'laonanhai', 'aa', 'b', 'taibai']
#l1=[i for i in l if len(i)>3]
#print(l1)

#name= [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         #['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
#for i in name:
    #print(i)
    #for v in i:
            #if v.count('e')>=2:
                #print(v)
#l1=[v for i in name for v in i if v.count('e')>=2]
#print(l1)

#lst1 = ['jay','jj','meet']
#lst2 = ['周杰伦','林俊杰','郭宝元']
#dic = {lst1[i]:lst2[i] for i in range(len(lst1))}
#print(dic)

#3.1
#func=lambda a,b: a if a>b  else b
#print(func(3,10))

func=lambda x:(x[0],x[5])
print(func('mortydaisy'))