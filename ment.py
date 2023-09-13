def check_lists(list1, list2):
    if list1[0] == list2[0] or list1[-1] == list2[-1]:
        return True
    else:
        return False
list1 = []
list2 = [] 
print(check_lists(list1, list2))
