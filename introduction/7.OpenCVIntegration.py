# import
import pygame
import cv2
import numpy as np


# initialization
pygame.init()

# create window/display
width, height = 1200, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

# CLOCK FPS
fps = 30
clock = pygame.time.Clock()

#Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)


# Main Loop
start = True
while start:
    #get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            statr = False
            pygame.quit()

    # LOGIC

    # OPENCV
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    frame = pygame.transform.flip(frame, True, False)
    window.blit(frame, (0, 0))

    # Update Display
    pygame.display.update()

    #Set FPS
    clock.tick(fps)

