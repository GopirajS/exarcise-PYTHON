Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>                      #Python Set add() Method
>>> 

>>> langs={}

>>> type(langs)
<class 'dict'>

>>> langs={'python ','jave','c','c++'}

>>> langs.add('Go')

>>> langs
{'jave', 'Go', 'c++', 'python ', 'c'}

>>> langs.add('Dark')

>>> langs
{'jave', 'Go', 'c++', 'python ', 'Dark', 'c'}



>>>                                  #add tuple to set

>>> langs={'python ','jave','c','c++'}

>>> lang_tuple=('Go','Dark','gopi')

>>> langs.add(lang_tuple)

>>> langs
{'jave', ('Go', 'Dark', 'gopi'), 'c++', 'python ', 'c'}

>>> 

>>>#-------------------------------------------------------------------------- 


>>>                                  #clear() and copy() method

>>> langs={'python ','jave','c','c++'}

>>> 

>>> s=langs.copy()

>>> langs.clear()

>>> print('copy set:',s)
copy set: {'c++', 'jave', 'python ', 'c'}

>>> print('original set:',langs)
original set: set()

>>> #--------------------------------------------------------------------------
>>>                 #Python Set difference(set) Method

>>> 

>>> one={1,2,3,4,5}

>>> two={4,5,6,7,8}

>>> one.difference(two)
{1, 2, 3}

>>> two.difference(one)
{8, 6, 7}

>>> one-two
{1, 2, 3}

>>> two-one
{8, 6, 7}

>>> cities={'bangalure','mumbai','new york','honk kong','chicago'}

>>> cities.difference('mumbai')
{'bangalure', 'mumbai', 'new york', 'honk kong', 'chicago'}

>>> s={'mumbai','bangalure'}

>>> cities.difference(s)
{'honk kong', 'chicago', 'new york'}

>>> cities
{'bangalure', 'mumbai', 'new york', 'honk kong', 'chicago'}
>>> cities.difference({'mumbai'})
{'bangalure', 'chicago', 'new york', 'honk kong'}
>>> cities.difference('mumabi')
{'bangalure', 'mumbai', 'new york', 'honk kong', 'chicago'}

>>> nums1 = {1, 2, 2, 3, 4, 5}

>>> nums2 = {4, 5, 6, 7, 8, 8}

>>> nums3 = { 3, 5, 8, 9, 10}

>>> nums1.difference(nums2,nums3)
{1, 2}

>>> nums2.difference(nums1,nums3)
{6, 7}

>>> nums3.difference(nums1, nums2)
{9, 10}

>>> #-----------------------------------------------------

>>>                #Python Set difference_update() Method

>>> one={1,2,3,4,5}

>>> two={4,5,6,7,8}

>>> one.difference_update(two)

>>> one
{1, 2, 3}

>>> one={1,2,3,4,5}

>>> two={4,5,6,7,8}

>>> two.difference_update(one)

>>> two
{6, 7, 8}

>>> cities={'bangalure','mumbai','new york','honk kong','chicago'}

>>> s=('mumbai','bangalure')

>>> cities.difference_update(s)

>>> cities
{'new york', 'honk kong', 'chicago'}

>>> cities
{'new york', 'honk kong', 'chicago'}

>>> cities={'bangalure','mumbai','new york','honk kong','chicago'}

>>> s=('mumbai','bangalure')

>>> s='mumbai'

>>> cities.difference_update(s)

>>> cities
{'bangalure', 'mumbai', 'new york', 'honk kong', 'chicago'}

>>> s={'mumbai'}

>>> cities.difference_update(S)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    cities.difference_update(S)
NameError: name 'S' is not defined

>>> cities.difference_update(s)

>>> cities
{'bangalure', 'new york', 'honk kong', 'chicago'}

>>> 
>>> 
>>>#-------------------------------------------------------------- 
>>>               #Python Set discard() Method
>>> 
>>>                #The set.discard() method removes a specific element from the set.

>>> langs = {'Python','Go','C++','Java'}

>>> langs.discard('C++')

>>> langs
{'Java', 'Go', 'Python'}

>>> langs = {'Python','Go','C++','Java'}

>>> langs.discard('Python')

