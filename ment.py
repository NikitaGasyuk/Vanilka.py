import random

"""
Написать функцию, которая принимает два целочис-
ленных списка и возвращает True, если первые или последние
элементы данных списков равны. Оба списка содержат 1 или
более элементов
"""

list1 = [random.randint(-1000000, 100000) for i in range(20)]
list2 = [random.randint(-1000000, 100000) for i in range(20)]
def check_lists(list1, list2):
    return list1[0] == list2[0] or list1[-1] == list2[-1]: # все равно вернет одно и то же
    #     return True 
    # else:
    #     return False

print(check_lists(list1, list2))
