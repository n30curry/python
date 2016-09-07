#!/usr/bin/python

import math

a = input()
b = input()
c = input()
    
if b * b < 4 * a * c:
    print"wu gen"

if b * b >= 4 * a * c:
    n = math.sqrt(b * b - 4 * a * c);
    y2 = (-b + n) / a * 2.0;
    y3 = (-b - n) / a * 2.0;
    print"x1 = %f,x2 = %f"%(y2,y3);

