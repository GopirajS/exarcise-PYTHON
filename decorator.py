
>>>#=======================================================================

>>> #   First class fuction in python

>>> s='gopi'
	
>>> def fuc(text):
	return text.upper()


>>> fuc('gopi raj satish kuamr')
'GOPI RAJ SATISH KUAMR'

>>> s=fuc('gopi raj satish kuamr')

>>> s
'GOPI RAJ SATISH KUAMR'

>>> 'GOPI RAJ SATISH KUAMR'
'GOPI RAJ SATISH KUAMR'

>>> ayfuc=fuc

>>> ayfuc('hellow world')
'HELLOW WORLD'

>>> #--------------------------

>>> def up(text):
	return text.upper()


>>> def low(text):
	return text.lower()

>>> def convert(fuc):
	text=input('Enter your string :')
	s=fuc(text)
	print(s)

	
>>> convert(low)
Enter your string :HELLOW
hellow

>>> convert(low)
Enter your string :'HELLOW'
'hellow'

>>> convert(up)
Enter your string :gopi raj sathish kumar
GOPI RAJ SATHISH KUMAR


>>> def up(text):
	print(text.upper())

	
>>> def convert(fuc):
	text=input('Enter your string :')
	fuc(text)

>>> convert(up)
Enter your string :hellow world 
HELLOW WORLD 




>>> s='gopi'

>>> s.capitalize()
'Gopi'

>>> def cap(text):
	print(text.capitalize())

	
>>> def convert(fuc):
	text=input('Enter your string :')
	fuc(text)

	
>>> convert(cap)
Enter your string :hellow world
Hellow world


>>> #-------------------------------------

>>> def fuc1(x):
	def fuc2(y):
		return x+y
	return fuc2

>>> fuc1(3)(4)
7

>>> fuc1(3)(7)
10

>>> s=fuc1(3)

>>> s(5)
8
>>> #===========================================


>>> #               python closures

>>> def outerfuction(txt):
	def  innerfuction():
		print(txt)
	innerfuction()

	

>>> outerfuction('hellow')
hellow

>>> def outerFunction(text):
    text = text
 
    def innerFunction():
        print(text)
 
    # Note we are returning function
    # WITHOUT parenthesis
    return innerFunction

>>> outerfuction('hellow')
hellow

>>> #-----------------------------------------------

>>> def hellow_fuction(fun):
	def inner_fuction():
		print('star inner_fuction')
		fun()
		print('end of inner_fuction')
	inner_fuction()

	

>>> def second_fuc():
	print('hellow world')

	
>>> fuction_to_be_access=hellow_fuction(second_fuc)
star inner_fuction
hellow world
end of inner_fuction


>>> def hellow_fuction(fun):
	def inner_fuction():
		print('star inner_fuction')
		fun()
		print('end of inner_fuction')
	return inner_fuction()


>>> def second_fuc():
	print('hellow world')

	
>>> fuction_to_be_access=hellow_fuction(second_fuc)
star inner_fuction
hellow world
end of inner_fuction


>>> def hello_decorator(func):
 
    def inner1():
        print("Hello, this is before function execution")
        func()
 
        print("This is after function execution")
         
    return inner1



>>> def function_to_be_used():
    print("This is inside the function !!")

    
>>> function_to_be_used = hello_decorator(function_to_be_used)


>>> function_to_be_used()
Hello, this is before function execution
This is inside the function !!
This is after function execution


>>> second_fuc=hellow_fuction(second_fuc)
star inner_fuction
hellow world
end of inner_fuction




>>> def hello_decorator(func):
	def inner1():
		print("Hello, this is before function execution")
		func()
		print("This is after function execution")
	return inner1


>>> def function_to_be_used():
    print("This is inside the function !!")

    
>>> function_to_be_used=hello_decorator(function_to_be_used)

>>> function_to_be_used()
Hello, this is before function execution
This is inside the function !!
This is after function execution
>>> s='gopi'

>>> n='raj'

>>> s=n+s

>>> s
'rajgopi'

>>> n
'raj'

>>> def hello_decorator(func):
	def inner1():
		print("Hello, this is before function execution")
		func()
		print("This is after function execution")
	inner1()

	
>>> def function_to_be_used():
    print("This is inside the function !!")

    

>>> function_to_be_used=hello_decorator(function_to_be_used)
Hello, this is before function execution
This is inside the function !!
This is after function execution
>>> #-----------------------------------------------------

