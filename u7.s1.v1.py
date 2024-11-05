'''
Recursion Notes:
    Base case is the condition that stops calling the recursive function and allows the outputs to bubble up the call stack.
    The recursive case is the condition that calls the recursive function approaching the base case.
    Recursive case input should be different for every call and approaching the base case.
    Something I noticed that may not be entirely true: Base case and recursive case-function call both go after a return statement
'''

#Problem 1 Hello Hello
def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
repeat_hello(5)


def repeat_hello2(n):
    for i in range(n):
        print("Hello")

repeat_hello2(3)


print("__________________________")
#Problem 2
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))



print("__________________________")
#Problem 3
def sum_list(lst):
    if len(lst) == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
