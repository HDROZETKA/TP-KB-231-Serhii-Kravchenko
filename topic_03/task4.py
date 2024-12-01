def find_insert_position(sorted_list, new_element):  # 1 СПОСІБ
    for i, val in enumerate(sorted_list):
        if new_element <= val:
            return i
    return len(sorted_list)  # Якщо новий елемент більший за всі


def find_insert_position_with_sort(sorted_list, new_element):  # 2 СПОСІБ
    new_list = sorted_list.copy()
    new_list.sort()
    return new_list.index(new_element)


start_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
element = 'e'
print(f'Початковий список: {start_list}')
print(f'Елемент для вставки: {element}')
print(f'Резульатат отриманий перебором та порівнянням кожного елемента: {find_insert_position(start_list, element)} місце')
print(f'Резульатат отриманий вставкою та викликом сортувальника: {find_insert_position_with_sort(start_list, element)} місце')
