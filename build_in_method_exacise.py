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


>>> #=======================================================

