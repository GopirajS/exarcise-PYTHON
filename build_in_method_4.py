Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>>    # reversed()   method

>>> s='gopiraj'

>>> d=reversed(s)

>>> next(d,'iter is complet')
'j'

>>> next(d,'iter is complet')
'a'

>>> next(d,'iter is complet')
'r'

>>> next(d,'iter is complet')
'i'

>>> next(d,'iter is complet')
'p'

>>> next(d,'iter is complet')
'o'

>>> next(d,'iter is complet')
'g'

>>> next(d,'iter is complet')
'iter is complet'

>>> d=reversed(s)

>>> d.__next__()
'j'

>>> d.__next__()
'a'

>>> d.__next__()
'r'

>>> d.__next__()
'i'

>>> d.__next__()
'p'

>>> d.__next__()
'o'

>>> d.__next__()
'g'

>>> d.__next__()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d.__next__()
StopIteration

>>> s='gopiraj'

>>> d=reversed(s)

>>> for i in d:
	print(i,end=' ')

	
j a r i p o g 

>>> s='gpiraj'

>>> l=[1,2,3,4,5]

>>> ll=reversed(l)

>>> for i in ll:
	i

	
5
4
3
2
1

>>> l=[1,2,3,4,5,'gopi','sathish']

>>> ll=reversed(l)

>>> for i in ll:
	i

	
'sathish'
'gopi'
5
4
3
2
1

>>> l=[1,2,3,4,5,'gopi','sathish',('raj','kumar')]

>>> ll=reversed(l)

>>> for i in ll:
	i

	
('raj', 'kumar')
'sathish'
'gopi'
5
4
3
2
1

>>> ll=list(reversed(l))

>>> ll
[('raj', 'kumar'), 'sathish', 'gopi', 5, 4, 3, 2, 1]

>>> ll=set(reversed(l))

>>> ll
{1, 2, 3, 4, 5, 'sathish', 'gopi', ('raj', 'kumar')}

>>> t=(10,20,30,40)

>>> d=set(reversed(t))

>>> d
{40, 10, 20, 30}

>>> t=[10,20,30,40]


>>> d=set(reversed(t))

>>> d
{40, 10, 20, 30}



>>> #=============================================================

>>> #  round()  method

>>> round(21)
21

>>> round(21.333)
21

>>> round(21.5)
22

>>> round(21.49999)
21

>>> round(21.5000)
22

>>> round(21.9)
22

>>> round(21.9)
22

>>> round(22.0)
22

>>> round(21.5000,3)
21.5

>>> round(21.5000,4)
21.5

>>> round(21.1234567,4)
21.1235

>>> round(21.1234567,5)
21.12346

>>> round(21.1234567,6)
21.123457

>>> round(21.012344556,6)
21.012345

>>> round(21.0123456789,6)
21.012346



>>> #=====================================================

>>> #    set()  method

>>> l=[1,2,3,4,5,6,7,8,7]

>>> s=set(l)

>>> s
{1, 2, 3, 4, 5, 6, 7, 8}

>>> len(l)==len(s)
False

>>> t=(1,2,3,4,4,5,6,6)

>>> s=set(t)

>>> s
{1, 2, 3, 4, 5, 6}


>>> d={1:'one',2:'two',3:'three',4:'four',5:'five'}

>>> s=set(d)

>>> s
{1, 2, 3, 4, 5}

>>> 

>>> s='hellow world'

>>> a=set(s)

>>> a

{'w', 'd', 'h', 'l', 'r', 'o', ' ', 'e'}
>>> #===============================================================

>>> #    setattr() method


>>> class gopi():
	print('hi')

	
hi

>>> gopi()
<__main__.gopi object at 0x00000268CB03E4C0>

>>> gopi
<class '__main__.gopi'>

>>> class myclass():
	def __init__(self,name):
		self.name=name
	def dis(self):
		print(self.name)

		
>>> s=myclass

>>> a=s

>>> d=a

>>> s=a('gopi')

>>> s.dis()
gopi

>>> s.name
'gopi'


>>> class student():
	name='gopiraj'
	age=21

	
>>> s=student()

>>> s.age
21

>>> s.name
'gopiraj'

>>> setattr(s,'name','sathish')

>>> s.name
'sathish'


>>> class student():
	name='gopiraj'
	age=21
	def dis(self):
		print(self.name,self.age)

		
>>> s=student()

>>> s.dis()
gopiraj 21

>>> setattr(s,'name','sathish kumar')

>>> s.dis()
sathish kumar 21


>>> class student():
	name=''
	age=""
	def dis(self):
		print(self.name,self.age)

		
>>> s=student()

>>> setattr(s,'name','sathish kumar')

