import pygame
import main
from random import randrange

def game():
    RES = 800
    SIZE = 50

    x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE) #обьявляем позиции змейки в случайном месте
    apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE) #обьявляем позиции яблока в случайном месте
    dirs = {'W': True, 'S': True, 'A': True, 'D': True}
    lenght = 1
    snake = [(x, y)]
    dx, dy = 0, 0 #направление змейки
    fps = 5 #скорость змейки
    score = 0 #счетчик очков
    game_over = False
    started = False  # Флаг начала движения
    show_choice = False  # Флаг показа выбора после проигрыша

    pygame.init() #инициализация компонентов
    sc = pygame.display.set_mode([RES, RES]) #созадем экран
    clock = pygame.time.Clock()
    font_score = pygame.font.SysFont('Arial', 26, bold=True)#шрифты для счета
    font_end = pygame.font.SysFont('Arial', 26, bold=True)#шрифты для game over
    font_choice = pygame.font.SysFont('Arial', 26, bold=True)

    while True:
        sc.fill(pygame.Color("black"))
        [(pygame.draw.rect(sc, pygame.Color("green"), (i, j, SIZE, SIZE))) for i, j in snake]#отрисовываем змейку на карте 
        pygame.draw.rect(sc, pygame.Color("red"), (*apple, SIZE, SIZE))#отрисовываем яблоко на карте 
        render_score = font_score.render(f"score {score}", 1, pygame.Color('orange'))#отображаем счет
        sc.blit(render_score, (10, 10))

        # Движение и логика игры только если игра не окончена
        if not game_over and started and not show_choice:
            # Вычисляем новую позицию
            new_x = x + dx * SIZE
            new_y = y + dy * SIZE

            # Проигрыш если выходим за границы
            if new_x < 0 or new_x >= RES or new_y < 0 or new_y >= RES:
                game_over = True
                show_choice = True
            else:
                x, y = new_x, new_y
                snake.append((x, y))

                # Проигрыш при столкновении с собой
                if len(snake) != len(set(snake)):
                    game_over = True
                    show_choice = True
                else:
                    #чтобы при запуске длина змейки была 1
                    snake = snake[-lenght:]
                        #когда съедаем яблоко
                    if snake[-1] == apple:
                        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
                        lenght += 1
                        score += 1
                        fps += 1

        # Отображение Game Over и выбора
        if game_over and show_choice:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (RES//2 - 200, RES//3))
            render_score_final = font_score.render(f"score {score}", 1, pygame.Color('orange'))
            sc.blit(render_score_final, (RES//2 - 200, RES//3 + 50))
            render_choice1 = font_choice.render("1 - Сыграть еще", 1, pygame.Color('orange'))
            sc.blit(render_choice1, (RES//2 - 200, RES//3 + 120))
            render_choice2 = font_choice.render("2 - Выйти в меню", 1, pygame.Color('orange'))
            sc.blit(render_choice2, (RES//2 - 200, RES//3 + 170))
        #обновляем экран
        pygame.display.flip()
        clock.tick(fps)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and show_choice:
                if event.key == pygame.K_1:
                    game()
                    return
                elif event.key == pygame.K_2:
                    pygame.quit()
                    main.main()
                    return
        #игровой контроллер
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and dirs['W'] and not game_over and not show_choice:
            dx, dy = 0, -1
            #чтобы при движении вперед мы не могли пойти назад и по аналогии с этим применимо к остальным движениям
            dirs = {'W': True, 'S': False, 'A': True, 'D': True}
            started = True
        if key[pygame.K_s] and dirs['S'] and not game_over and not show_choice:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True}
            started = True
        if key[pygame.K_a] and dirs['A'] and not game_over and not show_choice:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False}
            started = True
        if key[pygame.K_d] and dirs['D'] and not game_over and not show_choice:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True}
            started = True

