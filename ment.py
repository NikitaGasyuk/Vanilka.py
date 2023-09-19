import random

list1 = [random.randint(-1000000, 100000) for i in range(20)]
list2 = [random.randint(-1000000, 100000) for i in range(20)]
def check_lists(list1, list2):
    if list1[0] == list2[0] or list1[-1] == list2[-1]:
        return True
    else:
        return False

print(check_lists(list1, list2))
