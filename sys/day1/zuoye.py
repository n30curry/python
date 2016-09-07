#!/usr/bin/python

import time

while True:
    with open('test.txt','a+') as f:
        a = len(f.readlines()) + 1
    f = open('test.txt','a+')
    time.sleep(1)
    t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    
    d = str(a) + ',  ' + t  + "\n" 
    f.write(d)
    print d
    