>>> langs
{'C++', 'Java', 'Go'}

>>> langs = {'Python','Go','C++','Java'}

>>> langs.discard('PHP')

>>> langs
{'C++', 'Java', 'Go', 'Python'}


>>>#--------------------------------------------------------------------- 

>>> #Python Set pop() Method

>>> langs = {'Python','Go','C++','Java'}

>>> langs.pop('Go')
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    langs.pop('Go')
TypeError: set.pop() takes no arguments (1 given)

>>> c=langs.pop()

>>> print('first pop method',c)
first pop method C++


>>> print(langs)
{'Java', 'Go', 'Python'}

>>> langs = {'Python','Go','C++','Java'}

>>> langs = {'Python','Go','C++','Java'}

>>> s=langs.pop()

>>> print('poped element 1:',s)
poped element 1: C++

>>> print('update langs:',langs)
update langs: {'Java', 'Go', 'Python'}

>>> s=langs.pop()

>>> print('poped element 1:',s)
poped element 1: Java

>>> print('update langs:',langs)
update langs: {'Go', 'Python'}

>>> s=langs.pop()

>>> print('poped element 1:',s)
poped element 1: Go

>>> print('update langs:',langs)
update langs: {'Python'}

>>> #-------------------------------------------------------------
>>>                  #Python Set remove() Method
>>> 

>>> cities = {'Delhi','Chicago','New York'}
>>> 

>>> cities.remove('Delhi')

>>> cities
{'Chicago', 'New York'}

>>> cities.remove('New York')

>>> cities
{'Chicago'}

>>> cities.remove('Chicago')

>>> cities
set()



>>> cities = {'Delhi','Chicago','New York'}

>>> cities.remove('gopi')
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    cities.remove('gopi')
KeyError: 'gopi'


>>>#-----------------------------------------------------
>>> #   set.intersection(*other_sets)
 
>>> one={1,2,3,4,5}

>>> two={4,5,6,7,8}
>>> 
>>> one.intersection(two)
{4, 5}

>>> one&two
{4, 5}

>>> nums = {1, 2, 3, 4, 5}
>>> 

>>> oddNums = {1, 3, 5, 6, 7, 9}
>>> 

>>> primeNums = {2, 3, 5, 7}


>>> nums.intersection(oddNums,primeNums)
{3, 5}

>>> nums&oddNums&primeNums
{3, 5}

>>> 

>>> nums = {1,2,3,4,5,6,7,8,9,10}

>>> oddNums = {1,3,5,6,7,9}

>>> primeNums = {2,3,5,7}

>>> nums.intersection(oddNums,primeNums)
{3, 5, 7}

>>> nums & oddNums & primeNums
{3, 5, 7}

>>>#-------------------------------------------------------------

>>>              #Python Set isdisjoint() Method
>>> 
>>> nums = {1, 2, 3, 4, 5 }

>>> oddNums = {1, 3, 5, 7, 9}

>>> oddNums = {1, 3, 5, 7, 9}

>>> nums.isdisjoint(oddNums)
False

>>> primeNums = {7, 11, 13}

>>> nums.isdisjoint(primeNums)
True

>>> char_set = {'a','b','c','d','e'}

>>> char_list = ['b','c','d']

>>> char_str = 'ghij'

>>> char_dict = {'a':1,'b':2}

>>> char_tuple = ('x', 'y', 'z')

>>> char_set.isdisjoint(char_list)
False

>>> char_set.isdisjoint(char_str)
True

>>> char_set.isdisjoint(char_dict)
False

>>> char_set.isdisjoint(char_tuple)
True

>>> #------------------------------------------------------

>>>                    #set.issubset(other_set)

>>> nums = {1, 2, 3, 4, 5 }

>>> oddNums = {1, 3, 5}

>>> primeNums = {1, 3, 5, 7}

>>> oddNums.issubset(nums)
True

>>> primeNums.issubset(nums)
False

>>> char_set = {'a','b','c'}

>>> char_list = ['a','b','c','d']

>>> char_str = 'ghij'

>>> char_dict = {'a':1,'b':2}

>>> char_tuple = ('a', 'b', 'c', 'd')

>>> print(char_set.issubset(char_list))
True

