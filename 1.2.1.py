
lst = ["squirtle", "gengar", "charizard", "pikachu"]
def print_list(lst):
    for item in lst:
      print (item)

print_list(lst)

print("_______________________________________________")
lst = [1,2,3]
def doubled(lst):
    for item in lst:
        print(item*2)

doubled(lst)



print("_______________________________________________")
lst = [1,2,3]


def doubled(lst):
    for item in range(len(lst)):
        lst[item] = lst[item]*2
    return lst

new_lst = doubled(lst)
print(new_lst)


print("_______________________________________________")
lst = [1,-2,-3,4]
def flip_sign(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] *-1
    return lst

flipped_lst = flip_sign(lst)
print(flipped_lst)


print("_______________________________________________")
lst = [5,22,8,10,2]
def max_difference(lst):
    minimum = min(lst)
    maximum = max(lst)
    return maximum - minimum


max_diff = max_difference(lst)
print(max_diff)


print("_______________________________________________")
numbers = [12,8,2,4,4,10]
ans = []
def count_less_than(numbers, threshold):
    for i in numbers:
        if (i < threshold):
            ans.append(i) 
    return len(ans)



counter = count_less_than(numbers,5)
print(counter)




print("_______________________________________________")
lst = [1,2,3,4]
ans = []
def get_evens(lst):
    for i in lst:
        if (i%2 == 0):
            ans.append(i)

    return ans




evens_lst = get_evens(lst)
print(evens_lst)




print("_______________________________________________")
def multiples_of_five():
    for i in range(5, 101, 5):
        print (i)

multiples_of_five()






print("_______________________________________________")

def find_divisors(n):
    for


lst = find_divisors(6)
print(lst)



print("_______________________________________________")
# Resume 11
def print_indices(lst):
    pass

lst = [5,1,3,8,2]
print_indices(lst)
