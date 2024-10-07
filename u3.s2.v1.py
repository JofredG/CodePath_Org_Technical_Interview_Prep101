# Problem 1: Sum of Strings

#Understand: Given a list of strings containing numbers
# find the sum of the the string
#Plan: loop through list converting every string to a number
# and adding to the ans variable
def sum_of_number_strings(nums:list):
    ans = 0
    for i in nums:
        i = int(i)
        ans += i

    return ans

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

#Understand: Take input list of nums and return a list of nums w unique nums only(no duplicates)
#Planning: Loop through input list of numbers and add to dictionary. Iterate through dictionary
#appending only keys to new list

def remove_duplicates(nums: list) -> list:
    ans = []
    d = dict() 
    for num in nums:
        if num in nums:
            d[num] = 0
        d[num] += 1
    for key in d:
        ans.append(key)
    return ans




nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))


#Problem 3 Reverse Letters
#Understand: Take input string containing letters and  non-letters. Return a string that 
# has all letters reversed but non-letters keep their position
#Plan: Iterate through input string using .isalpha() to see if curr char is a letter.
# If letter, add to start of ans string. 
# Loop over the input string again looking for non-letters. If non-letter, insert non-letter to ans
# string using the index from input string. 
#def reverse_only_letters(s:str) -> str:
#    ans:str = ""
#    for i in s:
#        if i.isalpha():
#            ans.insert(0, i)
#    for i, char in enumerate(s):
#        if not i.isalpha():
#            ans.insert(i, char)
#    return ans
def reverse_only_letters(s:str) -> str:
    lst = list()
    ans = ""
    for char in s:
        if char.isalpha():
            lst.append(char)
    for char in s:
        if char.isalpha():
            ltr = lst.pop()
            ans = ans + ltr
        else:
            ans = ans + char
    return ans

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)



