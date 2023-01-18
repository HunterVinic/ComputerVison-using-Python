# import
import pygame

# initialization
pygame.init()

# create window/display
width, height = 1200, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

# CLOCK FPS
fps = 30
clock = pygame.time.Clock()

# load images
imgBackground = pygame.image.load("../Resourses/bb.png").convert_alpha()
imgBackground = pygame.transform.scale(imgBackground, (200, 300))
imgred = pygame.image.load("../Resourses/group.png").convert_alpha()
rectBalloon = imgBackground.get_rect()

# RECT
rectNew = pygame.Rect(500, 0, 200, 200)

# imgerd = pygame.transform.scale(imgred, (1, 1))
# imgred = pygame.transform.rotate(imgred, 90)
# imgBackground = pygame.transform.flip(imgBackground, True, False)


# Main Loop
start = True
while start:
    # get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            statr = False
            pygame.quit()

    # LOGIC
    imgred = pygame.transform.smoothscale(imgred, (100, 100))

    rectBalloon.colliderect(rectNew)
    rectBalloon.x += 5

    window.fill((223, 190, 155))
    window.blit(imgred, (200, 200))
    imgred = pygame.transform.rotate(imgred, 90)
    pygame.draw.rect(window, (0, 255, 0), rectBalloon)
    pygame.draw.rect(window, (0, 255, 0), rectNew)
    window.blit(imgBackground, rectBalloon)

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
