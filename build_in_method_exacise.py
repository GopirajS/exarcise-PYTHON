>>> #   abs() method

>>> print('absolute value of 10 :',abs(10))
absolute value of 10 : 10

>>> print('absolute value of -10 :',abs(-10))
absolute value of -10 : 10

>>> print('absolute value of 10.243442 :',abs(10.243442))
absolute value of 10.243442 : 10.243442

>>> print('absolute value of -10.243442 :',abs(-10.243442))
absolute value of -10.243442 : 10.243442

>>> print('absolute value of 12+3J :',abs(12+3J))
absolute value of 12+3J : 12.36931687685298

>>> print('absolute value of -12+3J :',abs(-12+3J))
absolute value of -12+3J : 12.36931687685298

>>> s=abs(12)

>>> s
12

>>> s=abs

>>> s(12.112)
12.112

>>> s.__call__
<method-wrapper '__call__' of builtin_function_or_method object at 0x00000204E0A5EC20>


>>> #===============================================================

>>> #   all() method

>>> l=[]   # empty list

>>> all(l)
True

>>> l=[0]   # empty list

>>> all(l)
False

>>> l=[0,1,2,3]

>>> all(l)
False



>>> t=(1,2,3,4,5)

>>> all(l)
False

>>> t=(1,2,3,4,5)

>>> all(t)
True

>>> t=(1,2,3,4,5,0)

>>> all(t)
False

>>> t=(1,2,3,4,5,False)

>>> all(t)
False

>>> t=()   # empty tuple

>>> all(t)
True

>>> s=set()   #empty set

>>> all(s)
True

>>> s={1,2,3,4,5,'python','java','php'}

>>> all(s)
True

>>> s={1,2,3,4,5,'python','java','php',False}

>>> all(s)
False

>>> s={1,-2,-3.13,4,5,'python','java','php'}

>>> all(s)
True

>>> s={1,-2,-3.13,4,5,'python','java','php',0}

>>> all(s)
False

>>> d={}    #empty  dictunery


>>> all(d)
True

>>> d={1,-2,3.12323,4,'gopi',True}


>>> d={}    #empty  dictunery

>>> d={1:'one',2:'two',3:'three'}

>>> all(d)
True

>>> d={1:'one',2:'two',3:0}

>>> all(d)
True

>>> d={1:'one',2:'two',3:0,0:'gopiraj'}

>>> all(d)
False

>>> s='gopiraj'

>>> all(s)
True

>>> s='gopiraj1'

>>> all(s)
True

>>> s='gopiraj0'

>>> all(s)
True

>>> s='00'

>>> all(s)
True

>>> s=False

>>> all(s)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    all(s)
TypeError: 'bool' object is not iterable


>>> s=False,2

>>> all(s)
False



>>> #================================================
>>> #    any()   method

>>> #any(iterable)  iterable: list,tuple,set,dict,string

>>> str =' '

>>> any(str)

True

>>> str =''

>>> any(str)
False

>>> l=[0,1,2,3]

>>> any(l)
True

>>> l=[0]

>>> any(l)
False

>>> l=[0]

>>> l=[]

>>> any(l)
False

>>> l=[0,False,1]

>>> any(l)
True

>>> l=[0,False]

>>> any(l)
False



>>> t=()

>>> any(l)

False

>>> t=(1,2,3,4,5)

>>> any(l)
False

>>> t=()

>>> any(l)
False

>>> t=(1,2,3,4,5)

>>> any(l)
False

>>> t=(0,False,0.123)

>>> any(l)

False

>>> t=(0.123)

>>> any(l)
False

>>> t=(-11)

>>> any(l)
False

>>> t=(-11)

>>> t=()

>>> any(t)
False



>>> t=(1,2,3,4,5)

>>> any(t)
True

>>> t=(1,2,3,4,5,False,0)

>>> any(t)
True
>>> t=(False,0)

>>> any(t)
False


>>> t=()

>>> any(t)
False
>>> s=set()

>>> any(s)
False

>>> s={1,2,3,4,5}

>>> any(s)
True


>>>#=====================================================

>>> #  int()

>>> int(12)
12

>>> int()
0

>>> n=12

>>> s='123'

>>> print(s+n)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(s+n)
TypeError: can only concatenate str (not "int") to str

>>> print(int(s)+n)
135


>>> int('1223',base=4)
107

>>> int('1223',base=6)
303

>>> int('1223',base=8)

659

>>> int('1223',base=10)
1223

