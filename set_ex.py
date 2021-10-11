Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=set()
>>> s
set()
>>> s={}
>>> s
{}
>>> s={'python','java','c++'}
>>> s. add('PHP')
>>> s
{'c++', 'java', 'python', 'PHP'}
>>> s.add(10)
>>> s
{'c++', 10, 'PHP', 'python', 'java'}
>>> s.add(12.33)
>>> s
{'c++', 10, 'PHP', 12.33, 'python', 'java'}
>>> d={'apple','orionge'}
>>> s.add()d
SyntaxError: invalid syntax
>>> s.add(d)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.add(d)
TypeError: unhashable type: 'set'
>>> d=('apple','orionge')
>>> s.add(d)
>>> s
{'c++', 10, 'PHP', 12.33, 'python', 'java', ('apple', 'orionge')}
>>> 
>>> s
{'c++', 10, 'PHP', 12.33, 'python', 'java', ('apple', 'orionge')}
>>> s={'python','java','c++'}
>>> 
>>> 
>>> # set add only iterm or tuple
>>> 
>>> 
>>> s
{'c++', 'java', 'python'}
>>> s.add(('gopi','raj'))
>>> s
{'c++', ('gopi', 'raj'), 'java', 'python'}
>>> 
>>> s={'python','java','c++',{'GOPI','RAJ'}}
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s={'python','java','c++',{'GOPI','RAJ'}}
TypeError: unhashable type: 'set'
>>> s={'python','java','c++',['gopi','raj']}
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s={'python','java','c++',['gopi','raj']}
TypeError: unhashable type: 'list'
>>> s={'python','java','c++',('gopi')}
>>> s
{'c++', 'java', 'python', 'gopi'}
>>> s={'python','java','c++',('gopi','raj')}
>>> s
{'c++', ('gopi', 'raj'), 'java', 'python'}
>>> #---------------------------------------
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s=set()
>>> s
set()
>>> s.add('dark')
>>> s
{'dark'}
>>> s.add('go')
>>> s
{'go', 'dark'}
>>> d=('gopi','raj')
>>> s.add(d)
>>> s
{('gopi', 'raj'), 'go', 'dark'}
>>> for i in s:
	i

	
('gopi', 'raj')
'go'
'dark'
>>> 
>>> 
>>> 
>>> #-------------------------------

>>> 
>>> s
{('gopi', 'raj'), 'go', 'dark'}
>>> s.clear()
\
>>> s
set()
>>> s={'gopi','raj','gopal','gowri'}
>>> d={'sathish','kumar'}
>>> s.update(d)
>>> s
{'gopal', 'raj', 'kumar', 'sathish', 'gowri', 'gopi'}
>>> 
>>> #-------------------------------------
>>> 
>>> 
>>> set={'dark','go'}
>>> t=('gopi','raj')
>>> set.update(t)
>>> set
{'raj', 'go', 'dark', 'gopi'}
>>> 
>>> 
>>> 
>>> set
{'raj', 'go', 'dark', 'gopi'}
>>> l=['python','java']
>>> set.update(l)
>>> set
{'raj', 'go', 'python', 'gopi', 'dark', 'java'}
>>> 
>>> 
>>> 
>>> set={'dark','go'}
>>> s={'gopi','raj'}
>>> set.update(s)
>>> set
{'gopi', 'go', 'dark', 'raj'}
>>> 
>>> 
>>> d={1:'gopi',2:'raj'}
>>> set
{'gopi', 'go', 'dark', 'raj'}
>>> set.update(d)
>>> set
{1, 2, 'dark', 'raj', 'go', 'gopi'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> set
{1, 2, 'dark', 'raj', 'go', 'gopi'}
>>> set.update('sathish')
>>> set
{1, 2, 's', 'go', 'a', 'dark', 'raj', 't', 'i', 'gopi', 'h'}
>>> 
>>> 
>>> set={'dark','go'}
>>> set
{'go', 'dark'}
>>> s={"sdfghjkl"}
>>> set={'dark','go'}
>>> set.update(s)
>>> set
{'sdfghjkl', 'go', 'dark'}
>>> 
>>> 
>>> #-----------------------------------------------------------
>>> 
>>> set={'dark','go'}
>>> d={1:'gopi',2:'raj'}
>>> s={"sdfghjkl"}
>>> set.union(d,s)
{1, 2, 'sdfghjkl', 'dark', 'go'}
>>> 
>>> 
>>> #--------------------------
>>> 
>>> set={'dark','go'}
>>> s={'gopi','raj'}
>>> d={'sathish','kumar'}
>>> set.union(s,d)
{'sathish', 'dark', 'raj', 'kumar', 'go', 'gopi'}
>>> set={'dark','go'}
>>> l=['gopi','raj']
>>> set.union(l)
{'raj', 'go', 'dark', 'gopi'}
>>> set | l
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    set | l
TypeError: unsupported operand type(s) for |: 'set' and 'list'
>>> set | s
{'gopi', 'go', 'dark', 'raj'}
>>> 
>>> 
>>> 
>>> nums1 = {1, 2, 2, 3, 4, 5}
>>> nums2 = {4, 5, 6, 7, 8, 8}
>>> nums1.difference(nums2)
{1, 2, 3}
>>> nums1 = {1, 2, 2, 3, 4, 5}
>>> l=['gopi','raj']
>>> nums1.difference(l)
{1, 2, 3, 4, 5}
>>> nums1 = {1, 2, 2, 3, 4, 5}
>>> nums2 = {4, 5, 6, 7, 8, 8}
>>> nums1-nums2
{1, 2, 3}
>>> nums1-l
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    nums1-l
TypeError: unsupported operand type(s) for -: 'set' and 'list'
>>> 
>>> 
>>> 
>>> 
>>> nums2.difference(nums1)
{8, 6, 7}
>>> nums1 = {1, 2, 2, 3, 4, 5}
>>> t=(1,2,3,4)
>>> d={1:'gopi',2:'raj',3:'sathish'}
>>> l=[1,2,3,6]
>>> 
>>> 
>>> nums1.difference(nums2)
{1, 2, 3}
>>> nums1.difference(t)
{5}
>>> nums1.difference(d)
{4, 5}
>>> nums1.difference(l)
{4, 5}
>>> nums1
{1, 2, 3, 4, 5}
>>> nums1.difference(d,l,t,nums2)
set()
>>> 