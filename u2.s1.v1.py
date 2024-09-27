# Problem 1:
def is_subsequence(lst, sequence):
    seq_index = 0
    for i in lst:
        if i == sequence[seq_index]:
            seq_index+= 1
        if seq_index == len(sequence):
            return True

            


lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))

print("___________________________")

# Problem 2:
def create_dictionary(keys, values):
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
    return dict



keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))
#dict2 = {4 : "davila", "peter": "samaan", "jofred":"gonzalez"}
#print(dict2[4])


print("___________________________")
# Problem 3:
def print_pair(dictionary, target):
    if target in dictionary:
        print(f"Key: {target}")
        print(f"Value: {dictionary[target]}")
    else:
        print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")



print("___________________________")





# Problem 4:
def keys_v_values(dictionary):
    pass

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)











# Problem 5:
def restock_inventory(current_inventory, restock_list):
    pass


current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}


restock_inventory(current_inventory, restock_list)




# Problem 6:
def calculate_gpa(report_card):
    pass

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))











# Problem 7:
def highest_rated(books):
    pass

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]


highest_rated(books)



# Problem 8:
def index_to_value_map(lst):
    pass


lst = ["apple", "banana", "cherry"]
