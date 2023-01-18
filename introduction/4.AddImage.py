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
imgred = pygame.image.load("../Resourses/group.png").convert_alpha()


# Main Loop
start = True
while start:
    #get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            statr = False
            pygame.quit()

    # LOGIC
    window.fill((223, 190, 155))
    window.blit(imgBackground, (0, 0))
    window.blit(imgred, (200, 300))

    # Update Display
    pygame.display.update()

    #Set FPS
    clock.tick(fps)

