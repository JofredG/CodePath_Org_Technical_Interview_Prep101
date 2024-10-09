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


#Problem 4: Longest Uniform Substring
#Understand: given a string with char in Unicode return the length of a substring consisting of a single repeated character
#Plan: Iterate through the list incrementing up for every letter equivalent to last letter. If there is a letter
# that is not equivalent to the last letter decrement.
def longest_uniform_substring(s):
    substringLength = 0
    ans = 0
    prevChar = s[0]
    for char in s:
        if char == prevChar:
            substringLength += 1
        else:
            if substringLength > ans:
                ans = substringLength
            substringLength = 1
            prevChar = char
    return ans



s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)



#Understand: Given a list with attack times and a single value for poison duration
# return the number of times where the poison state is active. Note that every state
# is either being attacked, poisoned or no action - not two at the same time.
#Plan: To take consideration of overlap of poison duration and attack time when Teemo 
# attacks before poison duration ends we will get the min value of time_series[n+1]-time_series[n]attack 
print("")
print("Problem 5: Teemo's Attack")
def find_poisoned_duration(time_series:list, duration:int)->int:
    total_duration:int = 0

    for i in range(len(time_series)):
        if i == len(time_series)-1:
            total_duration += duration
        else:
            actual_duration = min(time_series[i+1]-time_series[i]-1, duration)
            total_duration += actual_duration
    return total_duration

time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)


#Understand: Given two lists sum the elements in lst1 that are unique in the scope of lst1
# and ensure those that are unique in lst1 do not appear in lst2
#Plan: Create a dictionary and add all elements of lst1 keeping track of their count
# Iterate through dictionary. If element's count in dictionary ==1 and element not in lst2 add to sum
print("")
print("Problem 6: Sum Unique Elements")
def sum_of_unique_elements(lst1, lst2):
    d:dict = {}
    summation:int = 0
    for i in range(len(lst1)):
        if lst1[i] not in d:
            d[lst1[i]] = 1
        else:
            d[lst1[i]] += 1
    for element in d:
        if d[element] == 1 and element not in lst2:
            summation += element
    return summation

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)
    
