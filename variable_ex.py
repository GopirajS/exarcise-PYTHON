
>>> x=str(3)
>>> x
'3'
>>> y=int(3)
>>> y
3
>>> z=float(3)
>>> z
3.0
>>>                              # type check
                             
>>> x=4
>>> y=213.3
>>> z='string'

>>> print(type(x),type(y))
<class 'int'> <class 'float'>

>>> print(type(z))
<class 'str'>

>>> # case sensitive
 
>>> a=121
>>> A='this is string'
 
>>> a
121
>>> A
'this is string'
>>> x='23'

>>> print(x+2)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(x+2)
TypeError: can only concatenate str (not "int") to str

>>> x='dfdwf'

>>> print(x+2)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(x+2)
TypeError: can only concatenate str (not "int") to str

>>> print(x+"2")
dfdwf2

>>> print(x,2)
dfdwf 2

>>> p='gopi'

>>> r='raj'

>>> print(p+r)
gopiraj
>>> print(p,r)

gopi raj
>>> print(p,'',r)
gopi  raj

>>> x=5
>>> y='number'
>>> print(x+y)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(x+y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> 
>>> 
>>> #                  GLOBAL variable
>>> 
>>> x='awesome'
>>> def my_fuction():
	x='fantastic'
	print("python is ",x)

	
>>> print('python is ',x)
python is  awesome
>>> my_fuction()
python is  fantastic
>>> 
>>> 
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 'awesome', 'y': 'number', 'z': 'string', 'a': 121, 'A': 'this is string', 'p': 'gopi', 'r': 'raj', 'my_fuction': <function my_fuction at 0x00000205C25D75E0>}


>>> 
>>> 
>>> def fuction():
	global x
	x='hi im python'

	
>>> print(x)
awesome
>>> def fuction():
	global x
	x='hi im python'

	
>>> fuction()
>>> print(x)
hi im python
>>> 