>>> int('1223',base=12)
2043

>>> int('1223',base=14)
3167

>>> int('1223',base=16)
4643

>>> int('0',base=0)
0


>>> int('0',base=2)

0

>>> int('0',base=4)
0

>>> int('100',base=4)
16

>>> int('100',base=0)
100

>>> int('100',base=2)
4

>>> int('100',2)
4

>>> bin(4)
'0b100'

>>> int('123',10)
123

>>> int('123',8)
83

>>> oct(123)
'0o173'

>>> oct(83)
'0o123'

>>> oct(83)
'0o123'

>>> s='gopi'

>>> try:
	s='gopi'
	int(s,2)
except ValueError as e:
	print(e)

	
invalid literal for int() with base 2: 'gopi'


>>> #========================================

>>> # float() method

>>> float(0)
0.0

>>> float(12.22)
12.22

>>> float('12.22')
12.22

>>> float('-12.22')
-12.22

>>> x.__add__(12)
33

>>> x.__bool__()
True

>>> x=12.3

>>> x.__abs__()
12.3

>>> x=-12.3

>>> x.__abs__()
12.3

>>> x
-12.3

>>> abs(x)
12.3

>>> x.__divmod__(3)
(-5.0, 2.6999999999999993)
>>> x.__eq__(12.3)
False

>>> x.__eq__(-12.3)
True

>>> x.__floordiv__(12)
-2.0

>>> x.__floor__()
-13

>>> x=12.3

>>> x.__floor__()
12

>>> x=12.5

>>> x.__floor__()
12

>>> x=12.6

>>> x.__floor__()
12

>>> x=12.7

>>> x.__floor__()
12

>>> x=13.33333

>>> x.__floor__()
13

>>> #====================================================================

>>> # float() method

>>> float(10)
10.0

>>> float(10.122)
10.122

>>> float(10.1221234567)
10.1221234567

>>> float("10.1221234567")
10.1221234567

>>> float(-10.122)
-10.122

>>> 3e-002
0.03

>>> +1E3
1000.0

>>> #=====================================================

>>> float(True)
1.0

>>> float(False)
0.0

>>> float("nan")
nan

>>> float("inf")
inf

>>> float(        10)
10.0

>>> float( "       10\n")
10.0

>>> #========================================================

>>> #  complex()  method

>>> s=complex()

>>> s
0j

>>> type(s)
<class 'complex'>



>>> s="12+j"

>>> s
'12+j'


>>> s=12+1J

>>> s
(12+1j)

>>> s=12+0J

>>> s
(12+0j)

>>> s=complex(12,4)

>>> s
(12+4j)

>>> s=complex(-12,4)

>>> s
(-12+4j)

>>> complex(-12,-4)
(-12-4j)

>>> complex(-12)
(-12+0j)

>>> complex(-12,)
(-12+0j)


>>> complex()
0j

>>> complex(0,12)
12j

>>> c=complex('12+j')

>>> c
(12+1j)


>>> s=12+0j

>>> s
(12+0j)


>>> s=12+12j

>>> s
(12+12j)

>>> c=complex('15+12j')

>>> c
(15+12j)

>>> c=complex('+j')

>>> c
1j

>>> c=complex('-j')

>>> c
-1j

>>> #===================================

>>> # bool()  method

>>> bool(12)
True

>>> bool([0])
True

>>> l=[1,2,3]

>>> bool([0])
True

>>> bool(l)
True

>>> l=[0,False]

>>> bool(l)
True

>>> l=[]

>>> bool(l)
False

>>> s={}

>>> bool(s)
False

>>> s={'gopi'}

>>> bool(s)
True

>>> bool('string')
True

>>> bool(12.22)
True

>>> bool(12+12J)
True

>>> bool(+0J)
False

>>> bool(0+0J)
False

>>> bool(9+0J)
True

>>> bool(0+2J)
True

>>> #================================================================

>>> s=bytes('gopi',encoding='utf-8')

>>> s
b'gopi'

>>> s=bytes('கோபி',encoding='utf-8')

>>> s
b'\xe0\xae\x95\xe0\xaf\x87\xe0\xae\xbe\xe0\xae\xaa\xe0\xae\xbf'

>>> str(s,encoding='ascii',errors ="ignore")
''

>>> str(s,encoding='utf-8')
'கோபி'

>>> s=bytes('gopi',encoding='utf-16')

>>> s
b'\xff\xfeg\x00o\x00p\x00i\x00'


