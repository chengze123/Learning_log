# sum1 = 1
# num = 1
# while num <100:
# num += 1
# sum1 = sum1 + num
# print(sum1)

# for i in range(1,101):
# if i % 2 == 0:
# print(i)

# n = 1
# while n <=10:
# print(n)
# n = n + 1

# count = 0
# while count < 100:
# count += 1
# if count > 5 and count < 95:
# continue
# print(count)

# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# l1=li[:3]
# 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
# l2=li[3:6]
# 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# l4=li[1:6:2]
# 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
# l6=li[-3::-2]
# print(l1,'*',l2,'*',l4,'*',l6)

# l1 = [1, 2, 'taibai', [1, 'WuSir', 3]]
# l2=l1[2].upper()
# print(l2)

# l3=l1[3].append('laonanhai')
# l1[3][1]='alexsb'
# print(l1)

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 计算列表的长度并输出
# print(len(li))

# 列表中追加元素"seven",并输出添加后的列表
# li.append("seven")

# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# li.insert(0,"Tony")

# 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# li[1] = "Kelly"
l2 = [1, "a", 3, 4, "heart"]
# 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。

# 请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。

# 请删除列表中的元素"ritian",并输出添加后的列表
# li.remove("ritian")

# 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
#ret=li.pop(1)

# 请删除列表中的第2至4个元素，并输出删除元素后的列表
del li[2:5]
print(li)
