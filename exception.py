
>>> import masss
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import masss
ModuleNotFoundError: No module named 'masss'

>>> l=[1,2,3,4]

>>> l[9]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    l[9]
IndexError: list index out of range

>>> try:
	l[6]
except IndexError as s:
	print(s)

	
list index out of range

>>> try:
	l[6]
except NameError as s:
	print(s)

	
Traceback (most recent call last):
  File "<pyshell#12>", line 2, in <module>
    l[6]
IndexError: list index out of range

>>> try:
	l[6]
except None as s:
	print(s)

	
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    l[6]
IndexError: list index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#15>", line 3, in <module>
    except None as s:
TypeError: catching classes that do not inherit from BaseException is not allowed



>>> d={'name':'gopi','age':'21','city':'salem'}


>>> d[name]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d[name]
NameError: name 'name' is not defined


>>> d['name']
'gopi'


>>> d['sex']
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d['sex']
KeyError: 'sex'


>>>   import math
  
SyntaxError: unexpected indent


>>> import math


>>> from math import cube
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    from math import cube
ImportError: cannot import name 'cube' from 'math' (unknown location)

>>> from math import factorial


>>> factorial(5)
120


>>> l=[1,2,3,4,5,6]

>>> l=iter(l)

>>> l
<list_iterator object at 0x0000014CB579BD60>


>>> next(l)
1

>>> next(l)
2

>>> next(l)
3

>>> next(l)
4

>>> next(l)
5

>>> next(l)
6

>>> next(l)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    next(l)
StopIteration


>>> '2'+2
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    '2'+2
TypeError: can only concatenate str (not "int") to str


>>> int(21+21J)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    int(21+21J)
TypeError: can't convert complex to int


>>> int('133')
133

>>> int('qwer')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    int('qwer')
ValueError: invalid literal for int() with base 10: 'qwer'


>>> age=21

>>> ages
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    ages
NameError: name 'ages' is not defined


>>> x=12/0
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    x=12/0
ZeroDivisionError: division by zero

>>> x=12/0.23

>>> x
52.17391304347826


>>> name=input('enter your name')
enter your name^c


>>> name=input('enter your name')

enter your name^c

>>> l
<list_iterator object at 0x0000014CB579BD60>


>>> #========================================================================

>>> #    exception handling in python

>>> try:
	a=5
	b='0'
	print(a/b)
except:
	print('find of some encounter')

find of some encounter



>>> try:
	a=5
	b='0'
	print(a/b)
except:
	print('find of some encounter')
print('hellow')
SyntaxError: invalid syntax


>>> try:
	a=5
	b='0'
	print(a+b)
except:
	print('unsuppported operation')

	
unsuppported operation



>>> 5/0
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    5/0
ZeroDivisionError: division by zero

>>> try:
	a=5
	b='0'
	print(a/b)
except IOError as s:
	print(s)
except ZeroDivisionError as s:
	print(s)

	
Traceback (most recent call last):
  File "<pyshell#113>", line 4, in <module>
    print(a/b)
TypeError: unsupported operand type(s) for /: 'int' and 'str'


>>> try:
	a=5
	b=0
	print(a/b)
except IOError as s:
	print(s)
except ZeroDivisionError as s:
	print(s)

	
division by zero



>>> try:
	a=2
	b='5'
	print(a+b)
except TypeError :
	print('canot added str to int')

	
canot added str to int



>>> try:
	a=2
	b='5'
	print(a+b)
except TypeError as d:
	print(d)
	print('canot added str to int')

	
unsupported operand type(s) for +: 'int' and 'str'
canot added str to int



>>> try:
	a=5
	b=0
	print(5/0)
except TypeError:
	print('type error find')
except ZeroDivisionError as d:
	print(d)

	
division by zero



>>> try:
	a=5
	b=0
	print(5/0)
except TypeError:
	print('type error find')
except ZeroDivisionError as d:
	print('zero canot divided by zole number')
	print(d)

	
zero canot divided by zole number
division by zero


>>> try:
	print('try block ')
	x=int(input('enter a number :'))
	y=int(input('enter a number :'))
	z=x/y
except ZeroDivisionError as s:
	print('except block')
	print(s)
else:
	print('else block')
	print('divtion is :',z)
finally:
	print('finally block')
	print('ffinallly try , except ,else and finally block exciquat')

	
try block 
enter a number :4
enter a number :5
else block
divtion is : 0.8
finally block
ffinallly try , except ,else and finally block exciquat



>>> try:
	print('try block ')
	x=int(input('enter a number :'))
	y=int(input('enter a number :'))
	z=x/y
except ZeroDivisionError as s:
	print('except block')
	print(s)
else:
	print('else block')
	print('divtion is :',z)
finally:
	print('finally block')
	print('finallly try , except ,else and finally block exciquat')

	
try block 
enter a number :5
enter a number :0
except block
division by zero
finally block
finallly try , except ,else and finally block exciquat



>>> try:
	print('try block ')
	x=int(input('enter a number :'))
	y=int(input('enter a number :'))
	z=x/y
except ZeroDivisionError as s:
	print('except block')
	print(s)
else:
	print('else block')
	print('divtion is :',z)
finally:
	print('finally block')
	print('finallly try , except ,else and finally block exciquat')

	
try block 
enter a number :4
enter a number :sdf
finally block
finallly try , except ,else and finally block exciquat
Traceback (most recent call last):
  File "<pyshell#165>", line 4, in <module>
    y=int(input('enter a number :'))
ValueError: invalid literal for int() with base 10: 'sdf'


>>> try:
	print('try block ')
	x=int(input('enter a number :'))
	y=int(input('enter a number :'))
	z=x/y
except :
	print('except block')
else:
	print('else block')
	print('divtion is :',z)
finally:
	print('finally block')
	print('finallly try , except ,else and finally block exciquat')

	
try block 
enter a number :4
enter a number :df
except block
finally block
finallly try , except ,else and finally block exciquat



>>> try:
    x=int(input('Enter a number upto 100: '))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "is out of allowed range")
else:
    print(x, "is within the allowed range")

Enter a number upto 100: 
4 is out of allowed range



>>> try:
    x=int(input('Enter a number upto 100: '))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "is out of allowed range")
else:
    print(x, "is within the allowed range")

    
Enter a number upto 100: 111
111 is out of allowed range



>>> try:
    x=int(input('Enter a number upto 100: '))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "is out of allowed range")
else:
    print(x, "is within the allowed range")

    
Enter a number upto 100: 1
1 is within the allowed range
>>> 