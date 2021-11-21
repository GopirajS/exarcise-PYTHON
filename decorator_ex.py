
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
>>>
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


>>>#===================================================================


>>> def div(a,b):
	s=a/b
	return s

>>> def deco(fun):
	def inner(x,y):
		if y==0:
			print('canot divide by zero')
		else:
			print('divided...')
			s=fun(x,y)
			print(s)

			
>>> @deco
def div(a,b):
	s=a/b
	return s


>>> div

>>> def deco(fun):
	def inner(x,y):
		if y==0:
			print('canot divide by zero')
		else:
			print('divided...')
			s=fun(x,y)
			print(s)
	return inner

>>> @deco
def div(a,b):
	s=a/b
	return s

>>> div(2,4)
divided...
0.5

>>> div(2,0)
canot divide by zero

>>> d

>>> def fact(x):
	return x*fact(x-1)


>>> def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)

	
>>> fact(4)
24

>>> fact(1)
1


>>> fact(0)
1





>>> @deco
def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)

	


>>> def deco(fun):
	def inner(num):
		if num<0:
			print('negative numer cannot used !')
		else:
			s=fun(num)
			print(s)
	return inner


>>> @deco
def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)

	



>>> def deco(fun):
	def inner(num):
		if num<0:
			print('negative numer cannot used !')
		else:
			s=fun(num)
			print(s)
	return inner


>>> def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)

>>> fact(5)
120

>>> deco(fact)
<function deco.<locals>.inner at 0x0000028E09613790>

>>> s=deco(fact)

>>> s(5)
120

>>> s(-1)
negative numer cannot used !


>>> def deco(fun):
	def inner(num):
		if num<0:
			print('negative numer cannot used !')
		else:
			print('positive number can be use ')
			s=fun(num)
			print(s)
	return inner

>>> def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)

	

>>> fact(5)
120

>>> @deco
def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)

	


>>> def deco(fun):
	def inner(num):
		if num<0:
			print('negative numer cannot used !')
		else:
			print('positive number can be use ')
			s=fun(num)
			print(s)
	return inner


>>> def deco(fun):
	def inner(num):
		if num<0:
			print('negative numer cannot used !')
		else:
			s=fun(num)
			print(s)
	return inner

>>> def deco(fun):
	def inner(num):
		if num<0:
			print('negative numer cannot used !')
		else:
			s=fun(num)
			print(s)
	return inner


>>> def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)


>>> fact(6)
720

>>> fact(5)
120

>>> fact(3)
6

>>> fact(4)
24

>>> deco(fact)
<function deco.<locals>.inner at 0x0000028E09613820>

>>> s=deco(fact)

>>> s(8)
40320

>>> s(-1)
negative numer cannot used !



>>> def deco(fun):
	def inner(num):
		if num<0:
			print('negative numer cannot used !')
		else:
			s=fun(num)
			print(s)
	return inner()


>>> @deco
def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)



>>> def deco(fun):
	def inner(num):
		if num<0:
			print('negative numer cannot used !')
		else:
			return fun(num)
	return inner


>>> deco(fact)
<function deco.<locals>.inner at 0x0000028E09613940>

>>> s=deco(fact)

>>> s(4)
24

>>> s(-1)
negative numer cannot used !


>>> @deco
def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)


>>> fact(7)
5040

>>> fact(-1)
negative numer cannot used !

>>> fact(-1)
negative numer cannot used !

>>> def deco(fun):
	def inner(num):
		if num<0:
			print('negative numer cannot used !')
		else:
			return fun(num)
	return inner


>>> def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)

	

>>> deco(fact)
<function deco.<locals>.inner at 0x0000028E09613AF0>

>>> s=deco(fact)

>>> s(5)
120

>>> def deco(fun):
	def inner(num):
		if num<0:
			print('negative numer cannot used !')
		else:
			return fun(num)
	return inner()


>>> def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)

	

>>> def deco(fun):
	def inner(num):
		if num<0:
			print('negative numer cannot used !')
		else:
			return fun(num)
	return inner()(5)


