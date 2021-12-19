
>>> string='hellow world im gopi raj thish is python world'

>>> print(string)
hellow world im gopi raj thish is python world

>>> string='\nhellow world im gopi raj thish is python world'


>>> print(string)

hellow world im gopi raj thish is python world

>>> string='\nhellow world \nim gopi raj thish is python world'

>>> print(string)

hellow world 
im gopi raj thish is python world


>>> s='''gopi
          raj
          satish
          kuamr'''



>>> print(s)
gopi
          raj
          satish
          kuamr

>>> s='gopiraj'

>>> s
'gopiraj'

>>> s[-1]
'j'

>>> len(s)
7

>>> s[-7]
'g'


>>> s[-1]
'j'


>>> s[7]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s[7]
IndexError: string index out of range

>>> s[6]
'j'

>>> len(s)
7

>>> ~7
-8

>>> ~7-1
-9

>>> ~7+11
3

>>> ~7+1
-7


>>> for i in range(len(s)):
	print(s[i],end='')

	
gopiraj

>>> for i in range(len(s)):
	print(s[i],end=' ')

	
g o p i r a j 

>>> s[0]
'g'

>>> s[-1]
'j'

>>> s[-7]
'g'

>>> s[6]
'j'

>>> s='gopi raj satish kuamr'

>>> s[0]
'g'

>>> s[2]
'p'

>>> s[5]
'r'

>>> s[4]
' '

>>> s[4]
' '


>>> s
'gopi raj satish kuamr'

>>> len(s)
21

>>> s[0:12]
'gopi raj sat'

>>> s[0:19]
'gopi raj satish kua'

>>> s[0:15]
'gopi raj satish'

>>> slice(s)
slice(None, 'gopi raj satish kuamr', None)

>>> s[0:-4]
'gopi raj satish k'

>>> s[0:-4:2]
'gp a aihk'


>>> s[0:-4:1]
'gopi raj satish k'

>>> s[0:-4:-1]
''

>>> s[0:-4:-2]
''

>>> s
'gopi raj satish kuamr'

>>> s[3]
'i'

>>> del s[3]
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    del s[3]
TypeError: 'str' object doesn't support item deletion

>>> del s

>>> s
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s
NameError: name 's' is not defined



>>> print('I\'m \'\"gopi\"')
I'm '"gopi"

>>> print('I\'m \"gopi\"')
I'm "gopi"

>>> print("I'm \"gopi\"")
I'm "gopi"



>>> s="C:\\python\\geek\\"

>>> print(s)
C:\python\geek\


>>> hex(Gopi)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    hex(Gopi)
NameError: name 'Gopi' is not defined

>>> print('\x47\x65\x65\x6b\x73')
Geeks


>>> hex(2)
'0x2'


>>> 0x2
2


>>> 'x47'
'x47'

>>> '\x47'
'G'

>>> hex('G')
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    hex('G')
TypeError: 'str' object cannot be interpreted as an integer

>>> print('{} {} {}'.format('gopi','raj','sathish'))
gopi raj sathish

>>> print('{2} {1} {0}'.format('gopi','raj','sathish'))
sathish raj gopi

>>> print('{}{}{}'.format(name='gopi',age='21',city='salem'))
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    print('{}{}{}'.format(name='gopi',age='21',city='salem'))
IndexError: Replacement index 0 out of range for positional args tuple

>>> print('{name}{age}{city}'.format(name='gopi',age='21',city='salem'))
gopi21salem

>>> print('{name} :{age} :{city}'.format(name='gopi',age='21',city='salem'))

gopi :21 :salem

>>> 1/6
0.16666666666666666

>>> string='{}'.format(1/6)

>>> print(string)

0.16666666666666666

>>> string='{0:0.3}'.format(1/6)

>>> print(string)
0.167

>>> string='{:0.3}'.format(1/6)

>>> print(string)
0.167


>>> string='{1:0.3}'.format(1/6,1.2345)

>>> print(string)
1.23

>>> string='{0:0.3f}'.format(1/6)

>>> print(string)
0.167

>>> s='{:>10}{:^10}{:<10}'.format('gopi','raj','sathish')

>>> print(s)
      gopi   raj    sathish   

>>> print('{:^16} and his born {:>13}'.format('gopiraj',1999))
    gopiraj      and his born          1999

>>> s
'      gopi   raj    sathish   '

>>> s.capitalize
<built-in method capitalize of str object at 0x000001E7B36A81C0>


>>> s=''

>>> print(repr(s))
''

>>> print(s)


>>> print(s)


>>> # logical operator on string in python



>>> s1=''

>>> s2='gopi'

>>> s1 and s2
''

>>> s2 and s1
''

>>> s2 or s1
'gopi'

>>> s1 or s2
'gopi'

>>> s1='gopi'

>>> s2='raj'

>>> s1 and s2
'raj'

>>> s2 and s1
'gopi'


>>> s1 or s2
'gopi'

>>> s1 or s2
'gopi'

>>> s2 or s1
'raj'

>>> s=''

>>> s=' '

>>> not s
False

>>> s=''

>>> not s
True


>>> s='gopi'

>>> not s
False

>>> import string

>>> import string as s

>>> s.Formatter

<class 'string.Formatter'>

>>> t=s.Template('x is $x')

>>> print(t.substitute({'x':1}))
x is 1


>>> print(t.substitute({'x':'gopi'}))
x is gopi

>>> d=s.Template('hi hellow $name ')

>>> l=['gopi','sathish']



>>> for i in l:
	print(i)

	
gopi
sathish


>>> for i in l:
	print(d.substitute(name=i))

	
hi hellow gopi 
hi hellow sathish 

>>> l=[('gopi',12),('sathish',23),('parimala',34)]

>>> t=s.Template('hellow mr $name and you got $mark mark')

>>> for i in l:
	print(t.substitute(name=i[0],	mark=i[1]))

	
hellow mr gopi and you got 12 mark
hellow mr sathish and you got 23 mark
hellow mr parimala and you got 34 mark

>>> a=s.Template('hellow mr $name and his compeny %compeny')

>>> print(a.safe_substitute(name='sathish kuamr',compeny='hemex DX'))
hellow mr sathish kuamr and his compeny %compeny

>>> a=s.Template('hellow mr $name and his compeny $compeny')

>>> print(a.safe_substitute(name='sathish kuamr',compeny='hemex DX'))
hellow mr sathish kuamr and his compeny hemex DX


>>> t='$name is good boy and is age $age'

>>> t=s.Template('$name is good boy and is age $age')

>>> print(t.template())
Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    print(t.template())
TypeError: 'str' object is not callable

>>> print(t.template)
$name is good boy and is age $age


>>> t=s.Template('$$ is sympal of $name')

>>> print(t.substitute(name='gopi'))
$ is sympal of gopi

>>> t=s.Template('$$ is sympal of $name and $(name)y')

>>> print(t.substitute(name='gopiraj'))
Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    print(t.substitute(name='gopiraj'))
  File "C:\Users\gopir\AppData\Local\Programs\Python\Python39\lib\string.py", line 121, in substitute
    return self.pattern.sub(convert, self.template)
  File "C:\Users\gopir\AppData\Local\Programs\Python\Python39\lib\string.py", line 118, in convert
    self._invalid(mo)
  File "C:\Users\gopir\AppData\Local\Programs\Python\Python39\lib\string.py", line 101, in _invalid
    raise ValueError('Invalid placeholder in string: line %d, col %d' %
ValueError: Invalid placeholder in string: line 1, col 27
>>> t=s.Template('$$ is sympal of $name and ${name}y')

>>> print(t.substitute(name='gopiraj'))
$ is sympal of gopiraj and gopirajy

>>> variable=12

>>> variable='12'

>>> string='Variable as string = %s'%(variable)

>>> print(string)
Variable as string = 12

>>> string='Variable as string = %r'%(variable)


>>> print(string)
Variable as string = '12'

>>> variable=int(variable)

>>> variable
12

>>> string='Variable as string = %d'%(variable)

>>> print(string)
Variable as string = 12

>>> string='Variable as string = %o'%(variable)

>>> print(string)
Variable as string = 14

>>> string='Variable as string = %x'%(variable)

>>> print(string)
Variable as string = c

>>> def funtion():
	'''Demonstrate triple  double  question
          docstrings and does  nothing realy'''
	return 'hellow world'



>>> funtion()
'hellow world'


>>> funtion.__doc__
'Demonstrate triple  double  question\n          docstrings and does  nothing realy'

>>> print(funtion.__doc__)
Demonstrate triple  double  question
          docstrings and does  nothing realy

>>> help(funtion.__doc__)
No Python documentation found for 'Demonstrate triple  double  question\n          docstrings and does  nothing realy'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.


>>> def funtion():
	"""
           Demonstrate triple  double  question
          docstrings and does  nothing realy  """
	return 'hellow world'

>>> funtion.__doc__
'\n           Demonstrate triple  double  question\n          docstrings and does  nothing realy  '

>>> print(funtion.__doc__)

           Demonstrate triple  double  question
          docstrings and does  nothing realy  

>>> help(funtion.__doc__)
No Python documentation found for 'Demonstrate triple  double  question\n          docstrings and does  nothing realy'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.


>>> class myclass:
	"""
    This is a class for mathematical operations on complex numbers.
      
    Attributes:
        real (int): The real part of complex number.
        imag (int): The imaginary part of complex number.
    """
	def __init__(self):
		"""
        The constructor for ComplexNumber class.
  
        Parameters:
           real (int): The real part of complex number.
           imag (int): The imaginary part of complex number.   
        """
	def adding(self):
		"""
        The function to add two Complex Numbers.
  
        Parameters:
            num (ComplexNumber): The complex number to be added.
          
        Returns:
            ComplexNumber: A complex number which contains the sum.
        """
		return 'hellow world'

	

>>> myclass.__doc__
'\n    This is a class for mathematical operations on complex numbers.\n      \n    Attributes:\n        real (int): The real part of complex number.\n        imag (int): The imaginary part of complex number.\n    '

>>> print(myclass.__doc__)

    This is a class for mathematical operations on complex numbers.
      
    Attributes:
        real (int): The real part of complex number.
        imag (int): The imaginary part of complex number.
    



>>> help(myclass)
Help on class myclass in module __main__:

class myclass(builtins.object)
 |  This is a class for mathematical operations on complex numbers.
 |    
 |  Attributes:
 |      real (int): The real part of complex number.
 |      imag (int): The imaginary part of complex number.
 |  
 |  Methods defined here:
 |  
 |  __init__(self)
 |      The constructor for ComplexNumber class.
 |      
 |      Parameters:
 |         real (int): The real part of complex number.
 |         imag (int): The imaginary part of complex number.
 |  
 |  adding(self)
 |      The function to add two Complex Numbers.
 |      
 |      Parameters:
 |          num (ComplexNumber): The complex number to be added.
 |        
 |      Returns:
 |          ComplexNumber: A complex number which contains the sum.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)


