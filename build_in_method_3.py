>>>#================================================================

>>> hex(12)
'0xc'

>>> hex(120)
'0x78'

>>> oct(78)
'0o116'

>>> oct(1120)
'0o2140'

>>> oct(120)
'0o170'

>>> bin(2)
'0b10'

>>> hex(12)
'0xc'
>>> float.hex(12.1)
'0x1.8333333333333p+3'

>>> hex(123)
'0x7b'

>>> number=123

>>> print("Hexadecimal form of " + str(number) +
       " is " + hex(number).lstrip("0x").rstrip("L"))
Hexadecimal form of 123 is 7b

>>> print("Hexadecimal form of " + str(number) +
       " is " + hex(number).lstrip("0x"))
Hexadecimal form of 123 is 7b

>>> #=========================================================


>>> #  hasattr()  method

>>> str='this is string'

>>> hasattr(str,"zfill")
True

>>> hasattr(str,"strip")
True

>>> hasattr(str,"strim")
False

>>> class myclass():
	name='gopiraj'
	age=21

	
>>> myobj=myclass()

>>> hasattr(myobj,'name')
True

>>> hasattr(myobj,'age')
True

>>> hasattr(myobj,'__namea__')
False

>>> hasattr(myobj,'__name__')
False

>>> #===============================================================

>>> #   id()  method

>>> n=12

>>> id(12)

1785191164560

>>> id(n)
1785191164560

>>> 21
21

>>> id(21)
1785191164848

>>> s=12

>>> id(s)
1785191164560

>>> id(n)
1785191164560

>>> l=[1,2,3,4,5]

>>> id(l)
1785233509696

>>> s=(1,2,3,4,5)

>>> id(s)
1785232703712

>>> a=[1,2,3,4,5]

>>> id(a)
1785233514624

>>> id(l)
1785233509696

>>> class myclass:
	name='gopiraj'
	age=21

	
>>> s=myclass()

>>> id(s)
1785232672848

>>> s2=myclass()

>>> id(s)
1785232672848

>>> s3=myclass()

>>> id(s3)
1785233322384

>>> id(s)==id(s)
True

>>> id(s)==id(s)==id(s3)
False

>>> s=myclass()

>>> s1=myclass()

>>> id(s)==id(s1)
False

>>> id(s)
1785233325408

>>> id(s1)
1785232672848

>>> id(s)
1785233325408

>>> id(s)
1785233325408

>>> id(s2)
1785233632704

>>> s=myclass()


>>> id(s)
1785233325744

>>> s.name='sathish kumar'

>>> id(s)
1785233325744

>>> id(s.name)
1785233463024

>>> s=myclass()

>>> id(s.name)
1785233447856

>>> id(s.name)
1785233447856


>>> s.name='kumar'

>>> id(s.name)
1785233459760


>>> #==================================================================

>>> #  int()  method

>>> oct(123)
'0o173'

>>> int('173',8)
123

>>> int('173')
173

>>> int(0o173)
123

>>> bin(123)
'0b1111011'

>>> int('0b1111011',2)
123

>>> int('0b1111011',2)
123

>>> hex(123)
'0x7b'

>>> int('7b',16)
123

>>> int('0x7b',16)
123


>>> int(123)
123

>>> x=12

>>> int([x])

>>> i=int(12.3)

>>> i
12

>>> i=int('12')

>>> i
12

>>> i
12

>>> bin(123)
'0b1111011'

>>> int('0b1111011')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int('0b1111011')
ValueError: invalid literal for int() with base 10: '0b1111011'

>>> int('0b1111011',2)
123

>>> int(0b1111011)
123

>>> oct(123)
'0o173'

>>> int('0o173',8)
123

>>> int(0o173)
123

>>> hex(123)
'0x7b'

>>> int('0x7b',16)
123

>>>#=============================================================

>>> #  input() method of python

>>> user_imput=input()
How are you ?

>>> user_imput
'How are you ?'

>>> user=input("enter a input :")
enter a input : gopiraj sathish kumar

>>> user
' gopiraj sathish kumar'


