>>> #   abs() method

>>> print('absolute value of 10 :',abs(10))
absolute value of 10 : 10

>>> print('absolute value of -10 :',abs(-10))
absolute value of -10 : 10

>>> print('absolute value of 10.243442 :',abs(10.243442))
absolute value of 10.243442 : 10.243442

>>> print('absolute value of -10.243442 :',abs(-10.243442))
absolute value of -10.243442 : 10.243442

>>> print('absolute value of 12+3J :',abs(12+3J))
absolute value of 12+3J : 12.36931687685298

>>> print('absolute value of -12+3J :',abs(-12+3J))
absolute value of -12+3J : 12.36931687685298

>>> s=abs(12)

>>> s
12

>>> s=abs

>>> s(12.112)
12.112

>>> s.__call__
<method-wrapper '__call__' of builtin_function_or_method object at 0x00000204E0A5EC20>


>>> #===============================================================

>>> #   all() method

>>> l=[]   # empty list

>>> all(l)
True

>>> l=[0]   # empty list

>>> all(l)
False

>>> l=[0,1,2,3]

>>> all(l)
False



>>> t=(1,2,3,4,5)

>>> all(l)
False

>>> t=(1,2,3,4,5)

>>> all(t)
True

>>> t=(1,2,3,4,5,0)

>>> all(t)
False

>>> t=(1,2,3,4,5,False)

>>> all(t)
False

>>> t=()   # empty tuple

>>> all(t)
True

>>> s=set()   #empty set

>>> all(s)
True

>>> s={1,2,3,4,5,'python','java','php'}

>>> all(s)
True

>>> s={1,2,3,4,5,'python','java','php',False}

>>> all(s)
False

>>> s={1,-2,-3.13,4,5,'python','java','php'}

>>> all(s)
True

>>> s={1,-2,-3.13,4,5,'python','java','php',0}

>>> all(s)
False

>>> d={}    #empty  dictunery


>>> all(d)
True

>>> d={1,-2,3.12323,4,'gopi',True}


>>> d={}    #empty  dictunery

>>> d={1:'one',2:'two',3:'three'}

>>> all(d)
True

>>> d={1:'one',2:'two',3:0}

>>> all(d)
True

>>> d={1:'one',2:'two',3:0,0:'gopiraj'}

>>> all(d)
False

>>> s='gopiraj'

>>> all(s)
True

>>> s='gopiraj1'

>>> all(s)
True

>>> s='gopiraj0'

>>> all(s)
True

>>> s='00'

>>> all(s)
True

>>> s=False

>>> all(s)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    all(s)
TypeError: 'bool' object is not iterable


>>> s=False,2

>>> all(s)
False



>>> #================================================
>>> #    any()   method

>>> #any(iterable)  iterable: list,tuple,set,dict,string

>>> str =' '

>>> any(str)

True

>>> str =''

>>> any(str)
False

>>> l=[0,1,2,3]

>>> any(l)
True

>>> l=[0]

>>> any(l)
False

>>> l=[0]

>>> l=[]

>>> any(l)
False

>>> l=[0,False,1]

>>> any(l)
True

>>> l=[0,False]

>>> any(l)
False



>>> t=()

>>> any(l)

False

>>> t=(1,2,3,4,5)

>>> any(l)
False

>>> t=()

>>> any(l)
False

>>> t=(1,2,3,4,5)

>>> any(l)
False

>>> t=(0,False,0.123)

>>> any(l)

False

>>> t=(0.123)

>>> any(l)
False

>>> t=(-11)

>>> any(l)
False

>>> t=(-11)

>>> t=()

>>> any(t)
False



>>> t=(1,2,3,4,5)

>>> any(t)
True

>>> t=(1,2,3,4,5,False,0)

>>> any(t)
True
>>> t=(False,0)

>>> any(t)
False


>>> t=()

>>> any(t)
False
>>> s=set()

>>> any(s)
False

>>> s={1,2,3,4,5}

>>> any(s)
True
