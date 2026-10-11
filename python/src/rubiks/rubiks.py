import pygame
pygame.init() 
# ============ ЦВЕТА ИНТЕРФЕЙСА ============
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)       # Обычное состояние кнопки
DARK_GRAY = (120, 120, 120)  # При наведении курсора
BG_COLOR = (200, 200, 200)   # Серый фон окна, чтобы белый квадрат был заметен

# ============ ШРИФТ ============
font = pygame.font.SysFont("Arial", 24)
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
            1: (255, 0, 0),# Красный
            2: (255, 255, 255),# Белый
            3: (255, 255, 0),     # Жёлтый
            4: (255, 165, 0),     # Оранжевый
            5: (0, 255, 0),       # Зелёный
            6: (0, 0, 255),       # Синий
         
        }
        return [color_map[value] for value in self.front]
    
    #Функция поворота U
    def runU_revers (self):
        tempArrUp = self.up.copy()
        tempArrFront = self.front.copy()
        tempArrLeft = self.left.copy()
        tempArrTop = self.top.copy()
        tempArrRight = self.right.copy()
        self.up[0] = tempArrUp[6]
        self.up[1] = tempArrUp[3]
        self.up[2] = tempArrUp[0]    
        self.up[3] = tempArrUp[7]
        self.up[4] = tempArrUp[4]
        self.up[5] = tempArrUp[1] 
        self.up[6] = tempArrUp[8]
        self.up[7] = tempArrUp[5]
        self.up[8] = tempArrUp[2] 
        self.left[0] = tempArrTop[0]
        self.left[1] = tempArrTop[1]
        self.left[2] = tempArrTop[2]
        self.top[0] = tempArrRight[0]
        self.top[1] = tempArrRight[1]
        self.top[2] = tempArrRight[2]
        self.right[0] = tempArrFront[0]
        self.right[1] = tempArrFront[1]
        self.right[2] = tempArrFront[2]
        self.front[0] = tempArrLeft[0]
        self.front[1] = tempArrLeft[1]
        self.front[2] = tempArrLeft[2]
    #Функция поворота U    
    def runU (self):
        tempArrUp = self.up.copy()
        tempArrFront = self.front.copy()
        tempArrLeft = self.left.copy()
        tempArrTop = self.top.copy()
        tempArrRight = self.right.copy()
        self.up[0] = tempArrUp[2]
        self.up[1] = tempArrUp[5]
        self.up[2] = tempArrUp[8]    
        self.up[3] = tempArrUp[1]
        self.up[4] = tempArrUp[4]
        self.up[5] = tempArrUp[7] 
        self.up[6] = tempArrUp[0]
        self.up[7] = tempArrUp[3]
        self.up[8] = tempArrUp[6] 
        self.right[0] = tempArrTop[0]
        self.right[1] = tempArrTop[1]
        self.right[2] = tempArrTop[2]
        self.top[0] = tempArrLeft[0]
        self.top[1] = tempArrLeft[1]
        self.top[2] = tempArrLeft[2]
        self.left[0] = tempArrFront[0]
        self.left[1] = tempArrFront[1]
        self.left[2] = tempArrFront[2]
        self.front[0] = tempArrRight[0]
        self.front[1] = tempArrRight[1]
        self.front[2] = tempArrRight[2]
 
    #Функция поворота D    
    def runD_revers (self):
        tempArrDown = self.down.copy()
        tempArrFront = self.front.copy()
        tempArrLeft = self.left.copy()
        tempArrTop = self.top.copy()
        tempArrRight = self.right.copy()
        self.down[0] = tempArrDown[2]
        self.down[1] = tempArrDown[5]
        self.down[2] = tempArrDown[8]    
        self.down[3] = tempArrDown[1]
        self.down[4] = tempArrDown[4]
        self.down[5] = tempArrDown[7] 
        self.down[6] = tempArrDown[0]
        self.down[7] = tempArrDown[3]
        self.down[8] = tempArrDown[6] 
        self.right[6] = tempArrFront[6]
        self.right[7] = tempArrFront[7]
        self.right[8] = tempArrFront[8]
        self.top[6] = tempArrLeft[6]
        self.top[7] = tempArrLeft[7]
        self.top[8] = tempArrLeft[8]
        self.left[6] = tempArrFront[6]
        self.left[7] = tempArrFront[7]
        self.left[8] = tempArrFront[8]
        self.front[6] = tempArrRight[6]
        self.front[7] = tempArrRight[7]
        self.front[8] = tempArrRight[8]
 #Функция поворота D'
    def runD (self):
        tempArrDown = self.down.copy()
        tempArrLeft = self.left.copy()
        tempArrFront = self.front.copy()
        tempArrTop = self.top.copy()
        tempArrRight = self.right.copy()
        self.down[0] = tempArrDown[6]
        self.down[1] = tempArrDown[3]
        self.down[2] = tempArrDown[0]    
        self.down[3] = tempArrDown[7]
        self.down[4] = tempArrDown[4]
        self.down[5] = tempArrDown[1] 
        self.down[6] = tempArrDown[8]
        self.down[7] = tempArrDown[5]
        self.down[8] = tempArrDown[2] 
        self.left[6] = tempArrFront[6]
        self.left[7] = tempArrFront[7]
        self.left[8] = tempArrFront[8]
        self.top[6] = tempArrLeft[6]
        self.top[7] = tempArrLeft[7]
        self.top[8] = tempArrLeft[8]
        self.right[6] = tempArrTop[6]
        self.right[7] = tempArrTop[7]
        self.right[8] = tempArrTop[8]
        self.front[6] = tempArrRight[6]
        self.front[7] = tempArrRight[7]
        self.front[8] = tempArrRight[8]
    def runF (self):
        tempArrUp = self.up.copy()
        tempArrFront = self.front.copy()
        tempArrLeft = self.left.copy()
        #tempArrTop = self.top.copy()
        tempArrRight = self.right.copy()
        tempArrDown = self.down.copy()
        self.front[0] = tempArrFront[6]
        self.front[1] = tempArrFront[3]
        self.front[2] = tempArrFront[0]    
        self.front[3] = tempArrFront[7]
        self.front[4] = tempArrFront[4]
        self.front[5] = tempArrFront[1] 
        self.front[6] = tempArrFront[8]
        self.front[7] = tempArrFront[5]
        self.front[8] = tempArrFront[2] 
        self.up[6] = tempArrLeft[8]
        self.up[7] = tempArrLeft[5]
        self.up[8] = tempArrLeft[2]
        self.right[0] = tempArrUp[6]
        self.right[3] = tempArrUp[7]
        self.right[6] = tempArrUp[8]
        self.down[0] = tempArrRight[0]
        self.down[1] = tempArrRight[3]
        self.down[2] = tempArrRight[6]
        self.left[2] = tempArrDown[6]
        self.left[5] = tempArrDown[7]
        self.left[8] = tempArrDown[8] 
    def runL (self):
        tempArrUp = self.up.copy()
        tempArrFront = self.front.copy()
        tempArrLeft = self.left.copy()
        tempArrTop = self.top.copy()
        tempArrRight = self.right.copy()
        tempArrDown = self.down.copy()
        self.left[0] = tempArrLeft[2]
        self.left[1] = tempArrLeft[5]
        self.left[2] = tempArrLeft[8]    
        self.left[3] = tempArrLeft[1]
        self.left[4] = tempArrLeft[4]
        self.left[5] = tempArrLeft[7] 
        self.left[6] = tempArrLeft[0]
        self.left[7] = tempArrLeft[3]
        self.left[8] = tempArrLeft[6] 
        self.down[0] = tempArrFront[0]
        self.down[3] = tempArrFront[3]
        self.down[6] = tempArrFront[6]
        self.front[0] = tempArrUp[0]
        self.front[3] = tempArrUp[3]
        self.front[6] = tempArrUp[6]
        self.up[0] = tempArrTop[8]
        self.up[3] = tempArrTop[5]
        self.up[6] = tempArrTop[2]        
        self.top[0] = tempArrDown[0]
        self.top[3] = tempArrDown[3]
        self.top[6] = tempArrDown[6]
 
   
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
        self.rect3 = pygame.Rect(width_SCREEN*0.25, height_SCREEN*0.33, width_ONEelement, height_ONEelement)
        self.rect4 = pygame.Rect(width_SCREEN*0.43, height_SCREEN*0.33, width_ONEelement, height_ONEelement)
        self.rect5 = pygame.Rect(width_SCREEN*0.61, height_SCREEN*0.33, width_ONEelement, height_ONEelement)
        self.rect6 = pygame.Rect(width_SCREEN*0.25, height_SCREEN*0.51, width_ONEelement, height_ONEelement)
        self.rect7 = pygame.Rect(width_SCREEN*0.43, height_SCREEN*0.51, width_ONEelement, height_ONEelement)
        self.rect8 = pygame.Rect(width_SCREEN*0.61, height_SCREEN*0.51, width_ONEelement, height_ONEelement)
    def draw(self, surface, arrColor):
        pygame.draw.rect(surface, arrColor[0], self.rect0, border_radius = 3)
        pygame.draw.rect(surface, arrColor[1], self.rect1, border_radius = 3)
        pygame.draw.rect(surface, arrColor[2], self.rect2, border_radius = 3)
        pygame.draw.rect(surface, arrColor[3], self.rect3, border_radius = 3)
        pygame.draw.rect(surface, arrColor[4], self.rect4, border_radius = 3)
        pygame.draw.rect(surface, arrColor[5], self.rect5, border_radius = 3)
        pygame.draw.rect(surface, arrColor[6], self.rect6, border_radius = 3)
        pygame.draw.rect(surface, arrColor[7], self.rect7, border_radius = 3)
        pygame.draw.rect(surface, arrColor[8], self.rect8, border_radius = 3)
    
    
    
