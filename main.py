import ugadayka


def main():
    print("""    -----------------\n\tМини-игры\n
Меню игр:\n
    1 - крестики нолики
    2 - угадай число
    3 - виселица
    4 - змейка\n
Для выхода из приложения - введите '0'\n""")
    choice = int(input("Выберите номер игры, в который хотите поиграть: "))
    match choice:
        case 0:
            print("\nВы вышли из приложения\n")
        case 1:
            pass # Крестики-нолики
        case 2:
            ugadayka.ugadayka()
        case 3:
            pass # Виселица
        case 4:
            pass # Змейка
        case _:
            print("Нет такой игры.")

if __name__ == "__main__":
    main()
