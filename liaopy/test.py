#!/usr/bin/env python
# -*- coding: utf-8 -*-


def f1(a,b,c=0,*args,**kwargs):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kwargs=',kwargs)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

#f1(1,2,3,'a','b',x=99)
#f2(1,2,d=99,ext=None)
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
kw={'d':88,'*':'#'}
f2(*args,**kw)