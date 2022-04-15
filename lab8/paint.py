import pygame


WIDTH, HEIGHT = 1200, 800   # базовый размер окна
FPS = 60
draw = False                # нажатие, зажатие - рисуем, отжали - не рисуем 
lastPos = (0, 0)            # базовая позиция 
radius = 8            # базовый радиус для инструментов
color = 'blue'              # базовый цвет
mode = 'pen'                # базовый режим

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()
screen.fill(pygame.Color('white')) # закрашиваем в белый цвет, чтобы внутри цикла не обновлялось
fontRadius = pygame.font.SysFont('Arial', 66, bold=True)


def drawLine(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)


def drawCircle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)


def drawRectangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    widthr = abs(x1 - x2)
    height = abs(y1 - y2)
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)
    


def drawSquare(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    mn = min(abs(x2 - x1), abs(y2 - y1))


    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn))
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn))
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn))
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn))

def drawRightTriangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    if x2 > x1 and y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
    if y2 > y1 and x1 > x2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
    if x1 > x2 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)))
    if x2 > x1 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)))


def drawEquilateralTriangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    width_b = abs(x2 - x1)
    height = (3**0.5) * width_b / 2

    if y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width)
    else:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)))
    

def drawRhombus(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width)


while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        # Нажатия на клавиатуру
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rectangle'
            if event.key == pygame.K_c:
                mode = 'circle'
            if event.key == pygame.K_p:
                mode = 'pen'
            if event.key == pygame.K_e:
                mode = 'erase'
            if event.key == pygame.K_s:
                mode = 'square'
            if event.key == pygame.K_q:
                screen.fill(pygame.Color('white'))
            if event.key == pygame.K_y:
                color = 'yellow'
            if event.key == pygame.K_b:
                color = 'black'
            if event.key == pygame.K_g:
                color = 'gay'
            if event.key == pygame.K_t:
                mode = 'right_tri'
            if event.key == pygame.K_u:
                mode = 'eq_tri'
            if event.key == pygame.K_h:
                mode = 'rhombus'
            if event.key == pygame.K_UP:
                radius = min(200, radius + 1)   # ограничение по максимальному размеру радиуса
            if event.key == pygame.K_DOWN:
                radius = max(1, radius - 1)     # ограничение по минимальному размеру радиуса

        # Нажатие на мышку
        if event.type == pygame.MOUSEBUTTONDOWN: 
            draw = True
            if mode == 'pen':
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)
            prevPos = event.pos

        # Отпускание мышки
        if event.type == pygame.MOUSEBUTTONUP: 
            if mode == 'rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'circle':
                drawCircle(screen, prevPos, event.pos, radius, color)
            elif mode == 'square':
                drawSquare(screen, prevPos, event.pos, radius, color)
            elif mode == 'right_tri':
                drawRightTriangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'eq_tri':
                drawEquilateralTriangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'rhombus':
                drawRhombus(screen, prevPos, event.pos, radius, color)
            draw = False

        # Перемещение мышки
        if event.type == pygame.MOUSEMOTION: 
            if draw and mode == 'pen':
                drawLine(screen, lastPos, event.pos, radius, color)
            elif draw and mode == 'erase':
                drawLine(screen, lastPos, event.pos, radius, 'white')
            lastPos = event.pos

    # show radius & color
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))
    renderRadius = fontRadius.render(f'{radius}', True, pygame.Color(color))
    screen.blit(renderRadius, (5, 5))

    # display
    pygame.display.flip()
    clock.tick(FPS)
     