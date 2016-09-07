#!/usr/bin/python

a = input()

if a >= 0:
    if a < 20:
        print "0 <= a < 20"
    elif 20 <= a < 100:
        if 20 <= a <= 50:
            print "20 <= a <= 50"
        else:
            print "50 < a <= 100"
    else:
        print "a > 100"

else:
    if -10 <= a < 0:
        print "-10 <= a < 0"
    else:
        print "a < -10"
    
