
                                            # find()
>>> str='gopi raj'

>>> str.find('g')
0

>>> str.find('o')
1

>>> str.find('i')
3

>>> str.find('j')
7

>>> str.find('G')
-1

>>> str='gopi ipog'

>>> str.find('g')
0

>>> len(str)
9

>>> str.count('g')
2

>>> str.rfind('g')
8

>>> str='gopi ipgo'

>>> str.rfind('g')
7



>>>#-----------------------------------------------------------------------------


>>>                                             # index() and rindex()

>>> str
'gopi ipgo'

>>> str.index('g')
0

>>> str.index('o')
1

>>> str.index('p')
2

>>> str.index('i')
3

>>> str.index('G')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    str.index('G')
ValueError: substring not found



>>> str.rindex('g')
7


>>> str.rindex('o')
8


>>> str.rindex('i')
5

>>> str.rindex('f')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    str.rindex('f')
ValueError: substring not found

#----------------------------------------------------------------------------------------------


>>>                                     # ljust()          center()          rjust()


>>> s='Gopiraj'

>>> s.ljust(20,'*')
'Gopiraj*************'

>>> s='left justified'

>>> s.ljust(20,'*')
'left justified******'

>>> s.center(20,'*')
'***left justified***'

>>> s='Gopiraj'

>>> s.center(20,'*')
'******Gopiraj*******'

>>> s.rjust(20,'*')
'*************Gopiraj'

>>> s='left justified'

>>> s.rjust(20,'*')
'******left justified'




>>> 

>>> #-------------------------------------------------------------------------

>>>                                          # split()    and     rsplit()

>>> s='hellow world'

>>> s.split()
['hellow', 'world']

>>> s='hellow world'

>>> r='hellow\tworld'

>>> f='hellow\bworld'

>>> h='hellow\tworld'

>>> j='hellow\nworld'

>>> print(s.split())
['hellow', 'world']

>>> print(r.split())
['hellow', 'world']

>>> f.split()
['hellow\x08world']

>>> print(f.split())
['hellow\x08world']

>>> print(h.split())
['hellow', 'world']

>>> print(j.split())
['hellow', 'world']

>>> d='gopi raj kumar'

>>> d.split()
['gopi', 'raj', 'kumar']

>>> d='gopi*raj*kumar'

>>> d.split('*')
['gopi', 'raj', 'kumar']

>>> d='gopi\traj\tkumar'

>>> d.split('\t')
['gopi', 'raj', 'kumar']


>>> l='''
__future__          argparse            help_about          search
__main__            array               history             searchbase
_abc                ast                 hmac                searchengine
_aix_support        asynchat            html                secrets
_ast                asyncio             http                select

'''



>>> l.split(' ',10)
['\n__future__', '', '', '', '', '', '', '', '', '', 'argparse            help_about          search\n__main__            array               history             searchbase\n_abc                ast                 hmac                searchengine\n_aix_support        asynchat            html                secrets\n_ast                asyncio             http                select\n\n']

>>> l.split(,10)
SyntaxError: invalid syntax

>>> l.split(10)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    l.split(10)
TypeError: must be str or None, not int

>>> l.split(maxsplit=4)
['__future__', 'argparse', 'help_about', 'search', '__main__            array               history             searchbase\n_abc                ast                 hmac                searchengine\n_aix_support        asynchat            html                secrets\n_ast                asyncio             http                select\n\n']

>>> f=l.split(maxsplit=4)

>>> for i in f:
	print(i)

	
__future__
argparse
help_about
search
__main__            array               history             searchbase
_abc                ast                 hmac                searchengine
_aix_support        asynchat            html                secrets
_ast                asyncio             http                select


>>> for i in f:
	i

	
'__future__'
'argparse'
'help_about'
'search'
'__main__            array               history             searchbase\n_abc                ast                 hmac                searchengine\n_aix_support        asynchat            html                secrets\n_ast                asyncio             http                select\n\n'


>>> langs = 'C,Python,R,Java,SQL,Hadoop'

>>> langs.rsplit(',')
['C', 'Python', 'R', 'Java', 'SQL', 'Hadoop']

>>> langs.rsplit(',',3)
['C,Python,R', 'Java', 'SQL', 'Hadoop']

>>> s=langs.rsplit(',',3)

>>> for i in s:
	i

	
'C,Python,R'
'Java'
'SQL'
'Hadoop'
>>> 
>>> 
>>> 
>>> #---------------------------------------------------------------


>>>                                      # strip()   lstrip()    and  rstrip()
>>> 
>>> 

>>> s='gopi'

>>> f=s.center(20,'*')

>>> f
'********gopi********'

>>> f.strip('*')
'gopi'

>>> f=s.center(20)

>>> f
'        gopi        '

>>> f.strip()
'gopi'


>>> s
'gopi'

>>> f=s.ljust(20,"*")

>>> f
'gopi****************'

>>> f.rstrip('*')
'gopi'

>>> f=s.ljust(20)

>>> f
'gopi                '

>>> f.rstrip()
'gopi'

>>> s='Gopi Raj'

>>> f=s.rjust(20,'*')

>>> f
'************Gopi Raj'

>>> f.lstrip('*')
'Gopi Raj'

>>> f=s.rjust(20)


>>> f
'            Gopi Raj'


>>> f.lstrip()
'Gopi Raj'



>>> #----------------------------------------------------------------
>>>                                                 #partition()  and rpartition

>>> s='gopi raj'


>>> s.partition(' ')
('gopi', ' ', 'raj')

>>> s='gopi raj  s'

>>> s.partition('raj')
('gopi ', 'raj', '  s')

>>> s.partition('123')
('gopi raj  s', '', '')

>>> s.partition('$%')
('gopi raj  s', '', '')

>>> mystr = 'TutorialsTeacher is the best tutorials website.'

>>> mystr.partition("tutorials")
('TutorialsTeacher is the best ', 'tutorials', ' website.')

>>> mystr.partition("Tutorials")
('', 'Tutorials', 'Teacher is the best tutorials website.')

>>> s='gopi raj'

>>> s.partition()
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    s.partition()
TypeError: str.partition() takes exactly one argument (0 given)

>>> mystr = 'TutorialsTeacher is the best Tutorials website.'

>>> mystr.partition("Tutorials")
('', 'Tutorials', 'Teacher is the best Tutorials website.')


>>> s='gopiraj sathish kumar'


>>> s.rpartition('')
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    s.rpartition('')
ValueError: empty separator


>>> s.rpartition(' ')
('gopiraj sathish', ' ', 'kumar')

>>> s.rpartition('k')
('gopiraj sathish ', 'k', 'umar')

>>> s.rpartition('t')
('gopiraj sa', 't', 'hish kumar')

>>> s.rpartition('o')
('g', 'o', 'piraj sathish kumar')

>>> s.rpartition(sep='o')
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    s.rpartition(sep='o')
TypeError: str.rpartition() takes no keyword arguments
 