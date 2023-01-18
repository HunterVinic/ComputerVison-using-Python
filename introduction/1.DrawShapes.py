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
    red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
    pygame.draw.polygon(window, red, ((481, 100), (788, 100), (937, 357),
                                      (788, 614), (491, 614), (342, 357)))
    pygame.draw.circle(window, green, (640, 360), 200)
    pygame.draw.line(window, blue, (468, 392), (812, 392), 10)
    pygame.draw.rect(window, blue,(468, 307, 345, 70), border_radius= 50)
    


    # Update Display
    pygame.display.update()

    #Set FPS
    clock.tick(fps)