>>> age=input("Enter a age :")
Enter a age :21

>>> age
'21'

>>> int(age)
21


>>> #=======================================================


>>> #    isinstance()  method

>>> s='gopiraj sathish kumar'

>>> isinstance(s,(str,int))
True

>>> isinstance(s,(int))
False

>>> isinstance(s,(str))
True

>>> n=12

>>> isinstance(n,int)
True

>>> isinstance(n,float)
False


>>> isinstance(n,(float,class))
SyntaxError: invalid syntax

>>> isinstance(n,(float,class))
SyntaxError: invalid syntax

>>> isinstance(n,(float,int))
True

>>> class myclass():
	name='gopi'
	age=21

	
>>> obj=myclass()

>>> isinstance(obj,myclass)
True


>>> isinstance(obj.name,myclass)
False

>>> obj.name
'gopi'

>>> s=['gopi','raj','sathish','kumar']

>>> isinstance(s,list)
True

>>> isinstance(s,(list,tuple,str))
True

>>> isinstance(s,(tuple,str))
False

>>> isinstance(s,(tuple))
False

>>> isinstance(s,(list))
True

>>> isinstance(s,(myclass))
False
>>> #===========================================================

>>> # issubclass() methhod

>>> issubclass(int,int)
True

>>> issubclass(bool,int)
True

>>> issubclass(bool,float)
False

>>> issubclass(bool,(int,float,))
True

>>> import collections

>>> import collections as s

>>> issubclass(s.OrderedDict,dict)
True
>>> #---------------------------------------------------

>>> class mainclass():
	def __init__(self,name):
		self.name=name
		print('hellow',self.name)

		
>>> class subclass(mainclass):
	def __init__(self,age):
		self.age=age
		print('his age is',self.age)

		
>>> s=mainclass('gopi')
hellow gopi

>>> a=subclass(21)
his age is 21

>>> class subclass(mainclass):
	def __init__(self,age):
		self.age=age
		print(self.name,'his age is',self.age)

		
>>> s=mainclass('gopi')
hellow gopi

>>> issubclass(mainclass,subclass)
False
>>> #===========================================================

>>> # iter() method

>>> s='gopiraj'

>>> a=iter(s)

>>> a
<str_iterator object at 0x000001F6A61EECA0>

>>> for i in a:
	i

	
'g'
'o'
'p'
'i'
'r'
'a'
'j'

>>> for i in a:
	i

	
>>> a=list(iter(s))

>>> for i in a:
	i

	
'g'
'o'
'p'
'i'
'r'
'a'
'j'

>>> class Test:
 
    # Constructor
    def __init__(self, limit):
        self.limit = limit
 
    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self
 
    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
 
        # Store current value ofx
        x = self.x
 
        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration
 
        # Else increment and return old value
        self.x = x + 1;
        return x

>>>  
# Prints numbers from 10 to 15
for i in Test(15):
    print(i)

    
10
11
12
13
14
15

>>>  
# Prints nothing
for i in Test(5):
    print(i)

    
>>> class Test:

    def __init__(self, limit):
        self.limit = limit
    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x

        if x > self.limit:
            raise StopIteration
        self.x = x + 1;
        return x

>>> s=Test(20)

>>> s
<__main__.Test object at 0x000001F6A61EEEE0>


>>> for i in s:
	i
	
10
11
12
13
14
15
16
17
18
19
20

>>> s
<__main__.Test object at 0x000001F6A61EEEE0>

>>> for i in s:
	i

	
10
11
12
13
14
15
16
17
18
19
20

>>> for i in s:
	i
	
10
11
12
13
14
15
16
17
18
19
20

>>> Test(15)
<__main__.Test object at 0x000001F6A6224610>

>>> for i in Test(15):
	print(i,end=' ')	
10 11 12 13 14 15 

>>> l=[1,2,3,4,5,6]

>>> #==========================================================

>>> #    len() method

>>> help(len)
Help on built-in function len in module builtins:


len(obj, /)
    Return the number of items in a container.


>>> l=[1,2,3,'True','False']

