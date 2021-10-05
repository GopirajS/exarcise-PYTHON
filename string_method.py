>>>                                     #capitalize()	Converts the first character to upper case



>>> s='gopiraj'
>>> s.capitalize()
'Gopiraj'
>>> s='GOPIRAJ'

>>> s.casefold()
'gopiraj'

>>> s.casefold().capitalize().center(100)
'                                              Gopiraj                                               '



>>>                               #casefold()	Converts string into lower case
>>> s
'GOPIRAJ'

>>> s.casefold()
'gopiraj'


>>>                                    #center()	Returns a centered string
>>> s.center(100)
'                                              GOPIRAJ                                               '
>>> s.center(100,'@')
'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@GOPIRAJ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
>>> print("\U0001F917")
🤗
>>> e=print("\U0001F917")
🤗

 
>>> e="\U0001F917"

>>> e
'🤗'

>>> s.center(100,e)
'🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗GOPIRAJ🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗'
>>> t="\U0001F618"

>>> t
'😘'

>>> s.center(50,e)
'🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗GOPIRAJ🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗'

>>> s.center(50,t)
'😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘GOPIRAJ😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘'

>>> print(s.center(50,t))
😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘GOPIRAJ😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘
>>> 


#-----------------------------------------------------------------------------------------------------------------------------------

>>>                             #count()	Returns the number of times a specified value occurs in a string




>>> s
'GOPIRAJ'

>>> s.count('G')
1

>>> s='i love apple ,apple my favorite fruit'

>>> s.count('apple',0,30)
2

>>> len(s)
37

>>> s.count('apple',0,37)
2

#-------------------------------------------------------------------------------------------------------------------------------------

>>>                         #endswith()	Returns true if the string ends with the specified value

 

	

	
	
>>> txt = "Hello, welcome to my world."

>>> txt.endswith(".")
True

>>> txt.endswith("world")
False

>>> txt.endswith("world.")
True

>>> txt.endswith("my world.")
True

>>> len(txt)
27

>>> txt.endswith("my world.",0,27)
True

>>> txt.endswith(".",0,27)
True

>>> txt.endswith(".",0,26)
False

>>> txt.endswith(".",0,27)
TrueS



#---------------------------------------------------------------------------------------------------------------

                              #endswith()	Returns true if the string ends with the specified value

	
	
	
>>> txt = "Hello, welcome to my world."

>>> txt.endswith('.')
True

>>> txt.endswith('world.')
True

>>> txt.endswith('word.')
False

>>> txt.endswith('d.')
True

>>> len(txt)
27

>>> txt.endswith('d.',0,27)
True


#------------------------------------------------------------------------------------------------------------------- 
        
	                                           #expandtabs()	Sets the tab size of the string

	


>>> txt = "H\te\tl\tl\to"

>>> txt.expandtabs()
'H       e       l       l       o'

>>> txt.expandtabs(1)
'H e l l o'

>>> txt.expandtabs(0)
'Hello'

>>> txt.expandtabs(2)
'H e l l o'

>>> txt.expandtabs(3)
'H  e  l  l  o'

>>> txt.expandtabs(4)
'H   e   l   l   o'

>>> txt.expandtabs(5)
'H    e    l    l    o'

>>> txt.expandtabs(6)
'H     e     l     l     o'

>>> txt.expandtabs(7)
'H      e      l      l      o'

>>> txt.expandtabs(8)
'H       e       l       l       o'

>>> txt.expandtabs()
'H       e       l       l       o'

>>> txt.expandtabs(10)
'H         e         l         l         o'



#---------------------------------------------------------------------------------------------------------------------------------------
 
         #find()	Searches the string for a specified value and returns the position of where it was found

 

>>> txt = "Hello, welcome to my world."

>>> txt.find("welcome")
7

>>> txt.find('my')
18

>>> txt.find('gopi')
-1

>>> txt.count('gopi')
0

>>> txt.index('gopi')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    txt.index('gopi')
ValueError: substring not found
 
            

#------------------------------------------------------------------------------------------------------------------------------------
                                          #format()	Formats specified values in a string



 

>>> txt='im gopiraj ,ane my age is 22'

>>> print(txt)
im gopiraj ,ane my age is 22


>>> txt1='my name is {name},and my age is {age}'

>>> print(txt1.format(name='gopira',age=22))
my name is gopira,and my age is 22

>>> print(txt1.format(name='gopira',age=22))
my name is gopira,and my age is 22

