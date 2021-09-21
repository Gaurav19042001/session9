'''Anonymous function and Lambda Function
function without name
lambda keyword is used to create anonymous function
in lambda function you can take any no of arguments but there should be only single expression
'''

'''string='Python'
print(lambda string:string)'''

'''x='python'
(lambda x:print(x))(x)'''

'''def cube(x):
    return x*x*x

cube2=lambda x:x*x*x   #lambda argument:expression .....syntax

print(cube(3))
print(cube2(3))
'''
'''lambda function used inside a normal function'''
'''def power(n):
    return lambda x:x**n

base=power(2) 
print("8 power of 2= ",base(8))

base=power(5)
print("5 power of 5= ",base(5))'''

'''
Create a function that takes a "base number" as an argument. 
This function should return another function which takes a new argument, and returns the sum of the "base number" and the new argument.
Please check the examples below for a clearer representation of the behavior expected.
Examples
# Calling make_plus_function(5) returns a new function that takes an input,
# and returns the result when adding 5 to it.

plus_five = make_plus_function(5)

plus_five(2) ➞ 7

plus_five(-8) ➞ -3

'''

'''def plus_func(base_num):
    return lambda x:x+base_num
x=plus_func(7)
print(x(5))'''

'''filter()
allows you to process an iterable and extract those items that satisfy a given condition
'''

'''def func(variable):
    letters=['a','e','i','o','u']
    if (variable in letters):
        return True
    else:
        return False

sequence=['s','e','r','i','t']
filtered=filter(func,sequence)
print("the filtered letters are: ")
for i in filtered:
    print(i)'''

'''map()
allows you to process & transform all the items in an iterable without using an explicit for loop '''

'''def addition(n):
    return n+n

numbers=(1,2,3,4)
result=map(addition,numbers)
print(list(result))'''

'''create a function to check whether the number is divisible by 2 or not
take list of numbers and check all the numbers 
using lambda function ,filter(),map()'''

l=[100,2,8,60,5,4,3,31,10,11]

filtered=filter(lambda x:x%2==0,l)     #in filter we either use assignment or conditional operator , 
print(list(filtered))                  #the pass actual parameter will get return

maped=map(lambda x:x%2==0,l)           #in map we either use assignment or conditional operator ,
print(list(maped))                     #the result of value will get returned