>>> str(s,encoding='utf=8',errors ="ignore")
'g\x00o\x00p\x00i\x00'

>>> str(s,encoding='utf-16',errors ="ignore")
'gopi'

>>> n='கோபி'



>>> s=bytes(n,encoding='utf-16')

>>> s
b'\xff\xfe\x95\x0b\xc7\x0b\xbe\x0b\xaa\x0b\xbf\x0b'

>>> str(s,encoding='utf-16')
'கோபி'


>>> s=bytes(n,encoding='utf-8')


>>> str(s,encoding='utf-16',errors ="ignore")
'껠\ue095螯껠\ue0beꪮ껠'

>>> s=bytes('gopi',encoding='utf-16')

>>> str(s,encoding='utf-16',errors ="ignore")
'gopi'

>>> s=bytes('gopi',encoding='utf-8')

>>> str(s,encoding='utf-8',errors ="ignore")
'gopi'

>>> s=bytes('gopi',encoding='utf-16')

>>> str(s,encoding='utf-8',errors ="ignore")
'g\x00o\x00p\x00i\x00'

>>> s=bytes(n,encoding='utf-16')

>>> str(s,encoding='utf-16')
'கோபி'

>>> str(s,encoding='utf-8',errors ="ignore")
'\x0b\x0b\x0b\x0b\x0b'

>>> s=bytes(n,encoding='utf-16')

>>> str(s,encoding='utf-16')
'கோபி'

>>> s=bytes(n,encoding='utf-16')

>>> str(s,encoding='utf-16',errors ="ignore")
'கோபி'

>>> s=bytes('gopi',encoding='utf-16')

>>> str(s,encoding='utf-16',errors ="ignore")
'gopi'

>>> s=bytes('கோபி',encoding='utf-16')

>>> str(s,encoding='utf-16')
'கோபி'

>>> s=bytes('கோபி',encoding='utf-16')

>>> str(s,encoding='utf-16')
'கோபி'

>>> s=bytes('gopi',encoding='utf-16')

>>> str(s,encoding='utf-16',errors ="ignore")
'gopi'


>>> s=bytes('gopi',encoding='utf-16')

>>> str(s,encoding='utf-8',errors ="ignore")
'g\x00o\x00p\x00i\x00'

>>> s=bytes('gopi',encoding='utf-8')

>>> s
b'gopi'

>>> str(s,encoding='utf-8',errors ="ignore")
'gopi'

>>> str(s,encoding='utf-16',errors ="ignore")
'潧楰'

>>> str(s,encoding='utf-32',errors ="ignore")
''

>>> str(s,encoding='ascii',errors ="ignore")
'gopi'

>>> s=bytes('gopi',encoding='ascii')

>>> str(s,encoding='ascii',errors ="ignore")
'gopi'

>>> 'g\x00o\x00p\x00i\x00'
'g\x00o\x00p\x00i\x00'


>>> #==============================================


>>> # tuple()  method

>>> t=tuple()   #creat empty tuple

>>> t
()

>>> type(t)
<class 'tuple'>

>>> l=[1,2,3,4.444555,-5,'gopi',False]

>>> t=tuple(l)

>>> t=tuple(set(l))

>>> t
('gopi', 1, 2, 3, 4.444555, False, -5)

>>> t=tuple(l)

>>> t
(1, 2, 3, 4.444555, -5, 'gopi', False)

>>> l={1,2,3,4.444555,-5,'gopi',False}

>>> l={1,2,3,4.444555,-5,'gopi',False}

>>> s={1,2,3,4.444555,-5,'gopi',False}

>>> type(s)
<class 'set'>

>>> t=tuple(s)

>>> t
(False, 1, 2, 3, 4.444555, 'gopi', -5)



>>> d={1:'one',2:'two',3:'three',4:'four'}

>>> type(d)
<class 'dict'>



>>> t=tuple(d)

>>> t
(1, 2, 3, 4)

>>> s='hellow world'

>>> t=tuple(s)

>>> t
('h', 'e', 'l', 'l', 'o', 'w', ' ', 'w', 'o', 'r', 'l', 'd')




>>> #============================================================

>>> # list() method

>>> l=list()   #creat a empty list

>>> type(l)
<class 'list'>

>>> print(l)
[]

>>> t=(1,2,3,4.444555,-5,'gopi',False)

>>> type(t)
<class 'tuple'>

>>> l=list(t)