>>> txt1='my name is {0},and my age is {1}'

>>> print(txt1.format('gopiraj',22))
my name is gopiraj,and my age is 22

>>> txt1='my name is {0},and my age is {1}'

>>> print(txt1.format(22,'gopiraj'))
my name is 22,and my age is gopiraj

>>> txt1='my name is {},and my age is {}'

>>> print(txt1.format('gopiraj',22))
my name is gopiraj,and my age is 22
 

>>> txt="for only {price:.2f} doller "

>>> txt.format(price=49)
'for only 49.00 doller '

>>> txt.format(price=49.1324)
'for only 49.13 doller '


>>> txt="for only {:.2f} doller "

>>> txt.format(49.1324)
'for only 49.13 doller '
 

>>> print(txt.format(4))
this is string 4 and this is bynerry of the string100 

>>> txt='i have a doller{:f}'

>>> print(txt.format(23))
i have a doller23.000000

#------------------------------------------------------------------------------------------------------------

                                             #format_map()



>>> d={"name":'gopiraj','age':21}

>>> s='first candidate is {name} ,is age is {age}'

>>> s.format_map(d)
'first candidate is gopiraj ,is age is 21


>>> d={"name":['gopiraj','asthish kumar','raj'],'age':[21,27,13]}



>>> s='first candidate is {name[0]} ,is age is {age[0]}'

>>> s.format_map(d)
'first candidate is gopiraj ,is age is 21'

>>> s='first candidate is {name[1]} ,is age is {age[1]}'

>>> s.format_map(d)
'first candidate is asthish kumar ,is age is 27'
>>> s='first candidate is {name[2]} ,is age is {age[2]}'

>>> s.format_map(d)
'first candidate is raj ,is age is 13'
 
 



#--------------------------------------------------------------------------------------------------------------------------------------------------

                 # index()	Searches the string for a specified value and returns the position of where it was found
 



>>> string='well come this is  python tutoriel and im student '

>>> string.index('well',0,30)
0

>>> string.index('is',0,40)
12

>>> d=string.index('p',0,40)

>>> print('p is located :{} index'.format(d))
p is located :19 index


>>> print(f'p is located :{d} index')
p is located :19 index


>>> string.index('gopi')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    string.index('gopi')
ValueError: substring not found



>>> string.find('gopi')
-1





#------------------------------------------------------------------------------------------------------------------------

                 #isalnum()	Returns True if all characters in the string are alphanumeric
 

>>> str = "Welcome"

>>> str.isalnum()
True

>>> str = "Welcome12"

>>> str.isalnum()
True

>>> str = "Welcome 12"     # canot condain a space


>>> str.isalnum()
False

>>> str = "12"

>>> str.isalnum()
True

>>> str = "12@_gopi"

>>> str.isalnum()
False



#--------------------------------------------------------------------------------------------------------------------------------



                    #isalpha()	Returns True if all characters in the string are in the alphabet

>>>                   #   ****returns True if all the characters are ascii characters  (a-z).***


>>> str = "Welcome"

>>> str.isalpha()
True

>>> str = "Welcome1"

>>> str.isalpha()
False

>>> str = "1"

>>> str.isalpha()
False

>>> str = "g "

>>> str.isalpha()
False

>>> str = "gopi"

>>> str.isalpha()
True

>>> str = "gopi raj"

>>> str.isalpha()
False


>>> str = "gopiraj"

>>> if str.isalpha():
	print("the string is alpha")
else :
	print("this string is other formet too")

	
the string is alpha

#-----------------------------------------------------------------------------------------------------------------------------

>>>                         #isascii()	Returns True if all characters in the string are ascii characters

                


>>> str='gopiraj'

>>> str.isascii()
True

>>> str='gopi raj'

>>> str.isascii()
True

>>> str='gopi raj1'

>>> str.isascii()
True

>>> str='gopi raj1 @'

>>> str.isascii()
True

>>> str='gopi raj1.23'

>>> str.isascii()
True

>>> str='1.23'

>>> str.isascii()
True

>>> str='தமிழ்நாடு'

>>> str.isascii()
False

>>> str='   '

>>> str.isascii()
True


#--------------------------------------------------------------------------------------------------------------------------



                 #isdecimal()	Returns True if all characters in the string are decimals




>>> str='132435'

>>> str.isdecimal()
True



#---------------------------------------------------------------------------------------------------------------------------------------

                           #isidentifier()	Returns True if the string is an identifier

>>> str = "Welcome12"

