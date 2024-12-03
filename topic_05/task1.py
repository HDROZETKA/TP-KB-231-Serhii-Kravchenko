import random

options = ["камінь", "ножиці", "папір"]

user_choice = input("Ваш хід (камінь, ножиці, папір): ").strip().lower()

if user_choice not in options:
    print("Такого варіанту немає! Я пропонував камінь, ножиці, папір.")
else:
    print()
    computer_choice = random.choice(options)
    print(f"Мій хід: {computer_choice}")

    if user_choice == computer_choice:
        print("Це нічия! Перемогла дружба людини з комп'ютером!")
    elif (user_choice == "камінь" and computer_choice == "ножиці") or \
            (user_choice == "ножиці" and computer_choice == "папір") or \
            (user_choice == "папір" and computer_choice == "камінь"):
        print("Ти переміг! Удача на твоєму боці.")
    else:
        print("Я переміг! Повстання машин незабаром!")
