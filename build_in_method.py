Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # abs() method


>>> z='''
           Syntax:
                   abs(num)


          Parameters:
                    num: An int, float, or complex number.
'''

>>> print('absolute value of 10',abs(10))
absolute value of 10 10

>>> print('absolute value of -10:   ',abs(-10))
absolute value of -10:    10

>>> print('absolute value of -10:   ',abs(-10.32))
absolute value of -10:    10.32

>>> print('absolute value of -10.32:   ',abs(-10.32))
absolute value of -10.32:    10.32

>>> print('absolute value of -100:   ',abs(-100))
absolute value of -100:    100

>>> print('absolute value of 12.333:   ',abs(12.333))
absolute value of 12.333:    12.333

>>> print('absolute value of 2+3j:   ',abs(2+3j))
absolute value of 2+3j:    3.605551275463989

>>> print('absolute value of -2-3j:   ',abs(-2-3j))
absolute value of -2-3j:    3.605551275463989

>>> print('absolute value of -2+3j:   ',abs(-2+3j))
absolute value of -2+3j:    3.605551275463989

>>> print('absolute value of 2-3j:   ',abs(2-3j))
absolute value of 2-3j:    3.605551275463989

>>> bin(123)
'0b1111011'

>>> oct(244)
'0o364'

>>> hex(35)
'0x23'

>>> print('absolute value of bin od 123:   ',abs(0b1111011))
absolute value of bin od 123:    123

>>> print('absolute value of oct of 244:   ',abs(0o364))
absolute value of oct of 244:    244

>>> print('absolute value of hex of 35:   ',abs(0x23))
absolute value of hex of 35:    35



>>> #----------------------------------------------------------------------


>>> # all() method
>>> z='''
          all() Syntax:
                      all(iterable)


            Parameters:
                       iterable: A list, tuple, string, set, or dictionary object.
                       '''

>>> l=[]

>>> print('list of all() mehtod :  ',all(l))
list of all() mehtod :   True

>>> l=[1,2,3,4,5]

>>> print('list of all() mehtod :  ',all(l))
list of all() mehtod :   True

>>> l=[1,2,3,4,5,0]

>>> print('list of all() mehtod :  ',all(l))
list of all() mehtod :   False

>>> l=[1,2,3,4,5,False]

>>> print('list of all() mehtod :  ',all(l))
list of all() mehtod :   False

>>> s=set()

>>> print('set of all():   ',all(s))
set of all():    True

>>> s={'gopi','sathish'}

>>> print('set of all():   ',all(s))

set of all():    True

>>> s={'gopi','sathish',0}

>>> print('set of all():   ',all(s))
set of all():    False

>>> s={'gopi','sathish',False}

>>> print('set of all():   ',all(s))
set of all():    False

>>> s={'gopi','sathish',False,True}

>>> print('set of all():   ',all(s))
set of all():    False

>>> d={}

>>> print('dict of all():   ',all(d))
dict of all():    True

>>> d={'name':'gopi'}

>>> print('dict of all():   ',all(d))
dict of all():    True

>>> d={1:'gopi'}

>>> print('dict of all():   ',all(d))
dict of all():    True

>>> d={0:'gopi'}

>>> print('dict of all():   ',all(d))
dict of all():    False

>>> d={False:'gopi'}

>>> print('dict of all():   ',all(d))

dict of all():    False

>>> s=''

>>> print('string of all():   ',all(s))
string of all():    True

>>> s='hi hellow '

>>> print('string of all():   ',all(s))
string of all():    True

>>> s='       '

>>> print('string of all():   ',all(s))
string of all():    True

>>> s=False

>>> print('string of all():   ',all(s))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print('string of all():   ',all(s))
TypeError: 'bool' object is not iterable
>>> 
>>> #-----------------------------------------------------------

>>> z='''
        Syntax:
               any(iterable)

    Parameters:
              iterable: An iterable (list, tuple, string, set, dictionary).

              '''
>>> l=[]

>>> print(any(l))
False

>>> l=[1,2,3]

>>> print(any(l))
True

>>> l=[1,2,3,0]

>>> print(any(l))
True

>>> l=[1,2,3,0,False,True]

>>> print(any(l))
True

>>> l=[False]

>>> print(any(l))
False

>>> l=[0]

>>> print(any(l))
False

>>> l=[0]

>>> l=[0,1]

>>> print(any(l))
True

