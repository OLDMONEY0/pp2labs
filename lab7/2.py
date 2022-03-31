import pygame

pygame.init()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

_songs = ['music.mp3', 'music2.mp3']
H, M =768, 768
White = (255,255,255)

screen = pygame.display.set_mode((H, M))
pygame.display.set_caption('Spotify')
flpause = False
ord_music = 0
image = pygame.image.load('music.png')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flpause = not flpause
                if flpause:pygame.mixer.music.pause()
                else:pygame.mixer.music.unpause()
            if event.key == pygame.K_DOWN:
                pygame.mixer.music.stop()
            if event.key == pygame.K_RIGHT:
                if ord_music == len(_songs)-1:
                    ord_music = 0
                    pygame.mixer.music.load(_songs[ord_music])
                    pygame.mixer.music.play(-1)
                else:
                    ord_music +=1
                    pygame.mixer.music.load(_songs[ord_music])
                    pygame.mixer.music.play(-1)
            if event.key == pygame.K_LEFT:
                if ord_music == 0:
                    ord_music = len(_songs)
                    pygame.mixer.music.load(_songs[ord_music - 1])
                    pygame.mixer.music.play(-1)
                else:
                    ord_music -= 1
                    pygame.mixer.music.load(_songs[ord_music])
                    pygame.mixer.music.play(-1)
    screen.fill(White)
    screen.blit(image, (0,0))
    pygame.display.flip()




            

