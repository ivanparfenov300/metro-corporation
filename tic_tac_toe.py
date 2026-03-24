import main
import random

def game():
    
    # Основная логика игры: 
    # Вывод поля ---> Рандом определяет кто крест и ноль --->
    # Выполнение хода игрока или рандома ---> Вывод поля на экран --->
    # Проверка поля на наличие линии из трех элементов

    # Функция, которое выводит игровое поле
    def print_field(field: list[str]):
        first_row    = ''
        second_row   = ''
        third_row    = ''
        fourth_row   = ''
        fifth_row    = ''
        for i in range(0, 5):
            first_row   += field[i]
            second_row  += field[i + 5]
            third_row   += field[i + 10]
            fourth_row  += field[i + 15]
            fifth_row   += field[i + 20]
        print(first_row)
        print(second_row)
        print(third_row)
        print(fourth_row)
        print(fifth_row)

    def check_field(field: list[str]) -> bool: # !!! В РАЗРАБОТКЕ !!!
        return False


    print("    -----------------------\n\tКрестики-нолики\n")
    char_x: str = 'x'
    char_o: str = 'o'

    first_player_to_move: int = random.randint(1, 2)

    active_field: list[int] = [0, 2, 4, 10, 12, 14, 20, 22, 24]
    field: list[str] = [' ', '|', ' ', '|', ' ', # Индексы активных полей: 0, 2, 4, 10, 12, 14, 20, 22, 24
                        '=', '+', '=', '+', '=',
                        ' ', '|', ' ', '|', ' ',
                        '=', '+', '=', '+', '=',
                        ' ', '|', ' ', '|', ' ',]

    # Определение у кого будет первый ход
    if first_player_to_move == 1:
        print("\nВы начинаете игру.")
    else:
        print("\nБот начинает игру")
    
    # Функция, которое выводит игровое поле
    print_field(field)

    # Начало игры !!! В РАЗРАБОТКЕ !!!
    for i in range(10):
        pass
    
    # После окончания игры
    while True:
        choice = int(input("\nХотите сыграть еще или выйти в меню?\n\n"
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