>>> def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner


>>> def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner


>>> @decor1
@decor
def num():
    return 10

>>> num()
400

>>> @decor1
def num():
    return 10

>>> num()
100

>>> @decor
def num():
    return 10

>>> num()
20

>>> #-------------------------------------------------

>>> def div(a,b):
	return a/b

>>> div(2,4)
0.5

>>> div(2,5)
0.4

>>> div(6,5)
1.2


>>> try:
	div(12,0)
except ZeroDivisionError as s:
	print(s)

	
division by zero


>>> def dic_decoretor(fuc):
	def inner(*args):
		list1=[]
		list1=args
		for i in list1[1:]:
			if i==0:
				return "Give proper input !!!"
		return fuc(*args)
	return inner


>>> def div(a,b,c):
	return a/b/c


>>> @dic_decoretor
def div(a,b,c):
	return a/b/c


>>> div(1,2,3)
0.16666666666666666


>>> x=1

>>> def outer():
	x=2
	def inner():
		x=3
		print('x:',x)
	inner()

	
>>> outer()
x: 3

>>> x
1

>>> def outer():
	y=2
	def inner():
		z=3
		print('x:',x)
		print('y',y)
		print('z',z)
	inner()

	

>>> outer()
x: 1
y 2
z 3



>>> def outer():
	x=2
	def inner():
		y=3
		result=x+y
		return result
	return inner

>>> s=outer()

>>> s()
5

>>> outer()()
5


>>> def outer():
	msg='Hellow World'
	def inner():
		print(msg)
	return inner

>>> s=outer()()
Hellow World

>>> s

>>> print(s)
None

>>> def outer():
	msg='Hellow World'
	def inner():
		print(msg)
	return inner

>>> s=outer()

>>> s.__name__
'inner'


>>> inner=s

>>> inner()
Hellow World

>>> def outer():
	msg='Hellow World'
	def inner():
		print(msg)
	return inner()

>>> s=outer()
Hellow World

>>> s

>>> def outer():
	msg='Hellow World'
	def inner():
		return msg
	return inner


>>> s=outer()

>>> d=s()

>>> d
'Hellow World'


>>> s.__name__
'inner'

>>> s()
'Hellow World'

>>> #-----------------------

>>> def outer(fuct):
	def inner():
		s=fuct()
		return s.upper()
	return inner

>>> @outer
def print_str():
	return 'hellow world'


>>> print_str()
'HELLOW WORLD'

>>> print_str.__name__
'inner'

>>> def outer(fuct):
	def inner():
		s=fuct()
		return s.upper()
	return inner()

>>> @outer
def print_str():
	return 'hellow world'

>>> print_str
'HELLOW WORLD'



#==================================================

>>> import math

>>> math.factorial(4)
24

>>> def factorial(x):
	print(x*x)

	
>>> factorial(4)
16

>>> math.factorial(5)
120


>>> from math import factorial

>>> factorial(5)
120

>>> def factorial(x):
	print(x*x)

	
>>> factorial(5)
25

>>> math.factorial(5)
120

>>> #----------------------


>>> def fuction(x):
	y=123
	print(x+y)

	
>>> fuction(4)
127


>>> def fuction():
	s='gopi'
	print(s)

	
>>> fuction()
gopi


>>> name='gopi raj'

>>> def outer():
	name='sathis kuamr'
	def inner():
		name='indumathi'
		print(name)

		

>>> outer()


>>> def outer():
	name='sathis kuamr'
	def inner():
		name='indumathi'
		print(name)
	inner()

	
>>> outer()
indumathi

>>> def outer():
	name='sathis kuamr'
	def inner():
		name='indumathi'
		print(name)
	return inner()

>>> outer()
indumathi

>>> s=outer()
indumathi

>>> s

>>> def outer():
	name='sathis kuamr'
	def inner():
		name='indumathi'
		print(name)
	return inner

>>> s=outer()

>>> s
<function outer.<locals>.inner at 0x000001F14CC0FB80>

>>> s()
indumathi


>>> def outer():
	name='sathis kuamr'
	def inner():
		#name='indumathi'
		print(name)
	return inner

>>> s=outer()()
sathis kuamr


>>> s

>>> def outer():
	#name='sathis kuamr'
	def inner():
		#name='indumathi'
		print(name)
	return inner

>>> s=outer()


>>> s()
gopi raj

