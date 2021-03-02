#import os

#with open('a1.txt','rb') as read_f, open('.a1.txt.swap', 'w', encoding='utf-8') as write_f:
    #for line in read_f:
        #line = line.replace('alex', 'sb')
        #write_f.write(line)

#os.remove('a1.txt')
#os.rename('.a1.txt.swap', 'a1.txt')

#count = 1
#def search():
    #global count
    #count = 2
#search()
#print(count)

#def add_b():
    #b = 42
    #def do_global():
        #b = 10
        #print(b)
        #def dd_nonlocal():
            #nonlocal b
            #b = b + 20
            #print(b)
        #dd_nonlocal()
        #print(b)
    #do_global()
    #print(b)
#add_b()

def func1():
    print('in func1')

def func2(f):
    print('in func2')
    f()

func2(func1)