>>> str.isidentifier()
True

>>> str.isalnum()
True

>>> str = "Welcome12_"

>>> str.isalnum()
False

>>> str.isidentifier()
True

>>> str = "_Welcome12_"

>>> str.isidentifier()
True

>>> str = "_Welcome12+_"

>>> str.isidentifier()
False

#------------------------------------------------------------------------------------------------------------------------------


>>>                   #islower()	Returns True if all characters in the string are lower case

>>> s='gpoiraj'

>>> s.islower()
True

>>> s='gopi raj'
>>> s.islower()
True

>>> s='gopiRaj'

>>> s.islower()
False

>>> s='gpoiraj123'
>>> s.islower()
True

>>> s='gpoiraj123@'

>>> s.islower()
True

>>> s='2gpoi raj123@'

>>> s.islower()
True


#-------------------------------------------------------------------------------------------------------------------------------------


>>> 	      #isspace()	Returns True if all characters in the string are whitespaces



>>> s='   '

>>> s.isspace()
True

>>> s=''

>>> s.isspace()
False

>>> s='  s '

>>> s.isspace()
False
        

#-----------------------------------------------------------------------------------------------------------------------------------

                                  #istitle()	Returns True if the string follows the rules of a title
>>> s='Gopi Raj'

>>> s.istitle()
True

>>> s='Gopi Raj 12'

>>> s.istitle()
True

>>> s='Gopi e Raj 12'

>>> s.istitle()
False

>>> s='22 G H I'

>>> s.istitle()
True

>>> s='22 Gopi Harish I'

>>> s.istitle()
True

>>> 

#-----------------------------------------------------------------------------------------------------------------------------------
                                #join()	Joins the elements of an iterable to the end of the string
>>> 
>>> 

>>> s=('gopi',"raj",'sathish kumer')

>>> d=' '.join(s)

>>> d
'gopi raj sathish kumer'
 

>>> s=('gopi','satish','kumar','raj','gopal','gowri')


>>> d=':'.join(s)

>>> d
'gopi:satish:kumar:raj:gopal:gowri'


>>> s=['gopi','satish','kumar','raj']

>>> d='->'.join(s)

>>> d
'gopi->satish->kumar->raj'

>>> s={'gopi','satish','kumar','raj'}

>>> d='->'.join(s)

>>> d
'kumar->raj->satish->gopi'



#-------------------------------------------------------------------------------------------------------------------------------

>>>                        #ljust()	Returns a left justified version of the string



>>> s='bananan'

>>> s.ljust(20)
'bananan             '

>>> s.ljust(15,'#')
'bananan########'


>>> d=s.ljust(20,'$')

>>> print(d,'this is left justified version of the string')

bananan$$$$$$$$$$$$$ this is left justified version of the string



>>> fruit='banana'

>>> x=fruit.ljust(20)

>>> print(x,'this is my faviriet fruit')
banana               this is my faviriet fruit




#----------------------------------------------------------------------------------------------------------------------------------
                     #rjust()	Returns a right justified version of the string



>>> s='bananan'

>>> s.rjust(30)
'                       bananan'

>>> s.rjust(30,'*')
'***********************bananan'

>>> d=s.rjust(30,'*')


>>> print(d,'this is ringht justified vertion of string')
***********************bananan this is ringht justified vertion of string
 
 


>>> fruit='banana'

>>> x=fruit.rjust(30)


>>> print(x,'this is right justified')
                        banana this is right justified





#--------------------------------------------------------------------------------------------------------------------

                               #lower()	Converts a string into lower case



>>> s='GOPIRAJ'

>>> s.lower()
'gopiraj'

>>> s='gopiraj satish kumar'

>>> s.lower()
'gopiraj satish kumar'





#----------------------------------------------------------------------------------------------------------------------------

                                 #lstrip()   #trimming#  	Returns a left trim version of the string


>>> s='     gopiraj'


>>> s.lstrip(" ")
'gopiraj'


>>> s='     gopiraj    '


>>> s.lstrip(" ")
'gopiraj    '


>>> s='  @##$%^   gopiraj'



>>> s.lstrip(" @#$%^")
'gopiraj'


#--------------------------------------------------------------------------------------------------------------------------------------------

>>>                              #strip()   #trimming#	 Returns a trimmed version of the string

