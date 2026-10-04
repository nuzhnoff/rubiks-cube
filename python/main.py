from rubiks.rubiks import Cube, Button

import pygame
import sys

# Инициализация всех модулей pygame
pygame.init()
# ============ НАСТРОЙКИ ОКНА ============
WIDTH, HEIGHT = 600, 400
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



# def main() -> None:
    # cube = Cube() #reset
    # print(cube.front)
   
# ============ ГЛАВНЫЙ ЦИКЛ ============
running = True
while running:
    # --- Обработка событий ---
    for event in pygame.event.get():
        # Закрытие окна
        if event.type == pygame.QUIT:
            running = False

        # # Проверяем нажатие на кнопку "Вперёд"
        # if btn_next.is_clicked(event):
            # next_color()

        # # Проверяем нажатие на кнопку "Назад"
        # if btn_back.is_clicked(event):
            # prev_color()

    # --- Отрисовка ---

    # Заливаем фон серым цветом (чтобы белый квадрат был виден)
    screen.fill(BG_COLOR)

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

    # # Отрисовываем обе кнопки
    # btn_back.draw(screen)
    # btn_next.draw(screen)

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