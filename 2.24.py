dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic['k4']='v4'
# 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1']='alex'

# 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic['k3'].append(44)
#print(dic)
# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典



dic1 = {
 'name':['alex',2,3,5],
 'job':'teacher',
 'oldboy':{'alex':['python1','python2',100]}
 }
#1，将name对应的列表追加⼀个元素’wusir’。
#dic1['name'].append('wusir')

#2，将name对应的列表中的alex⾸字⺟⼤写
#ret=dic1['name']['alex'].capitalize()
#print(ret,dic1)

#3，oldboy对应的字典加⼀个键值对’⽼男孩’,’linux’。
#dic1['oldboy']['老男孩']='linux'
#print(dic1)
#4，将oldboy对应的字典中的alex对应的列表中的python2删除
del dic1['oldboy']['alex'][1]
print(dic1)