>>> def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)

	

>>> def div(a,b):
	return a/b


>>> div(1,3)
0.3333333333333333




>>> def deco(fuc):
	def inner(x,y):
		if y==0:
			print('canot division by zero')
		else:
			print('divided by {} and {}'.format(x,y))
			return fuc(x,y)
	return inner


>>> @deco
def div(a,b):
	return a/b



>>> div(2,4)
divided by 2 and 4
0.5

>>> div(2,0)
canot division by zero

>>> #------------------------------

>>> def normal_msg():
	s=input('enter a string:')
	return s


		
>>> def split_d(func):
	def inner():
		s=func()
		return s.split(" ")
	return inner

>>> s=split_d(normal_msg)

>>> s()
enter a string:hellow world
['hellow', 'world']


>>> def cap_d(func):
	def inner():
		s=func()
		return s.capitalize()
	return inner


>>> @split_d
@cap_d
def normal_msg():
	s=input('enter a string:')
	return s


>>> normal_msg()
enter a string:hellow world
['Hellow', 'world']

>>> s=['hellow', 'world']


>>> for i in s:
	i.capitalize()

	
'Hellow'
'World'

>>> #------------------------------

>>> s=['hellow', 'world']

>>> for i in s:
	l=[]
	l.append(i.capitalize())

	
>>> l
['World']

>>> l
['World']

>>> s=['hellow', 'world']

>>> for i in s:
	l=[]
	l.append(i.capitalize())

	
>>> l
['World']


>>> l=[]

>>> for i in s:
	l.append(i.capitalize())

	
>>> l
['Hellow', 'World']

>>> def cap_d(func):
	def inner():
		l=[]
		s=func()
		for i in s:
			l.append(i.capitalize())
		return l
	return inner

>>> def split_d(func):
	def inner():
		s=func()
		return s.split(" ")
	return inner


>>> @split_d
@cap_d
def normal_msg():
	s=input('enter a string:')
	return s


>>> @split_d
def normal_msg():
	s=input('enter a string:')
	return s


>>> normal_msg()
enter a string:hellow world
['hellow', 'world']


>>> @split_d
def normal_msg():
	return input('enter a string:')


>>> def normal_msg():
	return input('enter a string:')


>>> normal_msg()
enter a string:helow world
'helow world'


>>> @split_d
def normal_msg():
	return input('enter a string:')


>>> normal_msg()
enter a string:hellow world
['hellow', 'world']

>>> s=normal_msg()
enter a string:hellw world

>>> s
['hellw', 'world']

>>> s
['hellw', 'world']

>>> def cap_d(func):
	def inner():
		l=[]
		s=func()
		for i in s:
			l.append(i.capitalize())
		return l
	return inner



>>> @split_d
@cap_d
def normal_msg():
	return input('enter a string:')


>>>#=====================================================================



>>> s='gopi'

>>> def hello():
	t='raj'
	def inner():
		print(s)
	inner()

	
>>> hello()
gopi


>>> def outer(txt):
	def inner():
		print(txt)
	return inner

>>> obj=outer('hellow world')

>>> obj()
hellow world

>>> obj
<function outer.<locals>.inner at 0x00000180627A54C0>

>>> obj.__name__
'inner'

>>> def fuc():
	print('hellow world')

	
>>> fuc()
hellow world

>>> s=fuc

>>> s()
hellow world

>>> def string():
	s=input('enter a string :')
	return s


>>> string()
enter a string :hellow world
'hellow world'

>>> def upper_d(func):
	s=func()
	return s.upper()


>>> upper_d(string)
enter a string :hellow woorld
'HELLOW WOORLD'

>>> def cap_d(func):
	s=func()
	r=s.split(' ')
	l=[]
	for i in r:
		l.append(i.capitalize())
	return l

>>> cap_d(string)
enter a string :hellow world
['Hellow', 'World']

>>> def cap_d(func):
	s=func()
	r=s.split(' ')
	l=[]
	for i in r:
		l.append(i.capitalize())
	return ' '.join(l)

