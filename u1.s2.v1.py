print("_______________________________________________Problem 1 Print List")
lst = ["squirtle", "gengar", "charizard", "pikachu"]
def print_list(lst):
    for item in lst:
      print (item)

print_list(lst)

print("_______________________________________________Problem 2 Print Doubled List")
lst = [1,2,3]
def doubled(lst):
    for item in lst:
        print(item*2)

doubled(lst)



print("_______________________________________________Problem 3 Return Doubled List")
lst = [1,2,3]


def doubled(lst):
    for item in range(len(lst)):
        lst[item] = lst[item]*2
    return lst

new_lst = doubled(lst)
print(new_lst)


print("_______________________________________________Problem 4 Flip Signs")
lst = [1,-2,-3,4]
def flip_sign(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] *-1
    return lst

flipped_lst = flip_sign(lst)
print(flipped_lst)


print("_______________________________________________Problem 5 Max Difference")
lst = [5,22,8,10,2]
def max_difference(lst):
    minimum = min(lst)
    maximum = max(lst)
    return maximum - minimum


max_diff = max_difference(lst)
print(max_diff)


print("_______________________________________________Problem 6 Below Threshold")
numbers = [12,8,2,4,4,10]
ans = []
def count_less_than(numbers, threshold):
    for i in numbers:
        if (i < threshold):
            ans.append(i) 
    return len(ans)



counter = count_less_than(numbers,5)
print(counter)




print("_______________________________________________Problem 7 Evens List")
lst = [1,2,3,4]
ans = []
def get_evens(lst):
    for i in lst:
        if (i%2 == 0):
            ans.append(i)

    return ans




evens_lst = get_evens(lst)
print(evens_lst)




print("_______________________________________________Problem 8 Multiples of Five")
def multiples_of_five():
    for i in range(5, 101, 5):
        print (i)

multiples_of_five()






print("_______________________________________________Problem 9 Divisors")

def find_divisors(n):
    lst = []
    for num in range(1,n+1):
        if n%num == 0:
            lst.append(num)
    return lst

lst = find_divisors(6)
print(lst)



print("_______________________________________________Problem 10 FizzBuzz")

def fizzbuzz(n):
    for num in range(1,n):
        if num%5 == 0 and num%3 == 0:
            print("FizzBuzz")
        elif num%5 == 0:
            print("Buzz")
        elif num%3 == 0:
            print("Fizz")
        else:
            print(num)
fizzbuzz(18)

print("_______________________________________________Problem 11 Print the Index")
# Resume 11
def print_indices(lst):
    for index in range(len(lst)):
        print(index)

lst = [5,1,3,8,2]
print_indices(lst)


print("_______________________________________________Problem 12 Linear Search")
def linear_search(lst, target):
    for pos in range(len(lst)):
        if lst[pos] == target:
            print(f"Index of target: {pos}")
            return
    print("Target not found")
    return

lst = [1,4,5,2,8]
linear_search(lst,5)
#position = linear_search(lst,5)
#print(position)