>>> def checkEmpty(input, pattern): 
        
    # If both are empty  
    if len(input)== 0 and len(pattern)== 0: 
         return 'true'
    
    # If only pattern is empty 
    if len(pattern)== 0: 
         return 'true'
    
    while (len(input) != 0): 
  
        # find sub-string in main string 
        index = input.find(pattern) 
  
        # check if sub-string founded or not 
        if (index ==(-1)): 
          return 'false'
  
        # slice input string in two parts and concatenate 
        input = input[0:index] + input[index + len(pattern):]              
  
    return 'true'

>>> checkEmpty('Gopiraj','Gopi')
'false'

>>> checkEmpty('Gopiraj','Gopiraj')
'true'
>>> checkEmpty('Gopi','Gopiraj')
'false'

>>> input='gopi'

>>> len(input)
4

>>> patten='gopi'

>>> input.find(patten)
0

>>> patten='gopi raj'

>>> input.find(patten)
-1


>>> input = input[0:index] + input[index + len(patten):]
>>> input
'gop'

>>> input='gopiraj'

>>> patten='raj'

>>> index=input.find(patten)

>>> index
4

>>> input=input[0:index]

>>> input
'gopi'

>>> input[0]
'g'

>>> input[0:4]
'gopi'

>>> len(patten)
3

		     
>>>#==============================================================

		    

>>> import collections

>>> import collections as s

>>> s.Counter('gopiraj')
Counter({'g': 1, 'o': 1, 'p': 1, 'i': 1, 'r': 1, 'a': 1, 'j': 1})

>>> d=s.Counter('gopiraj')

>>> d.keys()
dict_keys(['g', 'o', 'p', 'i', 'r', 'a', 'j'])

>>> d.values()
dict_values([1, 1, 1, 1, 1, 1, 1])

>>> def fun(string):
	d=s.Counter(string)
	for i in d.values():
		if i==1:
			print('{} is {} times'.format(d[i],i))

		

>>> fun('gopiraj')
0 is 1 times
0 is 1 times
0 is 1 times
0 is 1 times
0 is 1 times
0 is 1 times
0 is 1 times

>>> d
Counter({'g': 1, 'o': 1, 'p': 1, 'i': 1, 'r': 1, 'a': 1, 'j': 1})

>>> for i in d.keys():
	print(i,end=' ')

	
g o p i r a j 

>>> for i in d.values():
	print(i,end=' ')

	
1 1 1 1 1 1 1 

>>> d[1]
0

>>> d[2]
0

>>> d
Counter({'g': 1, 'o': 1, 'p': 1, 'i': 1, 'r': 1, 'a': 1, 'j': 1})


>>> def fun(string):
	d=s.Counter(string)
	for i in d.values():
		if i==1:
			print('{} is {} times'.format(d[i],i))

			
>>> fun('gopi')
0 is 1 times
0 is 1 times
0 is 1 times
0 is 1 times

>>> d
Counter({'g': 1, 'o': 1, 'p': 1, 'i': 1, 'r': 1, 'a': 1, 'j': 1})

>>> for i in d.keys():
	print(i,end=' ')

	
g o p i r a j 

>>> for i in d.keys():
	print(d[i])

	
1
1
1
1
1
1
1

>>> for i in d.keys():
	print(i,end=' ')
	print(d[i])

	
g 1
o 1
p 1
i 1
r 1
a 1
j 1

>>> def fun(string):
	d=s.Counter(string)
	for i in d.values():
		print(i,'-->',d[i])

		
>>> fun('gopiraj')
1 --> 0
1 --> 0
1 --> 0
1 --> 0
1 --> 0
1 --> 0
1 --> 0

>>> def fun(string):
	d=s.Counter(string)
	for i in d.key():
		print(i)

		

>>> def counter(value):
	d=s.Counter(value)
	print(d)

	
>>> counter('Gopi')
Counter({'G': 1, 'o': 1, 'p': 1, 'i': 1})

>>> def counter(value):

	d=s.Counter(value)
	for i in d.keys():
		if d[i]==1:
			print(i,'-->',d[i])

			
>>> counter('gopiraj')
g --> 1
o --> 1
p --> 1
i --> 1
r --> 1
a --> 1
j --> 1

>>> def counter(value):
	d=s.Counter(value)
	for i in d.keys():
		print(i,'-->',d[i])

		
>>> counter('gopiraj')
g --> 1
o --> 1
p --> 1
i --> 1
r --> 1
a --> 1
j --> 1