>>> cap_d(string)
enter a string :hellow world
'Hellow World'

>>> @cap_d
def string():
	s=input('Enter your string :')
	return s

Enter your string :hellow world how are you ?

>>> def cap_d(func):
	def inner():
		s=func()
		s=s.split(' ')
		l=[]
		for i in s:
			l.append(i.capitalize())
		return ' '.join(l)
	return inner



>>> @cap_d
def string():
	string=input('Enter a string:')
	return string


>>> string()
Enter a string:hellow world
'Hellow World'

>>> string()
Enter a string:gopi raj sathish kuamr gowri gopal 
'Gopi Raj Sathish Kuamr Gowri Gopal '

>>> string()
Enter a string:a s d f g h  k l z x c v b n m q w e r t y u i o p 
'A S D F G H  K L Z X C V B N M Q W E R T Y U I O P '

>>> def upper(func):
	s=func()
	return s.upper()


>>> def lower(func):
	s=func()
	return s.lower()


>>> def string():
	s=input('enter a string :')
	return s

>>> string()
enter a string :hellow gopi raj how are you ?
'hellow gopi raj how are you ?'


>>> cap_d(string)
<function cap_d.<locals>.inner at 0x00000180627A5700>
>>> def cap_d(func):
	def inner():
		s=func()
		s=s.split(' ')
		l=[]
		for i in s:
			l.append(i.capitalize())
		return ' '.join(l)
	return inner

>>> cap_d(string)
<function cap_d.<locals>.inner at 0x00000180627A55E0>


>>> #-----------------------------------------------

>>> def cap_d(func):
	def inner():
		s=func()
		s=s.split(' ')
		l=[]
		for i in s:
			l.append(i.capitalize())
		return ' '.join(l)
	return inner


>>> def string():
	s=input('Enter A String :')
	return s


>>> string()
Enter A String :hellow how are you
'hellow how are you'


>>> cap_d(string)
<function cap_d.<locals>.inner at 0x00000180627A55E0>

>>> @cap_d
def string():
	s=input('Enter A String :')
	return s


>>> string()
Enter A String :hell kk
'Hell Kk'


>>> string()
Enter A String :k k k 
'K K K '


>>> string()
Enter A String :kk dd aa tt 
'Kk Dd Aa Tt '\

>>> #--------------------------------

>>> def upper(func):
	s=func()
	return s.upper()

>>> def lower(func):
	s=func()
	return s.lower()


>>> def string():
	s=input('enter a string :')
	return s


>>> lower(string)
enter a string :HELLE WORLD
'helle world'

>>> upper(string)
enter a string :
''

>>> upper(string)
enter a string :hello world
'HELLO WORLD'

>>> def deco1(fun):
	def inner():
		s=fun()
		return s*s
	return inner


>>> def deco2(fun):
	def wrape():
		s=fun()
		return s*2
	return wrape

>>> def cal():
	return 10

>>> deco1(cal)
<function deco1.<locals>.inner at 0x00000180627A5A60>

>>> s=deco1(cal)

>>> s()
100
>>> s=deco2(cal)
>>> 

>>> s
<function deco2.<locals>.wrape at 0x00000180627A5A60>

>>> s()
20

>>> @deco1
@deco2
def cal():
	return 10


>>> cal()
400

>>> @deco1
@deco2
def cal():
	num=int(input('enter a number:'))
	return num


>>> cal()
enter a number:3
36

>>> cal()
enter a number:1
4

>>> cal()
enter a number:1
4

>>> cal()
enter a number:2
16

>>> #----------------------------------------


>>> def split_d(func):
	def inner():
		s=func()
		return s.split(' ')
	return inner

>>> def cap(funs):
	def inner():
		s=funs()
		l=[]
		for i in s:
			l.append(i.capitalize())
		return ' '.join(l)
	return inner

>>> def string():
	s=input('Enter A string :')
	return s


>>> string()
Enter A string :helow worl
'helow worl'


