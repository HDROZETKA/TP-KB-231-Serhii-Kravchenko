START_DICT = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
print("Початковий словник:", START_DICT)
start_dict0 = START_DICT.copy()

start_dict0.update({"g": 7, "b": 999})
print("update({'g': 7, 'b': 999}) додає нові пари і оновлює існуючі ключі:", start_dict0)

del start_dict0["c"]
print("del dict0['c'] видаляє пару з ключем 'c':", start_dict0)

start_dict0.clear()
print("clear() очищає словник:", start_dict0)

start_dict0 = START_DICT.copy()

print("keys() повертає всі ключі:", start_dict0.keys())

print("values() повертає всі значення:", start_dict0.values())

print("items() повертає всі пари ключ-значення:", start_dict0.items())
