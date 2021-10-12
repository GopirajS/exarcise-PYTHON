Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #                   operator
>>> 
>>>  #bitwise operator
>>> # & , | , ~ , ^ ,>> ,<<
>>> 
>>> # AND  --->    &
>>> """
             X          Y      ans

             1     &    1   =    1

             1     &    0   =    0
             0     &    1   =    0
             0     &    0   =    0

     """

>>> 1 & 1
1

>>> 1 & 2
0
>>> 
>>> 
>>> 1 & 3
1
>>> 1 & 4
0
>>> 1 & 5
1
>>> 1 & 6
0
>>> 1 & 7
1
>>> 2 & 1
0
>>> 2 & 2
2
>>> 2 & 3
2
>>> 2 & 4
0
>>> 2 & 5
0
>>> 2 & 6
2
>>> 2 & 7
2
>>> bin(1)
'0b1'
>>> bin(2)
'0b10'
>>> #  01 & 10 ----> 00
>>> 0b00
0
>> bin(2)
'0b10'
>>> bin(7)
'0b111'
>>> #   2 & 7 --------->  0b010   &   0b111 ---> 0b010
>>> 0b010
2


>>> import operator
>>> operator.and_(2,5)
0
>>> operator.and_(2,6)
2
>>> operator.and_(6,6)
6
>>> operator.and_(6,5)
4
>>> operator.and_(6,9)
0
>>> operator.and_(6,10)
2
>>> 
>>> #-------------------------------------------------------
>>> 
>>> #      OR operator
>>> 
>>> 
>>> #  OR    ---->    |
>>> 
>>> 
>>> """
             X     OR     Y      ans

             1     |    1   =    1

             1     |    0   =    1
             0     |    1   =    1
             0     |    0   =    0


             """
>>> 
>>> 1 | 1
1
>>> 1 | 2
3
>>> 1 | 3
3
>>> 1 | 4
5
>>> 1 | 5
5
>>> 1 | 5
5
>>> 1 | 6
7
>>> 
>>> 2 | 1
3
>>> 2 | 2
2
>>> 2 | 3
3
>>> 2 | 4
6
>>> 2 | 5
7
>>> 2 | 6
6
>>> 2 | 7
7
>>> 
>>> 
>>> 3 | 1
3
>>> 3 | 4
7
>>> 3 | 6
7
>>> 3 | 8
11
>>> bin(3)
'0b11'
>>> bin(8)
'0b1000'
>>> #   3 | 8  _----->  0b0011  OR  0b1000 ---->  0b1011
>>> 0b1011
11
>>> 
>>> operator.or_(1,2)
3
>>> operator.or_(1,3)
3
>>> operator.or_(1,4)
5
>>> operator.or_(1,5)
5
>>> operator.or_(1,6)
7
>>> operator.or_(2,6)
6
>>> operator.or_(2,2)
2
>>> operator.or_(2,3)
3
>>> operator.or_(2,4)
6
>>> operator.or_(2,5)
7
>>> operator.or_(2,6)
6
>>> #----------------------------------------------------------
>>> 
>>> #   NOT  ------>   ~
>>> 
>>> """


             ~X         ans

             1           =    0

             0           =    1

             """

>>> ~1
-2
>>> ~2
-3
>>> ~3
-4
>>> ~4
-5
>>> ~5
-6
>>> ~50
-51
>>> ~56
-57
>>> bin(1)
'0b1'
>>> bin(-1)
'-0b1'
>>> bin(4)
'0b100'
>>> bin(-4)
'-0b100'
>>> bin(-5)
'-0b101'
>>> bin(5)
'0b101'
>>> bin(-6)
'-0b110'
>>> 
>>> 
>>> operator.invert(3)
-4
>>> operator.invert(5)
-6
>>> operator.invert(7)
-8
>>> operator.invert(70)
-71
>>> operator.invert(71)
-72
>>> operator.invert(-123)
122
>>> 

>>> #-------------------------------------------------
>>> # XOR -------->  ^
>>> 
>>> """

                 
             X     XOR     Y      ans

             1     ^    1   =    0

             1     ^    0   =    1
             0     ^    1   =    1
             0     ^    0   =    0

             """
'\n\n                 \n             X     XOR     Y      ans\n\n             1     ^    1   =    0\n\n             1     ^    0   =    1\n             0     ^    1   =    1\n             0     ^    0   =    0\n\n             '

>>> 
>>> 1 ^ 1
0
>>> 1 ^ 2
3
>>> 1 ^ 3
2
>>> 1 ^ 4
5
>>> 1 ^ 5
4
>>> 2 ^ 2
0
>>> 2 ^ 3
1
>>> 2 ^ 4
6
>>> 2 ^ 5
7
>>> 2 ^ 6
4
>>> bin(2)
'0b10'
>>> bin(4)
'0b100'
>>> # 2 ^ 4 -----> 0b010   ^   0b100 ---->   0b110
>>> bin(6)
'0b110'
>>>
>>> operator.xor(1,2)
3
>>> operator.xor(1,3)
2
>>> operator.xor(1,4)
5
>>> operator.xor(1,5)
4
>>> operator.xor(1,6)
7
>>> operator.xor(4,2)
6
>>> operator.xor(4,3)
7
>>> operator.xor(4,4)
0
>>> operator.xor(4,0)
4

>>> #-------------------------------------------------------------
>>> 
>>> 
>>> # right shift ----->  >>
>>> 
>>> 
>>> 
>>> 1 >> 1
0
>>> 10 >> 1
5
>>> 10 >> 2
2
>>> 10 >> 3
1
>>> 100 >> 1
50
>>> 100 >> 2
25
>>> 100 >> 3
12
>>> 100 >> 4
6
>>> operator.rshift(1,1)
0
>>> operator.rshift(1,2)
0
>>> operator.rshift(1,3)
0
>>> operator.rshift(1,4)
0
>>> 
>>> #  left shift
>>> 
>>> 
>>> 1 << 1
2
>>> 1 << 2
4
>>> 1 << 3
8
>>> 1 << 4
16
>>> -1 << 1
-2
>>> -1 << 2
-4
>>> -1 << 3
-8
>>> -100 << 3
-800
>>> -100 << 1
-200
>>> 
>>> operator.lshift(1,1)
2
>>> operator.lshift(1,3)
8
>>> operator.lshift(1,-1)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    operator.lshift(1,-1)
ValueError: negative shift count
>>> operator.lshift(1,5)
32
>>> operator.lshift(1,2)
4
>>> operator.lshift(1,3)
8
>>> operator.lshift(1,4)
16
>>> operator.lshift(1,5)
32
