print(2==3) #we will get flase becuse it conditon is false

print(1==1) # we will get true here

print(True and False) # The and operator always takes two Boolean values (or expressions), so it’s considered to be a binary Boolean operator

print(False or False)
print(False or True) # Like the and operator, the or operator also always takes two Boolean values (or expressions), and therefore is considered to be a binary Boolean operator

print(not True)
print(not False)

print((4 < 5) and (5 < 6))
print( (4 < 5) and (9 < 6))

#multiple boolean expression

spam = 4
print(2 + 2 == spam and not 2 + 2 == (spam + 1) and 2 * 2 == 2 + 2)

#The Boolean operators have an order of operations just like the math operators do. After any math and comparison operators evaluate, Python evaluates the not operators first, then the and operators, and then the or operators.

name = 'kasimn'

age = 3

if name == 'kasim':
    print("love you my baby")
elif age < 12:
    print("you are not my bvaba")    


name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')




