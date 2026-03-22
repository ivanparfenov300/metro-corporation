import main

def game():
    while True:
        choice = int(input("Хотите сыграть еще или выйти в меню?\n\n"
        "1 - Да\n"
        "2 - Нет\n\n---?> "))
        if choice == 1:
            game()
            break
        elif choice == 2:
            main.main()
            break
        else:
            print("Неверный выбор\n")
            continue