>>> l
[1, 2, 3, 4.444555, -5, 'gopi', False]

>>> type(l)
<class 'list'>

>>> s={1,2,3,4.444555,-5,'gopi',False}

>>> type(s)
<class 'set'>

>>> l=list(s)

>>> l
[False, 1, 2, 3, 4.444555, 'gopi', -5]

>>> s='hellow python '

>>> l=list(s)

>>> l
['h', 'e', 'l', 'l', 'o', 'w', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ']

>>> type(l)
<class 'list'>

>>> list(123454)
Traceback (most recent call last):
  File "<pyshell#346>", line 1, in <module>
    list(123454)
TypeError: 'int' object is not iterable

>>> list('123454')
['1', '2', '3', '4', '5', '4']




>>> #=====================================


>>> #  set() method

>>> l=[1,2,3,3,3.23456,'gopi','sathish',False,True]

>>> s=set()

>>> type(s)
<class 'set'>

>>> s
set()

>>> s=set(l)

>>> s
{'gopi', 1, 2, 3.23456, 3, False, 'sathish'}

>>> len(l)==len(s)
False


>>> t=(1,2,3,3,3.23456,'gopi','sathish',False,True)


>>> s=set(t)

>>> s
{'gopi', 1, 2, 3.23456, 3, False, 'sathish'}



>>> d={'name':'sathish','age':21,'city':'mumbai','education':'BE'}

>>> s=set(d)

>>> s
{'education', 'city', 'age', 'name'}

>>> s=set(d.values())

>>> s
{'BE', 'mumbai', 21, 'sathish'}

>>> #=========================================

>>> #  dict()  method

>>> d=dict()  # creat empty  dict method


>>> d
{}
>>> d={}

>>> s={}
\

>>> type(d)
<class 'dict'>


>>> d={1:'one',2:'two',3:'three'}

>>> d
{1: 'one', 2: 'two', 3: 'three'}

>>> d={'name':'}
   
SyntaxError: EOL while scanning string literal

>>> d={'name':'sathish','age':29,'city':'salem'}

>>> d
{'name': 'sathish', 'age': 29, 'city': 'salem'}



>>> s=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]

>>> d=dict(s)

>>> d
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}

>>> s={("I",'one'),("II",'two'),("III",'three'),('IV','four')}


>>> d=dict(s)

>>> d
{'II': 'two', 'III': 'three', 'I': 'one', 'IV': 'four'}

>>> s={("I",'one'),("II",'two'),("III",'three'),('IV','four'),('I','gopi')}

>>> d=dict(s)

>>> d
{'I': 'one', 'II': 'two', 'III': 'three', 'IV': 'four'}


>>> d=dict({'I': 'one', 'II': 'two', 'III': 'three', 'IV': 'four'})

>>> d
{'I': 'one', 'II': 'two', 'III': 'three', 'IV': 'four'}

>>> #==========================================================

>>> 
>>> #   frozen set()  method

>>> l='gopi'

>>> f=frozenset()

>>> type(f)
<class 'frozenset'>

>>> f=frozenset(l)

>>> f
frozenset({'o', 'i', 'g', 'p'})

>>> l='gopioo'

>>> f=frozenset(l)

>>> f
frozenset({'o', 'i', 'g', 'p'})

>>> l=[1,2,3,3,3.23456,'gopi','sathish',False,True]

>>> f=frozenset(l)

>>> f
frozenset({'gopi', 1, 2, 3.23456, 3, False, 'sathish'})

>>> for i in f:
	i
	
'gopi'
1
2
3.23456
3
False
'sathish'

>>> s={1,2,3,4.444555,-5,'gopi',False}

>>> f=frozenset(s)

>>> f
frozenset({False, 1, 2, 3, 4.444555, 'gopi', -5})

>>> t=('gopi','sathish','kumar','gapal')

>>> f=frozenset(t)

>>> f
frozenset({'gopi', 'kumar', 'sathish', 'gapal'})
>>> for i in f:
	i

	
'gopi'
'kumar'
'sathish'
'gapal'


>>> #===========================================================================================


>>> #  meth related of build in function

>>> #     sum()   method


>>> sum([1,2,3,4,5])
15

>>> sum([1,2,3,4,5],3)
18

>>> l=[1,2,3.3344,5]

>>> sum([1,2,3,4,5],3)
18

>>> sum(l,)
11.3344

>>> sum(l,2)
13.3344

>>> t=[1,2,3,4,5]

>>> sum(l)
11.3344