>>> s='bananan'
>>> 
>>> s='    bananan           '
>>> 
>>> s.strip(" ")
'bananan'
>>> s='    banana 333333'
>>> s.strip(" 3")
'banana'
>>> s.strip(" 3 ")
'banana'
>>> s='   4444 banana 333333'
>>> s.strip(" 3  4")
'banana'


#---------------------------------------------------------------------------------------------------------------------------------------------


                          #replace()	Returns a string where a specified value is replaced with a specified value



>>> s='one one two ,two two are four'


>>> s.replace('one','1')
'1 1 two ,two two are four'


>>> s.replace('one','three')
'three three two ,two two are four'


>>> s.replace('one','three',1)
'three one two ,two two are four'




#------------------------------------------------------------------------------------------------------------------------------------------------
                     #rfind()	Searches the string for a specified value and returns the last position of where it was foun



>>> s='Searches the string for a specified value and returns the last position of where it was foun'


>>> s.rfind("n")
91

>>> len(s)
92

>>> s='Searches the string for a specified value yes returns the last position of where it was yes'


>>> s.rfind("yes")
88


>>> s.rfind("Yes")
-1






#------------------------------------------------------------------------------------------------------------------------------



>>>                 #rsplit()	Splits the string at the specified separator, and returns a list
>>> 
>>> 



>>> s=('gopi,raj,satish,kumer,gopal,gowri')

>>> s
'gopi,raj,satish,kumer,gopal,gowri'

>>> s.rsplit(',')
['gopi', 'raj', 'satish', 'kumer', 'gopal', 'gowri']


>>> s.rsplit(',',3)
['gopi,raj,satish', 'kumer', 'gopal', 'gowri']


>>> s=('gopi raj satish kumer gopal gowri')

>>> s
'gopi raj satish kumer gopal gowri'

>>> s.rsplit(' ')
['gopi', 'raj', 'satish', 'kumer', 'gopal', 'gowri']

>>> s.rsplit(' ',4)
['gopi raj', 'satish', 'kumer', 'gopal', 'gowri']

>>> s.rsplit(' ',3)
['gopi raj satish', 'kumer', 'gopal', 'gowri']



#----------------------------------------------------------------------------------------------------------------------------------

               #split()	Splits the string at the specified separator, and returns a list


>>> s=('gopi raj satish kumer gopal gowri')


>>> s.split(' ')
['gopi', 'raj', 'satish', 'kumer', 'gopal', 'gowri']

>>> s.split(' ',3)
['gopi', 'raj', 'satish', 'kumer gopal gowri']

  



#----------------------------------------------------------------------------------------------------------------------------------------
                   #startswith()	Returns true if the string starts with the specified value


>>> txt = "Hello, welcome to my world."


>>> txt.startswith('world')
False

>>> txt.startswith('h')
False

>>> txt.startswith('H')
True

>>> txt.startswith('W',7,10)
False

>>> txt.startswith('w',7,10)
True





 #_-----------------------------------------------------------------------------------------------------------------------------
	
	
                      #swapcase()	Swaps cases, lower case becomes upper case and vice versa
>>> s='gopi RAJ'
>>> s.swapcase()
'GOPI raj'
>>> s='gopi RAJ 132 sathish kumar'
>>> s.swapcase()
'GOPI raj 132 SATHISH KUMAR'
 




#-----------------------------------------------------------------------------------------------------------------------------------------


>>>                      #title()	Converts the first character of each word to upper case




>>> s='gopi raj sathish kumar and gopial'
>>> s.title()
'Gopi Raj Sathish Kumar And Gopial'
>>> 
>>> 
>>> 
>>> s='gopi raj sathish kumar and 4gopial'
>>> s.title()
'Gopi Raj Sathish Kumar And 4Gopial'




#--------------------------------------------------------------------------------------------------------------------------

                           >>> #upper()	Converts a string into upper case





>>> s='gopi raj sathi kumar'
>>> s.upper()
'GOPI RAJ SATHI KUMAR'

>>> s.title()
'Gopi Raj Sathi Kumar'






>>>                    #zfill()	Fills the string with a specified number of 0 values at the beginning
>>> s='apple'
>>> s.zfill(10)
'00000apple'
>>> s='10000000'
>>> s.zfill(4)
'10000000'
>>> s.zfill(40)
'0000000000000000000000000000000010000000'
>>> s='satish kumar'
>>> s.zfill(30)
'000000000000000000satish kumar'
>>>  







>>> #----------------------------------------------------------------
>>>                                                 #partition()  

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

#-----------------------------------------------------------------------------------------------------------
>>>                                              # rpartition()



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
 