>>> s.dis()
sathish kumar 

>>> s=student()

>>> s.dis()
 
>>> #===============================================================

>>> #    slice() method

>>> s='gopirajsathishkumar'

>>> s[slice(9)]
'gopirajsa'

>>> s[9]
't'

>>> s[7]
's'

>>> s[6]
'j'

>>> s[slice(6)]
'gopira'

>>> s='gopirajsathishkumar'

>>> len(s)
19

>>> s[0:18:2]
'gprjahskm'

>>> s[0:18:1]
'gopirajsathishkuma'

>>> s[slice(0,18,1)]
'gopirajsathishkuma'

>>> s[slice(0,18,2)]
'gprjahskm'

>>> s[0:18:2]
'gprjahskm'

>>>#=========================================================================================

>>>  # sorted()  method


>>> code = ('bb','cd', 'aa', 'zc')

>>> for s in code:
	print(len(s),end=' ')

	
2 2 2 2 

>>> for s in code:
	print(len(s)-1,end=' ')

	
1 1 1 1 

>>> for s in code:
	print(s[len(s)-1],end=' ')

	
b d a c 


>>> code=['ab','cd','ef','gh','ij']

>>> s=sorted(code)

>>> s
['ab', 'cd', 'ef', 'gh', 'ij']

>>> s=sorted(code,reverse=True)

>>> s
['ij', 'gh', 'ef', 'cd', 'ab']

>>> l=[1,2,3,4,5]

>>> s=sorted(l)

>>> s
[1, 2, 3, 4, 5]

>>> s=sorted(l,reverse=True)

>>> s
[5, 4, 3, 2, 1]

>>> s=sorted(l,reverse=False)

>>> s
[1, 2, 3, 4, 5]

>>> s='asdfghjkqwertyui'

>>> d=sorted(s)

>>> d
['a', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'q', 'r', 's', 't', 'u', 'w', 'y']

>>> d=sorted(s,reverse=True)

>>> d
['y', 'w', 'u', 't', 's', 'r', 'q', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'a']

>>> d={1:'one',2:'two',3:'three',4:'four'}

>>> a=sorted(d)

>>> a
[1, 2, 3, 4]

>>> a=sorted(d,reverse=True)

>>> a
[4, 3, 2, 1]
>>> #========================================================

>>> #  str()  method

>>> str(3)
'3'

>>> str(12.2)
'12.2'

>>> str('gopi')
'gopi'

>>> str(gopi)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    str(gopi)
NameError: name 'gopi' is not defined

>>> s=str()

>>> type(s)
<class 'str'>

>>> str(True)
'True'

>>> str(False)
'False'

>>> str(2+4j)
'(2+4j)'

>>> str(2+4J)
'(2+4j)'

>>> s=bytes('gopi')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s=bytes('gopi')
TypeError: string argument without an encoding


>>> s=bytes(4)

>>> s
b'\x00\x00\x00\x00'

>>> b = bytes('Hellö Wörld', encoding='utf-8')

>>> b
b'Hell\xc3\xb6 W\xc3\xb6rld'

>>> str(b)
"b'Hell\\xc3\\xb6 W\\xc3\\xb6rld'"


>>> #=================================================

>>> # sum() method

>>> l=[1,2,3,4]

>>> sum(l)
10

>>> sum(l,2)
12

>>> sum(l,1)
11

>>> sum(l,55)
65

>>> sum(l,100)
110

>>> l=[1,2,3,4.4,33.2]

>>> sum(l)
43.6


>>> l=[3+3j,3+7j]

>>> sum(l)

(6+10j)
>>> #==============================================

>>> l=[1,2,3,4,5,6]

>>> t=(1,2,3,4,5,6,7)

>>> s={1,2,3,4,5,6,7,8}

>>> d={1:'one',2:'two',3:'three',4:'four'}

>>> sum(l)
21

>>> sum(t)
28

>>> sum(s)
36

>>> sum(d)
10

>>> #====================================================


>>> #  tuple() method

>>> l=[1,2,3,4,6]

>>> tuple(l)
(1, 2, 3, 4, 6)

>>> t=tuple()

>>> type(t)
<class 'tuple'>

>>> t=(1,2,3,4,5,6)

>>> tuple(t)
(1, 2, 3, 4, 5, 6)

>>> s={1,2,3,4,5,5,7}

>>> tuple(s)
(1, 2, 3, 4, 5, 7)

>>> d={1:'one',2:'two',3:'three',4:'four'}

>>> tuple(d)
(1, 2, 3, 4)

>>> tuple(d.values)

Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    tuple(d.values)
TypeError: 'builtin_function_or_method' object is not iterable

>>> tuple(d.values())
('one', 'two', 'three', 'four')