>>> s.__name__
'inner'

>>> #-------------------------------------

>>> def outer(fuc):
	def inner():
		s=fuc()
		return s.upper()
	return inner

>>> @outer
def print_str():
	s=input('Enter a string :')
	return s


>>> print_str()
Enter a string :hellow world
'HELLOW WORLD'


>>> def outer(fuc):
	def inner():
		s=fuc()
		return s.upper()
	print('before calling inner fuction')
	return inner


>>> @outer
def print_str():
	s=input('Enter a string :')
	return s

before calling inner fuction


>>> print_str()
Enter a string :'helllow'
"'HELLLOW'"


>>> def outer(fuc):
	def inner():
		s=fuc()
		print('before calling')
		return s.upper()
	return inner



>>> @outer
def print_str():
	s=input('Enter a string :')
	return s


>>> print_str()
Enter a string :hellow world
before calling
'HELLOW WORLD'


>>> def upper(fn):
	s=fn()
	return s.upper()

	

>>> @upper
def print_str():
	s=input('Enter a string :')
	return s

Enter a string :


>>> def s(fcn):
	def inner():
		f=fcn()
		return f.upper()
	return inner


>>> @s
def print_str():
	s=input("enter a string :")
	return s


>>> print_str()
enter a string :gopiraj
'GOPIRAJ'



>>> def s(fcn):
	f=fcn()
	return f.upper()


>>> @s
def print_str():
	return 'hellow world'


>>> print_str
'HELLOW WORLD'



>>> type(print_str)
<class 'str'>


>>> print_str
'HELLOW WORLD'


>>> def s(fcn):
	f=fcn()
	return f.upper()

>>> def print_str():
	return 'hellow world'


>>> s(print_str)
'HELLOW WORLD'

>>> print_str()
'hellow world'


>>> def s(fcn):
	def inner():
		f=fcn()
		return f.upper()
	return inner


>>> @s
def d():
	return 'hellow world'

>>> d
<function s.<locals>.inner at 0x000001F14CC2B040>

>>> @s
def d():
	n=input('Enter a string')
	return

>>> d()
Enter a string hellow
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    d()
  File "<pyshell#157>", line 4, in inner
    return f.upper()
AttributeError: 'NoneType' object has no attribute 'upper'

>>> @s
def d():
	n=input('Enter a string')
	return n

>>> d
<function s.<locals>.inner at 0x000001F14CC2B280>

>>> d()
Enter a string hellow
' HELLOW'

>>> d()
Enter a stringgopiraj
'GOPIRAJ'

>>>#======================================================================


Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> def outer(func):
	def inner():
		s=func()
		return s.upper()
	return inner

>>> 
>>> def string():
	return 'good  morning'

>>> 
>>> @outer
def string():
	return 'good  morning'

>>> 
>>> string()
'GOOD  MORNING'
>>> 
>>> def outer(func):
	def inner(string):
		print(string)
		s=func(string)
		return s.upper()
	return inner

>>> 
>>> @outer
def string(strs):
	return strs

>>> 
>>> string('good morning')
good morning
'GOOD MORNING'
>>> 
>>> 
>>> 
>>> 
>>> def outer(func):
	def inner():
		print('is inner function')
		return func
	return inner

>>> 
>>> @outer
def string(strs):
	return strs

>>> 
>>> @outer
def string():
	return 'hellow world'

>>> string()
is inner function
<function string at 0x000001674E9F8F70>
>>> string()()
is inner function
'hellow world'
>>> 
>>> 
>>> 
>>> 
>>> def decorator_fun(*arg,**kwarg):
	print('inside decorators')
	def oouter(func):
		def inner():
			s=func()
			return s.upper()
		return inner
	return ooter

>>> 
>>> @decorator_fun('parimala')
def string():
	return 'good morning'

inside decorators
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    @decorator_fun('parimala')
  File "<pyshell#52>", line 8, in decorator_fun
    return ooter
NameError: name 'ooter' is not defined

>>> 
>>> 
>>> def decorator_fun(*arg,**kwarg):
	print('inside decorators')
	def inner(func):
		s=func()
		return s.upper()
	return inner

>>> 
>>> @decorator_fun('parimala')
def string():
	return 'good morning'

inside decorators
>>> 
>>> string()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    string()
TypeError: 'str' object is not callable
>>> string
'GOOD MORNING'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def decorator_fun(func):
	print("Inside decorator")
	def inner(*args, **kwargs):
		print("Inside inner function")
		print("Decorated the function")
		func()return inner
		