>>> len(l)
5

>>> d=(1,2,3,4,5,6)

>>> len(d)
6

>>> s={1,2,3,4,5,6}

>>> len(s)
6

>>> d={1:'one',2:'two',3:'three'}

>>> len(d)
3

>>> len(True)
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    len(True)
TypeError: object of type 'bool' has no len()

>>> len(11)
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    len(11)
TypeError: object of type 'int' has no len()


>>> len("gopiraj")
7

>>> #================================================



>>>              #  list()  method

>>> s='gopiraj sathish kumar rajesh'

>>> list(s)
['g', 'o', 'p', 'i', 'r', 'a', 'j', ' ', 's', 'a', 't', 'h', 'i', 's', 'h', ' ', 'k', 'u', 'm', 'a', 'r', ' ', 'r', 'a', 'j', 'e', 's', 'h']

>>> tuple(s)
('g', 'o', 'p', 'i', 'r', 'a', 'j', ' ', 's', 'a', 't', 'h', 'i', 's', 'h', ' ', 'k', 'u', 'm', 'a', 'r', ' ', 'r', 'a', 'j', 'e', 's', 'h')

>>> l=[]

>>> for i in s:
	l.append(i)

	
>>> l
['g', 'o', 'p', 'i', 'r', 'a', 'j', ' ', 's', 'a', 't', 'h', 'i', 's', 'h', ' ', 'k', 'u', 'm', 'a', 'r', ' ', 'r', 'a', 'j', 'e', 's', 'h']

>>> s.split()
['gopiraj', 'sathish', 'kumar', 'rajesh']

>>> list({'gopi','sathish','raj','arun','aravinth'})
['raj', 'sathish', 'aravinth', 'arun', 'gopi']

>>> list({1:'one',2:'two',3:'three'})
[1, 2, 3]

>>> list(12345)
Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    list(12345)
TypeError: 'int' object is not iterable

>>> l=[1122]

>>> type(l)
<class 'list'>

>>> #================================================================


>>> #         map() method

>>> l=[1,2,3,4,5,6,7]

>>> map(lambda x:x*x,l)
<map object at 0x000001F6A6224D60>

>>> s=map(lambda x:x*x,l)

>>> s
<map object at 0x000001F6A6224EE0>

>>> for i in s:
	i

	
1
4
9
16
25
36
49

>>> for i in s:
	i

	
>>> bin(2)
'0b10'

>>> l=[1,2,3,4,5,6,7]

>>> pow(2,3)
8

>>> list(map(bin,l))
['0b1', '0b10', '0b11', '0b100', '0b101', '0b110', '0b111']


>>> #============================================================

>>>                #   max() method


>>> n=[1,2,3,4,5,6,7,8,22,6,7,9]

>>> max(n)
22

>>> l=['gopi','raj','sathish','kumar']

>>> max(l)
'sathish'

>>> d=['abc','def','ghi','jkl']

>>> max(d)
'jkl'

>>> d=['abc','def','jkl','ghi']

>>> max(d)
'jkl'

>>> d=['abc','def','jkl','ghi']

>>> max(d,key=len)
'abc'

>>> cities = ['Mumbai','New York','Paris','London']

>>> max(cities,key=len)
'New York'

>>> cities = ['a','ab','abc','abcd','ABC','ABCD','A']

>>> max(cities,key=len)
'abcd'

>>> cities = ['a','ab','abc','ABC','ABCD','A']

>>> max(cities,key=len)
'ABCD'

>>> cities = ['Mumbai','New York','Paris','London']

>>> favcities = ['Pune', 'New York', 'Johannesburg']

>>> max(cities,key=len)
'New York'

>>> max(favcities,key=len)
'Johannesburg'

>>> max(cities,favcities ,key=len)
['Mumbai', 'New York', 'Paris', 'London']

>>> max(favcities,cities ,key=len)
['Mumbai', 'New York', 'Paris', 'London']

>>> l=[1,2,3,4,5,6,7,8]

>>> max(l)
8
>>> t=(11,4,35,66,44,99,2334,2)

>>> max(t)
2334

