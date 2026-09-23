# this code will say hello and ask for my name

print("hello, ki khobor?")

print("whats your name?")

my_name = input('>') #inside input() function we can give a prompt to the user to enter the input. we used '>' as a prompt to the user to enter the input. it will be displayed before the input box.

#when we take as input from user it will be in string format so we don't need to convert it to string format. but if we want to take input as integer or float then we need to convert it to integer or float format using int() or float() function.
# input() user-এর typed text হিসেবে input নেয় এবং string return করে।
my_age = int(input('Enter your age: ')) # it will take input from user and convert it to integer format using int() function.
my_height = float(input('Enter your height in meters: ')) # it will take input from user and convert it to float format using float() function.
my_weight = float(input('Enter your weight in kg: ')) # it will take input from user and convert it to float format using float() function.



print("hello " + my_name + " nice to meet you")

print("the length of my name is :")
print(len(my_name)) #it will give the length of my name because we are using len() function to find the length of my name

print("what is your age")

my_age = input('>')

print("you will be " + str(int(my_age)+1)+ "in next year") #it will give the age of my name after adding 1
# because we are converting the input to integer and then adding 1 and then converting it back to string to
#  concatenate with the rest of the string 


#we can also use ' ' for printing strings in python but it is a good practice to use " " for printing strings in python
print('hello, ki khobor?')


print() # it will give a new line because we are using print() function without any argument



# Python string আর integer-কে + দিয়ে concatenate করতে দেয় না।
# print("i am " + 24 + " years old") #it will give error because we are trying to concatenate string and integer

#but if we do this
print("i am " + str(24) + " years old") #it will give "i am 24 years old" because we are converting integer to string using str() function and then concatenating with the rest of the string   



print(int(23.5)) #it will give 23 because we are converting float to integer using int() function and it will remove the decimal part of the float number   


#round() function will round the float number to the nearest integer
print(round(23.5)) #it will give 24 because we are rounding the float number to the nearest integer using round() function
print(round(23.4)) #it will give 23 because we are rounding the float number to the nearest integer using round() function
print(round(23.6)) #it will give 24 because we are rounding the float number to the nearest integer using round() function  



print(round(2.5)) #it will give 2 because we are rounding the float number to the nearest integer using round() function
print(round(3.5)) #it will give 4 because we are rounding the float` number to the nearest integer using round() function `

#it is called banker's rounding or round half to even. It is a method of rounding that rounds to the nearest even number when the number is exactly halfway between two integers.   



# abs() function will give the absolute value of a number
print(abs(-23)) #it will give 23 because we are taking the absolute value of -23 using abs() function
print(abs(23)) #it will give 23 because we are taking the absolute value of 23 using abs() function 