>>> sum(t)
15

>>> t=[1,2,3,4,5]

>>> sum(t,)
15

>>> sum(t,4)
19

>>> sum(t,5)
20


>>> s={1,2,3,4,5,6,7,7}

>>> sum(s)
28

>>> t=[1,2,3,4,5,6,7,7]

>>> sum(s)
28

>>> sum(t)
35

>>> len(s)==len(t)
False

>>> c=[12+0j,3-2j]

>>> sum(c)
(15-2j)


>>> #===================================================================

>>> #  pow(base,exponent,modules)

>>> pow(2,2)
4

>>> pow(2,3)
8

>>> pow(2,4)
16

>>> pow(2,4)  # 2 * 2 * 2 * 2
16

>>> pow(2,4,2)
0

>>> pow(3,3)
27

>>> pow(3,3,2)
1

>>> pow(3,3,4)
3

>>> pow(3,3,5)
2

>>> pow(3,3,6)
3

>>> pow(3,3,8)
3

>>> pow(3,3,9)
0

>>> pow(3,3,7)
6

>>> pow(2,2)
4

>>> pow(2,-2)
0.25

>>> 1/4
0.25



>>> #=====================================================

>>>     #  max() method
    

>>> l=[1,2,3,4,5,6,7.234,9,'gopiraj']

>>> max(l)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    max(l)
TypeError: '>' not supported between instances of 'str' and 'int'

>>> l=[1,2,3,4,5,6,7.234,9]

>>> max(l)
9

>>> l=['a','as','asd','asdf','asdfg']

>>> max(l,key=len)
'asdfg'

>>> max(l,key=len,default='no eleement')
'asdfg'

>>> l=[]

>>> max(l,key=len,default='no eleement')
'no eleement'

>>> l=[1,2,3,4]


>>> #   ============================================================

>>> #  min()  method

>>> nums = [1,7,8,5,4,6,2,3]

>>> lowest = min(nums)

>>> print(lowest)
1

>>> min('a','as','asd','asdf','asdfg')
'a'

>>> min('a','as','asd','asdf','asdfg',key=len)
'a'

>>> max('a','as','asd','asdf','asdfg',key=len)
'asdfg'

>>> c=[]


>>> min(c,key=len,default='no element')
'no element'


>>> #=====================================================================

>>> #   divmod() method


>>> divmod(12,2)
(6, 0)

>>> divmod(12,3)
(4, 0)

>>> divmod(12,4)
(3, 0)

>>> divmod(12,5)
(2, 2)

>>> divmod(12,6)
(2, 0)

>>> divmod(12,7)
(1, 5)

>>> divmod(12.123,7)
(1.0, 5.122999999999999)

>>> divmod(12.12,7)
(1.0, 5.119999999999999)

>>> divmod(12.12,8)
(1.0, 4.119999999999999)

>>> divmod(12.12,3)
(4.0, 0.11999999999999922)

>>> divmod(12,3)
(4, 0)

>>> divmod(6.5,2)
(3.0, 0.5)

>>> #================================================


>>> s=[1,2,3,4,5,6,7]

>>> a=iter(s)

>>> a
<list_iterator object at 0x000002176E45E160>

>>> next(a)
1

>>> next(a)
2

>>> next(a)
3

>>> next(a)
4

>>> 4
4

>>> next(a)
5


>>> s=[1,2,3,4,5,6,7]

>>> a=iter(s)

>>> next(a,'stop')
1

>>> next(a,'stop')
2

>>> next(a,'stop')
3

>>> next(a,'stop')
4

>>> 4
4

>>> next(a,'stop')
5

>>> next(a,'stop')
6

>>> next(a,'stop')
7

>>> next(a,'stop')
'stop'


>>> def traverse(iterable):
    it=iter(iterable)
    while True:
        try:
            item=next(it)
            print (item)
        except StopIteration:
            break

        

>>> s=[1,2,3,4,5,6,7]

>>> traverse(s)
1
2
3
4
5
6
7


>>> traverse(s)
1
2
3
4
5
6
7


>>> class DataStore:
	def __init__(self, data):
		self.data = data
	def __iter__(self):
		return self.data

	

>>> s=[1,2,3,4,5,6,7]


>>> d=DataStore(s)

>>> d
<__main__.DataStore object at 0x000002176E4A40D0>

>>> next(d)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    next(d)
TypeError: 'DataStore' object is not an iterator


>>> d.data
[1, 2, 3, 4, 5, 6, 7]

