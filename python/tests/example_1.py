import pygame
import sys

# Инициализация всех модулей pygame
pygame.init()

# ============ НАСТРОЙКИ ОКНА ============
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Смена цвета квадрата кнопками")

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

# Названия цветов — идут в том же порядке, что и COLORS!
# Если добавишь новый цвет в COLORS — не забудь добавить и сюда.
COLOR_NAMES = ["Красный", "Зелёный", "Синий", "Жёлтый", "Белый", "Оранжевый"]

# Индекс текущего цвета в массиве COLORS
# Начинаем с 0 — то есть с красного
current_color_index = 0

# ============ ЦВЕТА ИНТЕРФЕЙСА ============
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)       # Обычное состояние кнопки
DARK_GRAY = (120, 120, 120)  # При наведении курсора
BG_COLOR = (200, 200, 200)   # Серый фон окна, чтобы белый квадрат был заметен

# ============ ШРИФТ ============
font = pygame.font.SysFont("Arial", 24)


# ============ КЛАСС КНОПКИ ============
class Button:
    """Класс, описывающий кнопку."""

    def __init__(self, x, y, width, height, text):
        # Прямоугольник кнопки (позиция и размеры)
        self.rect = pygame.Rect(x, y, width, height)
        # Текст на кнопке
        self.text = text

    def draw(self, surface):
        """Отрисовка кнопки на экране."""
        # Проверяем, находится ли курсор над кнопкой
        mouse_pos = pygame.mouse.get_pos()
        # Если курсор над кнопкой — делаем её темнее (эффект наведения)
        color = DARK_GRAY if self.rect.collidepoint(mouse_pos) else GRAY

        # Рисуем прямоугольник кнопки
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        # Рисуем рамку кнопки
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=8)

        # Рендерим текст
        text_surface = font.render(self.text, True, BLACK)
        # Центрируем текст внутри кнопки
        text_rect = text_surface.get_rect(center=self.rect.center)
        # Рисуем текст
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        """Проверяет, была ли кнопка нажата левой кнопкой мыши."""
        # event.type == MOUSEBUTTONDOWN — событие нажатия кнопки мыши
        # event.button == 1 — именно левая кнопка
        # self.rect.collidepoint(event.pos) — курсор внутри кнопки
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


# ============ СОЗДАНИЕ КНОПОК ============
# Кнопка "Назад" — слева, внизу окна
btn_back = Button(x=50, y=320, width=180, height=50, text="<- Назад")

# Кнопка "Вперёд" — справа, внизу окна
btn_next = Button(x=370, y=320, width=180, height=50, text="Вперёд ->")


# ============ ФУНКЦИИ ДЛЯ СМЕНЫ ЦВЕТА ============
def next_color():
    """Переключает цвет на следующий в массиве (с зацикливанием)."""
    global current_color_index
    # Оператор % (остаток от деления) позволяет зациклить индекс:
    # после последнего элемента снова попадём на 0
    current_color_index = (current_color_index + 1) % len(COLORS)


def prev_color():
    """Переключает цвет на предыдущий в массиве (с зацикливанием)."""
    global current_color_index
    # Прибавляем len(COLORS), чтобы избежать отрицательного числа,
    # затем берём остаток от деления
    current_color_index = (current_color_index - 1) % len(COLORS)


# ============ ГЛАВНЫЙ ЦИКЛ ============
running = True
while running:
    # --- Обработка событий ---
    for event in pygame.event.get():
        # Закрытие окна
        if event.type == pygame.QUIT:
            running = False

        # Проверяем нажатие на кнопку "Вперёд"
        if btn_next.is_clicked(event):
            next_color()

        # Проверяем нажатие на кнопку "Назад"
        if btn_back.is_clicked(event):
            prev_color()

    # --- Отрисовка ---

    # Заливаем фон серым цветом (чтобы белый квадрат был виден)
    screen.fill(BG_COLOR)

    # Рисуем квадрат текущим цветом
    # Размер квадрата — 100x100, позиция — по центру верхней части окна
    square_size = 100
    square_x = (WIDTH - square_size) // 2  # Центрируем по горизонтали
    square_y = 80
    pygame.draw.rect(
        screen,
        COLORS[current_color_index],  # Цвет берём из массива по индексу
        (square_x, square_y, square_size, square_size)
    )

    # Рисуем рамку вокруг квадрата (для наглядности, особенно для белого)
    pygame.draw.rect(
        screen,
        BLACK,
        (square_x, square_y, square_size, square_size),
        3
    )

    # Отрисовываем обе кнопки
    btn_back.draw(screen)
    btn_next.draw(screen)

    # Подпись под квадратом: название текущего цвета
    label = font.render(
        f"Текущий цвет: {COLOR_NAMES[current_color_index]}",
        True,
        BLACK
    )
    label_rect = label.get_rect(center=(WIDTH // 2, 220))
    screen.blit(label, label_rect)

    # Обновляем экран (показываем всё, что нарисовали)
    pygame.display.flip()

    # Ограничиваем FPS до 60 кадров в секунду
    clock.tick(FPS)

# ============ ЗАВЕРШЕНИЕ ============
pygame.quit()
sys.exit()