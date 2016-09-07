#!/usr/bin/python

class Node(object):
    def __init__(self,val,p = None):
        self.val = val
        self.next = p
        self.prior = p

class LinkList(object): 