>>> print(char_set.issubset(char_str))
False

>>> print(char_set.issubset(char_dict))
False

>>> print(char_set.issubset(char_tuple))
True


>>> #---------------------------------------------------

>>>                   #set.symmetric_difference(other_set)

>>> 
>>> nums1 = {1,2,3,4,5}

>>> nums2 = {4,5,6,7,8}

>>> n=nums1.symmetric_difference(nums2)

>>> n
{1, 2, 3, 6, 7, 8}

>>> nums1.symmetric_difference(nums2)
{1, 2, 3, 6, 7, 8}

>>> nums2.symmetric_difference(nums1)
{1, 2, 3, 6, 7, 8}

>>> nums1 = {1,2,2,3,4,5}

>>> nums2 = {4,5,6,7,8,8}

>>> nums1.symmetric_difference(nums2)
{1, 2, 3, 6, 7, 8}

>>> nums2.symmetric_difference(nums1)
{1, 2, 3, 6, 7, 8}
>>> 

>>> nums1^nums2

{1, 2, 3, 6, 7, 8}

>>> nums2^nums1
{1, 2, 3, 6, 7, 8}



>>> #------------------------------------------------
>>>                    #set.symmetric_difference_update(other_Set)
>>> 

>>> nums = {1, 2, 3, 4, 5 }

>>> nums1 = {1,2,3,4,5}

>>> nums.symmetric_difference_update(nums1)

>>> nums
set()

>>> nums = {1, 2, 3, 4, 5 }

>>> nums1 = {6,7,8,9}

>>> nums.symmetric_difference_update(nums1)

>>> nums
{1, 2, 3, 4, 5, 6, 7, 8, 9}

>>> #-------------------------------------------------

>>> #            set.union(*other_sets)

>>> nums1 = {1, 2, 2, 3, 4, 5}

>>> nums2 = {4, 5, 6, 7, 7, 8}

>>> nums1.union(nums2)
{1, 2, 3, 4, 5, 6, 7, 8}

>>> cities={'mumbai','delhi','new yare'}

>>> cities1={'salem','coimbature'}

>>> cities.union(cities1)
{'mumbai', 'coimbature', 'salem', 'new yare', 'delhi'}

>>> cities1.union(cities)
{'mumbai', 'coimbature', 'new yare', 'salem', 'delhi'}

>>> nums1 = {1, 2, 2, 3, 4, 5}

>>> nums2 = {4, 5, 6, 6, 7, 8, 8}

>>> nums3 = {7, 8, 9, 10}

>>> distinct_nums = nums1.union(nums2, nums3)

>>> distinct_nums
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

>>> distinct_num = nums1 | nums2 |nums3

>>> distinct_num
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

>>> #--------------------------------------------------

>>>                  #set.update(*other_type_set)
>>> nums = {1, 2, 3}

>>> primeNums = {2, 3, 5, 7}
>>> 

>>> nums.update(primeNums)

>>> nums
{1, 2, 3, 5, 7}

>>> nums.union(primeNums)
{1, 2, 3, 5, 7}

>>> nums = { 1, 2, 3 }

>>> evenNums = { 2, 4, 6 }

>>> primeNums = { 5, 7 }

>>> nums.update(evenNums,primeNums)

>>> nums
{1, 2, 3, 4, 5, 6, 7}
>>> 
>>> 
>>> 
>>> nums=nums | evenNums | primeNums
>>> nums
{1, 2, 3, 4, 5, 6, 7}
>>> 
>>> 
>>> 

>>> nums = {1, 2, 3}

>>> n_list = [1, 3, 5, 7, 9]

>>> e_tuple = (2, 4, 6, 8, 10)

>>> nums.update(n_list)

>>> nums
{1, 2, 3, 5, 7, 9}

>>> nums.update(e_tuple)

>>> nums
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

>>> nums = {1, 2, 3}

>>> e_tuple = (2, 4, 6, 8, 10)

>>> nums.update(e_tuple)

>>> nums
{1, 2, 3, 4, 6, 8, 10}

>>> nums = {1,2,3,4,5}

>>> numsDict = {6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten'}

>>> nums.update(numsDict)

>>> nums
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>>  