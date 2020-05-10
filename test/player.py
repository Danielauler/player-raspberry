import pygame
file = 'test.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # Here we exit the Loop and execute what after.
pygame.quit()