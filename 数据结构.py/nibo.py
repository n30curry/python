#!/usr/bin/python

#def jia(x,y):
#    return x + y 
#def jian(x,y):
#    return x - y
#def cheng(x,y):
#    return x * y
#def chu(x,y):
#    return x / y
#
#def f(x,y,o):
#    ZD.get(o)(x,y)
def suan(x,y,o):
    if o == '+':
        return x + y
    if o == '-':
        return x - y
    if o == '*':
        return x * y
    if o == '/':
        return x / y
         

def nibolan(l):
    for i in l:
        if i in ['+','-','*','/']:
            n = l.index(i)
   #     break

            L = []
            L.append(int(l[n-2]))
            L.append(int(l[n-1]))
            L.append(l[n])
            print L
            #f(L[0],L[1],L[2])
            del(l[n-2])
            del(l[n-2])
            del(l[n-2])
            print l
            l.insert(n-2,suan(L[0],L[1],L[2]))
            print l
            break
    if len(l) == 1:
        #print l[0]
        return l[0]
    else:
        nibolan(l)
#ZD = {'+':jia,'-':jian,'*':cheng,'/':chu}
a = raw_input()
li = a.split(',')
nibolan(li)
#print l[0]
