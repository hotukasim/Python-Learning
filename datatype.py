print(5+3)
print("5"+3) #it will give error because we cannot concatenate string and integer
            
but
print("5"+"3") #it will give 53 because we are concatenating two strings
                #it is called string concatenation

#but
print("5"+str(3)) #it will give 53 because we are converting integer to string and then concatenating

#and
print(5*"3") #it will give error because we cannot multiply string and integer
#but
print("5"*3) #it will give 555 because we are multiplying string with integer
            #its called string replication

#but
print("sammo"*3.0) #it will give error because we cannot multiply string and float


print((type(5))) #it will give <class 'int'> because 5 is an integer
print((type(5.0))) #it will give <class 'float'> because 5.0 is a float
print((type("5"))) #it will give <class 'str'> because "5" is a string


"""
this code is about operator precedence in python
this code has some bug in it because it is not complete and it is not working properly
don't run this code because it will give error
the error line are mentioned by comments in the code
"""
