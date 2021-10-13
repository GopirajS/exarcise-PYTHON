Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #python while loop
>>> 
>>> n=0
>>> 
>>> while n<10:
	print(n)
	n+=1

	
0
1
2
3
4
5
6
7
8
9
>>> while n<10:
	n+=1
	print(n,end='')

	
>>> 
>>> n=0
>>> while n<10:
	n+=1
	print(n,end='')

	
12345678910
>>> while n<10:
	n+=1
	print(n,end=' ')

	
>>> 
>>> n=0
>>> while n<10:
	n+=1
	print(n,end=' ')

	
1 2 3 4 5 6 7 8 9 10 
>>> 
>>> 
>>> n=0
>>> while n<10:
	n+=1
	if n==5:
		break
		
	print(n,end=' ')

	
1 2 3 4 
>>> n=0
>>> while n<10:
	n+=1
	if n==5:
		continue

	print(n,end=' ')

	
1 2 3 4 6 7 8 9 10 
>>> 
>>> a = 'geeksforgeeks'
>>> n=0


>>> s='gopiraj'
>>> i=0

>>> i=0
>>> while i < len(a):
	if a[i] == 'e' or a[i] == 's':
		i += 1
		continue
	print("current letter :",a[i])
	i+=1

	
current letter : g
current letter : k
current letter : f
current letter : o
current letter : r
current letter : g
current letter : k
>>> n=0
>>> while n<6:
	n+=1
	print('hellow world')

	
hellow world
hellow world
hellow world
hellow world
hellow world
hellow world

>>> while s!=-1:
	s=int(input('enter a number -1 to press exit:'))

	
enter a number -1 to press exit:3
enter a number -1 to press exit:4
enter a number -1 to press exit:2
enter a number -1 to press exit:5
enter a number -1 to press exit:-1
>>> 
>>> 
>>> n=0
>>> while n <10:
	
	n+=1
	if n==5:
		continue
	if n==9:
		break
	print(i,end=" ")

	
13 13 13 13 13 13 13 
>>> while n <10:

	n+=1
	if n==5:
		continue
	if n==9:
		break
	print(n,end=" ")

	
10 
>>> n=0
>>> while n <10:

	n+=1
	if n==5:
		continue
	if n==9:
		break
	print(n,end=" ")

	
1 2 3 4 6 7 8 
>>> 
>>> n=0

>>> while n<5:
	print(i)
	n+=1
	
else:
	print('end')

	
13
13
13
13
13
end
>>> n=0
>>> while n<5:
	print(i)
	n+=1

else:
	print('end')

	
13
13
13
13
13
end
>>> while n<5:
	print(n)
	n+=1

	

else:
	print('end')

	
end
>>> 
>>> n=0
>>> while n<5:
	print(n)
	n+=1



else:
	print('end')

	
0
1
2
3
4
end
>>> while False:
	print('hi')
else:
	print('use else')

	
use else
>>> n=0
>>> while n<6:
	print('hi')
	n+=1
else:
	print('use else')

	
hi
hi
hi
hi
hi
hi
use else
>>> 



i=1
while i<=20:
    if i==7:
        i+=1
        break
    print(i)
    i+=1
i=1    
while i<=20:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1