>>> s=''

>>> print(any(s))
False

>>> s=' '

>>> print(any(s))
True

>>> s='gopi '

>>> print(any(s))
True

>>> s='False'

>>> print(any(s))
True
>>> s=set()

>>> print(any(s))
False

>>> s={'gopi','raj'}

>>> print(any(s))
True

>>> s={0,False}

>>> print(any(s))
False

>>> s={0,False,True}

>>> print(any(s))
True

>>> d={}

>>> print(any(d))
False

>>> d={1}

>>> print(any(d))
True

>>> d={0}

>>> print(any(d))
False

>>> d={0,1}

>>> print(any(d))
True
>>> 

#------------------------------------------------------------------------- 

>>> for i in range(0,4):

	chr(i)

	
'\x00'
'\x01'
'\x02'
'\x03'
>>> for i in range(0,4):
	print(chr(i))

	




>>> for i in range(0,4):
	print(chr(i),'  ',end='')

	
            
>>> for i in range(0,128):
	print(chr(i),' , ',end='')

	
  ,   ,   ,   ,   ,   ,   ,   ,   , 	  , 
  ,   ,   , 
  ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,
    ,   ,   ,   ,   ,   ,   ,    , !  , "  , #  , $  , %  , &  , '  ,
  (  , )  , *  , +  , ,  , -  , .  , /  , 0  , 1  , 2  , 3  , 4  , 5  , 6  , 7  , 8  , 9  ,
  :  , ;  , <  , =  , >  , ?  , @  , A  , B  , C  , D  , E  , F  , G  , H  , I  ,
  J  , K  , L  , M  , N  , O  , P  , Q  , R  , S  , T  , U  , V  , W  , X  , Y  , Z  ,
  [  , \  , ]  , ^  , _  , `  , a  , b  , c  , d  , e  , f  , g  , h  , i  ,
  j  , k  , l  , m  , n  , o  , p  , q  , r  , s  , t  , u  , v  , w  , x  , y  , z  ,
  {  , |  , }  , ~  ,   ,

  
>>> ascii('gopiraj')
"'gopiraj'"
>>> ascii(1234)
'1234'
>>> ascii('1234')
"'1234'"
>>> ascii('தமிழ்')
"'\\u0ba4\\u0bae\\u0bbf\\u0bb4\\u0bcd'"


>>> #---------------------------------------------
>>> z='''


           Syntax:
                  bin(num)
       Parameters:
                  num: An integer.
'''

>>> bin(2)
'0b10'

>>> bin(15)
'0b1111'

>>> for i in range(0,50):
	print(i,":",bin(i))

	
0 : 0b0
1 : 0b1
2 : 0b10
3 : 0b11
4 : 0b100
5 : 0b101
6 : 0b110
7 : 0b111
8 : 0b1000
9 : 0b1001
10 : 0b1010
11 : 0b1011
12 : 0b1100
13 : 0b1101
14 : 0b1110
15 : 0b1111
16 : 0b10000
17 : 0b10001
18 : 0b10010
19 : 0b10011
20 : 0b10100
21 : 0b10101
22 : 0b10110
23 : 0b10111
24 : 0b11000
25 : 0b11001
26 : 0b11010
27 : 0b11011
28 : 0b11100
29 : 0b11101
30 : 0b11110
31 : 0b11111
32 : 0b100000
33 : 0b100001
34 : 0b100010
35 : 0b100011
36 : 0b100100
37 : 0b100101
38 : 0b100110
39 : 0b100111
40 : 0b101000
41 : 0b101001
42 : 0b101010
43 : 0b101011
44 : 0b101100
45 : 0b101101
46 : 0b101110
47 : 0b101111
48 : 0b110000
49 : 0b110001
>>> #-----------------------------------------------------

>>> #bool() mehtod

>>> print(bool(1))
True

>>> print(bool(0))
False

>>> print(bool(True))
True

>>> print(bool(False))
False

>>> print(bool('hi'))
True

>>> print(bool('hi  '))
True

>>> print(bool('  '))
True

>>> print(bool('-1'))
True

>>> print(bool('0'))
True

>>> print(bool(0))
False

>>> print(bool(-0))
False

>>> print(bool(-1))
True

>>> print(bool([0]))
True

>>> print(bool([0,False]))
True

>>> print(bool([0,False]))
True

>>> print(bool(()))
False

>>> print(bool((0)))
False

>>> print(bool((0,'hi')))
True

>>> print(bool((0,False)))
True

>>> print(bool((0)))
False

>>> print(bool([0]))
True


>>> print(bool((0,1)))
True


>>> print(bool(0,1))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(bool(0,1))
TypeError: bool expected at most 1 argument, got 2

>>> print(bool(0))
False

>>> s=(0)

>>> type(s)
<class 'int'>

>>> 0==s
True
>>> #------------------------------------------------------

>>> # callable() mehtod

>>> print(callable(str))
True

>>> print(callable(int))
True

>>> print(callable(float))
True

>>> print(callable(bool))
True


>>> print(callable(dict))
True

>>> print(callable(bin))
True

>>> print(callable(hex))
True

>>> print(callable(oct))
True

>>> print(callable(set))
True

>>> print(callable(list))
True

>>> print(callable(tuple))
True

>>> s=12

>>> print(callable(s))
False

>>> s=int

>>> print(callable(s))
True

>>> s=int()

>>> print(callable(s))
False

>>> s=int

>>> print(callable(s))
True

>>> d=s(12.3)

>>> d
12

>>> s=float

>>> s(12)
12.0

>>> s(12.234)
12.234

>>> s('gopi')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s('gopi')
ValueError: could not convert string to float: 'gopi'

>>> float('gopi')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    float('gopi')
ValueError: could not convert string to float: 'gopi'


>>> class myclass():
	def fuc(self):
		print('hello world')

		
>>> s=myclass()

>>> print(callable(myclass))
True

>>> print(callable(s.fuc))
True

>>> print(callable(s))
False

>>> s=myclass

>>> print(callable(s))
True

>>> s()
<__main__.myclass object at 0x0000019B2ED0C280>

>>> s.fuc()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s.fuc()
TypeError: fuc() missing 1 required positional argument: 'self'

>>> class myclass():
	def __call__(self):
		print('hello world')

		
>>> s=myclass()

>>> s()
hello world

>>> myclass()
<__main__.myclass object at 0x0000019B2EDBECA0>

>>> myclass.__call__
<function myclass.__call__ at 0x0000019B2EDD4D30>

>>> s.__call__()
hello world


>>> s=myclass()

>>> s.fuc()
helow world

>>> s()

>>> s=myclass


>>> s.fuc('hi')
helow world
>>> class myclass():
	def fuction(self):
		print('hellow world')
	def __call__(self):
		print('callable class')

		
>>> s=myclass()

>>> print(callable(s))
True

>>> print(callable(myclass))
True

>>> print(callable(myclass.fuction))
True

>>> print(callable(s.fuction))
True

>>> print(callable(s.fuction()))
hellow world
False

>>> s=myclass

>>> print(callable(s))
True

>>> print(callable(myclass))
True

>>> print(callable(myclass.fuction))
True

>>> print(callable(s.fuction))
True

>>> def fuction():
	print('hellow world')

	
>>> print(callable(fuction))
True

>>> s=fuction

>>> print(callable(s))
True

>>> s()
hellow world

>>> class myclass():
	def fuc(self):
		print('hello world')
	def my(self):
		print('hi gopi')

		
>>> s=myclass()

>>> s.fuc()
hello world

>>> s.my()
hi gopi

>>> print(callable(myclass))
True

>>> print(callable(myclass.fuc))
True

>>> print(callable(myclass.my))
True

>>> print(callable(s.fuc))
True

>>> print(callable(s.my))
True

>>> print(callable(s))
False

>>> s=myclass

>>> s()
<__main__.myclass object at 0x0000019B2EDBEFD0>

>>> a=s()


>>> a.fuc()
hello world

>>> a.my()
hi gopi

>>> x=s

>>> callable(x)
True

>>> callable(a)
False

>>> class myclass():
	def fuc(self):
		print('hello world')
	def my(self):
		print('hi gopi')
	def __call__(self):
		print('im callable')

>>> s=myclass()

>>> s.fuc()
hello world

>>> s.my()
hi gopi

>>> callable(myclass)
True

>>> callable(myclass.fuc)
True

>>> callable(myclass.my)
True

>>> callable(s.fuc)
True

>>> callable(s.my)
True

>>> s=myclass

>>> d=s()

>>> d.fuc()
hello world

>>> d.my()
hi gopi

>>> callable(d)
True

>>> callable(s)
True

>>> callable(myclass)

True

