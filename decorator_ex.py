
>>> # GLOBAL VARIABLE AND LOCAL VARIABLE

>>> # creat local variables

>>> def f():
	s='I Love Python'
	print(s)

	
>>> f()
I Love Python

>>> def fuc():
	print('inside function :',s)

	
>>> s='hellow world'

>>> print('outside fuction :',s)
outside fuction : hellow world

>>> fuc()
inside function : hellow world


>>> def change():
	s='inside fuction s variable is change'
	print(s)

	
>>> change()
inside fuction s variable is change

>>> print(s)
hellow world



>>> def trying():
	s+='hellow'
	print(s)

	

>>> s
'hellow world'

>>> def trying():
	global s
	s+='hellow'
	print(s)

	
>>> trying()
hellow worldhellow

>>> s
'hellow worldhellow'

>>> #---------------------------------

>>> a=1
>>> def f():
	print('fuction f() :',a)

	
>>> def g():
	a=2
	print('fuction g() :',a)

	
>>> def h():
	global a
	a=3
	print('fuction h() :',h)

	
>>> print('global :',a)
global : 1

>>> f()
fuction f() : 1

>>> print('global :',a)
global : 1

>>> g()
fuction g() : 2

>>> print('global :',a)
global : 1
>>> h()
fuction h() : <function h at 0x0000027F59FC5670>

>>> def h():
	global a
	a=3
	print('fuction h() :',a)

	
>>> h()
fuction h() : 3

>>> print('global :',a)
global : 3

>>> a
3

>>> #-------------------------------------------------------

>>> def outer_fun():
	a=1
	print('outer_fun :',a)
	def enclose():
		a=2
		print('enclose :',a)
	return enclose

		
>>> s=outer_fun()
outer_fun : 1

>>> s()
enclose : 2

>>> name='gopi'


>>> def change():
	global name
	name='Gopi'

	
>>> name
'gopi'

>>> print(name)
gopi

>>> change()

>>> print(name)
Gopi

>>> def change():
	global name
	name+='Raj'

	
>>> name
'Gopi'

>>> change()

>>> print(name)
GopiRaj

>>> #---------------------------------------

>>> a=1
>>> def outer():
	x=1
	def inner():
		global x
		x=3
	print('before making change :',x)
	print('making change')
	print('after making change :',x)

	

>>> outer()
before making change : 1
making change
after making change : 1

>>> def outer():
	x=1
	def inner():
		global x
		x=3
	print('before making change :',x)
	print('making change')
	inner()
	print('after making change :',x)

	
>>> outer()
before making change : 1
making change
after making change : 1


>>> name='gopi'

>>> def f():
	name='f'
	def inner():
		global name
		name='inner'
	print('befors changing name :',name)
	print('making chage')
	inner()
	print('after mcking change :',name)

	
>>> f()
befors changing name : f
making chage
after mcking change : f


>>> name
'inner'

>>> clg='Muthayammal Collage of Atrs & Science'



>>> clg
'Muthayammal Collage of Atrs & Science'



>>> #----------------------------------------------

>>> def f():
	s='hellow world'
	print(s)

	
>>> f()
hellow world

>>> s=f

>>> f
<function f at 0x0000027F59FC59D0>

>>> s
<function f at 0x0000027F59FC59D0>
>>> s()
hellow world

>>> def shout(txt):
	return txt.upper()

>>> shout("hellow world")
'HELLOW WORLD'


>>> def shout(txt):
	return txt.upper(),text.lower()


>>> def shout(txt):
	return txt.upper(),txt.lower()

>>> shout("hellow world")
('HELLOW WORLD', 'hellow world')


>>> s
<function f at 0x0000027F59FC59D0>

>>> f
<function f at 0x0000027F59FC59D0>

>>> g=shout("hellow world")

>>> g
('HELLOW WORLD', 'hellow world')

>>> g[1]
'hellow world'

>>> g[0]
'HELLOW WORLD'

>>> #----------------------

>>> def take_str():
	string=input('Enter a string :')
	return string

>>> def low(fun):
	s=fun()
	return s.lower()

>>> def upper(fun):
	s=fun()
	return s.upper()

>>> take_str()
Enter a string :Hi , hellow gays ,how are you ?
'Hi , hellow gays ,how are you ?'

>>> low(take_str)
Enter a string :HI ,hellow how are you ?
'hi ,hellow how are you ?'

