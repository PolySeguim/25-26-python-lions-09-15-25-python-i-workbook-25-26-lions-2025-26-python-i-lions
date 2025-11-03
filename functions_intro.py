"""
header file with info
"""

#All import statements are here
import math

#Functions are either void or fruitful

#Global Variability
global f_name

#FUNCTION DECLARATIONS
#void function
def setName(fname):
    #fname is the local function variable
    #f_name is global variable set above
    f_name.set(fname)
    print(f_name)

#fruitful function
def getName():
    return f_name

"""
sum(list of numbers)
function <- adds up all the numeric values within a list
return int sum
author: Poly (10-08-25)
"""
def sum(numbers):
    sum = 0
    for i in numbers:  #[1:len(numbers)]
        sum += i  #  +=  -->  sum = sum + i
        #print(sum)
    return sum

def absValue(x):
    if x < 0:
        return -x  #If the number x meets the condition (x is negative)
    return x

def absoluteValue(x):
    if x < 0:
        return -x  # the return statement exits the function
    else:
        return x

def distance(x1, y1, x2, y2):
    return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
    #return ((x2-x1)**2 + (y2-y1)**2))**(0.5)

# Boolean Functions return a true or false
# examples of boolean functions are:
#   - is age 16?
#   - is the pwd correct?

# Fun Fact: boolean functions are normally name is____
def isDivisible(x, y):
    if (x%y == 0):
        return True
    else:
        return False


# A fruitful compare function that compares two integers
# and 
# ***  returns the largest integers
def compare(num1, num2):
    if(num1>num2):
        return num1
    elif(num2>num1):
        return num2
    else:
        print("Numbers are equal")
        return 0

print(compare(5, 4))
print(compare(5.0, 5.5))
print(compare(-5, 4.0))
print(compare(15, 40))
print(compare(1, -1000))
print(compare(10,10))
# SQUARE ROOT num**(1/2)

# A fruitful hypotenuse function that 
# *** returns the value of
# the hypotenuse given the a and b value

# A fruitful slope function that 
# *** returns the slope of a line
# given 4 parameters (x1, y1, x2, y2)

# A fruitful intercept function that will find the y-intercept
# given two points (x1, y1, x2, y2)
# ***  returns the y-intercept
# ***  This function should call the slope function in order to 
# *** calculate the y-intercept or b-value

# A fruitful function that will calculate whether a number is
# a factor of another number.  
# *** Is 3 a factor of 9?
# *** return a BOOLEAN (True or False)

# A fruitful function that will calculate whether a number is
# a multiple of another number.  
# *** Is 12 a multiple of 36?
# *** return a BOOLEAN (True or False)


#Function Calls
"""
num1 = 1,2,3,4,5,6,7,8,9,10,10
num1 = 2.3, 4.2, 6.2, 7.3
test1 = sum(num1)
print(test1)
"""
num1 = 1,2,3,4,5,6,7,8,9,10,10
test = sum(num1)

#Absolute Value
print(absValue(-23))

#Distance Formula
dist =  distance(1,2,3,4)
print(dist)

print(isDivisible(5,2))
print(isDivisible(12,4))
print(isDivisible(18,6))