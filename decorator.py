
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


