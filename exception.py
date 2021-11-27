
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



>>>#========================================================================



Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> amount=1000
>>> 
>>> if (amount>100)
SyntaxError: invalid syntax
>>> 
>>> 
>>> mark=1000
\
>>> mark
1000
>>> 
>>> a=mark/0
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a=mark/0
ZeroDivisionError: division by zero
>>> 
>>> 
>>> 
>>> a=[1,2,3,4]
>>> a[0]
1
>>> a[2]
3

>>> a[3]
4
>>> a[4]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a[4]
IndexError: list index out of range
>>> 
>>> 
>>> try:
	print('second element of list of a d%'%(a[1]))
except:
	print('list index is out of range')

	
list index is out of range
>>> try:
	print('second element of list of a d%' %(a[1]))
except:
	print('list index is out of range')

	
list index is out of range
>>>  a[1]
 
SyntaxError: unexpected indent
>>> a[1]
2
>>> 
>>> 
>>> try:
	print('second element of list of a :' ,a[1])
except:
	print('list index is out of range')

	
second element of list of a : 2
>>> 
>>> 
>>> 
>>> try:
	print('second element of list of a :' ,a[1])
	print('out of range element a:',a[10])
except:
	print('list index is out of range')

	
second element of list of a : 2
list index is out of range
>>> 
>>> try:
	print('out of range element a:',a[10])
	print('second element of list of a :' ,a[1])
	
except:
	print('list index is out of range')

	
list index is out of range
>>> 
>>> 
>>> 
>>> 
>>> def fun(x):
	b=x/(x-3)
	print('value of b =',b)

	
>>> fun(3)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    fun(3)
  File "<pyshell#49>", line 2, in fun
    b=x/(x-3)
ZeroDivisionError: division by zero
>>> fun('gopi')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    fun('gopi')
  File "<pyshell#49>", line 2, in fun
    b=x/(x-3)
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
>>> 
>>> fun(5)
value of b = 2.5
>>> 
>>> 
>>> 
>>> def fun(x):
	if x<4:
		b=x/(x-3)
	print()

	
>>> def fun(x):
	if x<4:
		b=x/(x-3)
	print(b)

	
>>> fun(3)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    fun(3)
  File "<pyshell#64>", line 3, in fun
    b=x/(x-3)
ZeroDivisionError: division by zero
>>> fun(4)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    fun(4)
  File "<pyshell#64>", line 4, in fun
    print(b)
UnboundLocalError: local variable 'b' referenced before assignment
>>> fun(5)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    fun(5)
  File "<pyshell#64>", line 4, in fun
    print(b)
UnboundLocalError: local variable 'b' referenced before assignment
>>> 
>>> 
>>> 
>>> x=3
>>> if x>2:
	s=x+2

	
>>> s
5
>>> 
>>> 
>>> def fun(a):
    if a < 4:
        b = a/(a-3)
 
    print("Value of b = ", b)

    
>>> fun(3)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    fun(3)
  File "<pyshell#79>", line 3, in fun
    b = a/(a-3)
ZeroDivisionError: division by zero
>>> fun(5)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    fun(5)
  File "<pyshell#79>", line 5, in fun
    print("Value of b = ", b)
UnboundLocalError: local variable 'b' referenced before assignment
>>> 
>>> 
>>> try:
    fun(3)
    fun(5)
 
# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

    
ZeroDivisionError Occurred and Handled
>>> try:
    #fun(3)
    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

    
NameError Occurred and Handled
>>> 
>>> 
>>> def fun(a):
    if a < 4:
        b = a/(a-3)

    print("Value of b = ", b)

    
>>> try:
    #fun(3)
    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except UnboundLocalError:
    print("local variable 'b' referenced before assignment")

    
local variable 'b' referenced before assignment
>>> 
>>> try:
    fun(3)
    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except UnboundLocalError:
    print("local variable 'b' referenced before assignment")

    
ZeroDivisionError Occurred and Handled
>>> try:
    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except UnboundLocalError:
    print("local variable 'b' referenced before assignment")

    
local variable 'b' referenced before assignment
>>> try:
    fun(3)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except UnboundLocalError:
    print("local variable 'b' referenced before assignment")

    
ZeroDivisionError Occurred and Handled
>>> 
>>> 
>>> 
>>> 
>>> def fun(a,b):
	try:
		c=((a+b)/(a-b))
	except ZeroDivisionError:
		print('a/b is divisin answer : 0')
	else:
		print(c)

		
>>> 
>>> fun(1,2)
-3.0
>>> fun(3,3)
a/b is divisin answer : 0
>>> fun(3,4)
-7.0
>>> fun(3,2)
5.0
>>> fun(7,2)
1.8
>>> 

>>> def fun(a,b):
	try:
		c=((a+b)/(a-b))
	except ZeroDivisionError:
		print('a/b is divisin answer : 0')
	else:
		print(c)
	finally:
		print('this is always exequat in finally')

		
>>> 
>>> fun(1,2)
-3.0
this is always exequat in finally
>>> fun(1,1)
a/b is divisin answer : 0
this is always exequat in finally
>>> 
>>> 
>>> raise NameError('hi hellow')
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    raise NameError('hi hellow')
NameError: hi hellow
>>> 
>>> try:
	raise NameError ('hi hellow')
except NameError:
	print('An exception')

	
An exception
