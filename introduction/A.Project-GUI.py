# import
import pygame

# initialization
pygame.init()

# create window/display
width, height = 1200, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("GUI")

# CLOCK FPS
fps = 30
clock = pygame.time.Clock()

# Images
imgBackground = pygame.image.load('../Resourses/Project1-GUI/background.png').convert_alpha()
imgBackground = pygame.transform.scale(imgBackground, (900, 900))
imgIcon1 = pygame.image.load('../Resourses/Project1-GUI/filter.png').convert_alpha()
imgIcon2 = pygame.image.load('../Resourses/Project1-GUI/black-and-white.png').convert_alpha()
imgIcon3 = pygame.image.load('../Resourses/Project1-GUI/color-palette.png').convert_alpha()
imgIcon4 = pygame.image.load('../Resourses/Project1-GUI/original.png').convert_alpha()
imgIcon5 = pygame.image.load('../Resourses/Project1-GUI/pencil.png').convert_alpha()
imgShadow = pygame.image.load('../Resourses/Project1-GUI/line.png').convert_alpha()
imgSwitchOn = pygame.image.load('../Resourses/Project1-GUI/switch-on.png').convert_alpha()
imgSwitchOff = pygame.image.load('../Resourses/Project1-GUI/switch-off.png').convert_alpha()


def drawWindowPad():
    pass


def drawAll():
    pass

# Main Loop
start = True
while start:
    #get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            statr = False
            pygame.quit()

    # LOGIC
    imgBackground.set_alpha(5)
    window.blit(imgBackground, (200, 0))

    # Update Display
    pygame.display.update()

    #Set FPS
    clock.tick(fps)

