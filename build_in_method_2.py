Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #     chr() method

>>> chr(65)
'A'

>>> for  i in range(65,95):
	print(chr(i),end=' ')

	
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ 

>>> 


>>> 
>>> chr(-1)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    chr(-1)
ValueError: chr() arg not in range(0x110000)

>>> 0x110000
1114112

>>> hex(110000)
'0x1adb0'

>>> hex(0x110000)
'0x110000'

>>> 1114112
1114112

>>> help(chr)
Help on built-in function chr in module builtins:

chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

>>> #------------------------------------------------------------------

>>> # complex() mehtod

>>> complex()
0j

>>> complex(1,3)
(1+3j)

>>> complex(2,5)
(2+5j)

>>> complex(,3)
SyntaxError: invalid syntax

>>> complex(0,3)
3j

>>> complex(0,-3)
-3j

>>> complex('0-3j')
-3j

>>> complex("0-3j")
-3j

>>> complex("-3j")
-3j

>>> complex("-j")
-1j

>>> complex("j")
1j

>>> #---------------------------------------------------

>>> # delattr() method

>>> class myclass():
	name="gopi"
	age=21
	def myname(self):
		print(self.name)
	def myage(self):
		print(self.age)

		
>>> s=myclass()

>>> s.age
21

>>> s.name
'gopi'

>>> s.myage()
21

>>> s.myname()
gopi

>>> delattr(myclass,"age")


		
>>> class myclass():
	name="gopi"
	age=21
	def myname(self):
		print(self.name)
	def myage(self):
		print(self.age)


>>> s=myclass()

>>> s.age
21

>>> class myclass():
	name="gopi"
	age=21
	def myname(self):
		print(self.name)
	def myage(self):
		print(self.age)

		
>>> delattr(myclass,'age')

>>> delattr(myclass,'name')

>>> dir(myclass)
['__class__', '__delattr__', '__dict__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
 '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
 '__weakref__', 'myage', 'myname']


>>> s.age

21
>>> s.name
'gopi'
>>> class myclass():
	name="gopi"
	age=21
	def myname(self):
		print(self.name)
	def myage(self):
		print(self.age)

		
>>> d=myclass()

>>> d.age
21

>>> d.name
'gopi'

>>> d.myage()
21

>>> d.myname
<bound method myclass.myname of <__main__.myclass object at 0x0000023C95D5D4C0>>

>>> d.myname()
gopi

>>> delattr(myclass,'name')

>>> delattr(myclass,'name')

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    delattr(myclass,'name')
AttributeError: name
>>> delattr(myclass,'age')

>>> d.myage()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    d.myage()
  File "<pyshell#81>", line 7, in myage
    print(self.age)
AttributeError: 'myclass' object has no attribute 'age'
>>> #-------------------------------------------------------------


>>> # dict() method

>>> d=dict()

>>> s=set()

>>> type(s)
<class 'set'>

>>> type(d)
<class 'dict'>

>>> d=dict

>>> d(name='gopi')

{'name': 'gopi'}

>>> s=d(name='gopi')

>>> s
{'name': 'gopi'}

>>> s=d(age=21)

>>> s
{'age': 21}

>>> f=dict()

>>> type(f)
<class 'dict'>

>>> d={}

>>> d={'name':'age'}

>>> d
{'name': 'age'}

>>> d={name:'age'}
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d={name:'age'}
NameError: name 'name' is not defined

>>> x=[('name','gopi')('age','21')('city','salem')]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x=[('name','gopi')('age','21')('city','salem')]
TypeError: 'tuple' object is not callable

>>> x=[('name','gopi'),('age','21'),('city','salem')]

>>> 

>>> d=dict(x)

>>> d
{'name': 'gopi', 'age': '21', 'city': 'salem'}

>>> y=[{'name','gopi'},{'age','21'},{'city','salem'}]

>>> s=dict(y)

>>> s
{'gopi': 'name', 'age': '21', 'salem': 'city'}
>>> z={(1,'one')(2,'two')(3,'three')}
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    z={(1,'one')(2,'two')(3,'three')}
TypeError: 'tuple' object is not callable

>>> z={(1,'one'),(2,'two'),(3,'three')}

>>> a=dict(z)

>>> a
{2: 'two', 3: 'three', 1: 'one'}

>>> #---------------------------------------------------------------------------

>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'd', 'f', 's', 'x', 'y', 'z']

>>> __doc__

