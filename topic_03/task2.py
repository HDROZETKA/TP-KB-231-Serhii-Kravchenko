START_LIST = [9, 8, 7, 6, 5, 6, 7, 8, 9]
print("Початковий список:", START_LIST)

start_list0 = START_LIST.copy()  # Створимо копію списку для подальшої роботи

start_list0.extend([8, 7, 6, 5, 4, 3, 2, 1])
print("extend() додає кожен елемент іншого списку:", start_list0)

start_list0.append(10)
print("append() додає один елемент на кінець:", start_list0)

start_list0.insert(2, 5)
print("insert(6, 5) вставляє 5 на місце 6:", start_list0)

start_list0.remove(5)
print("remove(5) видаляє першу 5-ку:", start_list0)

start_list0.clear()
print("clear() очищає список:", start_list0)
start_list0 = START_LIST.copy()

start_list0.sort()
print("sort() сортує список за зростанням:", start_list0)

start_list0.sort(reverse=True)
print("sort(reverse=True) сортує список за спаданням:", start_list0)

start_list0.reverse()
print("reverse() змінює порядок елементів на протилежний:", start_list0)

list_copy = start_list0.copy()
print("copy() створює копію списку:", list_copy)