>>> #==============================================================

>>>   #   type()   method

>>> s='string'

>>> type(s)
<class 'str'>


>>> l=[1,2,3,'gopi',False]

>>> type(l)
<class 'list'>

>>> t=(1,2,3.334,'gopi',)

>>> type(t)
<class 'tuple'>


>>> b=False

>>> type(b)
<class 'bool'>

>>> s=132

>>> type(s)

<class 'int'>
>>> f=1212.12333

>>> type(f)
<class 'float'>

>>> c=12+434J

>>> type(c)
<class 'complex'>


>>> #=========================================

>>> # super() method

>>> S="""

         **  super() method only usered in inheritens  **

         
       1.variable level
       
       2.constructor level

       3.method level

       """
>>> 


>>> class parent:
	name1='sanmugam'
	name2='parimal'
	def displey(self):
		print(self.name1,'  ',self.name2)

		
>>> class child(parent):
	name1='s.sathish kumar'
	name2='s.gopi raj'
	def pri(self):
		print(self.name1,'  ',self.name2)

		
>>> s=child()

>>> s.displey()
s.sathish kumar    s.gopi raj

>>> s.name1
's.sathish kumar'

>>> s.name2
's.gopi raj'

>>> s.pri()
s.sathish kumar    s.gopi raj


>>> #----------------

>>> class parent:
	name1='sanmugam'
	name2='parimal'
	def displey(self):
		print(self.name1,'  ',self.name2)

		
>>> class child(parent):
	name1='s.sathish kumar'
	name2='s.gopi raj'
	def pri(self):
		print(super().name1)
		print(super().name2)
		print(self.name1,'  ',self.name2)

		
>>> s=child()

>>> s.pri()
sanmugam
parimal
s.sathish kumar    s.gopi raj

>>> s.displey()
s.sathish kumar    s.gopi raj

>>> #---------------

>>> class parent:
	def __init__(self,name,age):
		print(name,age)

		
>>> s=parent('gopi',21)
gopi 21

		
>>> class parent:
	def __init__(self):
		print('im from parent class')

		
>>> class child(parent):
	name='sathish kumar'
	name2='gopi raj'
	def dis(self):
		print('im from child class')

		
>>> s=child()
im from parent class

>>> s.dis()
im from child class

>>> s.name
'sathish kumar'

>>> s.name2
'gopi raj'

>>> class parent:
	def __init__(self):
		print('im from parent class')

		
>>> class child(parent):
	name='sathish kumar'
	name2='gopi raj'
	def __init__(self):
		print('im from child class')

		
>>> s=child()
im from child class


>>> class parent:
	def __init__(self):
		print('im from parent class')



>>> class child(parent):
	name='sathish kumar'
	name2='gopi raj'
	def __init__(self):
		super().__init__()
		print('im from child class')

		
>>> s=child()
im from parent class
im from child class



>>> class parent:
	def __init__(self,name):
		print('im from parent class',name)

		
>>> class child(parent):
	def __init__(self):
		super().__init__('parent')
		print('im from child class')

		
>>> s=child()
im from parent class parent
im from child class




>>> class child(parent):
	def __init__(self,name):
		super().__init__('parent')
		print('im from child class',name)

		
>>> s=child('child')
im from parent class parent
im from child class child

>>> #----------------------------------------------------


	
>>> class parent:
	def __init__(self,name):
		self.name=name
		print('im from parent class',name)
	def dis(self):
		print("parent display",self.name)

		
>>> class child(parent):
	def __init__(self):
		print('im from child class')
	def dis(self):
		print('child class',super().name)

		
>>> s=child()
im from child class


>>> class child(parent):
	def __init__(self):
		print(super().__init__('parent'))
		print('im from child class')
	def dis(self):
		print('child class',super().name)

		
>>> s=child()
im from parent class parent
None
im from child class


>>> class parent:
	def __init__(self,name):
		self.name=name
		print('im from parent class',name)
	def dis(self):
		print("parent display")

		
>>> class child(parent):
	def __init__(self):
		print(super().__init__('parent'))
		print('im from child class')
	def dis(self):
		print('child class')
		print(super().dis())

		
>>> s=child()
im from parent class parent
None
im from child class

>>> s.dis()

child class
parent display
None



>>> #======================================================================
>>> #  vars()  method

>>> class myclass():
	name=''
	age=0
	def __init__(self):
		print('hellow python')

		
>>> s=myclass()
hellow python

>>> vars(s)
{}

>>> class myclass():
	def __init__(self):
		self.name=""
		self.age=0

		
>>> s=myclass()

>>> vars(s)
{'name': '', 'age': 0}

>>> s.age=21

>>> s.name='gopiraj'

