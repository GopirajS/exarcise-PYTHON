Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Arithmetic operator
>>> 
>>> # + , - , * ,**, / , // , %
>>> 
>>> 
>>> 
>>> 12 + 21
33
>>> 12 + 12.3
24.3
>>> 12 + 12.3
24.3
>>> 12 - 2
10
>>> 12 - 23
-11
>>> 12 - 3
9
>>> 12 * 3
36
>>> 12 * 31
372
>>> 12 * 1
12
>>> 
>>> 12 ** 2
144
>>> 12 ** 3
1728
>>> 2 ** 3
8
>>> 2 ** 4
16
>>> 2 ** 6
64
>>> 
>>> 
>>> 
>>> 6    /  2
3.0
>>> 6    /  3
2.0
>>> 60   /  3
20.0
>>> 60   /  4
15.0
>>> 60   /  5
12.0
>>> 60   /  7
8.571428571428571
>>> 60   /  8
7.5
>>> 
>>> 
>>> 
>>> 60   //  8
7
>>> 60   //  9
6
>>> 60   //  2
30
>>> 60   //  4
15
>>> 60   //  6
10
>>> 
>>> 
>>> 
>>> 60   %  7
4
>>> 60   %  8
4
>>> 60   %  9
6
>>> 60   %  10
0
>>> 
>>> 
>>> 
>>> #--------------------------------------
>>> 
>>> #   comparison operation
>>> 
>>> # >  ,  <  ,  >=  ,  <=  , ==  , !=
>>> 
>>> 
>>> 12 > 3
True
>>> 12 > 34
False
>>> 12 >  12.3
False
>>> 12 >  'sring'
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    12 >  'sring'
TypeError: '>' not supported between instances of 'int' and 'str'
>>> 12 >  1
True
>>> 
>>> 
>>> 12 < 3
False
>>> 12 < 30
True
>>> 12 < 3234
True
>>> 0 < 3234
True
>>> 0 < 3234
True
>>> 
>>> 
>>> 
>>> 12 >= 12
True
>>> 12 >= 13
False
>>> 12 >= 14
False
>>> 12 >= 16
False
>>> 12 >= 17
False
>>> 12 >= 17
False
>>> 
>>> 
>>> 12 <= 12
True
>>> 12 <= 120
True
>>> 12 <= 123
True
>>> 2 <= 123
True
>>> 2 <= 1
False
>>> 
>>> 
>>> 
>>> 
>>> 1 != 1
False
>>> 1 != 2
True
>>> 1 != 3
True
>>> 3 != 3
False
>>> 3 != 4
True
>>> 3 != 6
True
>>> 
>>> 
>>> #--------------------------------------------------------------
>>> 
>>> 
>>> 
>>> 
>>> # logical operator
>>> #  and , or , not
>>> 
>>> 
>>> 
>>> 12 > 2 and 12 > 2
True
>>> 12 > 2 and 12 > 12
False
>>> 12 > 2 and 12 > 1
True
>>> 2 > 2 and 12 > 1
False
>>> 
>>> 
>>> 12 > 2 or 12 > 2
True
>>> 12 > 2 or 12 > 24
True
>>> 12 > 2 or 1 > 24
True
>>> 1 > 2 or 1 > 24
False
>>> 1 > 2 or 1 > 24
False
>>> 
>>> 
>>> not 12 > 23
True
>>> not 12 < 2
True
>>> not 12 < 213
False
>>> not 12 != 13
False
>>> not 12 != 12
True
>>> 
>>> 
>>> #-----------------------------------------------
>>> 
>>> # identity operator
>>> #  is , is not
>>> 
>>> 12 is 12
True
>>> 12 is 13
False
>>> 'gopi' is  "gopi"
True
>>> 'gopi' is  "gopi raj"
False
>>> 'gopi' is not "gopi raj"
True
>>> 'gopi' is not "gopi "
True
>>> 'gopi' is not "gopi          "
True
>>> #-----------------------------------------------
>>> # membership operator
>>> # in , not in
>>> l=[1,2,3,4,5,6,7,'gopi']
>>> 5 in l
True
>>> 23 in l
False
>>> 'gopi' in l
True
>>> 'gopi'not in  l
False
>>> 'sathish' not in  l
True
>>> 'sathish' in  not l
SyntaxError: invalid syntax
>>> 'sathish'  not in  'sathish'
False
>>> 'sathish'  not in  'sathish'
False
>>> 
>>> #--------------------------------------------------