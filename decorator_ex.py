
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

