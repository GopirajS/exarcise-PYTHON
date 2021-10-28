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
