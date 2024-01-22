### Conditionals ###
#Python conditionals are statements that control the flow of a program by evaluating whether a given expression is true or false. 

# 1 - If Condition
if True:
    print('This is true')
# 2 - If Else
if True:
    print('This is true')
else:
    print('This is false')
# 3 - If Elif Else
a,b = 2, 3
if a > b:
    print('a is higher than b')
elif a == b:
    print('a and b are equal')
else:
    print('b is higher than a')
# 4 - Short Hand
print('A is positive') if a > 0 else print('A is negative')
# 5 - Nested Conditions
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
# 6 - If Condition and Logical Operators
    a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
# 7 - If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
