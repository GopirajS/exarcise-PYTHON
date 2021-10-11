Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


>>> s={1,2,3,4,5,6}

>>> print(type(s))
<class 'set'>

>>> s={1,1.23,'gopi','%',True}

>>> type(s)
<class 'set'>

>>> s={(1,2,'g'),3,4,5,6}

>>> type(s)

<class 'set'>

>>> s
{3, 4, 5, 6, (1, 2, 'g')}

>>> s={[1,2,'g'],3,4,5,6} #cannot add list
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s={[1,2,'g'],3,4,5,6} #cannot add list
TypeError: unhashable type: 'list'

>>> s={{1,2,'g'},3,4,5,6} #cannot add set
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s={{1,2,'g'},3,4,5,6} #cannot add set
TypeError: unhashable type: 'set'

>>> emp={}   #Creat empty set{}

>>> print(emp)
{}

>>> s=set(('gopiraj'))

>>> s
{'g', 'a', 'i', 'o', 'r', 'j', 'p'}

>>> s=set((1,2,3,4,5))

>>> s
{1, 2, 3, 4, 5}

>>> d={1:'gopi',2:'raj'}

>>> s=set(d)

>>> s
{1, 2}

>>> s={1,2,3,4,5,6}

>>> len(s)
6
>>> thisset = {"apple", "banana", "cherry"}

>>> for i in thisset:
	i

	
'apple'
'banana'
'cherry'
 