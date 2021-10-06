>>>                                   # maketrans() method

>>> s='gopi'

>>> s.maketrans('g',"G")
{103: 71}

>>> s.translate(_)
'Gopi'

>>> s.maketrans('g',"G",'p','b')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.maketrans('g',"G",'p','b')
TypeError: maketrans expected at most 3 arguments, got 4

>>> s.maketrans('g',"G",'p')
{103: 71, 112: None}

>>> s.translate(_)
'Goi'

>>> s='gopi raj sathish kumar'


>>> s.replace('raj','')
'gopi  sathish kumar'

>>> s='gopi raj sathish kumar'

>>> s='gobi rej sethish kumer'

>>> s.maketrans('eb','ap')
{101: 97, 98: 112}

>>> s.translate(_)
'gopi raj sathish kumar'


>>> s.maketrans('eb','ap','kumar')
{101: 97, 98: 112, 107: None, 117: None, 109: None, 97: None, 114: None}

>>> s.translate(_)
'gopi aj sathish a'

>>> s='gobirejs'

>>> s.maketrans('be','pa','s')
{98: 112, 101: 97, 115: None}

>>> s.translate(_)
'gopiraj'

 


>>> #-----------------------------------------------------------------------

>>> #                 replace()



>>> s='gopi kumar'

>>> s.replace('kumar','raj')
'gopi raj'

>>> s='gopi kumar raj kumar raj'

>>> s.replace('kumar','raj')
'gopi raj raj raj raj'


>>> s.replace('kumar','raj',1)
'gopi raj raj kumar raj'


>>> s='gopiraj is gopi '


>>> s.replace('gopi','Gopi')
'Gopiraj is Gopi '

>>> s.replace('o',"0")
'g0piraj is g0pi '

>>> s
'gopiraj is gopi '

>>> mystr = 'Tutorials Teacher'

>>> mystr.maketrans('tolh','1234')
{116: 49, 111: 50, 108: 51, 104: 52}

>>> mystr.maketrans('Tolh','1234')
{84: 49, 111: 50, 108: 51, 104: 52}

>>> mystr.translate(_)
'1ut2ria3s 1eac4er'

>>> chr(1)
'\x01'

>>> chr(49)
'1'

>>> trans_dict = {'T':'1','o':'2','l':'3','h':'4'}

>>> mytable = mystr.maketrans(trans_dict)

>>> mytable
{84: '1', 111: '2', 108: '3', 104: '4'}

>>> mytable = mystr.maketrans(_)
>>> mytable
{84: '1', 111: '2', 108: '3', 104: '4'}



>>> #----------------------------------------------------------------------
>>>                                          #isascii()
>>> 
>>> s='gopi raj'

>>> s.isascii()
True
>>> s=''

>>> s.isascii()
True

>>> s=' '

>>> s.isascii()
True

>>> s=1,2,3,4,5,6

>>> s="!@#$%^&*()_-+="

>>> s.isascii()
True

>>> s="!@#$%^&*()_-+=,ASDFGHJK,asdfghjk"

>>> s.isascii()
True





>>> #-----------------------------------
>>>                          #         isdecimal() methosd

>>> s='123'

>>> s.isdecimal()
True

>>> s='123A'

>>> s.isdecimal()
False

>>> s='12 3'

>>> s.isdecimal()
False

>>> 

>>> print('\u0032')
2

>>> print('\u0032')
2

>>> print('\u00B23455')
²3455



>>> #-----------------------------------------------------------------------------
>>>                                 #       translate()
>>> 

>>> s='python is first language'

>>> s.maketrans('plf','PLF')
{112: 80, 108: 76, 102: 70}

>>> s.translate(_)
'Python is First Language'

>>> s='python is first language 3'

>>> s.maketrans('plf','PLF',"3")
{112: 80, 108: 76, 102: 70, 51: None}

>>> s.translate(_)
'Python is First Language '



>>> #---------------------------------------------------

>>> '''
                               Syntax:

                                     str.join(iterable)

                               
                              Parameters:
                                          
                                      iterable: (Required) An iterable object such as list, tuple, string, set, dict.



'''






>>> s='g,d,f,h,e'

>>> ','.join(s)
'g,,,d,,,f,,,h,,,e'

>>> s='gopiraj'

>>> ','.join(s)

'g,o,p,i,r,a,j'

>>> ''.join(s)
'gopiraj'

>>> ' '.join(s)
'g o p i r a j'


>>> s=('gopi','raj','kuamr')

>>> for i in s:
	i

	
'gopi'
'raj'
'kuamr'

>>> s
('gopi', 'raj', 'kuamr')
>>> ','.join(s)
'gopi,raj,kuamr'
>>> d=','.join(s)
>>> d
'gopi,raj,kuamr'

>>> l=('1','2','3')

>>> d={'name':'gopi','age':'21','city':'salem'}

>>> print('->'.join(d))

name->age->city
>>> 