#23.12.2019
#Variable
>>> a = 1
>>> a
1
>>> b = 2
>>> b
2
>>> x = a + b
>>> x
3
>>> text = "Hello"
>>> text
'Hello'
>>> text = 'Hello'
>>> text
'Hello'
>>> text = Hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Hello' is not defined
>>> 2 + 2
4
>>> 50 - 5 * 6
20
>>> (50 - 5 * 6) / 4
5.0
>>> 8 / 5
1.6
>>> 17 / 3
5.666666666666667
>>> 17 // 3
5
>>> 16 // 2
8
>>> 16 // 2
8
>>> 17 // 3
5
>>> 21 // 2
10
>>> 17 % 3
2
>>> 19 % 2
1
>>> 23  =
  File "<stdin>", line 1
    23  =
        ^
SyntaxError: invalid syntax
>>> 23 + 20 - 40 % 4 * 2
43
>>> 25 % 2 * 3
3
>>> 40 - 20 % 9 * 2 - 2
34
>>> 5 ** 2
25
>>> 7 ** 2
49
>>> 2 ** 6
64
>>> 3 ** 9
19683
>>> width = 20
>>> height = 5*9
>>> width * height
900
>>>

#Loops

-While Loops
-for Loops

Condition is true, while loop execute a set of statements

x = 1
while x < 7:
	 print(x)
	   x += 1

Loops.py

Python Conditions

Equals         -> x == y
Not Equals     -> x != y
Less than      -> x < y
Less than or equal to   -> x >= y
Greater than     -> x > y
Greater than or equal to    -> x >= y 
Boolean OR     -> x or y , x | y
Bollean AND    -> x and y , x & y
Bollean NOT    -> not x

While loop require variable ready.
 x = 1
 while x < 7:
 	  print(x)
 	  if x == 5:
 	  	break
 	  x += 1

For Loops

#for loops is iterating over a sequence

fruits = [ "apple", "banana", "orange", "pineapple", "coconut", " cucumber" ]
for x in fruits:
	print(x)
	fruits = [ "apple", "banana", "orange", "pineapple", "coconut", " cucumber" ]
for x in fruits:
	print(
for x in fruits:
...     if x == "pineapple":
...             break
...     print(x)

 for x in fruits:
...     if x == "kiwi":
...             brake
...     print(x)

for x in fruits:
...     print(x)
...     if x == "coconut":
...             break
...             print(x)

for x in fruits:
...     if x == "orange":
...             continue
...     print(x)
 for x in fruits:
...     print(x)
...     if x == "coconut":
...             brake
...     print(x)
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
...     print(x)
for x in range(10):
...     print(x)
for x in range (10,100):
...     print(x)


NumberA = [1, 2, 3, 4, 5]
>>> NumberB = [1, 2, 3, 4, 5]
>>> for x in NumberA:
...     for y in NumberB:
...             print(x,y)
for x in NumberA:
...     print(x,y)

for y in NumberB:
...     print(x,y)

 NumberA = [1, 2, 3, 4, 5]
>>> NumberB = [1, 2, 3, 4, 5]
>>> NumberC = [1, 2, 3, 4, 5]
>>>
>>> for x in NumberA:
...     for y in NumberB:
...             for z in NumberC:
...                     print(x,y,z)

for x in [1, 2, 3, 4, 5]:
...     pass

 words = [ 'cat', 'window', 'defenestrate', 'hello world']
>>> for w in words:
...     print(w, len(w))

for n in range(2,10):
...     for x in range(2,n):
...             if n % x == 0:
...                     print(n, 'equals', x,  '*', n//x)
...                     break
...     else:
...             print(n, 'is a prime number')

for num in range(2,10):
...     if num % 2 == 0:
...             print("Found an even number", num)
...             break
...     print("Found a number", num)

for num in range(2,10):
...     if num % 2 == 0:
...             print("Found an even number", num)
...             pass
...     print("Found a number", num)
for num in range(2,10):
...     if num % 2 == 0:
...             print("Found an even number", num)
...             continue
...     print("Found a number", num)