SyntaxError: invalid syntax
>>> def decorator_fun(func):
	print("Inside decorator")
	def inner(*args, **kwargs):
		print("Inside inner function")
		print("Decorated the function")
		func()return inner
		
SyntaxError: invalid syntax
>>> def decorator_fun(func):
	print("Inside decorator")
	def inner(*args, **kwargs):
		print("Inside inner function")
		print("Decorated the function")
		func()
	return inner

>>> 
>>> @decorator_fun
def func_to():
    print("Inside actual function")

    
Inside decorator

>>> func_to()
Inside inner function
Decorated the function
Inside actual function
>>> func_to('parimal')
Inside inner function
Decorated the function
Inside actual function
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def outer(x,y):
	def inner(func):
		def wraps(name):
			s=func()
			return s.upper()
		return wraps
	return inner

>>> 
>>> 
>>> 
>>> def geets():
	return 'good morning'

>>> 
>>> def outer(x,y):
	def inner(func):
		def wraps(name):
			s=func()
			print(x+y)
			return s.upper()
		return wraps
	return inner

>>> 
>>> def geets():
	return 'good morning'

>>> 
>>> 
>>> outer(2,3)(geets)('gopi')
5
'GOOD MORNING'
>>> 
>>> 
>>> 
>>> 
>>> def decorator(x,y):
	def outer(func):
		def inner(*args,**kwargs):
			print('I like python')
			print('{} + {}= {}'.format(x,y,x+y))
			func(*args,**kwargs)
		return inner
	return outer

>>> def greet(*args)
SyntaxError: invalid syntax
>>> def greet(*args):
	for i in args:
		print(i)

		
>>> 
>>> decorator(2,3)(greet)('gopi','sathish','kumar')
I like python
2 + 3= 5
gopi
sathish
kumar
>>> 
>>> 
>>> def inner(x,y):
	return lambda x,y:x+y

>>> inner(2,4)
<function inner.<locals>.<lambda> at 0x000001674EAE2820>
>>> inner(2,4)()
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    inner(2,4)()
TypeError: <lambda>() missing 2 required positional arguments: 'x' and 'y'
>>> 
>>> 
>>> 
>>> 
>>> def inner():
	return lambda x,y:x+y

>>> inner()
<function inner.<locals>.<lambda> at 0x000001674EAE28B0>
>>> inner()(2,4)
6
>>> 
>>> 
>>> def inner(x,y):
	lambda x,y:print(x+y)

	
>>> inner(2,3)
>>> inner(2,3)(3,4)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    inner(2,3)(3,4)
TypeError: 'NoneType' object is not callable
>>> 
>>> 
>>> 
>>> 
>>> 
>>> l=[1,2,3,4,5]
>>> all(l)
True
>>> l=[1,2,3,4,5,0]
>>> 
>>> 
>>> 
>>> all([type(arg)==str for arg in l])
False
>>> 
>>> 
>>> def decorator(data_type,message1,message2):
	def outer(func):
		print(message1)
		def inner(*args,**kwargs):
			print(message2)
			if all([type(arg)==data_type for arg in args])
			
SyntaxError: invalid syntax
>>> def decorator(data_type,message1,message2):
	def outer(func):
		print(message1)
		def inner(*args,**kwargs):
			print(message2)
			if all([type(arg)==data_type for arg in args]):
				return func(*args,**kwargs)
			return 'invalid input'
		return inner
	return outer

>>> 
>>> @decorator(str,'decorator for string join','string join')
def stringJoin(*args):
	st=''
	for i in args:
		st+=i
	return st

decorator for string join
>>> stringJoin('i','love','my','fasion')
string join
'ilovemyfasion'
>>> 
>>> @decorator(str,'decorator for string join','string join')
def stringJoin(*args):
	st=''
	for i in args:
		st+=i
		st+=' '
	return st

decorator for string join
>>> stringJoin('i','love','my','fasion')
string join
'i love my fasion '
>>> 
>>> 
>>> 
>>> @decorator(int,'decorator for join int','integer added')
def add(*args):
	st=0
	for i in args:
		print(i,end=' ')
		st+=i
	return st

decorator for join int
>>> 
>>> add(1,2,3,4,5,6,7,7)
integer added
1 2 3 4 5 6 7 7 35
>>> 
