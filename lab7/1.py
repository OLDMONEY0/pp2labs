import pygame 
import datetime 
pygame.init() 
 
screen = pygame.display.set_mode((1400,1050))  
 
clock = pygame.time.Clock() 
running = True 
mainclock = pygame.image.load('mainclock.png') 
leftarm = pygame.image.load('leftarm.png') 
rightarm = pygame.image.load('rightarm.png') 
pygame.display.set_caption('Clock')
def rotate(image, rect, angle): 
    new_image = pygame.transform.rotate(image,-1*angle) 
    rect = new_image.get_rect(center=rect.center) 
    return new_image, rect
#second
image = pygame.Surface((63, 1050), pygame.SRCALPHA) 
image.blit(leftarm, (0, 0))   
orig_image = image 
rect = image.get_rect(center=(1400//2, 1050//2)) 
 
#minute 
imagem = pygame.Surface((1400, 1050), pygame.SRCALPHA) 
imagem.blit(rightarm, (0, 0)) 
orig_imagem = imagem 
rect1 = imagem.get_rect(center=(1400//2, 1050//2)) 
 
white = (255,255,255) 
while True: 
    clock.tick(30) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit() 
     
    current_time = datetime.datetime.now() 
    second = current_time.second 
    minute = current_time.minute 
    screen.blit(mainclock, (0, 0))  
    screen.blit(image, rect) 
    screen.blit(imagem, rect1) 
    image, rect = rotate(orig_image, rect, second*6) 
    imagem, rect1 = rotate(orig_imagem, rect1, minute*6)
      
     
    pygame.display.flip()