>>> @cap
@split_d
def string():
	s=input('Enter A string :')
	return s


>>> string()
Enter A string :hellow world
'Hellow World'



>>> string()
Enter A string :hellow how are you gopi raj ?
'Hellow How Are You Gopi Raj ?'


>>> string()
Enter A string :a s d f g h j k l z x c v b n m q w e r t y u i o p
'A S D F G H J K L Z X C V B N M Q W E R T Y U I O P'


>>> string()
Enter A string :aa ss dd ff gg hh jj kk ll qq ww ee rr tt yy uu ii oo pp zz xx cc vv bb nn mm 
'Aa Ss Dd Ff Gg Hh Jj Kk Ll Qq Ww Ee Rr Tt Yy Uu Ii Oo Pp Zz Xx Cc Vv Bb Nn Mm '


>>>#==================================================================================================


Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fuction1():
	print("im fuction one")

	
>>> def fuction2(func):
	print('im fuction two ,im calling fuction one')
	func()
	print('printing fuction one')

	
>>> fuction2(fuction1)
im fuction two ,im calling fuction one
im fuction one
printing fuction one
>>> 
>>> 
>>>  def greet():
	 
SyntaxError: unexpected indent
>>> def greet():
	s=input("enter a string :")
	return s

>>> 
>>> greet()
enter a string :hellow world
'hellow world'
>>> 
>>> greet()
enter a string :'hellow world'
"'hellow world'"
>>> 
>>> 
>>> 
>>> def deco(func):
	def inner():
		s=func()
		return s.upper()
	return inner

>>> 
>>> s=deco(greet)
>>> s()
enter a string :hellow world
'HELLOW WORLD'
>>> 
>>> 
>>> @deco
def greet():
	s=input("enter a string :")
	return s

>>> 
>>> greet()
enter a string :hellow world
'HELLOW WORLD'
>>> 
>>> 
>>> 
>>> 
>>> #================================
>>> 
>>> 
>>> # you can pass a perameter in decorator
>>> 
>>> def greet():
	s=input('enter greating message:')
	return s

>>> 
>>> def deco(exp):
	def outer(funs):
		def inner():
			s=funs()
			return s + exp
		return inner
	return outer

>>> 
>>> 
>>> @deco(' Gopi Raj ')
def greet():
	s=input('enter a string:')
	return s

>>> 
>>> greet()
enter a string:how are Mr
'how are Mr Gopi Raj '

>>>#=================================================================



>>> for i in range(5):
	if i==2:
		print('i=2')
else:
	print('for loop is closed')

	
i=2
for loop is closed

>>> for i in range(5):
	if i==2 or i==4:
		print('i=2')
else:
	print('for loop is closed')

	
i=2
i=2
for loop is closed

>>> for i in range(5):
	if i==2 or i==4:
		print('i=',i)
else:
	print('for loop is closed')

	
i= 2
i= 4
for loop is closed

>>> class myclass():
	def __init__(self,func):
		self.func=func
	def __call__(self,*arg):
		for i in arg[1:]:
			if i==0:
				print('you canot divide by zero give proper inout !!!')
		else:
			return self.func(*arg)

		

>>> @myclass
def greet(a,b):
	return a/b


>>> greet(1,3)
0.3333333333333333\

>>> greet(1,0)
you canot divide by zero give proper inout !!!
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    greet(1,0)
  File "<pyshell#24>", line 9, in __call__
    return self.func(*arg)
  File "<pyshell#31>", line 3, in greet
    return a/b
ZeroDivisionError: division by zero

>>> class myclass():
	def __init__(self,func):
		self.func=func
	def __call__(self,*arg):
		for i in arg[1:]:
			if i==0:
				print('you canot divide by zero give proper inout !!!')
			else:
				return self.func(*arg)

			
>>> @myclass
def greet(a,b):
	return a/b


>>> greet(1,0)
you canot divide by zero give proper inout !!!

>>> #---------------------------------------------