>>> d={'a':97,'b':98,'c':99,'d':100}

>>> max(d)
'd'


>>> max(d.values())
100

>>> l=['a','b','c','d','e','A','B','C','D','E','F']

>>> max(l)
'e'

>>> min(l)
'A'

>>> l=['aaaa','bbb','cc','dd','e']

>>> max(l)
'e'
>>> l=['aaaae','bbb','cc','dd','e']

>>> max(l)
'e'

>>> l=['faaaae','bbb','cc','dd','e']

>>> max(l)
'faaaae'
   
>>> l=['faaaae','bbb','cc','dd','e','h']

>>> max(l)
'h'

>>> max(l,key=len)
'faaaae'



>>> #====================================================


>>> #  next() method

>>> l=[1,2,3,4,5,6]

>>> s=iter(l)

>>> next(s)
1

>>> next(s)
2

>>> next(s)
3

>>> next(s)
4

>>> next(s)
5

>>> next(s)
6

>>> next(s)
Traceback (most recent call last):
  File "<pyshell#339>", line 1, in <module>
    next(s)
StopIteration

>>> s=iter(l)

>>> next(s,'iterator is complet')

1
>>> next(s,'iterator is complet')
2

>>> next(s,'iterator is complet')
3

>>> next(s,'iterator is complet')
4

>>> next(s,'iterator is complet')
5

>>> next(s,'iterator is complet')
6

>>> next(s,'iterator is complet')
'iterator is complet'

>>> next(s,'iterator is complet')
'iterator is complet'

>>> s=iter(l)

>>> s.__next__()
1

>>> s.__next__()
2

>>> s.__next__()
3

>>> s.__next__()
4

>>> s.__next__()
5

>>> s.__next__()
6

>>> s.__next__()
Traceback (most recent call last):
  File "<pyshell#358>", line 1, in <module>
    s.__next__()
StopIteration

>>> #==========================================================
>>> #     object()   method

>>> obj=object()

>>> type(obj)

<class 'object'>

>>> dir(obj)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']





>>> obj=object()

>>> obj='gopi'

>>> obj
'gopi'

>>> obj=object()

>>> print(obj.__doc__)

The base class of the class hierarchy.

When called, it accepts no arguments and returns a new featureless
instance that has no instance attributes and cannot be given any.

>>> obj=object()

>>> obj
<object object at 0x000002A25EA24030>
>>> #==================================================================

>>> #                 oct() method

>>> oct(123)
'0o173'

>>> 0o173
123

>>> bin(123)
'0b1111011'

>>> oct(0b1111011)
'0o173'

>>> oct('0b1111011')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    oct('0b1111011')
TypeError: 'str' object cannot be interpreted as an integer

>>> class Student:
    age = 15

    def __index__(self):
        return self.age



>>> s=Student()

>>> oct(s)
'0o17'

>>> oct(15)
'0o17'


>>> class Student:

    def __index__(self):
        return self.age

>>> s=Student()

>>> oct(s)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    oct(s)
  File "<pyshell#56>", line 4, in __index__
    return self.age
AttributeError: 'Student' object has no attribute 'age'
>>> #================================================

>>> #               ord()   method

>>> ord('A')
65

>>> chr(65)
'A'

>>> ord('B')
66

>>> ord('C')
67

>>> ord('d')
100

>>> ord('#')
35

>>> ord(' ')
32

>>> ord('%')
37
>>> ord('த')
2980

>>> ord('include')
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    ord('include')
TypeError: ord() expected a character, but string of length 7 found


>>> #=============================================================

>>>                 #   pow()  method

>>> pow(2,2)
4

>>> pow(2,3)
8

>>> pow(2,4)
16

>>> pow(2,5)
32

>>> pow(2,5) #2 x 2 x 2 x 2 x 2
32

>>> pow(2,5,2)
0

>>> 10%2
0

>>> 10%3
1

>>> 10//2
5

>>> 2*2
4

>>> 4%2
0

>>> pow(2,5,3)
2

>>> pow(2,5)
32

>>> pow(2,5,3)
2

