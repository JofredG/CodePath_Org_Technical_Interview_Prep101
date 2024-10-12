import math
#Problem 1: is_prime()
def is_prime(n):
    if n <=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
            return False
    return True


print(is_prime(1))
print(is_prime(121))
print(is_prime(3))


#Understand
#Plan: Loop through the len(lst/2) switch places of first and last using indexes in the for loop.
#use index to move right and len(lst)-i to move left 
#swap places of values on both sides
def reverse_list(lst):
    for i in range(len(lst)//2): #// is integer division
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
    return lst

#def reverse_list(lst):
#    num1:int = lst[0]
#    num2:int = lst[-1]
#    for i in range(ceil(lst/2)):
#        num1, num2 = num2, num1
#        lst[i] = num1
#        lst[-i] = num2
#    return lst


print(reverse_list([1, 2, 3, 4, 5]))


#Understand: given list of nums move evens to the start. Return a lst that has no odd numbers to left of even numbers
#Plan: Loop and look for evens. If even insert at start of lst else continue
#init 1 pointer outside of loop
#in for loop use index 
def sort_array_by_parity(nums):
    even = []
    odd = []
    if len(nums) <= 1:
        return nums
    for i in range(len(nums)//2):
        if nums[i] % 2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
        if nums[-i-1] % 2 == 0:
            even.append(nums[-i-1])
        else:
            odd.append(nums[-i-1])
    return even + odd

nums = [3,1,2,4]
nums2 = [0]
nums3 = [1]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
print(sort_array_by_parity(nums3))

#Understand: check that first and last characters moving towards center of word are equivalent
#Plan: Use ptr at start and end to check equivalence. If equivalent return word else don't

#def first_palindrome(words):
#    for word 


words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)
