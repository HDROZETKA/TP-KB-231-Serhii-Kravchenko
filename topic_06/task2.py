students = [
    {'name': 'Сергій', 'score': 5},
    {'name': 'Вася', 'score': 3},
    {'name': 'Катя', 'score': 1},
    {'name': 'Марія', 'score': 5}
]

sorted_by_name = sorted(students, key=lambda x: x['name'])
print("Сортування за ім'ям:", sorted_by_name)

sorted_by_score = sorted(students, key=lambda x: x['score'], reverse=True)
print("Сортування за оцінкою:", sorted_by_score)
