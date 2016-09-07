#!/usr/bin/python
#coding=utf-8

class color():
    _color = (0,0,0)

    @classmethod
    def value(cls):
        if cls.__name__ == 'Red': #__name__ 是文件名
           cls. _color = (255,0,0)
        elif cls.__name__ == 'Green':
            cls._color = (0,255,0)
        return cls._color

class Red (color):
    pass
class Green (color):
    pass
class xx (color):
    pass

red = Red()
green = Green()
x = xx()

print "red =",red.value()
print "green =",green.value()
print " unkown",x.value()
print Red.value()
