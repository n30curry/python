#!/usr/bin/python

def caculate(oper,x,y):
    if oper == '+':
        return x + y
    if oper == '-':
        return x - y
    if oper == '*':
        return x * y
    if oper == '/':
        return x / y

def evalRPN(tokens):
    if (len(tokens) == 0):
        return 0
     
