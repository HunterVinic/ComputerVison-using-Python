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

    # Update Display
    pygame.display.update()

    #Set FPS
    clock.tick(fps)

