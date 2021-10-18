>>> # variable scope
>>> 
>>> def fuc():
	name='gopi raj'
	print('hellow',name)

	
>>> fuc()
hellow gopi raj
>>> name
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> #---------------------------------------------------
>>> 
>>> name='gopiraj'
>>> def fuc():
	nam='sathish'
	print('hellow',name)

	
>>> fuc
<function fuc at 0x000001CCF2827430>
>>> fuc()
hellow gopiraj
>>> name
'gopiraj'
>>> #-------------------------------------------
>>> # use glopal
>>> 
>>> 
>>> name='gopiraj'
>>> def fuc():
	global name
	name='sathish'
	print(name)

	
>>> name
'gopiraj'
>>> fuc()
sathish
>>> name
'sathish'
>>> #------------------------------------
>>> globals()['name']='gopi'
>>> name='sathish'
>>> name
'sathish'
>>> name
'sathish'
>>> globals()['name']='gopi'
>>> name
'gopi'
>>> name
'gopi'
>>> 
>>> #----------------------------------
>>> 
>>> x=5
>>> y=6
>>> print(x,y)
5 6
>>> z='python'
>>> print(z)
python
>>> 
>>> 
>>> x=str(3)
>>> y=str(2.3)
>>> z=int(2.3)
>>> print(x)
3
>>> print(y)
2.3
>>> print(z)
2
>>> 
>>> 
>>> a=4
>>> A='sathish kumar'
>>> a
4
>>> A
'sathish kumar'
>>> 
>>> 
>>> 
>>> #-------------------------------------------------
>>> 
>>> #                           variable name
>>> 
>>> myvar='gopi'
>>> my_var='gopi'
>>> _my_var='gopi'
>>> Myvar='sathish'
\
>>> # camel case
>>> 
>>> myVariableName='gopiraj'
>>> 
>>> 
>>> 
>>> #pascal case
>>> 
>>> 
>>> MyVariableName='sathish kumar'
>>> 
>>> 
>>> 
>>> #Snake case
>>> 
>>> 
>>> My_Variable_Name='gopal'
>>> 
>>> 
>>> 
>>> 
>>> #---------------------------------------------------------
>>> 
>>> # multiple variable
>>> 
>>> 
>>> x,y,z='gopi','sathish','gopal'
>>> x
'gopi'
>>> y
'sathish'
>>> z
'gopal'
>>> 

>>> 
>>> 
>>> x=y=z='oringe'
>>> x
'oringe'
>>> x
'oringe'
>>> y
'oringe'
>>> z
'oringe'
>>> 
>>> 
>>> fruit=['apple','oringe','banana']
>>> x,y,z=fruit
>>> x
'apple'
>>> y
'oringe'
>>> z
'banana'
>>> 




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
