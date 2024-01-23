### Loops ###
# control flow structures that allow a set of instructions to be repeated multiple times
# until a certain condition is met. 

# 1 - While Loop
#is a control flow structure in programming that repeatedly executes a block
# of code as long as a specified condition is true.
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
# 2 - Break and Continue
# Break: statement is used to prematurely exit a loop, regardless of whether the loop condition is still true.
# Continue : is used to skip the rest of the code inside a loop for the current iteration and move to the next iteration.
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
# 3 - For Loop
# is a control flow structure in programming that is used to iterate over a sequence of elements.
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)
# 4 - Break and Continue
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
# 5 - The Range Function
# used to generate a sequence of numbers. It's commonly used in for loops to iterate over a specific range of values. 
for number in range(11):
    print(number)
# 6 - Nested For Loop
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
# 7 - For Else
for number in range(11):
    print(number) 
else:
    print('The loop stops at', number)
# 8 - Pass
#  is a null statement, a no-operation placeholder.
for number in range(6):
    pass
