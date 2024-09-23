# Problem Set Version 1
# Problem 1: Hello World!
def hello_world():
    print("Hello world!")

hello_world()

# Problem 2: Today's Mood
def todays_mood():
    mood = "👻";
    print("Today's mood: " + mood)
    
todays_mood()

# Problem 3: Lunch Menu
def print_menu(menu):
    print("Lunch today is: " + menu)

print_menu("🌮")

# Problem 4: Sum of Two Integers
def sum(a, b):
    return a + b

print(sum(5, 10))

#Problem 5: Product of Two Integers

def product(a, b):
    return a * b

print(product(5, 10))

# Problem 6: Classify Age
def classifyAge(age):
    if age < 18:
        return "child"
    else:
        return "adult"

print(classifyAge(4))
print(classifyAge(49))

# Problem 7: What time is it?
def  what_time_is_it(time):
    if time == 2:
        return "taco time 🌮"
    if time == 12:
        return "peanut butter jelly time 🥪"
    else:
        return "nap time 😴"

time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)


# Problem 8: BlackJack
def blackjack(score):
    if score==21:
        print("BlackJack")
    elif score>21:
        print("Bust!")
    elif score > 17 and score < 21:
        print("Nice hand!")
    elif score < 17:
        print("Hit me!")

blackjack(24)
blackjack(19)
blackjack(21)
blackjack(10)


#Problem 9 First Item

def get_first(lst):
    if lst[0]:
        return lst[0]

lst = [3,1,6,7,5]
print(get_first(lst))



# Problem 10 Last Item
lst = [3,1,6,7,5]
def get_last(lst):
    return lst[-1]

print(get_last(lst))


# Problem 11 Counter
def counter(stop):
    for i in range(1,stop+1):
        print(f"{i}")

counter(7)


# Problem 12 Sum of 1 to 10
def sum_ten():
    sum = 0
    for i in range(1,10):
        sum += i
    return sum

print(f"Sum of ten: {sum_ten()}")



# Problem 13 Sum of 1 to x
def sum_positive_range(stop):
    if stop >= 1:
        sum=0
        for i in range(1,stop+1):
            sum+=i
    return sum

print(f"Sum of x: {sum_positive_range(6)}")

# Problem 14 Total sum in range
def sum_range(start, stop):
    sum=0
    for i in range(start, stop+1):
        sum+=i
    return sum

print(f"Sum of range: {sum_range(3,9)}")




# Problem 15 Total sum in range
def print_negatives(lst):
    for i in lst:
        if i < 0:
            print(f"Negative: {i}")
lst = [3,-2,2,1,-5]
print_negatives(lst)
