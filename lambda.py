Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # lambda fuction
>>> def fuc():
	return 'Hellow Python '

>>> fuc()
'Hellow Python '

>>> lambda :'Hellow Python '
<function <lambda> at 0x000001DAF67D8F70>

>>> (lambda :'Hellow Python ')()
'Hellow Python '

>>> lambda :'Hellow Python '()
<function <lambda> at 0x000001DAF67D8F70>

>>> x=lambda :'Hellow Python '()

>>> x
<function <lambda> at 0x000001DAF67E5040>

>>> x=lambda :'Hellow Python '

>>> x()
'Hellow Python '

>>> def fuc(f,l):
	return "hellow {}{}".format(f,l)


>>> fuc('gopi','raj')
'hellow gopiraj'

>>> x=lambda f,l: "hellow {}{}".format(f,l)

>>> x('gopi','raj')
'hellow gopiraj'

>>> def fuc(name):
	if name[0]=='a' or name[0]=='A':
		return 'hellow ajith'
	else:
		return "name must start with ajith"

	
>>> fuc('ajith')
'hellow ajith'

>>> fuc('gopi')
'name must start with ajith'


>>> x=lambda name: 'hellow {}'.format(name) if name[0]=='a' or name[0]=='A' else 'name must start with  \'a\''

>>> x('ajith')
'hellow ajith'

>>> x('gopi')
"name must start with  'a'"

>>> def fuc(*args):
	return sum(args)

>>> fuc(1,2,3,4)
10

>>> x=lambda *args:sum(args)

>>> x(1,2,3,4)
10

>>> def fuc(**kwarg):
	result=''
	for i in kwarg.values():
		result=result+i
	return result


>>> fuc(name='gopi',name1='raj')
'gopiraj'

>>> fuc(name='gopi',name1='raj',name3='asthish kumar')
'gopirajasthish kumar'



>>> x=lambda **kwargs : [i for i in kwargs.values()]

>>> x(name='gopi',name2='raj',name3='sathish')
['gopi', 'raj', 'sathish']

>>> x=lambda **kwargs : "".join([i for i in kwargs.values()])

>>> x(name='gopi',name2='raj',name3='sathish')
'gopirajsathish'

>>> def prime(x):
	for i in range(2,x):
		if x%i==0:
			return "Not Prime"
		else:
			return 'Prime Number'

		

>>> prime(5)
'Prime Number'

>>> prime(6)
'Not Prime'

>>> x=lambda x:[i for i in range(2,x) if x%i==0   ]


>>> x=lambda x:[i for i in range(2,x) if x%i==0   ]

>>> x(4)
[2]

>>> x=lambda x:[x for i in range(2,x) if x%i==0   ]

>>> x(4)
[4]



>>> s=[('gopi',1000),('raj',1500),('sathish',2000),('kumar',2500)]
>>> sle=map(lambda x: x[1]+100,s)

>>> sle
<map object at 0x000001EFD0BFB9A0>

>>> for i in sle:
	i

	
1100
1600
2100
2600
>>> sle=map(lambda x:(x[0], x[1]+100),s)

>>> sle
<map object at 0x000001EFD0B5C280>

>>> sle=map(lambda x:(x[0], x[1]+100),s)

>>> list(sle)
[('gopi', 1100), ('raj', 1600), ('sathish', 2100), ('kumar', 2600)]

>>> tuple(sle)
()

>>> sl=filter(lambda x: x[1]>1500,s)

>>> list(sl)
[('sathish', 2000), ('kumar', 2500)]

>>> #--------------------------------------------------------------

>>> # syndex: lambda argument : expresion

>>> 
>>> 
>>> x=lambda :'hellow'
>>> x()
'hellow'
>>> x=lambda a:a+1
>>> x(2)
3
>>> 
>>> x=lambda a,b:a+b
>>> x(2,3)
5
>>> 
>>> 
>>> x=lambda a,b,c:a+b+c
>>> x(1,2,3)
6
>>> 
>>> 
>>> def fuc(n):
	print(n)
	return lambda x:x+n

>>> fuc(3)
3
<function fuc.<locals>.<lambda> at 0x0000014367294040>

>>> s=fuc(3)

3

>>> s(2)
5

>>> s=fuc(4)
4

>>> s(4)
8

>>> def fuction(n):
	return lambda x:x*n


>>> s=fuction(2)

>>> s(4)
8

>>> s=fuction(2);d=fuction(4)

>>> s(4);d(2)
8
8

>>> s=lambda a:a*a

>>> s(3)
9

>>> s=lambda name:print('hellow',name)

>>> s('gopi')
hellow gopi

>>> s=lambda *args:sum(args)

>>> s(1,2,23,4,45)
75

>>> (lambda x:x+x)(5)
10

>>> def dosomething(fn):
	print('calling fuction')
	fn()

	
>>> dosomething(lambda :print('hellow world'))
calling fuction
hellow world

>>> my=lambda :print('hellow python ')

>>> dosomething(my)
calling fuction
hellow python 

>>> s=map(lambda x:x,[1,2,3,4,5])

>>> print(s)
<map object at 0x000001436728C6D0>

>>> for i in s:
	i

	
1
2
3
4
5

>>> s=map(lambda x:x+10,[1,2,3,4,5])

>>> for i in s:
	i

	
11
12
13
14
15

>>> t=[i for i in range(1,11)]

>>> t
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> t=[i+2 for i in range(1,11)]

>>> t
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

>>> t=[i*10 for i in range(1,11)]

>>> t
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> for i in t:
	i

	
10
20
30
40
50
60
70
80
90
100

>>> s=lambda a,b:a if a>b else b

>>> s(1,2)
2

>>> l=[1,9,3,7,4,8]

>>> sorted(l)
[1, 3, 4, 7, 8, 9]

>>> List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

>>> List = [[2,4,3],[4, 1, 64, 16],[6, 3, 12, 9]]

>>> s=lambda x: (sorted(i) for i in x)

>>> s
<function <lambda> at 0x0000014367294E50>

>>> s=lambda x: [i for i in x]

>>> s(List)
[[2, 4, 3], [4, 1, 64, 16], [6, 3, 12, 9]]

>>> s=lambda x: [sorted(i) for i in x]

>>> s(List)
[[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

>>> a=s(List)

>>> a
[[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

>>> #d=lambda a:[ i(len(i)-1)for i in a]

>>> 

>>> a
[[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

>>> for i in a:
	i[len(i)-1]

	
4
64
12
>>> for i in a:
	i[len(i)-2]

	
3
16
9
>>> d=lambda a:[ i[len(i)-2] for i in a]

>>> d(a)
[3, 16, 9]

>>> li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

>>> s=list(filter(lambda x:x%2 !=0 ,li))
>>> s
[5, 7, 97, 77, 23, 73, 61]

>>> ages = [13, 90, 17, 59, 21, 60, 5]

>>> s=filter(lambda x:x>18,ages)

>>> s
<filter object at 0x000001436728C9D0>

>>> for i in s:
	i

	
90
59
21
60

>>> li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

 
>>> s=map(lambda x:x*2,li)

>>> list(s)
[10, 14, 44, 194, 108, 124, 154, 46, 146, 122]
>>> li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]


>>> import functools

>>> s=functools.reduce(lambda x,y:x if x>y else y,li)

>>> s
97