>>> low(take_str)
Enter a string :'HI HELLOW HOW ARE YOU'
"'hi hellow how are you'"


>>> upper(take_str)
Enter a string :'hell world'
"'HELL WORLD'"


>>> def take_str():
	string=input('Enter a string :')
	return string

>>> def upper(fun):
	Non=input('None values:')
	s=fun()
	return s.upper()


>>> upper(take_str)
None values:helow
Enter a string :hellow world
'HELLOW WORLD'


>>> def upper(fun):
	s=fun()
	Non=input('None values:')
	return s.upper()


>>> upper(take_str)
Enter a string :hellow
None values:hi
'HELLOW'

>>> def outer(x):
	def inner(y):
		return x+y
	return inner

>>> s=outer(3)

>>> s(5)
8

>>> x
3


>>> def outer(x):
	def inner(y):
		return x+y
	inner()

>>> def outer(x):
	def inner(y):
		return x+y
	inner()(4)

	

>>> def outer(x):
	def inner(y):
		return x+y
	inner(4)

	
>>> outer(4)

>>> s=outer(4)

>>> s

>>> def outer(x):
	def inner(y):
		return x+y
	return inner(4)

>>> outer(4)
8

>>> s=outer(4)

>>> s
8

>>> #---------------------------------

>>> def f(txt):
	txt=txt
	def inner():
		print(txt)

		
>>> def f(txt):
	txt=txt
	def inner():
		print(txt)
	inner()

	
>>> f('hellow')
hellow


>>> def f(txt):
	txt=txt
	def inner():
		print(txt)
	return inner()

>>> s=f('hellow')
hellow


>>> s

>>> s

>>> s=f('hellow')
hellow

>>> def f(txt):
	txt=txt
	def inner():
		print(txt)
	return inner

>>> s=f('hellow')

>>> s
<function f.<locals>.inner at 0x0000027F59FC5EE0>
>>> s()
hellow


>>> def f(txt):
	txt=txt
	def inner():
		print(txt)
	return inner

>>> s=f('hey!')

>>> s()
hey!

>>> import logging

>>> #---------------------------------------------

>>> def print_str(txt):
	return txt.capitalize()

>>> print_str('hellow')
'Hellow'

>>> print_str('hellow  im gopi raj im from salem')
'Hellow  im gopi raj im from salem'

>>> def print_str(txt):
	l=[]
	l=txt.split(' ')
	for i in l:
		l=i.capitalize()
		s=''.join(l)
		return s

	
>>> print_str('hellow')
'Hellow'

>>> print_str('hellow hi im gopi')
'Hellow'


>>> def print_str(txt):
	l=[]
	l=txt.split(' ')
	for i in l:
		l=i.capitalize()
		s=''.join(l)
		return s

	

>>> s=['gpi','hh','tt']

>>> def print_str(txt):
	l=[]
	l=txt.split(' ')
	for i in l:
		l.append(i.capitalize())
		s=''.join(l)
	return s


>>> def print_str(txt):
	l=[]
	l=txt.split(' ')
	for i in l:
		l.append(i.capitalize())
		s=' '.join(l)
	return s


>>> s='gopi raj satish kumar'

>>> s.split(' ')
['gopi', 'raj', 'satish', 'kumar']

>>> a=s.split(' ')

>>> for i in a:
	i.capitalize()

	
'Gopi'
'Raj'
'Satish'
'Kumar'
>>> l=[]


>>> l.append(i)

>>> l
['kumar']

>>> a
['gopi', 'raj', 'satish', 'kumar']
>>> 

>>> ' '.join(a)
'gopi raj satish kumar'

>>> a=' '.join(a)


>>> a
'gopi raj satish kumar'

>>> def print_str(txt):
	l=[]
	l=txt.split(' ')
	for i in l:
		l.append(i.capitalize())
		s=' '.join(l)
	return s


>>> def print_str(txt):
	l=[]
	l=txt.split(' ')
	for i in l:
		l.append(i.capitalize())
	s=' '.join(l)
	return s



>>> s='gopi raj satish kumar'

>>> s.split(' ')
['gopi', 'raj', 'satish', 'kumar']
>>> s=s.split(' ')

>>> s
['gopi', 'raj', 'satish', 'kumar']

>>> for i in s:
	i.capitalize()

	