>>> pow(2,6)
64

>>> pow(2,6,4)
0

>>> pow(2,6,5)
4

>>> 2**3
8

>>> pow(2,3)
8

>>> 2**5
32

>>> pow(2,5)
32

>>> 2**8
256

>>> pow(2,8)
256



>>> #====================================================
>>> #   print()  method

>>> print('learn python ')
learn python 

>>> s='imy name is gopi'

>>> a='and im learn python'

>>> print(s,a)
imy name is gopi and im learn python

>>> print(s, a)
imy name is gopi and im learn python

>>> print(s,sep='  ', a)
SyntaxError: positional argument follows keyword argument

>>> print(s, a ,sep='  ')
imy name is gopi  and im learn python

>>> print(s, a ,sep=' * ')
imy name is gopi * and im learn python

>>> print(s, a ,sep=' * ','hi hellow worls')
SyntaxError: positional argument follows keyword argument

>>> print(s, a ,sep=' * ','hi hellow worls',sep='  ')
SyntaxError: positional argument follows keyword argument

>>> print(s,a,sep='--',end='  ')
imy name is gopi--and im learn python  

>>> print(s,a,sep='--',end='  '); print('hellow python')
imy name is gopi--and im learn python  hellow python

>>> print(s,a,sep='--',end='  \n'); print('hellow python')
imy name is gopi--and im learn python  
hellow python

>>> print(s,a,sep='--',end='  \t'); print('hellow python')
imy name is gopi--and im learn python  	hellow python

>>> print(s,a,sep='--',end='......'); print('hellow python')
imy name is gopi--and im learn python......hellow python


>>> a='gopiraj'

>>> b='sathish'

>>> c='kumar'

>>> d='gopal'

>>> e='gowri'

>>> print(a,b,c,d,e)
gopiraj sathish kumar gopal gowri

>>> print(a,',',b,',',c,',',d,',',e)
gopiraj , sathish , kumar , gopal , gowri

>>> print(a,b,c,d,e,sep=',')
gopiraj,sathish,kumar,gopal,gowri

>>> print(a,b,c,d,e,sep=' , ')
gopiraj , sathish , kumar , gopal , gowri

>>> print(a,b,c,d,e,sep=':')
gopiraj:sathish:kumar:gopal:gowri

>>> print(a,b,c,d,e,sep=' : ')
gopiraj : sathish : kumar : gopal : gowri

>>> print(a,b,c,d,e,sep='___')
gopiraj___sathish___kumar___gopal___gowri

>>> print(a,b,c,d,e,sep='&&&')
gopiraj&&&sathish&&&kumar&&&gopal&&&gowri

>>> print(a,b,c,d,e,sep='  &&&  ')
gopiraj  &&&  sathish  &&&  kumar  &&&  gopal  &&&  gowri

>>> print(a,b,c,d,e,sep='<--->')
gopiraj<--->sathish<--->kumar<--->gopal<--->gowri

>>> print(a,b,c,d,e,sep=' , ',end='');print('hi')
gopiraj , sathish , kumar , gopal , gowrihi

>>> print(a,b,c,d,e,sep=' , ',end='');print('hi')
gopiraj , sathish , kumar , gopal , gowrihi

>>> print(a,b,c,d,e,sep=' , ',end=''); print('hi')
gopiraj , sathish , kumar , gopal , gowrihi

>>> print(a,b,c,d,e,sep=' , ',end=''); print('hi hellow ')
gopiraj , sathish , kumar , gopal , gowrihi hellow 

>>> print(a,b,c,d,e,sep=' , ',end=' '); print('hi hellow ')
gopiraj , sathish , kumar , gopal , gowri hi hellow 

>>> print(a,b,c,d,e,sep=' , ',end=' '); print(', hi hellow ')
gopiraj , sathish , kumar , gopal , gowri , hi hellow 

>>> print(a,b,c,d,e,sep=' , ',end=' /n '); print(' hi hellow ')
gopiraj , sathish , kumar , gopal , gowri /n  hi hellow 

