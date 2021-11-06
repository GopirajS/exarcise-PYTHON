Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> import keyword as kw

>>> s=kw.kwlist

>>> print('list of kwy words :')
list of kwy words :

>>> print(s)
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

>>> len(s)
36

>>> #    True ,  False , None

>>> print(False==0)
True

>>> print(False==1)
False

>>> print(False==1234)
False

>>> print(False==000)
True

>>> print(True==000)
False

>>> print(True==1)
True

>>> print(True==1234)
False

>>> print(True==1111)
False

>>> print(True==1)
True

>>> print(None==[])
False

>>> print(None==0)
False

>>> print(None)
None

>>> #====================================================

>>> #  and ,or ,not

>>> True and True
True

>>> True and False
False

>>> False and True
False

>>> False and  True
False

>>> 1 and 1
1

>>> 1 and 0
0

>>> 0 and 0
0

>>> 0 and 1
0

>>> 10 and  32
32

>>> 100 and  32
32

>>> 100 and  33
33

>>> 100 and  0
0

>>> 100 and  True
True

>>> 00 and  True
0

>>> 0 and  True
0

>>> 1 and  True
True

>>> None and  True

>>> True and  None

>>> None and  None

>>> 10 or 20 or 30
10

>>> 123 or 20 or 30
123

>>> 123 and 20 and 30
30

>>> 123 and 20 and 30 and 40
40

>>> 123 and 20 and 30 and 40 or 12
40

>>> True or True
True

>>> True or False
True

>>> False or False
False

>>> False or True
True

>>> not 12
False

>>> not 'gopi'
False

>>> not True
False

>>> not False
True

>>> #=====================================



>>> 'gopi' is 'gopi'
True

>>> 'gopi' is 'gopi raj'
False


>>> if True:
	print('hi')

	
hi

>>> if (True):
	print('hi')

	
hi



>>> if 's' in 'gopirajs':
	print("yes s is in string ")
	
yes s is in string 

>>> if 's' in 'gopirajs':
	print("yes 's' is in string ")

	
yes 's' is in string 


>>> for i in 'gopiraj':
	print(i,end=' ')

g o p i r a j 

>>> print('\r')


>>> #   break statement

>>> for i in range(10):
	print(i,end=' ')
	
0 1 2 3 4 5 6 7 8 9 
>>> for i in range(10):
	print(i,end='--> ')

	
0--> 1--> 2--> 3--> 4--> 5--> 6--> 7--> 8--> 9--> 

>>> for i in range(10):
	print(i,end='--> ')
	break

0--> 

>>> for i in range(10):
	print(i,end='--> ')
	if i==10:
		break
	
0--> 1--> 2--> 3--> 4--> 5--> 6--> 7--> 8--> 9--> 

>>> for i in range(10):
	print(i,end='-->')
	if i==6:
		break

0-->1-->2-->3-->4-->5-->6-->

>>> n=0

>>> while n>10:
	print(i,end=' ->')
	n+=1
	break

>>> while n<10:
	print(i,end=' ->')
	n+=1
	break

6 ->
>>> n=0

>>> while n<10:
	print(i,end=' ->')
	n+=1
	break

6 ->

>>> while n<10:
	print(i,end=' ->')
	n+=1

	
6 ->6 ->6 ->6 ->6 ->6 ->6 ->6 ->6 ->

>>> while n<10:
	print(n,end=' ->')
	n+=1

	
>>> n=0

>>> while n<10:
	print(n,end=' ->')
	n+=1

	
0 ->1 ->2 ->3 ->4 ->5 ->6 ->7 ->8 ->9 ->

>>> n=0

>>> while n<10:
	print(n,end=' ->')
	n+=1

	break

0 ->

>>> n=0

>>> while n<10:
	print(n,end=' ->')
	n+=1
	if n==6:
		break

	
0 ->1 ->2 ->3 ->4 ->5 ->

>>> n=0

>>> while n<10:
	print(n,end=' ->')
	n+=1
	if n==6:
		continue

	
0 ->1 ->2 ->3 ->4 ->5 ->6 ->7 ->8 ->9 ->

>>> while n<10:
	if n==6:
		continue
	print(n,end=' ->')
	n+=1

	
>>> n=0