'Gopi'
'Raj'
'Satish'
'Kumar'

>>> l=[]

>>> for i in s:
	a=i.capitalize()
	l.append(a)

	
>>> l
['Gopi', 'Raj', 'Satish', 'Kumar']

>>> ' '.join(l)
'Gopi Raj Satish Kumar'

>>> s='gopi raj satish kumar'

>>> def txt(s):
	l=[]
	s=s.split(' ')
	for i in s:
		a=i.capitalize()
		l.append(a)
	s=' '.join(l)

	
>>> txt(s)

>>> s
'gopi raj satish kumar'

>>> s
'gopi raj satish kumar'

>>> s='gopi raj satish kumar'


>>> l=[]

>>> def txt(s):
	s.capitalize()
	return s

>>> txt('hellow')
'hellow'

>>> s='gopi'

>>> s.capitalize()

'Gopi'
>>> def txt(s):
	a=s.capitalize()
	return s


>>> txt('hellow')
'hellow'

>>> def txt(s):
	a=s.capitalize()
	return a

>>> txt('hellow')
'Hellow'


>>> def txt(s):
	s=s.split(' ')
	for i in s:
		a=i.capitalize()
		l.append(a)
	print(l)

	
>>> txt('helow hi')
['Helow', 'Hi']

>>> l=[]

>>> def txt(s):
	s=s.split(' ')
	for i in s:
		a=i.capitalize()
		l.append(a)
	s=' '.join(l)
	return s

>>> txt='hellpw hie'

>>> txt
'hellpw hie'

>>> l=[]

>>> def txt(s):
	s=s.split(' ')
	for i in s:
		a=i.capitalize()
		l.append(a)
	print(l)

	
>>> txt('helow hi')
['Helow', 'Hi']


>>> def txt(s):
	s=s.split(' ')
	for i in s:
		a=i.capitalize()
		l.append(a)
	s=' '.join(l)
	return s

>>> txt('helow hi')
'Helow Hi Helow Hi'

>>> def txt(s):
	l=[]
	s=s.split(' ')
	for i in s:
		a=i.capitalize()
		l.append(a)
	s=' '.join(l)
	return s

>>> txt('helow hi')
'Helow Hi'

>>> txt('hellow how are you ')
'Hellow How Are You '

>>> def txt(s):
	l=[]
	s=s.split(' ')
	for i in s:
		l.append(i.capitalize())
	s=' '.join(l)
	return s

>>> txt('hellow how are you ')
'Hellow How Are You '

>>> def txt(s):
	l=[]
	s=s.split(' ')
	for i in s:
		l.append(i.capitalize())
	s=' '.join(l)
	return s


>>> def shout(txt):
	return txt.upper()

	
>>> def whisper(txt):
	return txt.lower()


>>> def txt(fun):
	s=fun('hellow world')
	print(s)

	
>>> txt(shout)
HELLOW WORLD

>>> txt(whisper)
hellow world

>>> def shout():
	txt=input('Enter a string to convert upper:')
	return txt.upper()

>>> def whisper():
	txt=input('Enter a string to convert lower :')
	return txt.lower()


>>> def txt(fun):
	s=fun()
	print(s)

	
>>> txt(shout)
Enter a string to convert upper:hellow world
HELLOW WORLD

>>> txt(whisper)
Enter a string to convert lower :dyfghfhjifbweygsdhvasldhbf
dyfghfhjifbweygsdhvasldhbf

>>> txt(whisper)
Enter a string to convert lower :ILJSDGIJHPIFJHBSLFDJVBSDFIJVBSDKV
iljsdgijhpifjhbslfdjvbsdfijvbsdkv


>>> def outer_add(x):
	def inner_add(y):
		ans=x+y
	return inner_add

>>> outer_add(6)(4)

>>> print(outer_add(6)(4))
None

>>> def outer_add(x):
	def inner_add(y):
		ans=x+y
	return inner_add()





>>> #=================================

>>> import math

>>> math.factorial(5)
120

>>> import time
>>> time.sleep(5)



>>> def sl(x):
	print('fuction is start :')
	time.sleep(5)
	s=math.factorial(x)
	print(s)

	
>>> sl(5)
fuction is start :
120

>>> sl(5)
fuction is start :
120
>>> def sl(x):
	print('fuction is started... :')
	time.sleep(5)
	s=math.factorial(x)
	print(s)

	
	
