#A1
print ("Jakob Schönberg")
print ("Python 2026")
print ("Python Fundamentals 1")

#A2
name = "Jakob"
age = 48
height = 1.95
is_student = True
print (name)
print (type(name))
print (age)
print (type(age))
print (height)
print (type(height))
print (is_student)
print (type(is_student))

#A3
number = "67"
print (type(number))
number = int(number)
print (type(number))
#In most cases you don't need to specify the data type,
# it is assigned automatically and the same variable can be
# reused with a new data type when assigning a new value

#A4
import math, numpy
val1 = math.pi
val2 = numpy.exp(1)
print (val1)
print (val2)
print ("pi + e: " + str(val1 + val2))
print ("pi - e: " + str(val1 - val2))
print ("pi * e: " + str(val1 * val2))
print ("pi / e: " + str(val1 / val2))
print ("pi // e: " + str(val1 // val2))
print ("pi % e: " + str(val1 % val2))
print ("pi ^ e: " + str(val1 ** val2))

#A5
number = "12"
number = int(number)
print(type(number))
number = 5/3
print (number)
print (type(number))
#not sure what we are supposed to do about this,
# from what I can see, in newer versions of python
# int to float conversion is automatic when the result is a float
number = str(number)
print(number)
print(type(number))