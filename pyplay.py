import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

pygame.display.set_caption('GAEM')

x, y, width, height, speed = 50, 50, 40, 60, 20

run = 1
while run:
    pygame.time.delay(100)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_UP]:
        y -= speed

    window.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(window, (0,0,255), (x,y,width,height))
    pygame.display.update()

pygame.quit()