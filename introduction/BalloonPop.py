# import
import random

import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from mediapipe.python.solutions import hands
import time

# initialization
pygame.init()

# create window/display
width, height = 1200, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball POP")

# CLOCK FPS
fps = 30
clock = pygame.time.Clock()

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Images
imgBackground = pygame.image.load('../Resourses/Project1-GUI/background.png').convert_alpha()
imgBackground = pygame.transform.scale(imgBackground, (1000, 700))
imgBalloon = pygame.image.load('../Resourses/ball.png').convert_alpha()
imgBalloon = pygame.transform.scale(imgBalloon, (100, 100))
rectBalloon = imgBalloon.get_rect()
rectBalloon.x, rectBalloon.y = 500, 200

# Variabes
speed = 5
score = 0
startTime = time.time()
totalTime = 30

# Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)


def resetBalloon():
    rectBalloon.x = random.randint(100, img.shape[1] - 100)
    rectBalloon.y = img.shape[0] + 50


# Main Loop
start = True
while start:
    # get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            statr = False
            pygame.quit()

    # LOGIC

    TimeRemain = int(totalTime-(time.time()-startTime))
    if TimeRemain < 0:
        window.fill((255,245,238))
        window.blit(imgBackground, (0, 0))


        font = pygame.font.SysFont('newyork', 80)
        textScore = font.render(f' Your Score:{score}', True, (139,69,19))
        textTime = font.render(f'Time UP', True, (139,69,19))
        window.blit(textScore, (450, 350))
        window.blit(textTime, (520, 450))

    else:
        # OPENCV

        success, img = cap.read()
        hands, detector.findHands(img)
        hands, img = detector.findHands(img, flipType=True)

        rectBalloon.y -= speed

        if rectBalloon.y < 0:
            resetBalloon()
            speed += 1

        if hands:
            hand = hands[0]
            x, y, *z = hand['lmList'][8]
            if rectBalloon.collidepoint(x, y):
                resetBalloon()
                score += 10
                speed += 1

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))
        window.blit(imgBalloon, (rectBalloon))

        font = pygame.font.SysFont('newyork', 50)
        textScore = font.render(f'Score:{score}', True, (119,136,153))
        textTime = font.render(f'Time:{TimeRemain}', True, (119,136,153))
        window.blit(textScore, (35, 35))
        window.blit(textTime, (1000, 35))

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