>>> class myclass():
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
		self.msg = self.name + " got " + self.grade

		

>>> s=myclass('gopi','B')

>>> s.name
'gopi'

>>> s.grade
'B'

>>> s.msg
'gopi got B'

>>> s.name='sathish'

>>> s.grade
'B'

>>> s.name
'sathish'



>>> s.name
'sathish'

>>> s.msg
'gopi got B'

>>> s.name
'sathish'


>>> class myclass():
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	def msg(self):
		self.grade +" got grade " + self.grade

		

>>> s=myclass('gopi',"D")

>>> s.name
'gopi'

>>> s.grade
'D'

>>> s.msg()

>>> s.msg
<bound method myclass.msg of <__main__.myclass object at 0x000001AE56AAE7C0>>


>>> class myclass():
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	def msg(self):
		return self.grade +" got grade " + self.grade

	

>>> s=myclass('gopi',"D")

>>> s.msg()
'D got grade D'

>>> class myclass():
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	def msg(self):
		return self.name +" got grade " + self.grade

	

>>> s=myclass('Gopi','A')

>>> s.name
'Gopi'

>>> s.grade
'A'


>>> s.msg()
'Gopi got grade A'

>>> s.name='sathish'



>>> s.msg()
'sathish got grade A'

>>> s.name
'sathish'

>>> s.grade='S'

>>> s.msg()
'sathish got grade S'

>>> def greet():
	return 'hellow world'


>>> @property
def greet():
	return 'hellow world'

>>> greet
<property object at 0x000001AE56AC3680>


>>> print(greet)
<property object at 0x000001AE56AC3680>

>>> s=greet

>>> s
<property object at 0x000001AE56AC3680>

>>> class myclass():
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	@property	
	def msg(self):
		return self.name +" got grade " + self.grade

	

>>> s=myclass('gopi','G')

>>> s.name
'gopi'

>>> s.msg
'gopi got grade G'

>>> s.grade
'G'

>>> s.msg
'gopi got grade G'

>>> s.name='Sathish'

>>> s.grade='S'

>>> s.msg
'Sathish got grade S'

>>> class myclass():
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	@property
	def msg(self):
		return self.name +" got grade " + self.grade
	@msg.setter
	def msg(self,msg):
		selt=msg.split(" ")
		self.name=selt[0]
		self.grade=selt[-1]

		

>>> s=myclass('Gopi','G')

>>> s.name
'Gopi'

>>> s.grade
'G'

>>> s.msg
'Gopi got grade G'

>>> s.msg='Sathishnkumar got grade S'

>>> s.name
'Sathishnkumar'

>>> s.msg
'Sathishnkumar got grade S'

>>> s.grade
'S'

>>> class my_mark():
	def __init__(self,name,mark):
		self.name=name
		self.__mark=mark
	def persentage(self):
		print('name:',self.name)
		return (self.__mark/500)*100

	

>>> s=my_mark('Gopi',450)

>>> s.name
'Gopi'

>>> s.persentage()
name: Gopi
90.0

>>> class my_mark():
	def __init__(self,name,mark):
		self.name=name
		self.__mark=mark
	def persentage(self):
		print('name:',self.name)
		return (self.__mark/500)*100 + '%'

	
>>> s=my_mark('Gopi',450)



>>> class my_mark():
	def __init__(self,name,mark):
		self.name=name
		self.__mark=mark
	def persentage(self):
		print('name:',self.name)
		return str((self.__mark/500)*100) + '%'

	
>>> s=my_mark('Gopi',450)

>>> s.persentage()
name: Gopi
'90.0%'

>>> s=my_mark('Gopi',477)

>>> s.name
'Gopi'

>>> s.persentage
<bound method my_mark.persentage of <__main__.my_mark object at 0x000001AE56A9B2E0>>


>>> s.persentage()
name: Gopi
'95.39999999999999%'

>>> class my_mark():
	def __init__(self,name,mark):
		self.name=name
		self.__mark=mark
	def persentage(self):
		print('name:',self.name)
		return str((self.__mark/500)*100) + '%'

	
