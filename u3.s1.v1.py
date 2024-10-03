#Problem 1: Calling Mississippi
def count_mississippi(limit):
    for num in range(1, limit):
	    print( f"{num} mississippi")

count_mississippi(6)


#Problem 2: Swap Ends
def swap_ends(my_str):
    if len(my_str) <= 1: return my_str
    return my_str[-1] + my_str[1:-1] + my_str[0]

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)


#Problem 3: Is Pangram
#Understand: we need to see that the input has all letter in the alphabet
#Plan: 
#Make a list containing alphabet and loop through it checking if every letter is in 
#the input string. This way if letter is not in string we return false. If we reach z
# in the alphabet and it's in the string we return True
# 
def is_pangram(my_str):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in alpha:
        if letter in my_str:
            if letter == 'z':
                return True
        else: return False


my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))


#Problem 4: Reverse String
#Understand: reverse the string
#Plan: append the last char in the string to a new variable
#pop the last char and repeat previous step for len(string)-1 iterations
# 
def reverse_string(my_str):
    newStr = ""
    for char in len(my_str):
        newStr.append(my_str[char])
        my_str.pop()


my_str = "live"
print(reverse_string(my_str))

