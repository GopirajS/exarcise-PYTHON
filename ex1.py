Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1
1
>>> 1+2
3
>>> 2+3
5
>>> 8+_
13
>>> 8+_
21
>>> 8+_
29
>>> 8+_
37
>>> 8+_
45
>>> 50-2*2
46
>>> (20-2+3)/3
7.0
>>> 3-2
1
>>> 3-4
-1
>>> 2*3
6
>>> 6/4
1.5
>>> 6/2
3.0

>>> 20//2 #floor divition
10

>>> 20%2 #remainder to the divtion
0

>>> 20%3 #remainder to the divtion
2

>>> 3**7 #3 to the power of 7
2187

>>> width=12
>>> height=23
>>> width*height
276

>>>#================================================================




>>> print('gopi raj is laning python at \n')
gopi raj is laning python at 


>>> print('gopi raj is leaning python at \n morning 5 am')
gopi raj is leaning python at 
 morning 5 am

>>> for i in range(5):
	print('hellow world',i,end=" ")

	
hellow world 0 hellow world 1 hellow world 2 hellow world 3 hellow world 4 

>>> for i in range(5):
	print('hellow world',i,end="")

	
hellow world 0hellow world 1hellow world 2hellow world 3hellow world 4

>>> print('gopi');print('raj')
gopi
raj


>>> print('gopi',end='\n');print('raj')
gopi
raj

>>> print('gopi',end='');print('raj')
gopiraj

>>> print('gopi',end=' ');print('raj')
gopi raj

>>> print('gopi',end='--> ');print('raj')
gopi--> raj


>>> l=[1,2,3,4,5]

>>> reversed(l)
<list_reverseiterator object at 0x0000018BC02DEC70>

>>> for i in reversed(l):
	print(i,end=' ')

	
5 4 3 2 1 

>>> l
[1, 2, 3, 4, 5]

>>> print(reversed(l))
<list_reverseiterator object at 0x0000018BC02DEC70>

>>> reversed(range(5))
<range_iterator object at 0x0000018BC234BE10>

>>> for i in reversed(range(5)):
	print(i,end='')

	
43210

>>> import time

>>> for i in reversed(range(4)):
	if i>0:
		print(i,end='>>>')
		time.sleep(1)
	else:
		print('Start')

		
3>>>2>>>1>>>Start

>>> for i in reversed(range(4)):
	if i>0:
		print(i,end='>>>')
		time.sleep(2)
	else:
		print('Start')

		
3>>>2>>>1>>>Start

>>> import os


>>> print('sathish')
sathish

>>> print('kumar')
kumar

>>> l
[1, 2, 3, 4, 5]

>>> print(*l)
1 2 3 4 5

>>> ord('D')
68

>>> ord('\n')
10




>>> print('%d, -->,%f' %(1,23.345))
1, -->,23.345000



>>> print('%d, -->,%5f' %(1,23.345))
1, -->,23.345000

>>> print('%d, -->,%5.2f' %(1,23.345))
1, -->,23.34


>>> print('%d'%12)
12

>>> print('%d'%12.123)
12

>>> print('%f'%12.123)
12.123000

>>> print('%.3f'%12.123)
12.123

>>> print('%1.3f'%12.123)
12.123

>>> print('%1.3f'%0011232.123)
11232.123

>>> print('%2.3f'%11232.123)
11232.123

>>> print('%2.3f'%11232.123)
11232.123

>>> print('%2.3E'%11232.123)
1.123E+04

>>> print('%2.4E'%11232.123)
1.1232E+04

>>> print('%1.4E'%11232.123)
1.1232E+04


>>> print('%o'%112)
160

>>> oct(112)
'0o160'


>>> print('%x'%112)
70

>>> hex(112)
'0x70'



>>> print('{}{}'.format('gopi','raj'))
gopiraj

>>> print('{} {}'.format('gopi','raj'))
gopi raj

>>> print('{1} {0}'.format('gopi','raj'))
raj gopi

>>> print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
I love Geeks for "Geeks!"

>>> print(f"I love Geeks for \"Geeks!\"")
I love Geeks for "Geeks!"

>>> print(f"I love Geeks for \"Geeks!\"")==print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
I love Geeks for "Geeks!"
I love Geeks for "Geeks!"
True



>>> print('{}{}and{other}'.format('gopi','raj',other='sathish kumar'))
gopirajandsathish kumar

>>> print('{} {} and {other}'.format('gopi','raj',other='sathish kumar'))
gopi raj and sathish kumar

>>> d={'name':'gopi','age':'21'}

>>> d2={'name':'sathish','age':'27'}

>>> print('{0[name]} and {0[age]} and {1[name]}'.format(d,d2))
gopi and 21 and sathish

>>> print('{0[name]:s} and {0[age]} and {1[name]}'.format(d,d2))
gopi and 21 and sathish

