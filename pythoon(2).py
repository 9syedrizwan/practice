# -*- coding: utf-8 -*-
"""pythoon(2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14f6R74X3_CGOD8gKPf6ecFPxhz3KWEcO
"""

print("pakistan zindabad")
print(3,34,4)
print()
print("won")
print("argument","argument",3,4)

print("rizwan","ali","hassnain", sep="<>")

print("rizwan","ali","hassnain", sep="*")

print("pakistan",end="\n")
print("china")
print("afghanistan",end="")
print("india")

print("we all our learners of \npython")

print("pakistan",end="\t")
print("china")
print("afghanistan",end="\t")
print("india")

print("yhis is a string") # string
print("100") # int
print("645.37") # float
print("true") # bool
print("false") # bool

print('this is my friend's book')

print("this is my friend's book")

print("this is my first \"python\" class")

#vary>>>changeable>increase>decrease
#real world quantities:age,height,day,date,weights
#       bloodgroup

marks = 90.6
age = 7
college = dha
exampasses = false
feespayed = true



print(type("marks"),type("age"),type("college"),type("exampasses"),type("feespayed"))

import math
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
    
d = (b**2) - (4*a*c)  
    
sol1 = (-b-math.sqrt(d))/(2*a)  
sol2 = (-b+math.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))

print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\n Twinkle, twinkle, little star,\n\tHow I wonder what you are")

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

import math
pi = 3.142
r = float(input("enter any radius  :"))
a = pi*math.pow(r,2)
print ("the area of the circle is :",a)

first = input("enter your first name:")
last = input("enter your last name:")
s1 = len(first)
s2 = len(last)
print("your name is :",last[:-1],first[::-1])

values = input("Input some comma seprated numbers : ")
lst = values.split(",")
# tup = tup(lst)
print('List:',lst)
# print('Tuple:',tup)

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : ",f_extns[-1])

import math
a = float(input("enterany number : "))
b = float(input("enterany number : "))
c = float(input("enterany number : "))
d = (b**2) - (4*a*c)
sol1 = (-b+math.sqrt(d))/(2*a)
sol2 = (-b+math.sqrt(d))/(2*a)
print("Ans is = ",sol1,sol2)

c=3
e=4
x=5
h="ok"
f="its not"
if c==3:
  if x==1:
    g==h
    print(g)
  elif a==2:
    g==h
    print(g)
  else:
    e==f
    print(e)
else:
  e==f
  print(e)

"""import math
a = input("enter any number : ")
dsgfggrgre
greegrege
grgrgerg
grgrergerer
gerger
gr
ger
ger
gerg"""
#fdsgfdrg

cities = ["karachu","balochistan","hyderabad","kyhber","larkana","punjab","sindh","111","1.1.1"]

cities[3]

cities[-2]

cities[7]

len(cities)

cities[3]="japan"

cities[3]

cities[:]

cities.append("new york")

cities[9]

vowels = ['a', 'e', 'i', 'o', 'i', 'u']
x = input("enter any thing")
index = vowels.index(x)
print('The index :', index)
y = input("enter any thing")
index = vowels.index(y)
print('The index :', index)

cities.insert(1,"karachi")

cities[:]

cities[::-1]

len(cities)

import datetime
first_date = input("enter any thing : ")
last_date = input("enter any thing : ")
x = first_date - last_date
print(x.date)

del cities[0]

cities

len(cities)

from datetime import date
f_date = input("enter : ")
l_date = input("enter : ")
delta = l_date - f_date
print(delta.days)

cities.remove("punjab")

cities

import math
a = float(input('enter a: '))  
b = float(input('enter b: '))  
c = float(input('enter c: '))  
    
d = (b**2) - (4*a*c)  
    
sol1 = (-b-math.sqrt(d))/(2*a)  
sol2 = (-b+math.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))

a=cities.pop(1)
print(a)

abc=[1,2,3,4,5,6,7,8,9,44,-1,-2]
print(sorted(abc))

abc[:]

print(abc.sort())

abc.sort(reverse=True)

abc[:]

print(abc[1:5])

print(abc[-1])

print(abc[-1:])

print(abc[-1:-1])

print(abc[-1:6])

print(abc[-6:])

print(abc[-6:-1:1])

print(abc[-6:-1:2])

abc= ("delaware","pennsylenvia","new jersy","georgia",5)

abc[:]

city=["karachi","balochistan","punjab","khyber","pakhtoon","rawalpindi","sindh","lahore","neelam","kashmir"]
city.sort()
print(city)

city.sort(reverse=True)
print(city)

sub=city[4:8]
print(sub)