>>> #============================================================

>>> #   filder() method

>>> s=[1,2,3,4,5,6,7]

>>> a=filter(None,s)

>>> a
<filter object at 0x000002176E53E6A0>

>>> for i in a:
	print(i,end=' ')
	
1 2 3 4 5 6 7 

>>> a=filter(lambda x:x%2==0,s)

>>> a
<filter object at 0x000002176E53E880>

>>> for i in a:
	print(i,end=' ')
	
2 4 6 

>>> a=filter(lambda x:x%2!=0,s)

>>> for i in a:
	print(i,end=' ')

	
1 3 5 7 

>>> mylist = [0, 1, 2, 3, False, True, 5]

>>> a=filter(lambda x:x%2!=0,mylist)

>>> for i in a:
	print(i,end=' ')

	
1 3 True 5 

>>> True%2
1

>>> True%3
1

>>> True%12
1

>>> for i in a:
	print(i,sep=',',end=' ')

	
>>> a=filter(lambda x:x%2!=0,mylist)

>>> for i in a:
	print(i,sep=',',end=' ')
	
1 3 True 5 

>>> s
[1, 2, 3, 4, 5, 6, 7]

>>> print(s)
[1, 2, 3, 4, 5, 6, 7]

>>> print(s,sep=',')
[1, 2, 3, 4, 5, 6, 7]

>>> print(s,sep=',',end=' ')
[1, 2, 3, 4, 5, 6, 7] 

>>> #==========================================


>>> # map()  method

>>> s=[1,2,3,4,5,6,7]

>>> 

>>> d=map(lambda x:x+1,s)

>>> d
<map object at 0x000002176E53E610>

>>> for i in d:
	i
	
2
3
4
5
6
7
8

>>> d=map(lambda x:x+3,s)

>>> next(d)
4

>>> next(d)
5

>>> next(d)
6

>>> next(d)
7

>>> next(d)
8

>>> next(d)
9

>>> next(d)
10

>>> next(d)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    next(d)
StopIteration

>>> s
[1, 2, 3, 4, 5, 6, 7]

>>> d=filter(lambda :True,s)

>>> d

<filter object at 0x000002176E53E610>


>>> d=filter(lambda x:True,s)

>>> for i in d:
	i	
1
2
3
4
5
6
7


>>> #=======================================================

>>> # sorted() method

>>> nums = [2,1,5,3,4]

>>> s=sorted(nums)

>>> s
[1, 2, 3, 4, 5]


>>> s=sorted(nums,reverse=True)

>>> s
[5, 4, 3, 2, 1]

>>> s=sorted(nums,reverse=False)

>>> s='asdfghjklqwertyuiop'

>>> s='asdfghjklqwertyuiopzxcvbnm'

>>> len(s)
26

>>> d=sorted(s,key=len)

