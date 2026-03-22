import random
import main


def ugadayka():
    x = random.randint(0,10)
    attempts = 3
    print("    --------------------\n\tУгадай число\n")
    while attempts != 0:
        y = int(input("Введите число от 1 до 10: "))
        if y != x:
            attempts -= 1
            print(f"\nНеверно, осталось {attempts} попыток\n")
        elif y == x:
            print("\nВы угадали!!!\n")
            break
        else:
            print("\nПопытки кончились.\n")

    while True:
        choice = int(input("Хотите сыграть еще или выйти в меню?\n\n"
        "1 - Да\n"
        "2 - Нет\n\n---?> "))
        if choice == 1:
            ugadayka()
            break
        elif choice == 2:
            main.main()
            break
        else:
           print("Неверный выбор\n")
           continue



