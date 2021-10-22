
>>>                                                              # lists
>>> 

>>> sqr=[]

>>> type(sqr)
<class 'list'>

>>> sqr=[1,4,9,16,25]

>>> sqr[0]
1

>>> sqr[6]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sqr[6]
IndexError: list index out of range

>>> sqr[4]
25

>>> sqr[:4]
[1, 4, 9, 16]

>>> sqr[-1]
25

>>> sqr[-2]
16

>>> sqr[-3:]
[9, 16, 25]

>>> sqr[-3::-1]
[9, 4, 1]

>>> sqr[-3::1]
[9, 16, 25]
>>> 


>>> sqr[:]
[1, 4, 9, 16, 25]

>>> sqr + [36,49,64,81,100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

>>> s=sqr + [36,49,64,81,100]

>>> s
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

>>> s[0]
1

>>> s[0]=2

>>> s
[2, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 


>>> s
[2, 4, 9, 16, 25, 36, 49, 64, 81, 100]

>>> s[5]
36

>>> s[5]=55

>>> s
[2, 4, 9, 16, 25, 55, 49, 64, 81, 100]



>>> letter=['a','b','c','d','e','f','g']

>>> letter
['a', 'b', 'c', 'd', 'e', 'f', 'g']

>>> letter[2:5]=['C','D','E']

>>> letter
['a', 'b', 'C', 'D', 'E', 'f', 'g']

>>> letter[2:5]=[]
>>> letter
['a', 'b', 'f', 'g']
>>> letter[:]
['a', 'b', 'f', 'g']
>>> letter[:]=[]
>>> letter
[]
>>> 	letter=['a','b','c','d','e','f','g']
	
SyntaxError: unexpected indent
>>> letter=['a','b','c','d','e','f','g']
>>> len(letter)
7
>>> 