>>> def counter(value):
	d=s.Counter(value)
	d.pop(d[' ']
	for i in d.keys():
		print(i,'-->',d[i])
	      

>>> def counter(value):
	d=s.Counter(value)
	d.pop(d[' '])
	for i in d.keys():
		print(i,'-->',d[i])

		



>>> d
Counter({'g': 1, 'o': 1, 'p': 1, 'i': 1, 'r': 1, 'a': 1, 'j': 1})

>>> s.Counter('gopi raj')
Counter({'g': 1, 'o': 1, 'p': 1, 'i': 1, ' ': 1, 'r': 1, 'a': 1, 'j': 1})

>>> f=s.Counter('gopi raj')

>>> f.elements()

<itertools.chain object at 0x0000020F1493E520>
>>> for i in f:

	print(i,end=' ')

	
g o p i   r a j 

>>> f
Counter({'g': 1, 'o': 1, 'p': 1, 'i': 1, ' ': 1, 'r': 1, 'a': 1, 'j': 1})

>>> f.get('g')
1

>>> f.most_common()
[('g', 1), ('o', 1), ('p', 1), ('i', 1), (' ', 1), ('r', 1), ('a', 1), ('j', 1)]

>>> f.pop('g')
1

>>> d
Counter({'g': 1, 'o': 1, 'p': 1, 'i': 1, 'r': 1, 'a': 1, 'j': 1})

>>> def counter(value):
	d=s.Counter(value)
	d.pop(' ')
	for i in d.keys():
		print(i,'-->',d[i])

		

>>> counter('gopi raj')
g --> 1
o --> 1
p --> 1
i --> 1
r --> 1
a --> 1
j --> 1

>>> counter('gopi raj sayish')
g --> 1
o --> 1
p --> 1
i --> 2
r --> 1
a --> 2
j --> 1
s --> 2
y --> 1
h --> 1

>>> l=[1,2,3,4]

>>> reversed(l)
<list_reverseiterator object at 0x0000020F1493E490>

>>> print(reversed(l))
<list_reverseiterator object at 0x0000020F1493EAF0>

>>> for i in reversed(l):
	print(i,end=' ')

	
4 3 2 1 

>>> for i in reversed('gopiraj'):
	print(i)

	
j
a
r
i
p
o
g

>>> def funtion(s):
	str=''
	for i in s:
		str=i+str
	return str


>>> s='gopiraj'

>>> print('original string is:',s)
original string is: gopiraj

>>> print('reversed string is :',s,end='\n')
reversed string is : gopiraj

>>> funtion(s)
'jaripog'

>>> def funtion(s):
	str=''
	for i in s:
		str=str+i
	return str

>>> funtion(s)
'gopiraj'

>>> s
'gopiraj'

>>> def fun(s):
	if len(s)==0:
		return s
	else:
		return reversed(s[1:])

	
>>> fun(s)
<reversed object at 0x0000020F1492BA00>

>>> for i in fun(s):
	print(i,end='')

	
jaripo

>>> def fun(s):
	if len(s)==0:
		return s
	else:
		return reversed(s[1:])+s[0]

	

>>> def fun(s):
	if len(s)==0:
		return s
	else:
		d=reversed(s[1:])
		return d+s[0]

	

>>> def fun(s):
	if len(s)==0:
		return s
	else:
		return reversed(s[1:]) + s[0]

	

>>> return
SyntaxError: 'return' outside function
return

>>> True = return
SyntaxError: cannot assign to True

>>> string='gopiraj'

>>> string=''.join(reversed(string))

>>> print(string)
jaripog

>>> l=''

>>> l=[1,2,3,4,5]

>>> s=' '.join(l)
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    s=' '.join(l)
TypeError: sequence item 0: expected str instance, int found

>>> l=['gopi','raj','sathish']

>>> ''.join(l)
'gopirajsathish'

>>> ' '.join(l)
'gopi raj sathish'

>>> reversed(l)
<list_reverseiterator object at 0x0000020F1492BA00>

>>> for i in reversed(l):
	print(i,end=' ')

	
sathish raj gopi 

>>> for i in reversed(l):
	print(i)

	
sathish
raj
gopi

>>> list(reversed(l))
['sathish', 'raj', 'gopi']

>>> string
'jaripog'

>>> s='gopiraj'

>>> s
'gopiraj'

>>> 7/2
3.5

>>> int(7/2)
3

>>> def funtion(s):
	s=s.lower()
	l=len(s)
	if l<2:
		return "true"
	elif s[0]==s[l-1]:
		return funtion(s[0:l-1])
	else:
		return 'false'

	
>>> funtion('gopiraj')
'false'

>>> funtion('gh')
'false'

>>> len('gj')
2

>>> len('g')
1

>>> funtion('g')
'true'

>>> funtion('malayalam')
'false'

>>> funtion('malayalam')
'false'

>>> s='malayalam'

>>> l=len(s)

>>> s[1:l-1]
'alayala'

>>> s=s[1:l-1]

>>> s[1:l-1]
'layala'

>>> s=s[1:l-1]

>>> s[1:l-1]
'ayala'

>>> s=s[1:l-1]

>>> s[1:l-1]
'yala'

>>> s=s[1:l-1]

>>> s[1:l-1]
'ala'

>>> s=s[1:l-1]

>>> s[1:l-1]
'la'

>>> s=s[1:l-1]

>>> s[1:l-1]
'a'

>>> def isPalindrome(s):
       
    #to change it the string is similar case
    s = s.lower()
    # length of s
    l = len(s)
     
    # if length is less than 2
    if l < 2:
        return True
 
    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:
        
        # Call is pallindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])
 
    else:
        return False


>>> isPalindrome('malayalm')
False

>>> isPalindrome('malayal')
False

>>> isPalindrome('m')
True

>>> def funtion(s):
	s=s.lower()
	l=len(s)
	if l==3:
		return "true"
	elif s[0]==s[l-1]:
		return funtion(s[0:l-1])
	else:
		return 'false'

	
>>> funtion('malayalam')
'false'


>>> def funtion(s):
	s=s.lower()
	l=len(s)
	if l==7:
		return "true"
	elif s[0]==s[l-1]:
		return funtion(s[0:l-1])
	else:
		return 'false'

	
>>> funtion('malayalam')
'false'

>>> def funtion(s):
	s=s.lower()
	l=len(s)
	if l==9:
		return "true"
	elif s[0]==s[l-1]:
		return funtion(s[0:l-1])
	else:
		return 'false'

	
>>> funtion('malayalam')
'true'



>>> def funtion(s):
	s=s.lower()
	l=len(s)
	if l==2:
		return True
	elif s[0]==s[l-1]:
		return funtion(s[1:l-1])
	else:
		return False

	

>>> def funtion(s):
	s=s.lower()
	l=len(s)
	if l<2:
		return True
	elif s[0]==s[l-1]:
		return funtion(s[1:l-1])
	else:
		return False

	
>>> funtion('ala')
True

>>> funtion('malam')
True

>>> s='ala'

>>> l=len(s)

>>> s[1]
'l'

>>> s[1:l-1]
'l'

>>> s
'ala'

>>> s='gopiraj'

>>> reversed(s)

<reversed object at 0x0000020F1493E460>

>>> for i in s:
	print(i,end= ' ')

	
g o p i r a j 

>>> for i in reversed(s):
	print(i,end='')

	
jaripog

>>> s=''.join(s)

>>> s
'gopiraj'

>>> ''.join(s)
'gopiraj'

>>> ''.join(reversed(s))
'jaripog'

		     
		     

>>> import string

>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'

>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

>>> string.capwords('G')
'G'

>>> string.capwords('a')
'A'

>>> string.capwords('gopi')
'Gopi'

>>> string.digits
'0123456789'

>>> type(string.digits)
<class 'str'>

>>> string.hexdigits
'0123456789abcdefABCDEF'

>>> string.hexdigits
'0123456789abcdefABCDEF'

>>> string.octdigits
'01234567'

>>> string.printable
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

>>> string.__doc__
'A collection of string constants.\n\nPublic module variables:\n\nwhitespace -- a string containing all ASCII whitespace\nascii_lowercase -- a string containing all ASCII lowercase letters\nascii_uppercase -- a string containing all ASCII uppercase letters\nascii_letters -- a string containing all ASCII letters\ndigits -- a string containing all ASCII decimal digits\nhexdigits -- a string containing all ASCII hexadecimal digits\noctdigits -- a string containing all ASCII octal digits\npunctuation -- a string containing all ASCII punctuation characters\nprintable -- a string containing all ASCII characters considered printable\n\n'


>>> string.octdigits
'01234567'


>>> import random


>>> random.__doc__
'Random variable generators.\n\n    bytes\n    -----\n           uniform bytes (values between 0 and 255)\n\n    integers\n    --------\n           uniform within range\n\n    sequences\n    ---------\n           pick random element\n           pick random sample\n           pick weighted random sample\n           generate random permutation\n\n    distributions on the real line:\n    ------------------------------\n           uniform\n           triangular\n           normal (Gaussian)\n           lognormal\n           negative exponential\n           gamma\n           beta\n           pareto\n           Weibull\n\n    distributions on the circle (angles 0 to 2pi)\n    ---------------------------------------------\n           circular uniform\n           von Mises\n\nGeneral notes on the underlying Mersenne Twister core generator:\n\n* The period is 2**19937-1.\n* It is one of the most extensively tested generators in existence.\n* The random() method is implemented in C, executes in a single Python step,\n  and is, therefore, threadsafe.\n\n'



>>> random.choice.__doc__
'Choose a random element from a non-empty sequence.'




>>> p = ''.join([random.choice(
                        string.ascii_letters + string.digits)
                        for n in range(10)])

>>> p
'jRreynPe9M'

>>> p
'jRreynPe9M'

>>> p = ''.join([random.choice(
                        string.ascii_letters + string.digits)
                        for n in range(10)])
>>> p
'E9roLfaPM3'

>>> p = ''.join([random.choice(
                        string.ascii_letters + string.digits)
                        for n in range(10)])

>>> p
'yTSfaHWtEA'
>>> p = ''.join([random.choice(string.ascii_letters + string.digits)for n in range(10)])


>>> random.choice(string.ascii_letters+string.hexdigits)
'R'

>>> random.choice(string.ascii_letters+string.hexdigits)
'I'

>>> random.choice(string.ascii_letters+string.hexdigits)
'0'


>>> [random.choice(string.ascii_letters+string.hexdigits) if True else 'false']
['a']

>>> [random.choice(string.ascii_letters+string.hexdigits) if True else 'false']
['Q']

>>> [random.choice(string.ascii_letters+string.hexdigits) if True else 'false']
['4']

>>> [random.choice(string.ascii_letters+string.hexdigits) if False else True ]
[True]

>>> [random.choice(string.ascii_letters+string.hexdigits) if False else True ]
[True]


>>> [random.choice(string.ascii_letters+string.hexdigits) for i in range(10) ]
['b', 'M', 'u', '3', 'W', '9', 'E', 'k', 'm', 'Z']

>>> [random.choice(string.ascii_letters+string.hexdigits) for i in range(10) ]
['c', 'X', 'f', 'b', 'E', '9', 'f', 'D', 'F', 'L']

>>> [random.choice(string.ascii_letters+string.hexdigits) for i in range(10) ]
['C', 's', 'r', 'R', 'W', 'y', '8', 'L', 'd', 'I']

>>> [random.choice(string.ascii_letters+string.hexdigits) for i in range(10) ]
['A', 'u', 'd', 'B', 'C', 'S', '5', 'y', '8', 'c']

>>> ''.join([random.choice(string.ascii_letters+string.hexdigits) for i in range(10) ])
'jVabTAaDbi'


>>> ''.join([random.choice(string.ascii_letters+string.hexdigits) for i in range(10) ])
'F6CTKYF9Ea'

>>> random.choice('gopiraj')
'g'

>>> random.choice('gopiraj')
'p'

>>> random.choice('gopiraj')
'g'

>>> random.choice('gopiraj')
'p'

>>> random.choice('gopiraj')
'o'

>>> random.choice('gopiraj')
'o'

>>> random.choice('gopiraj')
'j'

>>> random.choice('gopiraj')
'r'

>>> random.choice('gopiraj')
'j'

>>> random.choice('asdfghertyuw345567')
't'

>>> random.choice('asdfghertyuw345567')
'5'

>>> random.choice('asdfghertyuw345567')
'e'

>>> random.choice('1234567890')
'0'

>>> random.choice('1234567890')
'7'

>>> random.choice('1234567890')
'4'


>>>#==============================================



>>> import string as a

>>> a.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

>>> s=a.ascii_uppercase


>>> s
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

>>> s
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

>>> def fun(value):
	
	for i in value:
		if i not in a.ascii_letters:
			return False
	return True

>>> fun('gopiraj')
True

>>> fun('gopiraj ')
False

>>> fun('gop iraj ')
False

>>> fun('gop iraj @@')
False

>>> def fun(value):

	for i in value:
		if i  in a.ascii_letters:
			return False
	return True


>>> fun('gopiraj')
False

>>> def fun(s):
	for i in s:
		if i in 'asdfgh':
			return 'True'
		elif i in 'jklzxv':
			return 'YES'
		else:
			return 'NO'
	return 'Complete'

>>> fun('gopirajxyz@@%^')
'True'

>>> fun('opirajxyz@@%^')
'NO'

>>> fun('pirajxyz@@%^')
'NO'

>>> fun('rajxyz@@%^')
'NO'

>>> fun('ajxyz@@%^')
'True'

>>> fun('jxyz@@%^')
'YES'

>>> fun('jxyz@@%^')
'YES'


>>> def fun(s):
	for i in s:
		if i in 'asdfgh':
			print('True')
		elif i in 'jklzxv':
			print('YES')
		else:
			print('No')
	print('complete')

	
>>> fun('gopirajxyz@@%^')
True
No
No
No
No
True
YES
YES
No
YES
No
No
No
No
complete

>>> def fun(s):
	for i in s:
		if i in 'asdfgh':
			print(i,'=','True')
		elif i in 'jklzxv':
			print(i,'=','YES')
		else:
			print(i,'=','No')
	print('complete')

	

>>> fun('gopirajxyz@@%^')
g = True
o = No
p = No
i = No
r = No
a = True
j = YES
x = YES
y = No
z = YES
@ = No
@ = No
% = No
^ = No
complete

>>> a.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

>>> a.Formatter()
<string.Formatter object at 0x000001DDA88ABA30>

>>> a.Formatter.__doc__

>>> a.Formatter.__doc__

>>> print(a.Formatter.__doc__)
None

>>> a.Formatter
<class 'string.Formatter'>

>>> a.Formatter()
<string.Formatter object at 0x000001DDA88ABB20>

>>> a.Formatter('gopiraj')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.Formatter('gopiraj')
TypeError: Formatter() takes no arguments

>>> s=a.Formatter()

>>> s
<string.Formatter object at 0x000001DDA88BE280>

>>> s.parse
<bound method Formatter.parse of <string.Formatter object at 0x000001DDA88BE280>>


>>> t=a.Template('$name is good man' )

>>> t.flags
re.IGNORECASE


>>> import string as s

>>> s.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

>>> s.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'

>>> s.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

>>> s.capwords
<function capwords at 0x000001DDA6A70670>

>>> s.capwords('g')
'G'

>>> s.digits
'0123456789'

>>> s.hexdigits
'0123456789abcdefABCDEF'

>>> s.hexdigits
'0123456789abcdefABCDEF'

>>> s.octdigits
'01234567'

>>> s.printable
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

>>> print(s.printable)
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 	



>>> s.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

>>> s.whitespace
' \t\n\r\x0b\x0c'

>>> print(s.whitespace)
 	

	     	      
	      
	      
>>>#=============================================================



>>> import string as s

>>> s.whitespace
' \t\n\r\x0b\x0c'

>>> print(s.whitespace)
 	


>>> s.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

>>> s.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'

>>> s.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

>>> s.capwords
<function capwords at 0x000001AA8FC00670>

>>> s.capwords('G')
'G'

>>> s.digits
'0123456789'

>>> s.hexdigits
'0123456789abcdefABCDEF'

>>> s.octdigits
'01234567'

>>> s.printable
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

>>> s.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

>>> s.whitespace
' \t\n\r\x0b\x0c'

>>> s.Template
<class 'string.Template'>

>>> 


>>> s.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'

>>> s.ascii_lowercase='gopi'

>>> s
<module 'string' from 'C:\\Users\\gopir\\AppData\\Local\\Programs\\Python\\Python39\\lib\\string.py'>

>>> s.ascii_lowercase
'gopi'

>>> s.ascii_lowercase
'gopi'

>>> import string as s

>>> s.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

>>> s.ascii_lowercase
'gopi'

>>> s.ascii_lowercase='abcdefghijklmnopqrstuvwxyz'

>>> s.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'

>>> text='raj'

>>> text='gopiraj'

>>> result=text.endswith('raj')

>>> result
True

>>> result=text.endswith('raj.')

>>> result
False

>>> len(text)
7

>>> result=text.endswith('raj',0,7)

>>> result
True

>>> result=text.endswith('raj',0,6)

>>> result
False

>>> result=text.endswith('raj',0,8)

>>> result
True

>>> result=text.endswith('raj',0,5)

>>> result
False

>>> result=text.endswith('raj',0,7)


>>> text.startswith('gopi',0,7)
True

>>> text.startswith('gopi',0)
True

>>> text.startswith('gopi',7)
False

>>> text.startswith('opi',1)
True

>>> text.startswith('opi',)
False

>>> text.startswith('opi',)
False

>>> number=123

>>> number.isdigite()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    number.isdigite()
AttributeError: 'int' object has no attribute 'isdigite'

>>> number='123456asd'

>>> number.isdigit()
False

>>> number='123456'

>>> number.isdigit()
True


>>> chr(1)
'\x01'

>>> chr(2)
'\x02'

>>> print(chr(2))


>>> type(chr(2))
<class 'str'>

>>> s=chr(2)

>>> s.isdigit()
False



>>> count=0


>>> count=0

>>> newstring=''

	b=chr(i)
	if b.isdigit()==True:
		count+=1
		newstring+=b

		
>>> count
7

>>> newstring
'0123456'

>>> chr(1)
'\x01'

>>> chr(55)
'7'

>>> chr(3)
'\x03'

>>> for i in range(55):
	print(chr(i),end=' ')

	
         	 
   
                     ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 

>>> s = '\u00B23455'

>>> s
'²3455'


>>> chr('\u00BD')
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    chr('\u00BD')
TypeError: an integer is required (got type str)

>>> print('{}'.format('gopiraj'))
gopiraj

>>> print('{}'.format(122))
122

>>> '{} is {} in {}'.format('gopiraj','math student','muthayammal collage of atrs and science')
'gopiraj is math student in muthayammal collage of atrs and science'

>>> ' hi! my name is{} and im {} years old'.format('gopiraj',22)
' hi! my name isgopiraj and im 22 years old'

>>> '1:{}2:{}3:{}4:{}'.format('one','two','three','four')
'1:one2:two3:three4:four'\

>>> '{3} {2} {1} {0}'.format('first','second','third','fourth')
'fourth third second first'

>>> '{0} is bad boy and his also {1}'.format('gopi','bad')
'gopi is bad boy and his also bad'

>>> '{0:} is bad boy and his also {1}'.format('gopi','bad')
'gopi is bad boy and his also bad'

>>> '{0:7} is bad boy and his also {1}'.format('gopi','bad')
'gopi    is bad boy and his also bad'

>>> '{0:4} is bad boy and his also {1}'.format('gopi','bad')
'gopi is bad boy and his also bad'

>>> '{0:5} is bad boy and his also {1}'.format('gopi','bad')
'gopi  is bad boy and his also bad'

>>> '{0:5} is bad boy and his also {1:10}'.format('gopi','bad')
'gopi  is bad boy and his also bad       '

>>> '{0:5} is bad boy and his also {1:10}'.format('gopi','bad')
'gopi  is bad boy and his also bad       '

>>> def fun(a,b):
	for i in range(a,b):
		print(i,  i**2,  i**3,  i**4)

		

>>> fun(1,6)
1 1 1 1
2 4 8 16
3 9 27 81
4 16 64 256
5 25 125 625

>>> def fun(a,b):
	for i in range(a,b):
		print('{0:6}{1:6}{2:6}'.format(i,  i**2,  i**3))

		
>>> fun(1,6)
     1     1     1
     2     4     8
     3     9    27
     4    16    64
     5    25   125
>>> def fun(a,b):
	for i in range(a,b):
		print('{0:<6}{1:<6}{2:<6}'.format(i,  i**2,  i**3))

		

>>> fun(1,6)
1     1     1     
2     4     8     
3     9     27    
4     16    64    
5     25    125   

>>> def fun(a,b):
	for i in range(a,b):
		print('{0:^6}{1:^6}{2:^6}'.format(i,  i**2,  i**3))

		
>>> fun(1,6)
  1     1     1   
  2     4     8   
  3     9     27  
  4     16    64  
  5     25   125  


>>> def fun(a,b):
	for i in range(a,b):
		print('{0:*^6}{1:^6}{2:^6}'.format(i,  i**2,  i**3))

		

>>> fun(1,6)
**1***  1     1   
**2***  4     8   
**3***  9     27  
**4***  16    64  
**5***  25   125  


>>> def fun(a,b):
	for i in range(a,b):
		print('{0:*^6}{1:$^6}{2:@^6}'.format(i,  i**2,  i**3))

		
>>> fun(1,6)
**1***$$1$$$@@1@@@
**2***$$4$$$@@8@@@
**3***$$9$$$@@27@@
**4***$$16$$@@64@@
**5***$$25$$@125@@

>>> string='{first} {second} {third} '

>>> d={'first':'gopiraj','second':'sathish kumar','third':'gopal'}


>>> string.format(**d)
'gopiraj sathish kumar gopal '



>>> string.format(**d)
'gopiraj sathish kumar gopal '

>>> s='gopiraj'

>>> s.index('gopi')
0


>>> s.find('gopi')
0

>>> s.find('gi')
-1


>>> len('11123 DC')
8

>>> len('11123 DC')-2
6

>>> d='11123 DC'

>>> d[6]
'D'
>>> d[6]!='D'
False


>>> bit_len=d.index('DC')-1

>>> bit_len
5

>>> '\f'
'\x0c'

>>> print('\f')


>>> print('\r')


>>> print('')

>>> ''.isspace()
False

>>> 'gopi'.isspace()
False

>>> 'gopi'.isspace()
False

>>> 'gopi\r'.isspace()
False

>>> '\r'.isspace()
True

>>> '\r gopi'.isspace()
False


>>> s='my name is gopi raj'

>>> c=0

>>> for i in s:
	if s.isspace()==True:
		c+=1

		
>>> c
0

>>> for i in s:
	if (s.isspace())==True:
		c+=1

		
>>> for i in s:
	if (s.isspace())==True:
		c+=1

	
>>> print(c)
0

>>> string = 'My name is Ayush'

>>> for i in s:

	if (string.isspace())==True:
		c+=1

		
>>> c
0


>>> count=0


>>> string = 'My name is Ayush'

>>> for a in string:
    if (a.isspace()) == True:
        count+=1

        
>>> count
3


>>> ''.isspace()
False

>>> ' '.isspace()
True

>>> '  g'.isspace()
False

>>> for i in string:
	if i.isspace():
		count+=1

		
>>> count
6

>>> string
'My name is Ayush'

>>> count=0

>>> for i in string:
	if i.isspace():
		count+=1

		
>>> count
3

>>> s='gopiRAJ sathish KUMAR'

>>> s.swapcase()
'GOPIraj SATHISH kumar'


>>> s='satring'

>>> s.swapcase()
'SATRING'


>>> s='gopi is gopi and gopi is gopi'

>>> s.replace('gopi','Gopiraj')
'Gopiraj is Gopiraj and Gopiraj is Gopiraj'

>>> s.replace('gopi','Gopiraj',3)

'Gopiraj is Gopiraj and Gopiraj is gopi'

>>> s='gopi gopi gopi'

>>> s.replace('o','O')
'gOpi gOpi gOpi'
	      

>>>=========================================================



>>> s='gopiraj'

>>> s.capitalize()
'Gopiraj'

>>> s='GOPIRAJ'

>>> s.casefold()
'gopiraj'

>>> s.center(15,'*')
'****GOPIRAJ****'

>>> s.count('g')
0

>>> s='gopiraj'

>>> s.count('g')
1

>>> s.count('o')
1

>>> s.count('0')
0

>>> s.count('0')
0


>>> s.endswith('i')
False

>>> s.endswith('j')
True

>>> s.endswith('raj')
True

>>> s.endswith('raj')
True

>>> s='gopiraj \t'

>>> s.expandtabs(8)
'gopiraj         '

>>> s.expandtabs(4)
'gopiraj     '

>>> s.find('g')
0

>>> s.find('o')
1

>>> s.find('p')
2

>>> s.find('i')
3

>>> s.find('j')
6

>>> s.find('G')
-1

>>> s='gopi raj  is {}'

>>> s.format('student')
'gopi raj  is student'

>>> s.format_map
<built-in method format_map of str object at 0x000001B703E4CEB0>

>>> s.format_map.__doc__
"S.format_map(mapping) -> str\n\nReturn a formatted version of S, using substitutions from mapping.\nThe substitutions are identified by braces ('{' and '}')."

>>> print(s.format_map.__doc__)
S.format_map(mapping) -> str

Return a formatted version of S, using substitutions from mapping.
The substitutions are identified by braces ('{' and '}').

>>> s.index('g')
0

>>> s.index('G')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s.index('G')
ValueError: substring not found

>>> s.index('g',0,1)
0

>>> s.isalnum()
False

>>> s.isalnum()
False

>>> s='gopi123'

>>> s.isalpha()
False

>>> s.isalnum()
True

>>> 

>>> 
>>> s='gopi  123'


>>> s.isalnum()
False

>>> s.isascii()
True


>>> bin(12)
'0b1100'

>>> s='0b1100'

>>> s.isascii()
True

>>> s.isdecimal()
False

>>> s='12345'

>>> s.isdecimal()
True

>>> s.isdigit()
True

>>> s='12.233'

>>> s.isdecimal()
False

>>> s.isdigit()
False

>>> import encodings

>>> import encodings as e

>>> e.aliases
<module 'encodings.aliases' from 'C:\\Users\\gopir\\AppData\\Local\\Programs\\Python\\Python39\\lib\\encodings\\aliases.py'>

>>> print(e.aliases)
<module 'encodings.aliases' from 'C:\\Users\\gopir\\AppData\\Local\\Programs\\Python\\Python39\\lib\\encodings\\aliases.py'>


>>> e.aliases.aliases.keys()

dict_keys(['646', 'ansi_x3.4_1968', 'ansi_x3_4_1968', 'ansi_x3.4_1986', 'cp367', 'csascii', 'ibm367', 'iso646_us', 'iso_646.irv_1991', 'iso_ir_6', 'us', 'us_ascii', 'base64', 'base_64', 'big5_tw', 'csbig5', 'big5_hkscs', 'hkscs', 'bz2', '037', 'csibm037', 'ebcdic_cp_ca', 'ebcdic_cp_nl', 'ebcdic_cp_us', 'ebcdic_cp_wt', 'ibm037', 'ibm039', '1026', 'csibm1026', 'ibm1026', '1125', 'ibm1125', 'cp866u', 'ruscii', '1140', 'ibm1140', '1250', 'windows_1250', '1251', 'windows_1251', '1252', 'windows_1252', '1253', 'windows_1253', '1254', 'windows_1254', '1255', 'windows_1255', '1256', 'windows_1256', '1257', 'windows_1257', '1258', 'windows_1258', '273', 'ibm273', 'csibm273', '424', 'csibm424', 'ebcdic_cp_he', 'ibm424', '437', 'cspc8codepage437', 'ibm437', '500', 'csibm500', 'ebcdic_cp_be', 'ebcdic_cp_ch', 'ibm500', '775', 'cspc775baltic', 'ibm775', '850', 'cspc850multilingual', 'ibm850', '852', 'cspcp852', 'ibm852', '855', 'csibm855', 'ibm855', '857', 'csibm857', 'ibm857', '858', 'csibm858', 'ibm858', '860', 'csibm860', 'ibm860', '861', 'cp_is', 'csibm861', 'ibm861', '862', 'cspc862latinhebrew', 'ibm862', '863', 'csibm863', 'ibm863', '864', 'csibm864', 'ibm864', '865', 'csibm865', 'ibm865', '866', 'csibm866', 'ibm866', '869', 'cp_gr', 'csibm869', 'ibm869', '932', 'ms932', 'mskanji', 'ms_kanji', '949', 'ms949', 'uhc', '950', 'ms950', 'jisx0213', 'eucjis2004', 'euc_jis2004', 'eucjisx0213', 'eucjp', 'ujis', 'u_jis', 'euckr', 'korean', 'ksc5601', 'ks_c_5601', 'ks_c_5601_1987', 'ksx1001', 'ks_x_1001', 'gb18030_2000', 'chinese', 'csiso58gb231280', 'euc_cn', 'euccn', 'eucgb2312_cn', 'gb2312_1980', 'gb2312_80', 'iso_ir_58', '936', 'cp936', 'ms936', 'hex', 'roman8', 'r8', 'csHPRoman8', 'cp1051', 'ibm1051', 'hzgb', 'hz_gb', 'hz_gb_2312', 'csiso2022jp', 'iso2022jp', 'iso_2022_jp', 'iso2022jp_1', 'iso_2022_jp_1', 'iso2022jp_2', 'iso_2022_jp_2', 'iso_2022_jp_2004', 'iso2022jp_2004', 'iso2022jp_3', 'iso_2022_jp_3', 'iso2022jp_ext', 'iso_2022_jp_ext', 'csiso2022kr', 'iso2022kr', 'iso_2022_kr', 'csisolatin6', 'iso_8859_10', 'iso_8859_10_1992', 'iso_ir_157', 'l6', 'latin6', 'thai', 'iso_8859_11', 'iso_8859_11_2001', 'iso_8859_13', 'l7', 'latin7', 'iso_8859_14', 'iso_8859_14_1998', 'iso_celtic', 'iso_ir_199', 'l8', 'latin8', 'iso_8859_15', 'l9', 'latin9', 'iso_8859_16', 'iso_8859_16_2001', 'iso_ir_226', 'l10', 'latin10', 'csisolatin2', 'iso_8859_2', 'iso_8859_2_1987', 'iso_ir_101', 'l2', 'latin2', 'csisolatin3', 'iso_8859_3', 'iso_8859_3_1988', 'iso_ir_109', 'l3', 'latin3', 'csisolatin4', 'iso_8859_4', 'iso_8859_4_1988', 'iso_ir_110', 'l4', 'latin4', 'csisolatincyrillic', 'cyrillic', 'iso_8859_5', 'iso_8859_5_1988', 'iso_ir_144', 'arabic', 'asmo_708', 'csisolatinarabic', 'ecma_114', 'iso_8859_6', 'iso_8859_6_1987', 'iso_ir_127', 'csisolatingreek', 'ecma_118', 'elot_928', 'greek', 'greek8', 'iso_8859_7', 'iso_8859_7_1987', 'iso_ir_126', 'csisolatinhebrew', 'hebrew', 'iso_8859_8', 'iso_8859_8_1988', 'iso_ir_138', 'csisolatin5', 'iso_8859_9', 'iso_8859_9_1989', 'iso_ir_148', 'l5', 'latin5', 'cp1361', 'ms1361', 'cskoi8r', 'kz_1048', 'rk1048', 'strk1048_2002', '8859', 'cp819', 'csisolatin1', 'ibm819', 'iso8859', 'iso8859_1', 'iso_8859_1', 'iso_8859_1_1987', 'iso_ir_100', 'l1', 'latin', 'latin1', 'maccyrillic', 'macgreek', 'maciceland', 'maccentraleurope', 'mac_centeuro', 'maclatin2', 'macintosh', 'macroman', 'macturkish', 'ansi', 'dbcs', 'csptcp154', 'pt154', 'cp154', 'cyrillic_asian', 'quopri', 'quoted_printable', 'quotedprintable', 'rot13', 'csshiftjis', 'shiftjis', 'sjis', 's_jis', 'shiftjis2004', 'sjis_2004', 's_jis_2004', 'shiftjisx0213', 'sjisx0213', 's_jisx0213', 'tis620', 'tis_620_0', 'tis_620_2529_0', 'tis_620_2529_1', 'iso_ir_166', 'u16', 'utf16', 'unicodebigunmarked', 'utf_16be', 'unicodelittleunmarked', 'utf_16le', 'u32', 'utf32', 'utf_32be', 'utf_32le', 'u7', 'utf7', 'unicode_1_1_utf_7', 'u8', 'utf', 'utf8', 'utf8_ucs2', 'utf8_ucs4', 'cp65001', 'uu', 'zip', 'zlib', 'x_mac_japanese', 'x_mac_korean', 'x_mac_simp_chinese', 'x_mac_trad_chinese'])

>>> e.aliases.aliases()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    e.aliases.aliases()
TypeError: 'dict' object is not callable

>>> e.aliases.aliases
{'646': 'ascii', 'ansi_x3.4_1968': 'ascii', 'ansi_x3_4_1968': 'ascii', 'ansi_x3.4_1986': 'ascii', 'cp367': 'ascii', 'csascii': 'ascii', 'ibm367': 'ascii', 'iso646_us': 'ascii', 'iso_646.irv_1991': 'ascii', 'iso_ir_6': 'ascii', 'us': 'ascii', 'us_ascii': 'ascii', 'base64': 'base64_codec', 'base_64': 'base64_codec', 'big5_tw': 'big5', 'csbig5': 'big5', 'big5_hkscs': 'big5hkscs', 'hkscs': 'big5hkscs', 'bz2': 'bz2_codec', '037': 'cp037', 'csibm037': 'cp037', 'ebcdic_cp_ca': 'cp037', 'ebcdic_cp_nl': 'cp037', 'ebcdic_cp_us': 'cp037', 'ebcdic_cp_wt': 'cp037', 'ibm037': 'cp037', 'ibm039': 'cp037', '1026': 'cp1026', 'csibm1026': 'cp1026', 'ibm1026': 'cp1026', '1125': 'cp1125', 'ibm1125': 'cp1125', 'cp866u': 'cp1125', 'ruscii': 'cp1125', '1140': 'cp1140', 'ibm1140': 'cp1140', '1250': 'cp1250', 'windows_1250': 'cp1250', '1251': 'cp1251', 'windows_1251': 'cp1251', '1252': 'cp1252', 'windows_1252': 'cp1252', '1253': 'cp1253', 'windows_1253': 'cp1253', '1254': 'cp1254', 'windows_1254': 'cp1254', '1255': 'cp1255', 'windows_1255': 'cp1255', '1256': 'cp1256', 'windows_1256': 'cp1256', '1257': 'cp1257', 'windows_1257': 'cp1257', '1258': 'cp1258', 'windows_1258': 'cp1258', '273': 'cp273', 'ibm273': 'cp273', 'csibm273': 'cp273', '424': 'cp424', 'csibm424': 'cp424', 'ebcdic_cp_he': 'cp424', 'ibm424': 'cp424', '437': 'cp437', 'cspc8codepage437': 'cp437', 'ibm437': 'cp437', '500': 'cp500', 'csibm500': 'cp500', 'ebcdic_cp_be': 'cp500', 'ebcdic_cp_ch': 'cp500', 'ibm500': 'cp500', '775': 'cp775', 'cspc775baltic': 'cp775', 'ibm775': 'cp775', '850': 'cp850', 'cspc850multilingual': 'cp850', 'ibm850': 'cp850', '852': 'cp852', 'cspcp852': 'cp852', 'ibm852': 'cp852', '855': 'cp855', 'csibm855': 'cp855', 'ibm855': 'cp855', '857': 'cp857', 'csibm857': 'cp857', 'ibm857': 'cp857', '858': 'cp858', 'csibm858': 'cp858', 'ibm858': 'cp858', '860': 'cp860', 'csibm860': 'cp860', 'ibm860': 'cp860', '861': 'cp861', 'cp_is': 'cp861', 'csibm861': 'cp861', 'ibm861': 'cp861', '862': 'cp862', 'cspc862latinhebrew': 'cp862', 'ibm862': 'cp862', '863': 'cp863', 'csibm863': 'cp863', 'ibm863': 'cp863', '864': 'cp864', 'csibm864': 'cp864', 'ibm864': 'cp864', '865': 'cp865', 'csibm865': 'cp865', 'ibm865': 'cp865', '866': 'cp866', 'csibm866': 'cp866', 'ibm866': 'cp866', '869': 'cp869', 'cp_gr': 'cp869', 'csibm869': 'cp869', 'ibm869': 'cp869', '932': 'cp932', 'ms932': 'cp932', 'mskanji': 'cp932', 'ms_kanji': 'cp932', '949': 'cp949', 'ms949': 'cp949', 'uhc': 'cp949', '950': 'cp950', 'ms950': 'cp950', 'jisx0213': 'euc_jis_2004', 'eucjis2004': 'euc_jis_2004', 'euc_jis2004': 'euc_jis_2004', 'eucjisx0213': 'euc_jisx0213', 'eucjp': 'euc_jp', 'ujis': 'euc_jp', 'u_jis': 'euc_jp', 'euckr': 'euc_kr', 'korean': 'euc_kr', 'ksc5601': 'euc_kr', 'ks_c_5601': 'euc_kr', 'ks_c_5601_1987': 'euc_kr', 'ksx1001': 'euc_kr', 'ks_x_1001': 'euc_kr', 'gb18030_2000': 'gb18030', 'chinese': 'gb2312', 'csiso58gb231280': 'gb2312', 'euc_cn': 'gb2312', 'euccn': 'gb2312', 'eucgb2312_cn': 'gb2312', 'gb2312_1980': 'gb2312', 'gb2312_80': 'gb2312', 'iso_ir_58': 'gb2312', '936': 'gbk', 'cp936': 'gbk', 'ms936': 'gbk', 'hex': 'hex_codec', 'roman8': 'hp_roman8', 'r8': 'hp_roman8', 'csHPRoman8': 'hp_roman8', 'cp1051': 'hp_roman8', 'ibm1051': 'hp_roman8', 'hzgb': 'hz', 'hz_gb': 'hz', 'hz_gb_2312': 'hz', 'csiso2022jp': 'iso2022_jp', 'iso2022jp': 'iso2022_jp', 'iso_2022_jp': 'iso2022_jp', 'iso2022jp_1': 'iso2022_jp_1', 'iso_2022_jp_1': 'iso2022_jp_1', 'iso2022jp_2': 'iso2022_jp_2', 'iso_2022_jp_2': 'iso2022_jp_2', 'iso_2022_jp_2004': 'iso2022_jp_2004', 'iso2022jp_2004': 'iso2022_jp_2004', 'iso2022jp_3': 'iso2022_jp_3', 'iso_2022_jp_3': 'iso2022_jp_3', 'iso2022jp_ext': 'iso2022_jp_ext', 'iso_2022_jp_ext': 'iso2022_jp_ext', 'csiso2022kr': 'iso2022_kr', 'iso2022kr': 'iso2022_kr', 'iso_2022_kr': 'iso2022_kr', 'csisolatin6': 'iso8859_10', 'iso_8859_10': 'iso8859_10', 'iso_8859_10_1992': 'iso8859_10', 'iso_ir_157': 'iso8859_10', 'l6': 'iso8859_10', 'latin6': 'iso8859_10', 'thai': 'iso8859_11', 'iso_8859_11': 'iso8859_11', 'iso_8859_11_2001': 'iso8859_11', 'iso_8859_13': 'iso8859_13', 'l7': 'iso8859_13', 'latin7': 'iso8859_13', 'iso_8859_14': 'iso8859_14', 'iso_8859_14_1998': 'iso8859_14', 'iso_celtic': 'iso8859_14', 'iso_ir_199': 'iso8859_14', 'l8': 'iso8859_14', 'latin8': 'iso8859_14', 'iso_8859_15': 'iso8859_15', 'l9': 'iso8859_15', 'latin9': 'iso8859_15', 'iso_8859_16': 'iso8859_16', 'iso_8859_16_2001': 'iso8859_16', 'iso_ir_226': 'iso8859_16', 'l10': 'iso8859_16', 'latin10': 'iso8859_16', 'csisolatin2': 'iso8859_2', 'iso_8859_2': 'iso8859_2', 'iso_8859_2_1987': 'iso8859_2', 'iso_ir_101': 'iso8859_2', 'l2': 'iso8859_2', 'latin2': 'iso8859_2', 'csisolatin3': 'iso8859_3', 'iso_8859_3': 'iso8859_3', 'iso_8859_3_1988': 'iso8859_3', 'iso_ir_109': 'iso8859_3', 'l3': 'iso8859_3', 'latin3': 'iso8859_3', 'csisolatin4': 'iso8859_4', 'iso_8859_4': 'iso8859_4', 'iso_8859_4_1988': 'iso8859_4', 'iso_ir_110': 'iso8859_4', 'l4': 'iso8859_4', 'latin4': 'iso8859_4', 'csisolatincyrillic': 'iso8859_5', 'cyrillic': 'iso8859_5', 'iso_8859_5': 'iso8859_5', 'iso_8859_5_1988': 'iso8859_5', 'iso_ir_144': 'iso8859_5', 'arabic': 'iso8859_6', 'asmo_708': 'iso8859_6', 'csisolatinarabic': 'iso8859_6', 'ecma_114': 'iso8859_6', 'iso_8859_6': 'iso8859_6', 'iso_8859_6_1987': 'iso8859_6', 'iso_ir_127': 'iso8859_6', 'csisolatingreek': 'iso8859_7', 'ecma_118': 'iso8859_7', 'elot_928': 'iso8859_7', 'greek': 'iso8859_7', 'greek8': 'iso8859_7', 'iso_8859_7': 'iso8859_7', 'iso_8859_7_1987': 'iso8859_7', 'iso_ir_126': 'iso8859_7', 'csisolatinhebrew': 'iso8859_8', 'hebrew': 'iso8859_8', 'iso_8859_8': 'iso8859_8', 'iso_8859_8_1988': 'iso8859_8', 'iso_ir_138': 'iso8859_8', 'csisolatin5': 'iso8859_9', 'iso_8859_9': 'iso8859_9', 'iso_8859_9_1989': 'iso8859_9', 'iso_ir_148': 'iso8859_9', 'l5': 'iso8859_9', 'latin5': 'iso8859_9', 'cp1361': 'johab', 'ms1361': 'johab', 'cskoi8r': 'koi8_r', 'kz_1048': 'kz1048', 'rk1048': 'kz1048', 'strk1048_2002': 'kz1048', '8859': 'latin_1', 'cp819': 'latin_1', 'csisolatin1': 'latin_1', 'ibm819': 'latin_1', 'iso8859': 'latin_1', 'iso8859_1': 'latin_1', 'iso_8859_1': 'latin_1', 'iso_8859_1_1987': 'latin_1', 'iso_ir_100': 'latin_1', 'l1': 'latin_1', 'latin': 'latin_1', 'latin1': 'latin_1', 'maccyrillic': 'mac_cyrillic', 'macgreek': 'mac_greek', 'maciceland': 'mac_iceland', 'maccentraleurope': 'mac_latin2', 'mac_centeuro': 'mac_latin2', 'maclatin2': 'mac_latin2', 'macintosh': 'mac_roman', 'macroman': 'mac_roman', 'macturkish': 'mac_turkish', 'ansi': 'mbcs', 'dbcs': 'mbcs', 'csptcp154': 'ptcp154', 'pt154': 'ptcp154', 'cp154': 'ptcp154', 'cyrillic_asian': 'ptcp154', 'quopri': 'quopri_codec', 'quoted_printable': 'quopri_codec', 'quotedprintable': 'quopri_codec', 'rot13': 'rot_13', 'csshiftjis': 'shift_jis', 'shiftjis': 'shift_jis', 'sjis': 'shift_jis', 's_jis': 'shift_jis', 'shiftjis2004': 'shift_jis_2004', 'sjis_2004': 'shift_jis_2004', 's_jis_2004': 'shift_jis_2004', 'shiftjisx0213': 'shift_jisx0213', 'sjisx0213': 'shift_jisx0213', 's_jisx0213': 'shift_jisx0213', 'tis620': 'tis_620', 'tis_620_0': 'tis_620', 'tis_620_2529_0': 'tis_620', 'tis_620_2529_1': 'tis_620', 'iso_ir_166': 'tis_620', 'u16': 'utf_16', 'utf16': 'utf_16', 'unicodebigunmarked': 'utf_16_be', 'utf_16be': 'utf_16_be', 'unicodelittleunmarked': 'utf_16_le', 'utf_16le': 'utf_16_le', 'u32': 'utf_32', 'utf32': 'utf_32', 'utf_32be': 'utf_32_be', 'utf_32le': 'utf_32_le', 'u7': 'utf_7', 'utf7': 'utf_7', 'unicode_1_1_utf_7': 'utf_7', 'u8': 'utf_8', 'utf': 'utf_8', 'utf8': 'utf_8', 'utf8_ucs2': 'utf_8', 'utf8_ucs4': 'utf_8', 'cp65001': 'utf_8', 'uu': 'uu_codec', 'zip': 'zlib_codec', 'zlib': 'zlib_codec', 'x_mac_japanese': 'shift_jis', 'x_mac_korean': 'euc_kr', 'x_mac_simp_chinese': 'gb2312', 'x_mac_trad_chinese': 'big5'}


>>> s=e.aliases.aliases.keys()

>>> for i in s:
	print('{0:6}'.format(i),end=' ')

	
646    ansi_x3.4_1968 ansi_x3_4_1968 ansi_x3.4_1986 cp367  csascii ibm367 iso646_us iso_646.irv_1991 iso_ir_6 us     us_ascii base64 base_64 big5_tw csbig5 big5_hkscs hkscs  bz2    037    csibm037 ebcdic_cp_ca ebcdic_cp_nl ebcdic_cp_us ebcdic_cp_wt ibm037 ibm039 1026   csibm1026 ibm1026 1125   ibm1125 cp866u ruscii 1140   ibm1140 1250   windows_1250 1251   windows_1251 1252   windows_1252 1253   windows_1253 1254   windows_1254 1255   windows_1255 1256   windows_1256 1257   windows_1257 1258   windows_1258 273    ibm273 csibm273 424    csibm424 ebcdic_cp_he ibm424 437    cspc8codepage437 ibm437 500    csibm500 ebcdic_cp_be ebcdic_cp_ch ibm500 775    cspc775baltic ibm775 850    cspc850multilingual ibm850 852    cspcp852 ibm852 855    csibm855 ibm855 857    csibm857 ibm857 858    csibm858 ibm858 860    csibm860 ibm860 861    cp_is  csibm861 ibm861 862    cspc862latinhebrew ibm862 863    csibm863 ibm863 864    csibm864 ibm864 865    csibm865 ibm865 866    csibm866 ibm866 869    cp_gr  csibm869 ibm869 932    ms932  mskanji ms_kanji 949    ms949  uhc    950    ms950  jisx0213 eucjis2004 euc_jis2004 eucjisx0213 eucjp  ujis   u_jis  euckr  korean ksc5601 ks_c_5601 ks_c_5601_1987 ksx1001 ks_x_1001 gb18030_2000 chinese csiso58gb231280 euc_cn euccn  eucgb2312_cn gb2312_1980 gb2312_80 iso_ir_58 936    cp936  ms936  hex    roman8 r8     csHPRoman8 cp1051 ibm1051 hzgb   hz_gb  hz_gb_2312 csiso2022jp iso2022jp iso_2022_jp iso2022jp_1 iso_2022_jp_1 iso2022jp_2 iso_2022_jp_2 iso_2022_jp_2004 iso2022jp_2004 iso2022jp_3 iso_2022_jp_3 iso2022jp_ext iso_2022_jp_ext csiso2022kr iso2022kr iso_2022_kr csisolatin6 iso_8859_10 iso_8859_10_1992 iso_ir_157 l6     latin6 thai   iso_8859_11 iso_8859_11_2001 iso_8859_13 l7     latin7 iso_8859_14 iso_8859_14_1998 iso_celtic iso_ir_199 l8     latin8 iso_8859_15 l9     latin9 iso_8859_16 iso_8859_16_2001 iso_ir_226 l10    latin10 csisolatin2 iso_8859_2 iso_8859_2_1987 iso_ir_101 l2     latin2 csisolatin3 iso_8859_3 iso_8859_3_1988 iso_ir_109 l3     latin3 csisolatin4 iso_8859_4 iso_8859_4_1988 iso_ir_110 l4     latin4 csisolatincyrillic cyrillic iso_8859_5 iso_8859_5_1988 iso_ir_144 arabic asmo_708 csisolatinarabic ecma_114 iso_8859_6 iso_8859_6_1987 iso_ir_127 csisolatingreek ecma_118 elot_928 greek  greek8 iso_8859_7 iso_8859_7_1987 iso_ir_126 csisolatinhebrew hebrew iso_8859_8 iso_8859_8_1988 iso_ir_138 csisolatin5 iso_8859_9 iso_8859_9_1989 iso_ir_148 l5     latin5 cp1361 ms1361 cskoi8r kz_1048 rk1048 strk1048_2002 8859   cp819  csisolatin1 ibm819 iso8859 iso8859_1 iso_8859_1 iso_8859_1_1987 iso_ir_100 l1     latin  latin1 maccyrillic macgreek maciceland maccentraleurope mac_centeuro maclatin2 macintosh macroman macturkish ansi   dbcs   csptcp154 pt154  cp154  cyrillic_asian quopri quoted_printable quotedprintable rot13  csshiftjis shiftjis sjis   s_jis  shiftjis2004 sjis_2004 s_jis_2004 shiftjisx0213 sjisx0213 s_jisx0213 tis620 tis_620_0 tis_620_2529_0 tis_620_2529_1 iso_ir_166 u16    utf16  unicodebigunmarked utf_16be unicodelittleunmarked utf_16le u32    utf32  utf_32be utf_32le u7     utf7   unicode_1_1_utf_7 u8     utf    utf8   utf8_ucs2 utf8_ucs4 cp65001 uu     zip    zlib   x_mac_japanese x_mac_korean x_mac_simp_chinese x_mac_trad_chinese 



>>> for i in s:
	if i=='utf8':
		print('yes')

		
yes

>>> type(s)
<class 'dict_keys'>

>>> for i in s:
	if i=="ascii":
		print('yes')


>>> for i in s:
	if i=='ascii':
		print('yes')

		

>>> for i in s:
	if i=='ascii':
		print('yes')
else:
	print('No')

	
No


>>> d='gopi raj sathish'

>>> d.encode('utf8','ignore')
b'gopi raj sathish'

>>> d.encode('ascii','ignore')
b'gopi raj sathish'

>>> d.encode('ascii','replace')
b'gopi raj sathish'

>>> def fun(input,replaces,str):
	return input.replece(replaces,str)



>>> def fun(inpu,replaces,str):
	return inpu.replece(replaces,str)



>>> def fun(inpu,replaces,st):
	return inpu.replece(replaces,st)


>>> s='gopi'

>>> s=''

>>> def fun(s,d,t):
	return s.replace(d,t)

>>> fun('gopi raj sathish ','sathish','SATHGIUSH')
'gopi raj SATHGIUSH '

>>> s='gopi'

>>> s.zfill(4)
'gopi'

>>> s.zfill(6)
'00gopi'

>>> s='weekyourweek'

>>> s.maketrans('wy','gf','u')
{119: 103, 121: 102, 117: None}

>>> d=s.maketrans('wy','gf','u')

>>> s.translate(d)
'geekforgeek'

>>> s='GopiRaja'

>>> s[0]
'G'


>>> s.maketrans('GR','gr')
{71: 103, 82: 114}

>>> s.maketrans('GR','gr','a')
{71: 103, 82: 114, 97: None}

>>> s.translate(s.maketrans('GR','gr','a'))
'gopirj'

>>> s
'GopiRaja'

>>> s=s.translate(s.maketrans('GR','gr','a'))

>>> s
'gopirj'


>>> s='gopiraj'

>>> s.isidentifier()
True

>>> s='Gopi'

>>> s.isidentifier()
True

>>> s='gopi raj'

>>> s.isidentifier()
False

>>> s.title()

'Gopi Raj'
>>> s.lower()
'gopi raj'

>>> s.splitlines()
['gopi raj']

>>> s='gopi raj sarhish\n and this is my name'

>>> s.splitlines()
['gopi raj sarhish', ' and this is my name']


>>> s.upper()
'GOPI RAJ SARHISH\n AND THIS IS MY NAME'


>>> s.zfill(12)
'gopi raj sarhish\n and this is my name'

>>> s.zfill(56)
'0000000000000000000gopi raj sarhish\n and this is my name'


>>> s.startswith('g')
True

>>> s.startswith('gopi')
True

>>> s
'gopi raj sarhish\n and this is my name'

>>> s='gopi raj sathish'

>>> s.split(' ')
['gopi', 'raj', 'sathish']

>>> s.partition('raj')
('gopi ', 'raj', ' sathish')

>>> s.partition(' ')
('gopi', ' ', 'raj sathish')



>>> s='gopi raj sathish raj and raj'

>>> s.replace('raj','RAJ')
'gopi RAJ sathish RAJ and RAJ'

>>> s.replace('raj','RAJ',2)
'gopi RAJ sathish RAJ and raj'

>>> s='gopi raj sathish '

>>> s.replace('raj','RAJ')
'gopi RAJ sathish '

>>> s='weekyourweek'

>>> s.maketrans('wyu','gf@')
{119: 103, 121: 102, 117: 64}

>>> s.translate(s.maketrans('wyu','gf@'))
'geekfo@rgeek'

>>> s='gopirajsathish raja'

>>> s.lstrip('$')
'gopirajsathish raja'

>>> d=s.maketrans('gr','GR')

>>> s.translate(d)
'GopiRajsathish Raja'

>>> s.replace('a','A')
'gopirAjsAthish rAjA'
>>> s='gopirajsathish raja'

>>> import string

>>> import collections

>>> reversed(s)

<reversed object at 0x00000203A565EC70>

>>> list(reversed(s))
['a', 'j', 'a', 'r', ' ', 'h', 's', 'i', 'h', 't', 'a', 's', 'j', 'a', 'r', 'i', 'p', 'o', 'g']

>>> s
'gopirajsathish raja'

>>> s[::-1]
'ajar hsihtasjaripog'

>>> s.replace('a','@',-1)
'gopir@js@thish r@j@'

>>> s.replace('a','@',1)
'gopir@jsathish raja'

>>> s[::-1]
'ajar hsihtasjaripog'

>>> s=s[::-1]

>>> s.replace('a','@')
'@j@r hsiht@sj@ripog'

>>> s.replace('a','@',1)
'@jar hsihtasjaripog'

>>> s.replace('a','@',1)
'@jar hsihtasjaripog'

>>> s=s.replace('a','@',1)

>>> s[::-1]
'gopirajsathish raj@'

>>> s=s[::-1]

>>> d=s.maketrans('gr','GR','@')

>>> s.translate(d)
'GopiRajsathish Raj'

>>> s='gopiraj'

>>> max(s)
'r'

>>> s=line = "Geek1 \nGeek2 \nGeek3"

>>> s = "Geek1 \nGeek2 \nGeek3"

>>> s.split(' ',1)
['Geek1', '\nGeek2 \nGeek3']

>>> import string

>>> t=string.Template('hi $name how are u?')


>>> t.safe_substitute({'name':'gopi'})
'hi gopi how are u?'
	      
	      
