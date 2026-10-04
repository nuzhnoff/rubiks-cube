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

