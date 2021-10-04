
>>>                                                  #string
                   1. to creat string

>>> str='hello world'

>>> str1="hellow world"

>>> str2="""HELLOW WORLD
hellow world
Hellow World
"""

>>> print(str)
hello world

>>> print(str1)
hellow world

>>> print(str2)
HELLOW WORLD
hellow world
Hellow World
            2.string idex and splitting

>>> s='hellow'

>>> s[:]
'hellow'

>>> s[0]
'h'

>>> s[1]
'e'

>>> s[2]
'l'

>>> s[3]
'l'

>>> s[4]
'o'
 
>>> s[5]
'w'

>>> s[6]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s[6]
IndexError: string index out of range

>>> s[0:]
'hellow'

>>> s[0:5]
'hello'

>>> s[:5]
'hello'

>>> s[4:5]
'o'

>>> s[2:4]
'll'
                                 3.negative parrameter
>>> s[-1]
'w'

>>> s[-5]
'e'

>>> s[-6]
'h'

>>> s[-6:]
'hellow'

>>> s[-6::]
'hellow'

>>> s[-6:::]
SyntaxError: invalid syntax

>>> s[-6::1]
'hellow'

>>> s[-6::2]
'hlo'

>>> s[0:5]
'hello'
>>> s[0:6]
'hellow'

>>> s[0:6:-1]
''

>>> s[::-1]
'wolleh'

>>> s[-4:-1]
'llo'
 
                  4.Reassinging String

>>> s
'hellow'

>>> s[0]='e'
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s[0]='e'
TypeError: 'str' object does not support item assignment

>>> s
'hellow'

>>> s='HELLOW'
>>> print(s)
HELLOW 
             5.Delete String

>>> s
'HELLOW'

>>> s='gopiraj'

>>> print(s)
gopiraj

>>> del s

>>> print(s)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(s)
NameError: name 's' is not defined

 
              6. string Operater

>>> # + , * , [] , [:] ,in ,not in ,r/R, %
 

>>> str='gopi'

>>> str1='raj'

>>> print(str+str1)
gopiraj

>>> print(str*3)
gopigopigopi

>>> print(str*4)
gopigopigopigopi

>>> print(s[])
SyntaxError: invalid syntax

>>> print(s[3])
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print(s[3])
NameError: name 's' is not defined

>>> print(s[2])
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print(s[2])
NameError: name 's' is not defined

>>> print(str[3])
i

>>> print(str[2])
p

>>> print(str[1])
o

>>> print(str[2:3])
p

>>> print(str[1:3])
op

>>> print(str[1:4])
opi

>>> print("gopi" in str)
True

>>> print("goi" in str)
False

>>> print("goi"  not in str)
True

>>> print(r'ceeofnwe\'9k1\\083police')
ceeofnwe\'9k1\\083police

>>> print('\\')
\

      
>>> print(r'c\\gopi')
c\\gopi


>>> print(r'c\\\'d')
c\\\'d
            

   

>>>                      7. they said,"what's going on".

>>> print('they said,"what\'s going on"')
they said,"what's going on"

>>> print("""they said,"what's going on""")
they said,"what's going on

 
                           8. Using % operater
>>> integer=21
>>> Float=324.232
>>> String='gopiraj'
>>> print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(integer,Float,String))
Hi I am Integer ... My value is 21
Hi I am float ... My value is 324.232000
Hi I am string ... My value is gopiraj



 
>>> name='gpoiraj'

>>> print("first candidate to select job for date scienties: %s"%(name))

first candidate to select job for date scienties: gpoiraj
 
>>> n=23

>>> print("first candidate to select job for date scienties: %i"%(n))
first candidate to select job for date scienties: 23

>>> print("first candidate to select job for date scienties: %d"%(n))
first candidate to select job for date scienties: 23

>>> print("first candidate to select job for date scienties: %s"%(n))
first candidate to select job for date scienties: 23

>>> print("first candidate to select job for date scienties: %f"%(n))
first candidate to select job for date scienties: 23.000000

>>> print("first candidate to select job for date scienties: %c"%(n))
first candidate to select job for date scienties: 

>>> print("first candidate to select job for date scienties: %x"%(n))
first candidate to select job for date scienties: 17

>>> print("first candidate to select job for date scienties: %o"%(n))
first candidate to select job for date scienties: 27

>>> print("first candidate to select job for date scienties: %b"%(n))
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    print("first candidate to select job for date scienties: %b"%(n))
ValueError: unsupported format character 'b' (0x62) at index 51