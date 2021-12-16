
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
 	

	     	      
	      
	      
