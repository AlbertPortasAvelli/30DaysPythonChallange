### Exercises Day 3 ###

# 1 - Declare your age as integer variable
age = 30
# 2 - Declare your height as a float variable
height = 1.84
# 3 - Declare a variable that store a complex number
complex_number = complex()
# 4 - Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input('Enter the base of your triangle : '))
height = float(input('Enter the height of your triangle : '))
area = 0.5 * base * height
print('The area of the triangle is {}'.format(area))
# 5 - Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = input('Enter the side A : ')
side_b = input('Enter the side B : ')
side_c = input('Enter the side C :')
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is {}'.format(perimeter))
# 6 - Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length_rectangle = float(input('Length Rectangle : '))
width_rectangle = float(input('Width Rectangle :'))
area_rectangle = length_rectangle * width_rectangle
perimeter_rectangle = 2 * length_rectangle * width_rectangle
# 7 - Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input ('Radius : '))
from exercices_day02 import area_calculation, circum_calculation
area_circle = area_calculation(radius)
print('Area : {}'.format(area_circle))
circum_circle = circum_calculation(radius)
print('Circumference : {}'.format(circum_circle))
# 8 - Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope0 = 2
y_intercept = 2
x_intercept = (y_intercept + 2)/2
print('Slope : {}\nX : {}\nY : '.format(slope0, x_intercept, y_intercept))
# 9 - Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope1 = (2 - 2) / (10 - 6)
import math
euclideanDistance = math.sqrt(((2 -2)**2)+((10 - 6)**2)) 
# 10 - Compare the slopes in tasks 8 and 9.
slope0 > slope1
slope0 < slope1
slope0 == slope1
# 11 - Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
import sympy as sp
x = sp.symbols('x')
y = x**2 + 6*x + 9
x_values = [-3, -2, -1, 0, 1, 2, 3]
for val in x_values:
    result = y.subs(x, val)
    print(f'For x = {val}, y = {result}')
roots = sp.solve(y, x)
print(f'Roots (x values when y is 0): {roots}')
# 12 - Find the length of 'python' and 'dragon' and make a falsy comparison statement.
word0 = 'python'
word1 = 'dragon'
len(word0) != len(word1)
# 13 - Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in word1 and 'on' in word0)
# 14 - I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')
# 15 - There is no 'on' in both dragon and python
print(not ('on' in word1 and 'on' in word0))
# 16 - ind the length of the text python and convert the value to float and convert it to string
float_len = float(len('python'))
print('{} : {}'.format(float_len, type(float_len)))
string_num = str(float_len)
print('{} : {}'.format(string_num, type(string_num)))
# 17 - Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
def is_even(number):
    return number % 2 == 0
num = 10

if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
# 18 - Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print((7 // 3) == int(2.7))
# 19 - Check if type of '10' is equal to type of 10
print(type('10') == 10)
# 20 - Check if int('9.8') is equal to 10
#print(int('9.8') == 10) invalid input
# 21 - Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input('Hours : '))
rate = float(input('Rate per hour : '))
print('Your weekly earning is {}'.format(hours * rate))
# 22 - Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years_lived = int(input('Years you have lived : '))
print('You have lived {} seconds'.format(years_lived * 31536000))
# 23 - Write a Python script that displays the following table
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
def exponentials_cube():
    for column in range(1, 6):
        for row in range(1, 6):
            if row == 1:
                print('{} '.format(column), end ='')
            else:
                if row == 5:
                    print('{}\n'.format(column ** (row-2)), end = '')
                else:
                    print('{} '.format(column ** (row-2)), end = '')

            

# Call the function
exponentials_cube()