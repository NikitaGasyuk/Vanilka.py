def compare_lists(list1, list2):
if len(list1) != len(list2):
return False
for i in range(len(list1)):
if list1[i] != list2[-1]:
return False
return True