>>> s=my_mark('Gopi',356)

>>> s.name
'Gopi'

>>> s.persentage()
name: Gopi
'71.2%'


>>> class my_mark():
	def __init__(self,name,mark):
		self.name=name
		self.__mark=mark
	def persentage(self):
		print('name:',self.name)
		return str((self.__mark/500)*100) + '%'
	def setter(self,value):
		self.__mark=value
	def getter(self):
		return self.__mark

	

>>> s=my_mark('Gopi',345)

>>> s.getter()
345

>>> s.name
'Gopi'

>>> s.persentage
<bound method my_mark.persentage of <__main__.my_mark object at 0x000001AE56A9B280>>

>>> s.persentage()
name: Gopi
'69.0%'

>>> s.setter('234')

>>> s.setter(132)

>>> s.persentage()
name: Gopi
'26.400000000000002%'

>>> class my_mark():
	def __init__(self,name,mark):
		self.name=name
		self.__mark=mark
	def persentage(self):
		print('name:',self.name)
		return str((self.__mark/500)*100) + '%'
	def setter(self,value):
		self.__mark=value
	def getter(self):
		return self.__mark


>>> class my_mark():
	def __init__(self,name,mark):
		self.name=name
		self.__mark=mark
	@property	
	def mark(self):
		return self.__mark
	@mark.setter
	def mark(self,value):
		self.__mark=value
	@mark.deleter	
	def mark(self):
		return self.__mark


>>> s=my_mark('Gopi',234)

>>> s.name
'Gopi'

>>> s.mark
234

>>> s.mark=234

>>> s.mark=111

>>> s.mark
111

>>> del s.mark

>>> s.name
'Gopi'

>>> s.mark
111

>>> class my_mark():
	def __init__(self,name,mark):
		self.name=name
		self.__mark=mark
	@property
	def mark(self):
		return self.__mark
	@mark.setter
	def mark(self,value):
		self.__mark=value
	@mark.deleter
	def mark(self):
		del self.__mark


>>> s=my_mark('Gopi',234)

>>> s.mark=345

>>> s.mark
345
>>> s.name='Gopi'

>>> s.mark
345
>>> s.name
'Gopi'

>>> del s.mark

>>> s.name
'Gopi'


>>> del s.name

>>> s.mark=123

>>> s.mark
123

>>> class my_mark():
	def __init__(self,name,mark):
		self.name=name
		self.__mark=mark
	def getter(self):
		return self.__mark
	def setter(self,value):
		self.__mark=value
	def deleter(self):
		del self.__mark
	mark=property(getter,setter,deleter)

	
>>> s=my_mark('gopi',234)

>>> s.mark
234


>>> class my_mark():
	def __init__(self,mark):
		self.__mark=mark
	def per(self):
		return (self.__mark/500)*100
	def getter(self):
		return self.__mark
	def setter(self,value):
		self.__mark = self.value
	def deleter(self):
		del self.__mark
	mark=property(getter,setter,deleter)

	

>>> s=my_mark(234)

>>> s.mark
234

>>> class my_mark():
	def __init__(self,mark):
		self.__mark=mark
	def per(self):
		return (self.__mark/500)*100
	def getter(self):
		return self.__mark
	def setter(self,value):
		if 0<value or 500>value:
			self.__mark = self.value
		else:
			print('value is out or rasio,canot set values')
	def deleter(self):
		del self.__mark
	mark=property(getter,setter,deleter)


>>> s=my_mark(123)

>>> s.mark
123

>>> s.per()
24.6
>>> s.setter
<bound method my_mark.setter of <__main__.my_mark object at 0x000001AE56AAECD0>>

>>> class my_mark():
	def __init__(self,mark):
		self.__mark=mark
	def per(self):
		return (self.__mark/500)*100
	def getter(self):
		return self.__mark
	def setter(self,value):
		if 0<value or value>500:
			self.__mark = self.value
		else:
			print('value is out or rasio,canot set values')
	def deleter(self):
		del self.__mark
	mark=property(getter,setter,deleter)