>>> d
['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

>>> d=sorted(s)

>>> d
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

>>> d=sorted(s,reverse=True)


>>> d
['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']


>>> #========================================================

>>> #   reverse()   method

>>> s='gopiraj'

>>> reversed(s)
<reversed object at 0x000002176E53E340>

>>> for i in reversed(s):
	i

	
'j'
'a'
'r'
'i'
'p'
'o'
'g'

>>> for i in reversed(s):
	i
	
'j'
'a'
'r'
'i'
'p'
'o'
'g'

>>> d=reversed(s)

>>> next(d)
'j'

>>> next(d)
'a'

>>> next(d)
'r'

>>> next(d)
'i'

>>> next(d)
'p'

>>> next(d)
'o'

>>> next(d)
'g'


>>> for i in reversed(s):
	print(i,end=' ')
	
j a r i p o g 

>>> s='gopiraj'

>>> d=reversed(s)

>>> d
<reversed object at 0x000002176E53E340>

>>> d=list(reversed(s))

>>> d
['j', 'a', 'r', 'i', 'p', 'o', 'g']

>>> s=(1,2,3,4,5,6)

>>> d=tuple(reversed(s))

>>> d
(6, 5, 4, 3, 2, 1)

>>> s=[10,20,30,40]

>>> d=tuple(reversed(s))


>>> d
(40, 30, 20, 10)

>>> d=set(reversed(s))

>>> d
{40, 10, 20, 30}

>>> #=================================================

>>> #   other build in method

>>> # abs()

>>> abs(21)
21

>>> abs(-21)
21


>>> abs(12+2j)

12.165525060596439

>>> #================================

>>> T=[1,2,3,4,5,6]

>>> all(T)
True

>>> T=[1,2,3,4,5,6,0]

>>> all(T)
False

>>> t=[]

>>> all(T)
False

>>> all(t)
True

>>> #=======================================

>>> # any method

>>> t=[]


>>> any(t)
False

>>> t=[1]

>>> any(t)
True

>>> t=[1,False,0]

>>> any(t)
True

>>> t=[1,False,0,None]

>>> any(t)
True

>>> t=[False,0,None]

>>> any(t)
False

>>> #======================================

>>> t=[1,2,3,4,5,6]


>>> enumerate(t)
<enumerate object at 0x000002176E53D940>

>>> for i in enumerate(t):
	i
	
(0, 1)
(1, 2)
(2, 3)
(3, 4)
(4, 5)
(5, 6)

>>> for i in enumerate(t,5):
	i

(5, 1)
(6, 2)
(7, 3)
(8, 4)
(9, 5)
(10, 6)


>>> l=['gopi','sathish','kumar','raj','gopal']

>>> enumerate(l)
<enumerate object at 0x000002176E53D840>

>>> s=enumerate(l)

>>> for i in s:
	i
	
(0, 'gopi')
(1, 'sathish')
(2, 'kumar')
(3, 'raj')
(4, 'gopal')

>>> for i in s:
	i


>>> s=enumerate(l,10)

>>> for i in s:
	i
	
(10, 'gopi')
(11, 'sathish')
(12, 'kumar')
(13, 'raj')
(14, 'gopal')

>>> for i in s:
	i[0]

	
>>> s=enumerate(l,10)

>>> for i in s:
	i[0]
	
10
11
12
13
14

>>> for i in enumerate(l,10):
	i[0]
	
10
11
12
13
14

>>> for i in enumerate(l,10):
	i[0] ;i[1]

	
10
'gopi'
11
'sathish'
12
'kumar'
13
'raj'
14
'gopal'

>>> #===========================================


>>> # help() method

>>> help(object)


>>> bin
<built-in function bin>

>>> help(bin)
Help on built-in function bin in module builtins:

bin(number, /)
    Return the binary representation of an integer.
    
    >>> bin(2796202)
    '0b1010101010101010101010'


>>> #==============================================================

>>> #  id() method

>>> id(12)
2299617307280

>>> id(123)
2299617499312

>>> s=12

>>> id(s)
2299617307280

>>> a=12

>>> id(a)
2299617307280

>>> name='gopiraj'


>>> id(name)
2299658701040

>>> s='gopiraj'

>>> id(s)
2299658701040

>>> id(name)==id(s)
True

>>> id('gopiraj')
2299658701040

>>> class my:
	name='string'
	age=21

	
>>> s=my()

>>> id(s)
2299658496368

>>> d=my()

>>> id(d)
2299658495888

>>> g=my()

>>> id(g)
2299658497472

>>> id(s)==id(d)
False

>>> id(s)==id(d)==id(g)
False


>>> #=========================================================

>>> input()
how age u?
'how age u?'

>>> input('enter your name')
enter your name  gopi
'  gopi'

>>> input(None)
None sss
' sss'



>>> input(prompt='enter your name')
Traceback (most recent call last):
  File "<pyshell#338>", line 1, in <module>
    input(prompt='enter your name')
TypeError: input() takes no keyword arguments


>>> input('enter your name: ')
enter your name: கோபிராஜ்
'கோபிராஜ்'

>>> #==============================================

>>> l=[1,2,3,4,5,6,6,6]

>>> len(l)
8

>>> s={1,2,3,4,5,6,6,6}

>>> len(s)
6

>>> s='gopiraj'

>>> len(s)
7

>>> d={1:'one',2:'two',3:'three'}

>>> len(d)
3

>>> ascii('gopi')
"'gopi'"


>>> len(range(2))
2

>>> len(range(10))
10

>>> len(10)
Traceback (most recent call last):
  File "<pyshell#370>", line 1, in <module>
    len(10)
TypeError: object of type 'int' has no len()


>>> len(True)
Traceback (most recent call last):
  File "<pyshell#371>", line 1, in <module>
    len(True)
TypeError: object of type 'bool' has no len()

>>> #============================================================




>>> # print() method

>>> print('jellow')
jellow

>>> print('jellow','world')
jellow world

>>> print('jellow','world','python')
jellow world python

>>> print('jellow','world','python',sep=',')
jellow,world,python

>>> print('jellow','world','python',sep='--->')
jellow--->world--->python

>>> print('jellow','world','python',sep='--->');print('gopiraj')
jellow--->world--->python
gopiraj

>>> print('jellow','world','python',sep='--->',end=' ');print('gopiraj')
jellow--->world--->python gopiraj

>>> print('jellow','world','python',sep='--->',end='\n ');print('gopiraj')
jellow--->world--->python
 gopiraj

>>> print('jellow','world','python',sep='--->');print('gopiraj')

jellow--->world--->python
gopiraj

>>> name='gopiraj'


>>> print('hellow python',name)
hellow python gopiraj

>>> #===================================================

>>> # range() method

>>> range(10)
range(0, 10)

>>> for i in range(10):
	i
	
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

>>> for i in range(1,10):
	print(i,end=' ')

	
1 2 3 4 5 6 7 8 9 

>>> for i in range(1,20):
	print(i,end=' ')

	
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 
>>> for i in range(1,20,2):
	print(i,end=' ')

	
1 3 5 7 9 11 13 15 17 19 
>>> for i in range(1,20,3):
	print(i,end=' ')

	
1 4 7 10 13 16 19 

>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> set(range(10))
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

>>> set(range(10,1))
set()

>>> set(range(10,1,-1))
{2, 3, 4, 5, 6, 7, 8, 9, 10}

>>> set(range(10,0,-1))
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

>>> set(range(10,0,-2))
{2, 4, 6, 8, 10}

>>> tuple(range(10,0,-2))
(10, 8, 6, 4, 2)

>>> #======================================================




>>> #  slice() method

>>> l=[1,2,3,4,5,6,7,8,9]

>>> l[slice(9)]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> l[slice(4)]
[1, 2, 3, 4]

>>> l[slice(1,4)]
[2, 3, 4]

>>> l[slice(0,4)]
[1, 2, 3, 4]

>>> l[slice(0,4,3)]
[1, 4]


>>> l[slice(0,9,3)]
[1, 4, 7]

>>> l[slice(0,10,3)]
[1, 4, 7]

>>> l[slice(0,100,3)]
[1, 4, 7]


>>> l[0:1:1]
[1]

>>> l[0:9:1]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> l[0:10:1]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> l[0:10:2]
[1, 3, 5, 7, 9]


>>> #===================================================




>>> #   type() method

>>> type(s)
<class 'str'>

>>> s='gopi'

>>> type(s)
<class 'str'>

>>> l=[1,2,3]

>>> type(l)
<class 'list'>

>>> t=(1,2,3,4)

>>> type(t)
<class 'tuple'>

>>> 

>>> s={'gopi','raj','sathish'}


>>> type(s)
<class 'set'>


#=============================================================
       
       
>>> exec("print('hellow python')")
hellow python

>>> exec("print('hellow python')")
hellow python

>>> code=input("enter your code :")
enter your code :[print(x**2) for x in [1,2,3,4,5]]


>>> code
'[print(x**2) for x in [1,2,3,4,5]]'

>>> exec(code)
1
4
9
16
25

>>> mycode='''
a=12
b=32

print(a+b)'''

>>> exec(mycode)
44

>>> exec('abs(-9)')


>>> exec('print(abs(-9))')
9

>>> abs(--9)
9

>>> abs(-9)
9

>>> mycode='''
from math import *
s=sqrt(9)
print(s)
'''


>>> exec(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    exec(s)
NameError: name 's' is not defined

>>> exec(mycode)
3.0

>>> from math import *


>>> from math import *

>>> exec("print(dir())")
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'b', 'ceil', 'code', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'mycode', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 's', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

>>> exec("print(sqrt(4))")
2.0

>>> exec("print(sq(4))",{'sq':sqrt})
2.0

>>> exec
<built-in function exec>

>>> code=input('enter a code :')
enter a code :x*(x+1)*(x+2)

>>> x=2

>>> eval(code)
24

>>> code
'x*(x+1)*(x+2)'

>>> def mycode():
	return 12345


>>> code=input('enter a code :')
enter a code :mycode()

>>> eval(code)
12345



>>> #                 eval()  method

>>> def my_fuction():
	code=input('enter a code for execute :')
        print(code)
	x=int(input('enter a number:'))
        s=eval(code)
	print(s)
	


>>> my_fuction()
enter a code for execute :x*(x+1)*(x+2)
enter a number:3

60       
       