>>> while n<10:
	if n==6:
		n+=1
		continue
	
	print(n,end=' ->')
	n+=1

	
7 ->8 ->9 ->

>>> n=0

>>> while n<10:
	if n==6:
		n+=1
		continue

	print(n,end=' ->')
	n+=1
	
0 ->1 ->2 ->3 ->4 ->5 ->7 ->8 ->9 ->

>>> n=0

>>> while n<=10:
	if n==6:
		n+=1
		continue

	print(n,end=' ->')
	n+=1

	
0 ->1 ->2 ->3 ->4 ->5 ->7 ->8 ->9 ->10 ->
>>> #====================================

>>> #  if ,elif,else

>>> n=2

>>> if n==2:
	print('condition is True')

	
condition is True

>>> if n==1:
	print('empty')
else :
	print('condition is False or excisute else statument')

	
condition is False or excisute else statument

>>> if n==0:
	print('contion is True is run')
elif n==1:
	print('condition is True is run')
else:
	print('else statemnt')

	
else statemnt

>>> n
2

>>> if n==0:
	print('contion is True is run')
elif n==1:
	print('condition is True is run')
elif n==2:
	print('condition is True is run ekif')

	
condition is True is run ekif

>>> #================================================

>>> #   def keyword


>>> def fuction():
	pass

>>> fuction()

>>> def fuction():
	print('hellow world')

	
>>> fuction()
hellow world



>>> def fun():
	s=0
	for i in range(10):
		s+=i
		yield s

		
>>> fun()
<generator object fun at 0x000002243F3D0510>

>>> list(fun())
[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

>>> def fun():
	s=0
	for i in range(10):
		s+=i
		return s

	
>>> fun()
0

>>> def fun():
	s=0
	for i in range(10):
		s+=i
	return s

>>> fun()
45

>>> def fun():
	s=0
	for i in range(10):
		s+=i

	
>>> fun()




>>> def fun():
	s=0
	for i in range(10):
		s+=i
		yield s

		
>>> fun()
<generator object fun at 0x000002243F48F890>

>>> for i in fun():
	print(i,end=' ')

	
0 1 3 6 10 15 21 28 36 45 

>>> def fun():
	s=0
	for i in range(10):
		s+=i
	yield s

	
>>> fun()
<generator object fun at 0x000002243F3D0510>

>>> for i in fun():
	print(i,end=' ')

	
45 

>>> #====================================================

>>> #  class

>>> class myclass(object):
	f='gopi'
	l='raj'
	def fun(self):
		self.f=f
		self.l=l
		print(self.s  ,'and', self.l)

		
>>> s=myclass()

>>> s.f
'gopi'

>>> s.l
'raj'


>>> class myclass(object):
	f='gopi'
	l='raj'
	def fun(self):
		self.f=f
		self.l=l
		print(self.f  ,'and', self.l)

		
>>> s=myclass()


>>> class myclass():
	name='gopi'
	def pri(self):
		print(self.name)

		
>>> d=myclass()

>>> d.pri()
gopi

>>> import math as m

>>> m.factorial(25)
15511210043330985984000000

>>> m.factorial(2)
2

>>> m.factorial(22)
1124000727777607680000

>>> m.factorial(5)
120

>>> m.factorial(6)
720

>>> def myfuc():
	pass




>>> myfuc()


>>> def myfuc():
	print('hellow world')

	

>>> n=10

>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9




>>> b=0


>>> #===============================================================

>>> # del keyword

>>> my_name='gopiraj'


>>> print(my_name)
gopiraj

>>> del my_name


>>> #=========================================

>>> # glopal and nonglopal

>>> s='gopiraj'


>>> def g():
	print(s)

	
>>> g()
gopiraj

>>> name='sathish'

>>> class myclass():
	def myfun(self):
		print(name)

		
>>> s=myclass()

>>> s.myfun()
sathish

>>> class myclass():
	name='gopiraj'
	def myfun(self):
		print(name)

		
>>> s=myclass()

>>> s.myfun()
sathish

>>> s.name
'gopiraj'

>>> s.myfun()
sathish

>>> class myclass():
	name='gopiraj'
	def myfun(self):
		print(self.name)

		
>>> s=myclass()

>>> s.myfun()
gopiraj

>>> s.name
'gopiraj'

>>> d=s.myfun()
gopiraj


