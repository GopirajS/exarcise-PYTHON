>>> lambda x:x
<function <lambda> at 0x00000283C3C29EE0>

>>> (lambda x:x)('gopiraj')
'gopiraj'

>>> s=lambda x:x

>>> s('gopi')
'gopi'

>>> (lambda x:print(x))('gopi')
gopi

>>> lambda x,y:x+y-y
<function <lambda> at 0x00000283C3C29F70>

>>> (lambda x,y:x+y-y)(1,2)
1

>>> 1+2-2
1

>>> def cube(x):
	return x*x*x

>>> p=lambda x:x*x*x

>>> print(p(3))
27

>>> cube(3)
27

>>> a=[100,23,4,6,9,23,5,10,35,222]

>>> s=filter(lambda x:x%2==0,a)

>>> s
<filter object at 0x00000283C3C1DFD0>

>>> type(s)
<class 'filter'>


>>> for i in s:
	i

	
100
4
6
10
22

>>> s
<filter object at 0x00000283C3C1DFD0>

>>> list(s)
[]

>>> for i in s:
	i

	
>>> s=filter(lambda x:x%2==0,a)

>>> list(s)
[100, 4, 6, 10, 22]

>>> list(s)
[]

>>> a=[100,23,4,6,9,23,5,10,35,22]

>>> s=map(lambda x:x%2==0,a)

>>> list(s)
[True, False, True, True, False, False, False, True, False, True]

>>> s=map(lambda x:x%2==0,a)

>>> d=list(s)

>>> d
[True, False, True, True, False, False, False, True, False, True]

>>> empty=[]

>>> a=[]

>>> for i in d:
	if i == "True":
		empty.append(i)
	else:
		a.append(i)

		
>>> empty
[]

>>> a
[True, False, True, True, False, False, False, True, False, True]

>>> d
[True, False, True, True, False, False, False, True, False, True]

>>> for i in d:
	i

	
True
False
True
True
False
False
False
True
False
True

>>> empty=[]

>>> a=[]


>>> for i in d:
	if i==True:
		empty.append(i)
	else:
		a.append(i)

		
>>> empty
[True, True, True, True, True]

>>> a
[False, False, False, False, False]

>>> s='i love python'



>>> print('oout side of fuction :',s)
oout side of fuction : i love python

>>> def fun():
	print('inside of function :',s)

	
>>> fun()
inside of function : i love python

>>> s
'i love python'

>>> def fun():
	s='inside of function off local variable'
	print(s)

	
>>> fun()
inside of function off local variable

>>> print(s)
i love python


>>> def fun():
	s+='extence'
	print('inside the variable:',s)

	

>>> s
'i love python'


>>> def fun():
	global s
	s+='extence'
	print('inside the variable:',s)

	

>>> s
'i love python'

>>> fun()
inside the variable: i love pythonextence


>>> s
'i love pythonextence'

>>> s
'i love pythonextence'

>>> a=1

>>> def f():
	a=2
	print('inside fuction :',a)

	
>>> def g():
	print('inside fuction g():',a)

	

>>> def w():
	global a
	a=23322
	print('inside fuction with global ky:',a)

	
>>> f()
inside fuction : 2

>>> g()
inside fuction g(): 1

>>> a
1

>>> w()
inside fuction with global ky: 23322

>>> a
23322


>>> import config
>>> import config as con


>>> x=1

>>> y=2

>>> z=3

>>> con.x='one'

>>> con.y='two'

>>> con.z='three'

>>> x
1
>>> y
2
>>> z
3
>>> con.x
'one'
>>> con.z
'three'
>>> z
3

>>> def x():
	variable=15
	def y():
		global variable
		variable =20
		print('after changing variable',variable)
	print('before changing variable :',variable)
	y()

	
>>> x()
before changing variable : 15
after changing variable 20

>>> def x():
	variable=15
	def y():
		global variable
		variable =20
		
	print('before changing variable :',variable)
	y()
	print('after changing variable',variable)

	
>>> x()
before changing variable : 15
after changing variable 15

>>> x
<function x at 0x00000283C3C67160>

>>> variable
20

>>> def upper(txt):
	return txt.upper()


>>> def lower(txt):
	return txt.lower()


>>> def myfun(fun):
	returning=fun('hi hellow gays how are your  ,IM SO GOOD TO SEE U AGAIN IN PYTHON CLASS')
	print(returning)

	
>>> myfun(upper)
HI HELLOW GAYS HOW ARE YOUR  ,IM SO GOOD TO SEE U AGAIN IN PYTHON CLASS

>>> myfun(lower)
hi hellow gays how are your  ,im so good to see u again in python class

>>> def creating_add(x):
	def adder(y):
		return x+y
	return adder

>>> creating_add(2)(3)
5
