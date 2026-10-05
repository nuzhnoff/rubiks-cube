import pygame
class Cube:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.front = [1]*9
        self.up    = [2]*9
        self.down  = [3]*9
        self.top   = [4]*9
        self.left  = [5]*9
        self.right = [6]*9
#Создаем массив цветов для вывода на экран согласно растановки(показывается всегда только фронт)    
    def createFrontArrCurent(self):
        color_map = {
            1: (255, 0, 0),
            2: (0, 255, 0),
            3: (0, 0, 255),
            4: (255, 255, 0),
            5: (255, 165, 0),
            6: (255, 255, 255),
        }
        return [color_map[value] for value in self.front]
                    
   
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
#============== КЛАСС КУБИКА РУБИКА=========================
class CubeRender:
    def __init__(self, width_ONEelement, height_ONEelement, width_SCREEN, height_SCREEN):
        self.rect0 = pygame.Rect(width_SCREEN*0.25, height_SCREEN*0.15, width_ONEelement, height_ONEelement)
        self.rect1 = pygame.Rect(width_SCREEN*0.43, height_SCREEN*0.15, width_ONEelement, height_ONEelement)
        self.rect2 = pygame.Rect(width_SCREEN*0.61, height_SCREEN*0.15, width_ONEelement, height_ONEelement)
        self.rect3 = pygame.Rect(width_SCREEN*0.25, height_SCREEN*0.42, width_ONEelement, height_ONEelement)
        self.rect4 = pygame.Rect(width_SCREEN*0.43, height_SCREEN*0.42, width_ONEelement, height_ONEelement)
        self.rect5 = pygame.Rect(width_SCREEN*0.61, height_SCREEN*0.42, width_ONEelement, height_ONEelement)
        self.rect6 = pygame.Rect(width_SCREEN*0.25, height_SCREEN*0.69, width_ONEelement, height_ONEelement)
        self.rect7 = pygame.Rect(width_SCREEN*0.43, height_SCREEN*0.69, width_ONEelement, height_ONEelement)
        self.rect8 = pygame.Rect(width_SCREEN*0.61, height_SCREEN*0.69, width_ONEelement, height_ONEelement)
    def draw(self, surface, arrColor):
        pygame.draw.rect(surface, arrColor[0], self.rect0, border_radius = 3)
        pygame.draw.rect(surface, arrColor[1], self.rect1, border_radius = 3)
        pygame.draw.rect(surface, arrColor[2], self.rect2, border_radius = 3)
        pygame.draw.rect(surface, arrColor[3], self.rect3, border_radius = 3)
        pygame.draw.rect(surface, arrColor[4], self.rect4, border_radius = 3)
        pygame.draw.rect(surface, arrColor[5], self.rect5, border_radius = 3)
        pygame.draw.rect(surface, arrColor[5], self.rect6, border_radius = 3)
        pygame.draw.rect(surface, arrColor[5], self.rect7, border_radius = 3)
        pygame.draw.rect(surface, arrColor[5], self.rect8, border_radius = 3)
    
    
    
