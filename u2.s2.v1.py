# Problem 1: Cast Vote
def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes.update({candidate:1})



votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)


def common_keys(dict1, dict2):
    lst = []
    for key in dict1:
        if key in dict2:
            lst.append(key)
    return lst

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)



# Highest Priority Task
def get_highest_priority_task(tasks):
    pass


tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
lst = tasks.values() # Debug line
print("tasks.values() = ", lst) # Debug print


#perform_task = (get_highest_priority_task(tasks))
#print(perform_task)
#
#perform_task = (get_highest_priority_task(tasks))
#print(perform_task)
#
#perform_task = (get_highest_priority_task(tasks))
#print(perform_task)
#
#print(tasks)
