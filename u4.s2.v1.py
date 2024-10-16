#Problem 1: Long Pressed
#Understand: we are trying to return true if a single character differs from the start to the end between the name and typed strings
#Match: Two pointer
#Plan: Iterate through both strings to see if any characters differ from each other
# ptr1 will track the characters in the "name" string
# ptr2 will track the characters in the "typed" string
def is_long_pressed(name:str, typed:str):
    ptr2:int = 0
    for ptr1, char in enumerate(name):
        if name[ptr1] != typed[ptr2]:
            return True
        else:
            ptr2 += 1
    return False


name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))