>>> vars(s)
{'name': 'gopiraj', 'age': 21}

>>> s.__dict__
{'name': 'gopiraj', 'age': 21}

>>> str.__dir__
<method '__dir__' of 'object' objects>

>>> dict()
{}
>>> #=============================================

>>> # zip()  method

>>> l=[1,2,3,4]

>>> s=['one','two','three','four']

>>> a=zip(l,s)

>>> a
<zip object at 0x0000019AAD573EC0>

>>> a=list(zip(l,s))

>>> a
[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

>>> a=dict(zip(l,s))

>>> a
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}

>>> a=tuple(zip(l,s))

>>> a
((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'))

>>> a=set(zip(l,s))

>>> a
{(2, 'two'), (3, 'three'), (4, 'four'), (1, 'one')}

>>> a=set(sorted(zip(l,s)))

>>> a
{(2, 'two'), (3, 'three'), (4, 'four'), (1, 'one')}


>>> a=sorted(zip(l,s))

>>> for i in  a:
	i	
(1, 'one')
(2, 'two')
(3, 'three')
(4, 'four')

>>> l=[1,2,3,4]

>>> s=['one','two','three','four']

>>> s=('one','two','three','four')

>>> d=['I','II','III']

>>> a=zip(l,s,d)

>>> a
<zip object at 0x0000019AAD55E800>

>>> a=list(zip(l,s,d))

>>> a
[(1, 'one', 'I'), (2, 'two', 'II'), (3, 'three', 'III')]

>>> teams = ["India", "England", "NZ", "Aus"]

>>> captains = ["Kohli","Root","Williaamson", "Smith"]

>>> a=zip(teams,captains)

>>> a=list(zip(teams,captains))

>>> a
[('India', 'Kohli'), ('England', 'Root'), ('NZ', 'Williaamson'), ('Aus', 'Smith')]

>>> a=zip(teams,captains)

>>> while True:
	try:
		s=next(a)
		print(s[0],'-->',s[1])
	except StopIteration:
		break

	
India --> Kohli
England --> Root
NZ --> Williaamson
Aus --> Smith

>>> a=zip(teams,captains)

>>> next(a,'loop close')
('India', 'Kohli')

>>> next(a,'loop close')
('England', 'Root')

>>> a=zip(teams,captains)


>>> a=list(zip(teams,captains))

>>> len(a)
4

>>> a=list(zip(teams,captains))

>>> a
[('India', 'Kohli'), ('England', 'Root'), ('NZ', 'Williaamson'), ('Aus', 'Smith')]

>>> p='python'

>>> j='java'

>>> a='php'

>>> s=zip(p,j,a)

>>> s=list(zip(p,j,a))

>>> s
[('p', 'j', 'p'), ('y', 'a', 'h'), ('t', 'v', 'p')]

>>> import itertools

>>> p='python'

>>> j='java'

>>> a='php'

>>> s=list(itertools.zip_longest(p,j,a,fillvalue="empty"))

>>> s
[('p', 'j', 'p'), ('y', 'a', 'h'), ('t', 'v', 'p'), ('h', 'a', 'empty'), ('o', 'empty', 'empty'), ('n', 'empty', 'empty')]

>>> for i in s:
	print(i)	
('p', 'j', 'p')
('y', 'a', 'h')
('t', 'v', 'p')
('h', 'a', 'empty')
('o', 'empty', 'empty')
('n', 'empty', 'empty')

>>> s=list(itertools.zip_longest(p,j,a,fillvalue=" "))

>>> for i in s:
	print(i)
	
('p', 'j', 'p')
('y', 'a', 'h')
('t', 'v', 'p')
('h', 'a', ' ')
('o', ' ', ' ')
('n', ' ', ' ')

>>> s
[('p', 'j', 'p'), ('y', 'a', 'h'), ('t', 'v', 'p'), ('h', 'a', ' '), ('o', ' ', ' '), ('n', ' ', ' ')]


>>> for x,y,z in s:
	print(x,y,z)

	
p j p
y a h
t v p
h a  
o    
n    

>>> digits = [1,2,3,4,5]

>>> words = ['one', 'two', 'three', 'four','five']

>>> zipobj = zip(digits, words)

>>> for i in zipobj:
	i

	
(1, 'one')
(2, 'two')
(3, 'three')
(4, 'four')
(5, 'five')

>>> zipobj = zip(digits, words)

>>> obj = list(zip(digits, words))

>>> print(obj)
[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]



>>> zip(obj)

<zip object at 0x0000019AAAE75B80>

>>> x,y=zip(*obj)

>>> x
(1, 2, 3, 4, 5)

>>> y
('one', 'two', 'three', 'four', 'five')