>>> print(a,b,c,d,e,sep=' , ',end=' \n '); print(' hi hellow ')
gopiraj , sathish , kumar , gopal , gowri 
  hi hellow 

>>> print(a,b,c,d,e,sep=' , ',end=' \n '); print('hi hellow ')
gopiraj , sathish , kumar , gopal , gowri 
 hi hellow 

>>> print(a,b,c,d,e,sep=' , ',end=' \n ');print('hi hellow ')
gopiraj , sathish , kumar , gopal , gowri 
 hi hellow 

>>> print(a,b,c,d,e,sep=' , ',end='\n');print('hi hellow ')
gopiraj , sathish , kumar , gopal , gowri
hi hellow 


>>> #=================================================================

>>> #   range() method


>>> dir(range)
['__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index', 'start', 'step', 'stop']

>>> type(range)
<class 'type'>


>>> range(12)
range(0, 12)

>>> for i in range(12):
	print(i,end=' ')
	
0 1 2 3 4 5 6 7 8 9 10 11 

>>> l=[range(12)]

>>> l
[range(0, 12)]

>>> l=[list(range(12))]

>>> l
[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]

>>> t=(tuple(range(12)))

>>> t
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

>>> s=set(range(12))

>>> s
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

>>> for i in range(12):
	print(i,end=' ')

	
0 1 2 3 4 5 6 7 8 9 10 11 

>>> #===========================================================================

>>> #   repr()   method

>>> help(repr)
Help on built-in function repr in module builtins:

repr(obj, /)
    Return the canonical string representation of the object.
    
    For many object types, including most builtins, eval(repr(obj)) == obj.

>>> repr(10)
'10'

>>> repr('gopi')
"'gopi'"

>>> str('gopi')
'gopi'

>>> repr(str)
"<class 'str'>"

>>> repr(12.2)
'12.2'

>>> repr(True)
'True'
>>> repr(None)
'None'

>>> repr(False)
'False'

>>> class myclass():
	n=''
	
>>> s=myclass()

>>> repr(s)
'<__main__.myclass object at 0x000001F1E97EE730>'

>>> str(s)
'<__main__.myclass object at 0x000001F1E97EE730>'

>>> class myclass():
	n='gopi'
	
>>> s=myclass()

>>> str(s)
'<__main__.myclass object at 0x000001F1E9815940>'

>>> repr(s)
'<__main__.myclass object at 0x000001F1E9815940>'

>>> class myclass():
	n=''
	def __repr__(self):
		return "hellow repr"

	
>>> s=myclass()

>>> repr(s)
'hellow repr'

>>> class myclass():
	n=''
	def __repr__(self):
		return "hellow repr"
	def __str__(self):
		return 'hellow str'

	
>>> s=myclass()

>>> repr(s)
'hellow repr'

>>> str(s)
'hellow str'

>>> l=[1,2,3,4,5]

>>> s=iter(l)

>>> s
<list_iterator object at 0x000001F1E97EE4C0>

>>> repr(s)
'<list_iterator object at 0x000001F1E97EE4C0>'

>>> s.__repr__()
'<list_iterator object at 0x000001F1E97EE4C0>'

>>> class my():
	"hi this this is class"
	def __init__(self,name):
		self.name=name
		print('welcome to learn python',self.name)

		
>>> s=my('gopi')
welcome to learn python gopi

>>> s.__repr__()
'<__main__.my object at 0x000001F1E9815BB0>'

>>> s.__doc__()
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    s.__doc__()
TypeError: 'str' object is not callable


>>> class fuc():
	def __init__(self,name,age):
		self.myname=name
		self.myage=age
		print(self.myname)
		print(self.myage)
	def my(self):
		print('hellow',self.myname,'How are you?','and my age is','self.myage')

		
>>> s=fuc('gopi',21)
gopi
21


>>> init(s)
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    init(s)
NameError: name 'init' is not defined

>>> l=[1,2,3,4,5,6]

>>> repr(l)
'[1, 2, 3, 4, 5, 6]'

>>> eval(repr(l))
[1, 2, 3, 4, 5, 6]
