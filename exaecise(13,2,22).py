>>> #  python string

>>> s='This is string'

>>> print(s)
This is string


>>> s='changing a string'

>>> s
'changing a string'


>>> l=[1,'string',12.33,"A",1*4]

>>> l
[1, 'string', 12.33, 'A', 4]

>>> l.append(6)

>>> l
[1, 'string', 12.33, 'A', 4, 6]

>>> l.pop()
6

>>> l
[1, 'string', 12.33, 'A', 4]

>>> t=(1,'string',12.22,'A',2+4)

>>> t
(1, 'string', 12.22, 'A', 6)

>>> t.index()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    t.index()
TypeError: index expected at least 1 argument, got 0

>>> t.index(0)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t.index(0)
ValueError: tuple.index(x): x not in tuple

>>> t.index(1)
0

>>> t.index('string')
1


>>> t.count('string')
1

>>> t.count('strin')
0

>>> i=1

>>> while i<10:
	print(i)
	i+=1

	
1
2
3
4
5
6
7
8
9



>>> for i in 'hellow world':
	print(i)
	
h
e
l
l
o
w
 
w
o
r
l
d



>>> for i in 'hellow','world','python':
	print(i)

	
hellow
world
python

>>> l=[1,2,3,4,'string',12.234]

>>> for i in l:
	print(i)

	
1
2
3
4
string
12.234

>>> for i in range(0,7):
	print(i)

	
0
1
2
3
4
5
6

>>> #===================================================

>>> # string
'

>>> s='A'

>>> S='string'

>>> type(s)
<class 'str'>

>>> type(S)
<class 'str'>

>>> s='welcome to my home'

>>> print(s)
welcome to my home

>>> print('strings with a sing quotes')
strings with a sing quotes

>>> print("I'm gopiraj")
I'm gopiraj

>>> s=''' im studieng python '''

>>> print(s)
 im studieng python 

>>> string='''gopi
              raj
              raj'''

>>> print(string)
gopi
              raj
              raj


>>> print('\n string is sequance of charectors')

 string is sequance of charectors

>>> s='''
         python
         is
         my
         faveride
         language
         '''

>>> print(s)

         python
         is
         my
         faveride
         language
         

>>> s='gopiraj is python student'

>>> s[0]
'g'

>>> s[1]
'o'

>>> len(s)
25

>>> for i in range(0,len(s)):
	print(s[i])

	
g
o
p
i
r
a
j
 
i
s
 
p
y
t
h
o
n
 
s
t
u
d
e
n
t

>>> s[-1]
't'

>>> s[-3]
'e'

>>> s[-24]
'o'

>>> s[-26]
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    s[-26]
IndexError: string index out of range

>>> s['gopi']
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    s['gopi']
TypeError: string indices must be integers

>>> s
'gopiraj is python student'

>>> s[0]
'g'

>>> s[-1]
't'

>>> s='python'

>>> s[0:4]
'pyth'

>>> s[0:]
'python'

>>> s[0:-1]
'pytho'

>>> s[:-1]
'pytho'

>>> s[:]
'python'

>>> s[:4]
'pyth'

>>> s[0::]
'python'

>>> s[0::2]
'pto'

>>> s[0::1]
'python'

>>> s[0::0]
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    s[0::0]
ValueError: slice step cannot be zero

>>> s='gopi raj'


>>> s[0]
'g'

>>> #  string canot changing in bitvin of the string

>>> # only changing  entierd string

>>> s='im so happy'

>>> s='IM SO HAPPY'

>>> print(s)
IM SO HAPPY

>>> s
'IM SO HAPPY'

>>> s[0]
'I'



>>> del s

>>> s
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    s
NameError: name 's' is not defined

>>> s=''' I'm "gopi"'''

>>> print(s)
 I'm "gopi"

>>> s='I\'m "gopi"'

>>> print(s)
I'm "gopi"

>>> s=" I'm \"gopi\""

>>> s
' I\'m "gopi"'

>>> print(s)
 I'm "gopi"

>>> s='c:\\\python\\\myfile'

>>> print(s)
c:\\python\\myfile



>>> s=r'i\'m  gopirasj'

>>> print(s)
i\'m  gopirasj

>>> s=r"i'm  gopirasj"

>>> print(s)

i'm  gopirasj

>>> s=r"i'm  gopirasj \\gopi\\c"

>>> print(s)
i'm  gopirasj \\gopi\\c

>>> string="{}{}{}".format('python ','is','best language')

>>> string
'python isbest language'

>>> string="{2}{1}{0}".format('python ','is','best language')

>>> string
'best languageispython '

>>> string="{first}{second}{third}".format(first='python ',second='is',third='best language')

>>> string
'python isbest language'

>>> string='{0:b}'.format(16)

>>> string
'10000'

>>> print(string)
10000

>>> bin(16)
'0b10000'
>>> 0b10000
16

>>> string='{0:e}'.format(1223.23456789)

>>> print(string)
1.223235e+03

>>> string='{0:.2f}'.format(13/2)

>>> print(string)
6.50

>>> string='{0:.5f}'.format(13/2)

>>> print(string)
6.50000

>>> s="{:<10}{:^10}{:>10}".format('gopi','raj','sathish')

>>> s
'gopi         raj       sathish'

>>> s='{0:^16} is born in {1:<4}'.format('gopiraj',1999)

>>> s
'    gopiraj      is born in 1999'
>>> print(s)

    gopiraj      is born in 1999
