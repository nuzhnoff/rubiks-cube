from rubiks.rubiks import Cube, Button, CubeRender

import pygame
import sys
import time

# Инициализация всех модулей pygame
pygame.init()
# ============ НАСТРОЙКИ ОКНА ============
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кубик Рубика")

# Часы для контроля FPS
clock = pygame.time.Clock()
FPS = 60
# ============ ЦВЕТА ============
# Массив цветов, по которому будем переключаться
COLORS = [
    (255, 0, 0),       # Красный
    (0, 255, 0),       # Зелёный
    (0, 0, 255),       # Синий
    (255, 255, 0),     # Жёлтый
    (255, 255, 255),   # Белый
    (255, 165, 0),     # Оранжевый
]
# ============ ЦВЕТА ИНТЕРФЕЙСА ============
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)       # Обычное состояние кнопки
DARK_GRAY = (120, 120, 120)  # При наведении курсора
BG_COLOR = (200, 200, 200)   # Серый фон окна, чтобы белый квадрат был заметен

# ============ ШРИФТ ============
font = pygame.font.SysFont("Arial", 24)



# ============ СОЗДАЕМ КУБИК ============
rubiksMain =  CubeRender(width_ONEelement = WIDTH*0.175, height_ONEelement = WIDTH*0.175, width_SCREEN = WIDTH, height_SCREEN = HEIGHT)
# ============ ПОДГОТАВЛИВАЕМ КУБИК В ИСХОДНОЕ СОСТОЯНИЕ ============
cube = Cube()
# ============ СОЗДАЕМ КНОПКУ U ============
btn_U_revers = Button(x=WIDTH*0.8, y=WIDTH*0.20, width=WIDTH*0.08, height=HEIGHT*0.08, text="U'")
# ============ СОЗДАЕМ КНОПКУ U' ============
btn_U = Button(x=WIDTH*0.15, y=WIDTH*0.20, width=WIDTH*0.08, height=HEIGHT*0.08, text="U")
# ============ СОЗДАЕМ КНОПКУ D' ============
btn_D_revers = Button(x=WIDTH*0.15, y=WIDTH*0.57, width=WIDTH*0.08, height=HEIGHT*0.08, text="D'")
# ============ СОЗДАЕМ КНОПКУ D ============
btn_D = Button(x=WIDTH*0.8, y=WIDTH*0.57, width=WIDTH*0.08, height=HEIGHT*0.08, text="D")
# ============ СОЗДАЕМ КНОПКУ F ============
btn_F = Button(x=WIDTH*0.8, y=WIDTH*0.45, width=WIDTH*0.08, height=HEIGHT*0.08, text="F")
# ============ СОЗДАЕМ КНОПКУ F ============
btn_L = Button(x=WIDTH*0.15, y=WIDTH*0.10, width=WIDTH*0.08, height=HEIGHT*0.08, text="L")
# ============ ГЛАВНЫЙ ЦИКЛ ============

running = True
while running:
    # --- Обработка событий ---
    for event in pygame.event.get():
        # Закрытие окна
        if event.type == pygame.QUIT:
            running = False

        # Проверяем нажатие на кнопку U'
        if btn_U_revers.is_clicked(event):
            cube.runU_revers()
        # Проверяем нажатие на кнопку U
        if btn_U.is_clicked(event):
            cube.runU()
        # Проверяем нажатие на кнопку D'
        if btn_D_revers.is_clicked(event):
            cube.runD_revers()
        # Проверяем нажатие на кнопку D
        if btn_D.is_clicked(event):
            cube.runD()
            # Проверяем нажатие на кнопку F
        if btn_F.is_clicked(event):
            cube.runF()
           # Проверяем нажатие на кнопку L
        if btn_L.is_clicked(event):
            cube.runL()
            
            
        # # Проверяем нажатие на кнопку "Назад"
        # if btn_back.is_clicked(event):
            # prev_color()
    COLORS_CURENT = cube.createFrontArrCurent()
    # --- Отрисовка ---

    # Заливаем фон серым цветом (чтобы белый квадрат был виден)
    screen.fill(BG_COLOR)
    rubiksMain.draw(screen, arrColor = COLORS_CURENT )
    #print(COLORS_CURENT)
    #time.sleep(1)

    # # Рисуем квадрат текущим цветом
    # # Размер квадрата — 100x100, позиция — по центру верхней части окна
    # square_size = 100
    # square_x = (WIDTH - square_size) // 2  # Центрируем по горизонтали
    # square_y = 80
    # pygame.draw.rect(
        # screen,
        # COLORS[current_color_index],  # Цвет берём из массива по индексу
        # (square_x, square_y, square_size, square_size)
    # )

    # # Рисуем рамку вокруг квадрата (для наглядности, особенно для белого)
    # pygame.draw.rect(
        # screen,
        # BLACK,
        # (square_x, square_y, square_size, square_size),
        # 3
    # )

    # Отрисовываем кнопки
    btn_U_revers.draw(screen)
    btn_U.draw(screen)
    btn_D_revers.draw(screen)
    btn_D.draw(screen)
    btn_F.draw(screen)
    btn_L.draw(screen)


    # # Подпись под квадратом: название текущего цвета
    # label = font.render(
        # f"Текущий цвет: {COLOR_NAMES[current_color_index]}",
        # True,
        # BLACK
    # )
    # label_rect = label.get_rect(center=(WIDTH // 2, 220))
    # screen.blit(label, label_rect)

    # Обновляем экран (показываем всё, что нарисовали)
    pygame.display.flip()

    # Ограничиваем FPS до 60 кадров в секунду
    clock.tick(FPS)

# ============ ЗАВЕРШЕНИЕ ============
pygame.quit()
sys.exit()




#if __name__ == "__main__":
#   main()