>>>#========================================================	
>>> def fuc():
	return 'hellow'

>>> fuc()
'hellow'

>>> s=fuc()

>>> s
'hellow'


>>> def s():
	s='hellow python '
	print(s)

	
>>> s()
hellow python 

>>> a=s()
hellow python 
>>> a


>>> def f():
	x=3
	def inner():
		y=4
		s=x+y
		print(s)
	return inner()

>>> f()
7

>>> s=f()
7

>>> def f():
	x=3
	def inner():
		y=4
		s=x+y
		return s
	return inner()

>>> f()
7

>>> def f():
	x=3
	def inner():
		y=4
		s=x+y
		return s
	return inner

>>> f()
<function f.<locals>.inner at 0x000001D808671430>

>>> s=f()



>>> s()
7

>>> f
<function f at 0x000001D8086714C0>

>>> s
<function f.<locals>.inner at 0x000001D808671550>
>>> s=f()


>>> s()
7

>>> #=================================================

>>> def fuction():
	x='hellow'
	print(x)

	
>>> fuction()
hellow

>>> s=fuction()
hellow

>>> s

>>> def fuction():
	x='hellow'
	return x

>>> fuction()
'hellow'

>>> s=fuction()

>>> s
'hellow'

>>> print(s)
hellow

>>> def fuction(x):
	return x

>>> fuction('hellow')
'hellow'

>>> s=fuction('hellow')

>>> s
'hellow'

>>> def fuction(x):
	print(x)

	

>>> fuction('hellow')
hellow

>>> s=fuction('hellow')
hellow

>>> s

>>> def fuction(x):
	x+='hellow'

	
>>> fuction('gopi')

>>> print(fuction('gopi'))
None

>>> def outer(x):
	def inner(y):
		print(x+y)
	return inner()


>>> def outer(x):
	def inner(y):
		print(x+y)
	return inner

>>> s=outer(5)

>>> s(7)
12

>>> outer(5)
<function outer.<locals>.inner at 0x000001D808671700>

>>> outer(5)(5)
10

>>> def outer():
	x=3
	def inner():
		y=6
		return x+y
	return inner

>>> s=outer()

>>> s()
9

>>> outer()()
9

>>> def outer():
	x=3
	def inner():
		y=6
		return x+y
	return inner

>>> a=outer()

>>> a.__name__
'inner'

>>> a()
9

>>> def fuction1():
	print('hi im fuction 1 ')

	
>>> def fuction2(fun):
	print('hi im fuction 2 and im calling fuction 1')
	fun()

	
>>> fuction2(fuction1)
hi im fuction 2 and im calling fuction 1
hi im fuction 1 


>>> @fuction2
def fuction1():
	print('hi im fuction 1 ')

	
hi im fuction 2 and im calling fuction 1
hi im fuction 1 


>>> fuction1

>>> #-------------------------

>>> def print_str():
	return 'python'

>>> def deco(fun):
	s=fun()
	s.upper()
	return s

>>> deco(print_str)
'python'

>>> s='ggg'

>>> s.upper()
'GGG'


>>> print_str()
'python'

>>> s=print_str()

>>> s
'python'

>>> s.upper()
'PYTHON'

>>> def deco(fun):
	s=fun()
	s.upper()
	return s

>>> def print_str():
	return 'python'

>>> deco(print_str)
'python'

>>> def deco(fun):
	s=fun()
	return s.upper()

>>> deco(print_str)
'PYTHON'


>>> def deco(fun):
	def inner():
		s=fun()
		return s.upper()
	return inner

>>> s=deco(print_str)

>>> s()
'PYTHON'

>>> s
<function deco.<locals>.inner at 0x000001D8086715E0>

>>> s.__name__
'inner'


>>> print_str
<function print_str at 0x000001D8086719D0>

>>> print_str.__name__
'print_str'

>>> def deco(fun):
	def inner():
		s=fun()
		return s.upper()
	return inner

>>> @deco
def print_str():
	return 'python'


>>> print_str.__name__
'inner'


>>> print_str()
'PYTHON'

>>> print_str
<function deco.<locals>.inner at 0x000001D808671A60>


>>> def upper(fun):
	def inner():
		s=fun()
		return s.upper()
	return inner

>>> @upper
def print_str():
	return 'hellow world'


