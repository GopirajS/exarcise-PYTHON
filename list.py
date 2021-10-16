Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>#---------------------------------------------------------------------
>>>                                         #list

>>> lis=[]

>>> type(lis)

<class 'list'>

>>> lis=['gopi','raj',1,True]

>>> type(lis)
<class 'list'>

>>> lis=[1,2,3,4,5,6,6,7,8]

>>> type(lis)
<class 'list'>

>>> lis=['gopi','raj','kumar','satish','salem']

>>> type(lis)
<class 'list'>

>>> lis=['gopi','raj','kumar','satish','salem']

>>> lis[0]
'gopi'

>>> lis[1]
'raj'

>>> lis[:]
['gopi', 'raj', 'kumar', 'satish', 'salem']

>>> lis[0]='Gopiraj'

>>> lis[2]='Sathish'

>>> lis[3]='Kumar'

>>> lis
['Gopiraj', 'raj', 'Sathish', 'Kumar', 'salem']

>>> len(lis)
5

>>> lin[5]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    lin[5]
NameError: name 'lin' is not defined

>>> lin[5]='chennai'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    lin[5]='chennai'
NameError: name 'lin' is not defined

>>> lis=[1,2,3,[4,5,6,[7,8,[9]]],10]

>>> lis[0]
1

>>> lis[2]
3

>>> lis[3]
[4, 5, 6, [7, 8, [9]]]

>>> lis[4]
10

>>> lis[3][0]
4


>>> lis[3][1]
5

>>> lis[3][2]
6

>>> lis[3][3]
[7, 8, [9]]

>>> lis[3][3][0]
7

>>> lis[3][3][1]
8
>>> lis[3][3][2]
[9]

>>> lis[3][3][3]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    lis[3][3][3]
IndexError: list index out of range

>>>#------------------------------------------------------------------------------------------------
>>>                                       #list class

>>> lis=list('hellow')

>>> lis
['h', 'e', 'l', 'l', 'o', 'w']

>>> lis=list((1,2,3))

>>> lis
[1, 2, 3]

>>> lis=list({'gopi','raj','gopi'})
>>> lis
['raj', 'gopi']
>>> 

>>> lis=list({'name':'gopi','age':'21'})
>>> lis
['name', 'age']

>>>#-------------------------------------------------------------
>>>                                     #iterate list


>>> lis=['gopi','raj','kumar','satish','salem']

>>> for i in lis:
	i

	
'gopi'
'raj'
'kumar'
'satish'
'salem'

>>>#--------------------------------------------------------------------
>>>                                    #update list

>>> lis[0]='Gopi'

>>> lis[1]='Raj'


>>> li=['parimal','shanmugam','sathish']

>>> lis.append('parimal')

>>> lis
['Gopi', 'Raj', 'kumar', 'satish', 'salem', 'parimal']

>>>#----------------------------------------------------------------------


>>> #list operater            +,*,[],[:],in,not in

>>> 

>>> l1=['gopi','raj','kumar','satish','salem']
>>> 
>>> 

>>> l2=['parimal','shanmugam','coimpatur']

>>> l1+l2
['gopi', 'raj', 'kumar', 'satish', 'salem', 'parimal', 'shanmugam', 'coimpatur']
>>> 

>>> l1*2
['gopi', 'raj', 'kumar', 'satish', 'salem', 'gopi', 'raj', 'kumar', 'satish', 'salem']

>>> l2*2
['parimal', 'shanmugam', 'coimpatur', 'parimal', 'shanmugam', 'coimpatur']
>>> 
>>> 

>>> l1[0]
'gopi'

>>> l2[0]
'parimal'

>>> l2[3]
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    l2[3]
IndexError: list index out of range


>>> l1[2]
'kumar'

>>> l1[3]
'satish'

>>> l1[4]
'salem'

>>> l1[:]
['gopi', 'raj', 'kumar', 'satish', 'salem']

>>> l1[:4]
['gopi', 'raj', 'kumar', 'satish']

>>> l1[:5]
['gopi', 'raj', 'kumar', 'satish', 'salem']

>>> l1[3:5]
['satish', 'salem']

>>> 'gopi' in l1
True

>>> 'raj' in l1
True

>>> 'gpiraj' not in l1
True

>>> 'kumar' in l1
True
 
	
	
	                                                >>> # list comprehension
>>> 

>>> fruit=['apple','oringe','banana','kiwi','mango']

>>> l=[]

>>> l=[x for x in fruit]

>>> l
['apple', 'oringe', 'banana', 'kiwi', 'mango']

>>> l=[fruit]

>>> l
[['apple', 'oringe', 'banana', 'kiwi', 'mango']]

>>> l=[x for x in fruit if x=='a']

