import random
import main
words = [
    "воздух", "огонь", "вода", "земля", "лес", "гора", "река", "море", "поле", "небо",
    "ветер", "дождь", "снег", "град", "туча", "солнце", "луна", "звезда", "радуга", "облако"
]

def game():
    player_count = 0
    comp_count = 0
    word = random.choice(words)
    print("=" * 50)
    print(" " * 18 + "ВИСЕЛИЦА")
    print("=" * 50)
    print("\n Вам нужно угадать слово, вводя буквы \n")
    print(f" Слово состоит из {len(word)} букв\n")
    while(player_count < len(word) or comp_count < len(word)):
        symbol = input("Введите букву!\n")
        if symbol in word:
            print("буква есть в слове!\n")
            player_count += 1
        else:
            print("буквы нет в слове!\n")
            comp_count += 1

        if player_count == len(word):
            print("Вы победили!")
            break
        elif comp_count == len(word):
            print("Вы проиграли!")
            break

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