>>> print_str
<function upper.<locals>.inner at 0x000001D808671CA0>

>>> type(print_str)
<class 'function'>


>>> print_str.__name__
'inner'

>>> print_str()
'HELLOW WORLD'

>>> print(print_str)
<function upper.<locals>.inner at 0x000001D808671CA0>

>>> def upper(fun):
	def inner():
		s=fun()
		return s.upper()
	return inner()

>>> print(print_str)
<function upper.<locals>.inner at 0x000001D808671CA0>

>>> @upper
def print_str():
	return 'hellow world'

>>> print_str
'HELLOW WORLD'

>>> def upper(fun):
	def inner():
		s=fun()
		return s.upper()
	return inner



>>> print_str
'HELLOW WORLD'

>>> @upper
def print_str():
	return 'hellow world'


>>> print_str
<function upper.<locals>.inner at 0x000001D808671B80>

>>> print_str()
'HELLOW WORLD'

>>> #--------------------------

>>> def greet(name):
	s='welcome to my class , Mr.',name
	return s


>>> name='gopi'

>>> s='hellow',name

>>> s
('hellow', 'gopi')

>>> greet('gopi')
('welcome to my class , Mr.', 'gopi')

>>> " ".join(s)
'hellow gopi'


>>> def greet(name):
	s='welcome to my class , Mr.',name
	return " ".join(s)

>>> def deco(fuc):
	s=fuc()
	return s.upper()


>>> def deco(fun):
	def inner(name):
		
		s=fun(name)
		return s.upper()
	return inner



>>> @deco
def greet(name):
	s='welcome to my class , Mr.',name
	return " ".join(s)

>>> greet.__name__
'inner'


>>> greet('gopi')
'WELCOME TO MY CLASS , MR. GOPI'

>>> #=====================================

>>> for i in range(10):
	print(i,end=' ')

	
0 1 2 3 4 5 6 7 8 9 

>>> import math

>>> math.factorial(4)
24

>>> def fac(n):
	if n==0:
		return 0
	else:
		for i in range(n):
			return i*fac(n-1)

		
>>> fac(5)
0

>>> def fac(n):
	if n==0:
		return 0
	else:
		for i in range(1,n+1):
			return i*fac(n-1)

		
>>> fac(5)
0

>>> def fac(n):
	if n==0:
		return 0
	else:
		for i in range(1,n+1):
			print(i*fac(n-1))

			

>>> def factorial(n):
	if n<=0:
		return -1
	else:
		return n*factorial(n-1)

	
>>> factorial(5)
-120

>>> def factorial(n):
	if n<0:
		return 1
	else:
		return n*factorial(n-1)


>>> factorial(5)
0

>>> factorial(4)
0


>>> def f(n):
	if n<0:
		return 1
	else:
		return n*f(n-1)

	
>>> f(5)
0

>>> def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


>>> factorial(7)
5040

>>> def factorial(n):
	if n<0:
		return 1
	else:
		return n*factorial(n-1)

	
>>> factorial(5)
0

>>> def factorial(n):
	if n==0:
		return 1
	else:
		return n * factorial(n-1)

	
>>> factorial(5)
120

>>> def factorial(n):
	if n<0:
		return 1
	else:
		return n * factorial(n-1)

	
>>> factorial(5)
0

>>> def factorial(n):
	if n==0:
		return 1
	else:
		return n * factorial(n-1)

	

>>> factorial(5)
120


>>> def outer(fuc):
	def inner(x):
		if x==0:
			print('facrorial',x ,' :',0)
		else :
			print('factorial ',x,':',fun(x))
	return inner



>>> def outer(fuc):
	def inner(x):
		if x==0 or x==1:
			print('facrorial',x ,' :',0)
		else :
			print('factorial ',x,':',fun(x))
	return inner


>>> @outer
def factorial(n):
	return n*factorial(n-1)


>>> def outer(fuc):
	def inner(x):
		if x==0 or x==1:
			print('facrorial',x ,' :',0)
		else :
			print('factorial ',x,':',fuc(x))
	return inner


>>> @outer
def factorial(n):
	return n*factorial(n-1)


>>> def outer(fuc):
	def inner(x):
		if x==0 or x==1:
			print('x==0 or x==1')
		else :
			print('factorial :',fuc(x))
	return inner


>>> @outer
def factorial(n):
	return n*factorial(n-1)
