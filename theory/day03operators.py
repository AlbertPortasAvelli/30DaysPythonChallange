### Operators ###
#   1 - Boolean
#       A boolean data type represents one of the two values: True or False. 

boolean_one = True
boolean_two = False

#   2 - Operators
#       symbols or keywords that perform operations on operands.

#       2.1 - Assignment Operators
num = 4  # x = 4
num += 2 # x = x + 2
num -= 4 # x = x - 4
num *= 3 # j = j x 3
num /= 3 # x = x / 3
num %= 1 # x = x % 1
num //= 4 # x = x // 4
num **= 3 # x = x ** 3
num &= 3 # x = x & 3
num |= 2 # x = x | 2
num ^= 9 # x = x ^ 9
num >>= 3 # x = x >> 3
num <<= 4 # x = x << 4
#       2.2 - Arithmetic Operators
# Addition +
num = 2 + 3
# Substraction -
num = 4 -2
# Multiplication *
num = 2 * 5
# Division /
num = 3/2
# Modulus %
num = 2 % 4
# Exponentiation **
num = 2 ** 4
# Floor division
num = 2 // 3
#       2.3 - Comparison Operators
#           used in programming languages to compare two values and determine the relationship between them.
# Equal ==
2 == 2
# Not equal !=
1 != 3
# Greater than >
4 > 2
# Less than <
2 < 5
# Greater than or equal to >=
2 >= 1
2 >= 2
# Less than or equal to <=
1 <= 3
1 <= 1
'''In addition to the above comparison operator Python uses:
        - is: Returns true if both variables are the same object(x is y)
        - is not: Returns true if both variables are not the same object(x is not y)
        - in: Returns True if the queried list contains a certain item(x in y)
        - not in: Returns True if the queried list doesn't have a certain item(x in y)
'''

#Examples

print(1 is 1)
print(1 is not 2)
print('A' in 'Albert')
print('C' not in 'Albert')

#       2.4 - Logical Operators
#           Logical operators are used to perform logical operations on Boolean values or expressions.

# And 
print(2 == 2 and 1 == 4)
print(2 == 2 and 1 == 1)
# or
print(2 == 2 or 1 == 4)
print(2 != 2 or 1 != 1)
print(2 != 2 or 1 == 1)
print(1 == 1 or 2 == 2)
# not
print(not True)
print(not False)
