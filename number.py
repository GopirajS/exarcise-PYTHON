>>>                        #         Number

>>> #int

>>> 0
0

>>> 100
100

>>> -10
-10

>>> 4000000000000000000000000000000000000000000000000000000000000000
4000000000000000000000000000000000000000000000000000000000000000

>>> y=50000000000000000000000000000000000000000000000000000000000000000000000000000000000000

>>> type(y)
<class 'int'>

>>> z=1

>>> id(z)
2430073530672

>>> id(y)
2430115577968

>>> bin(19)
'0b10011'

>>> _
'0b10011'

>>> print(_)
0b10011

>>> s=0b10011

>>> s
19

>>> oct(16)
'0o20'

>>> oct(8)
'0o10'

>>> oct(7)
'0o7'

>>> oct(74)
'0o112'

>>> 0o20
16

>>> 0o20
16

>>> 0o112
74

>>> hex(16)
'0x10'
>>> hex(15)
'0xf'
>>> 0x10
16
>>> 0xf
15

>>> x=0233
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers


>>> x=1_222_333_444

>>> x
1222333444

>>> x=1 222 333 444
SyntaxError: invalid syntax

>>> x
1222333444

>>> x=1 222 333 444
SyntaxError: invalid syntax

>>> x
1222333444

>>> type(s)

<class 'float'>


>>> 10.0
10.0

>>> -10.4
-10.4

>>> x-100
1222333344

>>> x=100

>>> type(x)
<class 'int'>

>>> int(100)
100

>>> int(-10)
-10


>>> int(12.43)
12

>>> int(5.5)
5

>>> int('100',2)

4

>>> int('1')
1
>>> int('10')
10

>>> int('1')
1

>>> int('5')
5

>>>                      #binary
>>> 
>>> s=0b11011000
>>> s
216
>>> s=0b_11_011_000
>>> s
216
>>> 
>>> 
>>>                          #octel
>>> d=0o12
>>> type(d)
<class 'int'>
>>> 
>>> 
>>>                        #hexadecimal
>>> 
>>> hex(15)
'0xf'
>>> s=0xf
>>> type(s)
<class 'int'>

>>> #=-------------------------------------------------------------------------------------------------
>>>                                                                   #float
>>> 
>>> f=12.4

>>> type(f)
<class 'float'>

>>> 

>>> f=1233456.1324356

>>> type(f)
<class 'float'>

>>> f=12_3_345_6.13_24_35_6

>>> type(f)
<class 'float'>

>>> f
1233456.1324356

>>> f=2e400


>>> f=2e1

>>> f
20.0

>>> f=2e2

>>> f
200.0

>>> f=2e40

>>> f
2e+40

>>> f=2e30

>>> f
2e+30

>>> 1e5
100000.0

>>> 1e6
1000000.0

>>> 1e19
1e+19

>>> 1e10
10000000000.0

>>> 1e11
100000000000.0

>>> f=3.13224354e4

>>> f
31322.4354

>>> float(5)
5.0

>>> float(5.5)
5.5

>>> float('5')
5.0

>>> float('5.5')
5.5

>>> float('-5.5')
-5.5

>>> float('     -5.5')
-5.5

>>> float('-5.5')
-5.5

>>> float('-infinity')
-inf

>>> float('Inf')
inf


>>>#--------------------------------------------------------------------------------------------------
>>>                                         #complex number

>>> c=1+3j
>>> type(c)
<class 'complex'>

>>> c=1+3J

>>> type(c)
<class 'complex'>

>>> c=3J+1

>>> type(c)
<class 'complex'>

>>> c=3+1J

>>> type(c)
<class 'complex'>

>>> c=3+J2
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    c=3+J2
NameError: name 'J2' is not defined

>>> type(c)
<class 'complex'>

>>> c
(3+1j)

>>> c=1+2K
SyntaxError: invalid syntax

>>> c=5

>>> type(c)
<class 'int'>

>>> type(complex(c))
<class 'complex'>

>>> c=5+j
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    c=5+j
NameError: name 'j' is not defined

>>> c=5j+5j

>>> c
10j

>>> type(c)
<class 'complex'>


>>>#---------------------------------------------------------------------------------
>>>                                    #arithmetic operation
>>> 
>>> 1+4
5
>>> 4-3
1
>>> 4-8
-4

>>> 2*3
6

>>> 1.2*4
4.8

>>> 1.4+1.5
2.9

>>> 10/20
0.5

>>> 10/2
5.0

>>> 10/3
3.3333333333333335

>>> 10%4
2
>>> 10%3
1

>>> 10//3
3

>>> 10//2
5


>>>#----------------------------------------------------------------------------------------

>>>                                   #arithmetic operation on complex

>>> a=6+4j

>>> a+2
(8+4j)

>>> a*2
(12+8j)

>>> a/2
(3+2j)

>>> a**2
(20+48j)
>>> 