>>> s=my_mark(123)

>>> s.mark
123

>>> s.getter
<bound method my_mark.getter of <__main__.my_mark object at 0x000001AE56AD16A0>>

>>> s.getter()
123


>>>#============================================================================





>>> class my_class():
	def __init__(self,name,marks):
		self.name=name
		self.mark=marks
	def msg(self):
		return self.name +' got marks persentage'+self.mark

	

>>> s=my_class('Gopi',"60%")

>>> s.msg()
'Gopi got marks persentage60%'

>>> name='Sathish Kumar'

>>> m=456

>>> marks=(m/500)*100

>>> s=my_class(name,marks)


>>> marks
91.2

>>> class my_class():
	def __init__(self,name,marks):
		self.name=name
		self.mark=marks
	def msg(self):
		return self.name +' got marks persentage'+str(self.mark)

	

>>> obj=my_class('Gopi',60)

>>> obj.msg()
'Gopi got marks persentage60'

>>> obj=my_class('Gopi',"60 %")

>>> obj.msg()
'Gopi got marks persentage60 %'

>>> name='Sathish kumar'

>>> m=345

>>> marks=str((m/500)*100) + "%"

>>> marks
'69.0%'

>>> s=my_class(name,marks)

>>> s.msg()
'Sathish kumar got marks persentage69.0%'

>>> s.mark
'69.0%'

>>> s.name
'Sathish kumar'

>>> class my_class():
	def __init__(self,name,marks):
		self.name=name
		self.mark=marks
	def msg(self):
		return self.name +' got marks persentage'+str(self.mark)

	
>>> s=my_class('Gopi','60 %')

>>> s.mark
'60 %'

>>> s.name
'Gopi'

>>> s.msg()
'Gopi got marks persentage60 %'


>>> class my_class():
	def __init__(self,name,marks):
		self.name=name
		self.mark=marks
	def msg(self):
		return self.name +' got marks persentage '+ str(self.mark)
	@classmethod
	def per(cls,name,marks):
		return cls(name,str((marks/500)*100))


>>> s=my_class('Gopi',224)

>>> s.msg()
'Gopi got marks persentage 224'


>>> s.per('gopi',224)
<__main__.my_class object at 0x0000015BC47AC280>

>>> s=my_class.per('gopiraj',234)

>>> s.mark
'46.800000000000004'

>>> s.msg()
'gopiraj got marks persentage 46.800000000000004'

>>> class my_mark():
	def __init__(self,name,mark):
		self.name=name
		self.mark=mark
	def persentage(self):
		return self.name +"is got a persentage "+ str(self.mark)
	def get_per(cls,name,mark):
		return cls(name,str((mark/500)*100))
	def get_age(age):
		if age<18:
			print('you are miner ')
		else:
			print('you are mager ')

			

>>> s=my_mark('Gopi',123)

>>> s.mark
123

>>> s.name
'Gopi'

>>> s.persentage()
'Gopiis got a persentage 123'


>>> class my_mark():
	def __init__(self,name,mark):
		self.name=name
		self.mark=mark
	def persentage(self):
		return self.name +"is got a persentage "+ str(self.mark)
	@classmethod
	def get_per(cls,name,mark):
		return cls(name,str((mark/500)*100))
	@staticmethod
	def get_age(age):
		if age<18:
			print('you are miner ')
		else:
			print('you are mager ')

			

>>> s=my_mark.get_per('gopi',234)

>>> s.persentage()
'gopiis got a persentage 46.800000000000004'

>>> s.mark
'46.800000000000004'

>>> s.mark
'46.800000000000004'

>>> s.name
'gopi'

>>> s.persentage()
'gopiis got a persentage 46.800000000000004'

>>> s.get_age(34)
you are mager 

>>> s.get_age(12)
you are miner 

>>> s.name='Sathish'

>>> s.persentage()
'Sathishis got a persentage 46.800000000000004'