>>> dir(__doc__)
['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> s=1

>>> s.as_integer_ratio()
(1, 1)

>>> s=12

>>> s.as_integer_ratio()
(12, 1)

>>> dir(s.as_integer_ratio)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']

>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


>>> def fuction(name):

	print(name)

	
>>> fuction('gopi')
gopi

>>> dir(fuction)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

>>> fuction.__name__
'fuction'

>>> fuction.__call__()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    fuction.__call__()
TypeError: fuction() missing 1 required positional argument: 'name'


>>> fuction.__call__
<method-wrapper '__call__' of function object at 0x0000024AAF6C55E0>

>>> class myclass:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print(self.name)
		print(self.age)

		
>>> myclass('gopi',21)
<__main__.myclass object at 0x0000024AAF6BE460>

>>> s=myclass('gopi',21)

>>> s.display()
gopi
21

>>> s.age
21

>>> s.name
'gopi'

>>> dir(myclass)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', 'display']

>>> dir(s)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', '__weakref__', 'age', 'display', 'name']


>>> #--------------------------------------------------------------------
>>> # divmod() method

>>> 12 % 3
0

>>> 12 % 2
0

>>> 12 / 2
6.0

>>> divmod(12,2)
(6, 0)

>>> divmod(12,3)
(4, 0)

>>> divmod(12,5)
(2, 2)

>>> help(divmod)
Help on built-in function divmod in module builtins:

divmod(x, y, /)
    Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.


>>> divmod(12.3,3)
(4.0, 0.3000000000000007)

>>> 12.3 // 3
4.0

>>> 12.3 % 3
0.3000000000000007

>>> divmod(2+2j,3+2j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    divmod(2+2j,3+2j)
TypeError: can't take floor or mod of complex number.


>>> #----------------------------------------------------------------------

>>> #              enumerate() method

>>> l=['gopi','sathish','kumar','raj','gopal','gowri']

>>> s=enumerate(l)

>>> print(s)
<enumerate object at 0x0000023010FD40C0>


>>> for i in s:
	print(i)

	
(0, 'gopi')
(1, 'sathish')
(2, 'kumar')
(3, 'raj')
(4, 'gopal')
(5, 'gowri')


>>> list(s)
[]


>>> list(s)
[]

>>> s
<enumerate object at 0x0000023010FD40C0>


>>> a=list(s)


>>> a
[]


>>> l1 = ["eat","sleep","repeat"]


>>> print (list(enumerate(l1)))
[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

>>> print (enumerate(l1))
<enumerate object at 0x000002300F018FC0>

>>> s=enumerate(l1)

>>> list(s)
[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

>>> for i in s:
	i

	
>>> s
<enumerate object at 0x00000230110D2C00>

>>> s.__next__()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s.__next__()
StopIteration

>>> s.__next__
<method-wrapper '__next__' of enumerate object at 0x00000230110D2C00>



>>> l=['gopi','sathish','kumar','raj','gopal','gowri']

>>> enumerate(iterable=l)
<enumerate object at 0x000002301118C180>

>>> list(enumerate(iterable=l))
[(0, 'gopi'), (1, 'sathish'), (2, 'kumar'), (3, 'raj'), (4, 'gopal'), (5, 'gowri')]

>>> for i in list(enumerate(iterable=l)):
	i

	
(0, 'gopi')
(1, 'sathish')
(2, 'kumar')
(3, 'raj')
(4, 'gopal')
(5, 'gowri')


>>> for i in list(enumerate(iterable=l)):
	i

	
(0, 'gopi')
(1, 'sathish')
(2, 'kumar')
(3, 'raj')
(4, 'gopal')
(5, 'gowri')


>>> d=list(enumerate(iterable=l))


>>> d
[(0, 'gopi'), (1, 'sathish'), (2, 'kumar'), (3, 'raj'), (4, 'gopal'), (5, 'gowri')]

>>> d
[(0, 'gopi'), (1, 'sathish'), (2, 'kumar'), (3, 'raj'), (4, 'gopal'), (5, 'gowri')]

>>> d
[(0, 'gopi'), (1, 'sathish'), (2, 'kumar'), (3, 'raj'), (4, 'gopal'), (5, 'gowri')]

>>> for i in d:
	i

	
(0, 'gopi')
(1, 'sathish')
(2, 'kumar')
(3, 'raj')
(4, 'gopal')
(5, 'gowri')


>>> for i in d:
	i

	
(0, 'gopi')
(1, 'sathish')
(2, 'kumar')
(3, 'raj')
(4, 'gopal')
(5, 'gowri')


>>> l
['gopi', 'sathish', 'kumar', 'raj', 'gopal', 'gowri']


>>> list(enumerate(l,3))
[(3, 'gopi'), (4, 'sathish'), (5, 'kumar'), (6, 'raj'), (7, 'gopal'), (8, 'gowri')]

>>> for i  in list(enumerate(l,3)):
	i

	
(3, 'gopi')
(4, 'sathish')
(5, 'kumar')
(6, 'raj')
(7, 'gopal')
(8, 'gowri')


>>> l
['gopi', 'sathish', 'kumar', 'raj', 'gopal', 'gowri']


>>> s=enumerate(l)

>>> s.__next__()
(0, 'gopi')

>>> s.__next__()
(1, 'sathish')

>>> s.__next__()
(2, 'kumar')

>>> s.__next__()
(3, 'raj')

>>> s.__next__()
(4, 'gopal')

>>> s
<enumerate object at 0x00000230111698C0>

>>> list(s)
[(5, 'gowri')]

>>> s
<enumerate object at 0x00000230111698C0>

>>> for i in s:
	i

	
>>> (4, 'gopal')
(4, 'gopal')


>>> # enumerate()  method

>>> l=['gopi','raj','sathish','kumar']

>>> enumerate(l)
<enumerate object at 0x00000226A7C12380>

>>> for i in enumerate(l):
	i

	
(0, 'gopi')
(1, 'raj')
(2, 'sathish')
(3, 'kumar')

>>> for i in enumerate(l):
	i

	
(0, 'gopi')
(1, 'raj')
(2, 'sathish')
(3, 'kumar')
>>> for i in enumerate(l):
	i

	
(0, 'gopi')
(1, 'raj')
(2, 'sathish')
(3, 'kumar')

>>> s=list(enumerate(l))

>>> s
[(0, 'gopi'), (1, 'raj'), (2, 'sathish'), (3, 'kumar')]

>>> s
[(0, 'gopi'), (1, 'raj'), (2, 'sathish'), (3, 'kumar')]

>>> for i in  s:
	print(i)

	
(0, 'gopi')
(1, 'raj')
(2, 'sathish')
(3, 'kumar')

>>> d=list(enumerate(l,5))

>>> d
[(5, 'gopi'), (6, 'raj'), (7, 'sathish'), (8, 'kumar')]

>>> for i in d:
	i

	
(5, 'gopi')
(6, 'raj')
(7, 'sathish')
(8, 'kumar')

>>> for i,j in d:
	print(i)
	print(j)

	
5
gopi
6
raj
7
sathish
8
kumar

>>> for index,name in d:
	print(index,name)

	
5 gopi
6 raj
7 sathish
8 kumar

>>> s='GOPIRAJ'

>>> d=enumerate(s,4)

>>> for i in d:
	i

	
(4, 'G')
(5, 'O')
(6, 'P')
(7, 'I')
(8, 'R')
(9, 'A')
(10, 'J')

>>> print(list(d))
[]

>>> for i in d:
	i

	
>>> for i in enumerate(s):
	i

	
(0, 'G')
(1, 'O')
(2, 'P')
(3, 'I')
(4, 'R')
(5, 'A')
(6, 'J')

>>> l
['gopi', 'raj', 'sathish', 'kumar']

>>> s=enumerate(l)

>>> l=list(s)

>>> l
[(0, 'gopi'), (1, 'raj'), (2, 'sathish'), (3, 'kumar')]

>>> l=['gopi','raj','sathish','kumar']

>>> s=enumerate(l)

>>> s
<enumerate object at 0x00000226A9DC88C0>

>>> for i in s:
	i

	
(0, 'gopi')
(1, 'raj')
(2, 'sathish')
(3, 'kumar')

>>> for i in s:
	i

	

	
>>> s=list(enumerate(l))

>>> for i in s:
	i

	
(0, 'gopi')
(1, 'raj')
(2, 'sathish')
(3, 'kumar')
>>> for i in s:
	i

	
(0, 'gopi')
(1, 'raj')
(2, 'sathish')
(3, 'kumar')
>>> l=list(s)

>>> l
[(0, 'gopi'), (1, 'raj'), (2, 'sathish'), (3, 'kumar')]

>>> l=['gopi','raj','sathish','kumar']

>>> s=enumerate(l)

>>> s
<enumerate object at 0x00000226A9DC88C0>

>>> for i in s:
	i


(0, 'gopi')
(1, 'raj')
(2, 'sathish')
(3, 'kumar')



>>> s=list(enumerate(l))

>>> for i in s:
	i


(0, 'gopi')
(1, 'raj')
(2, 'sathish')
(3, 'kumar')
>>> l=list(s)

>>> l
[(0, 'gopi'), (1, 'raj'), (2, 'sathish'), (3, 'kumar')]

>>> l=['gopi','raj','sathish','kumar']

>>> s=enumerate(l)
>>> s
<enumerate object at 0x00000226A9DC88C0>

>>> for i in s:
	i


(0, 'gopi')
(1, 'raj')
(2, 'sathish')
(3, 'kumar')

>>> for j in s:
	j

>>> s=list(enumerate(l))

>>> for i in s:
	i


(0, 'gopi')
(1, 'raj')
(2, 'sathish')
(3, 'kumar')

>>> dir(enumerate)
['__class__', '__class_getitem__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
 '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__']


>>> l
['gopi', 'raj', 'sathish', 'kumar']

>>> d=enumerate(l)

>>> d.__next__()
(0, 'gopi')

>>> d.__next__()
(1, 'raj')

>>> d.__next__()
(2, 'sathish')

>>> d.__next__()
(3, 'kumar')

>>> d.__next__()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    d.__next__()
StopIteration

>>> d=enumerate(l)

>>> d.__next__()
(0, 'gopi')

>>> d.__next__(3)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    d.__next__(3)
TypeError: expected 0 arguments, got 1


