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
