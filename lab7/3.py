import pygame 
pygame.init()
clock = pygame.time.Clock()

H, M = 850, 450

screen = pygame.display.set_mode((H, M))
pygame.display.set_caption('circle move')
running = True

WHITE = (255, 255, 255)
RED = (255, 0, 0)

x = H//2
y = M//2
radius = 25
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - radius > 0:
        y-=radius
    if keys[pygame.K_DOWN] and y + radius < M:
        y += radius
    if keys[pygame.K_RIGHT] and x + radius < H:
        x += radius
    if keys[pygame.K_LEFT] and x - radius > 0:
        x -= radius
            

    screen.fill(0)
    pygame.draw.circle(screen, RED , (x, y), radius )
    pygame.display.flip() 

    clock.tick(60)