>>> l
[]
>>> l=[x for x in fruit if x!='apple']

>>> l
['oringe', 'banana', 'kiwi', 'mango']

>>> s=[x for x in range(10)]

>>> s
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> s=[x for x in range(10) if x<5]

>>> s
[0, 1, 2, 3, 4]

>>> s=[x.upper() for x in fruit]

>>> s
['APPLE', 'ORINGE', 'BANANA', 'KIWI', 'MANGO']

>>> s=['hello' for i in fruit]

>>> s
['hello', 'hello', 'hello', 'hello', 'hello']

>>> s=[x if x!='banana' else 'sss' for x in fruit ]

>>> s
['apple', 'oringe', 'sss', 'kiwi', 'mango']

>>> s
['apple', 'oringe', 'sss', 'kiwi', 'mango']



>>>                                             # list comrehension
>>> string='This Is An Apple'

>>> n=[]

>>> for i in string:
	if i.lower() in 'aeiou':
		n.append(i)

		
>>> n
['i', 'I', 'A', 'A', 'e']

>>> x=[i for i in string if i.lower() in 'aeiou']

>>> x
['i', 'I', 'A', 'A', 'e']



>>> a1=['live','arm','strong']

>>> a2=['lively','harm','sun','armstrong']

>>> n.clear()

>>> for i in a1:
	for j in a2:
		if i in j :
			n.append(j)

			
>>> n
['lively', 'harm', 'armstrong', 'armstrong']

>>> x=[ j for i in a1 for j in a2 if i in j ]

>>> x
['lively', 'harm', 'armstrong', 'armstrong']

>>> a2
['lively', 'harm', 'sun', 'armstrong']


>>> x=[ i for i in a1 for j in a2 if i in j ]

>>> x
['live', 'arm', 'arm', 'strong']

>>> n=[]

>>> for i in range(1,11):
	if i%2==0:
		n.append(str(i)+':even')
	else:
		n.append(str(i)+":odd")

		
>>> n
['1:odd', '2:even', '3:odd', '4:even', '5:odd', '6:even', '7:odd', '8:even', '9:odd', '10:even']

>>> x=[ str(i)+':even' if i%2==0 else str(i)+':odd' for i in range(1,11) ]

>>> x
['1:odd', '2:even', '3:odd', '4:even', '5:odd', '6:even', '7:odd', '8:even', '9:odd', '10:even']

>>> n=[]

>>> number=[]


>>> n=[]

>>> number=[]

>>> for i in range(3):
	for j in range(3):
		n.append(i)
	number.append(n)

	
>>> number
[[0, 0, 0, 1, 1, 1, 2, 2, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2]]

>>> for i in range(3):
	for j in range(3):
		n.append(j)
	number.append(n)

	
>>> number.clear()

>>> n.clear()

>>> for i in range(3):
	for j in range(3):
		n.append(j)
	number.append(n)

	
>>> number
[[0, 1, 2, 0, 1, 2, 0, 1, 2], [0, 1, 2, 0, 1, 2, 0, 1, 2], [0, 1, 2, 0, 1, 2, 0, 1, 2]]

>>> n.clear()

>>> number.clear()

>>> for i in range(3):
	for j in range(3):
		n.append(j)

>>> n
[0, 1, 2, 0, 1, 2, 0, 1, 2]
>>> for i in range(3):
	for j in range(3):
		n.append(i)

		
>>> n
[0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> n=[]
>>> s=[]
>>> x=[[ i for j in range(3)]for i in range(3)]
>>> x
[[0, 0, 0], [1, 1, 1], [2, 2, 2]]

>>> for i in range(3):
	for j in range(3):
		print(i,end=' ')

		
0 0 0 1 1 1 2 2 2 
>>> for i in range(3):
	for j in range(3):
		print(i,end=' ')
	print('')

	
0 0 0 
1 1 1 
2 2 2 
>>> for i in range(3):
	for j in range(3):
		n.append(i)
	s.append(n)

	
>>> s
[[0, 0, 0, 1, 1, 1, 2, 2, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2]]
>>> for i in range(3):
	n=[]
	for j in range(3):
		n.append(i)
	s.append(n)

	
>>> s.clear()
>>> n.clear()
>>> for i in range(3):
	n=[]
	for j in range(3):
		n.append(i)
	s.append(n)

	
>>> s
[[0, 0, 0], [1, 1, 1], [2, 2, 2]]

>>> a1=['live','arm','strong']

>>> a2=['lively','harm','sun','armstrong']

>>> word=[]

>>> for i in a1:
	for j in a2:
		if i in j:
			word.append(j)

			
>>> word
['lively', 'harm', 'armstrong', 'armstrong']
