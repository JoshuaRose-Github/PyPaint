# draw mouse trail

import pygame
import math

from pygame import gfxdraw

# WINDOW = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE) # STILL IN TESTING
WINDOW = pygame.display.set_mode((500,450))


running = 1

BLUE_TRAIL = []
RED_TRAIL = []
GREEN_TRAIL = []
YELLOW_TRAIL = []
MAGENTA_TRAIL = []
ORANGE_TRAIL = []

paint_mode = 1
index = paint_mode - 1
paint_color = (255, 255, 255)

X_DIM_IMAGE = pygame.image.load("x_hover.png")
X_DIM_IMAGE = pygame.transform.scale(X_DIM_IMAGE, (40, 40))

X_HOVER_IMAGE = pygame.image.load("x_dim.png")
X_HOVER_IMAGE = pygame.transform.scale(X_HOVER_IMAGE, (40, 40))

paint = True

pygame.display.set_caption("PyPaint Alpha Version 1.0")

while running:

    pygame.draw.rect(WINDOW, (50, 40, 40), (0, 0, 40, 450))
    pygame.draw.rect(WINDOW, (255, 0, 0), (0, 20, 40, 40))
    pygame.draw.rect(WINDOW, (0, 255, 0), (0, 70, 40, 40))
    pygame.draw.rect(WINDOW, (0, 100, 200), (0, 120, 40, 40))
    pygame.draw.rect(WINDOW, (255, 255, 0), (0, 170, 40, 40))
    pygame.draw.rect(WINDOW, (128, 0, 128), (0, 220, 40, 40))
    pygame.draw.rect(WINDOW, (255, 69, 0), (0, 270, 40, 40))
    WINDOW.blit(X_HOVER_IMAGE, (-2, 400))


    def draw_trail(color):
        for line in BLUE_TRAIL:
            pygame.draw.circle(WINDOW, color, (line[0], line[1]), paint_mode, index)
        for line in RED_TRAIL:
            pygame.draw.circle(WINDOW, color, (line[0], line[1]), paint_mode, index)
        for line in GREEN_TRAIL:
            pygame.draw.circle(WINDOW, color, (line[0], line[1]), paint_mode, index)


    def clearTrails():
        BLUE_TRAIL.clear()
        RED_TRAIL.clear()
        GREEN_TRAIL.clear()
        YELLOW_TRAIL.clear()
        MAGENTA_TRAIL.clear()
        ORANGE_TRAIL.clear()


    for event in pygame.event.get():
        key = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                paint_mode += 2
                print(paint_mode)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] in range(7, 29) and pygame.mouse.get_pos()[1] in range(400, 436):
                clearTrails()
                WINDOW.fill((0, 0, 0))
                pygame.draw.rect(WINDOW, (50, 40, 40), (0, 0, 40, 450))
                pygame.draw.rect(WINDOW, (255, 0, 0), (0, 20, 40, 40))
                pygame.draw.rect(WINDOW, (0, 255, 0), (0, 70, 40, 40))
                pygame.draw.rect(WINDOW, (0, 100, 200), (0, 120, 40, 40))
                pygame.draw.rect(WINDOW, (255, 255, 0), (0, 170, 40, 40))
                pygame.draw.rect(WINDOW, (128, 0, 128), (0, 220, 40, 40))
                pygame.draw.rect(WINDOW, (255, 69, 0), (0, 270, 40, 40))

            if pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(
                    0, 450):
                clearTrails()
                draw_trail((255, 0, 0))  # default
                print(paint_color)
                paint = False
            if pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(
                    20, 60):
                clearTrails()
                draw_trail((255, 0, 0))
                paint_color = (255, 0, 0)
                print(paint_color)
                paint = True

            elif pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(
                    70, 110):
                clearTrails()
                draw_trail((0, 255, 0))
                paint_color = (0, 255, 0)
                print(paint_color)
                paint = True

            elif pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(
                    120, 160):
                clearTrails()
                draw_trail((0, 100, 200))
                paint_color = (0, 100, 200)

            elif pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(
                    170, 210):
                clearTrails()
                draw_trail((255, 255, 0))
                paint_color = (255, 255, 0)

                print(paint_color)
                paint = True

            elif pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(
                    220, 270):
                clearTrails()
                draw_trail((128, 0, 128))
                paint_color = (128, 0, 128)

                print(paint_color)
                paint = True

            elif pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(170, 320):
                clearTrails()
                draw_trail((255, 69, 0))
                paint_color = (255, 69, 0)

                print(paint_color)
                paint = True

        elif event.type == pygame.MOUSEMOTION:

            print(pygame.mouse.get_pos())
            if pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(0, 450):
                paint = False

                if pygame.mouse.get_pos()[0] in range(7, 29) and pygame.mouse.get_pos()[1] in range(400, 436):
                    WINDOW.blit(X_DIM_IMAGE, (-2, 400))

                if pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(120, 160):
                    pygame.draw.rect(WINDOW, (255, 0, 0), (0, 20, 40, 40))
                    pygame.draw.rect(WINDOW, (0, 255, 0), (0, 70, 40, 40))
                    pygame.draw.rect(WINDOW, (0, 0, 255), (0, 120, 40, 40))

                elif pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(20, 60):
                    pygame.draw.rect(WINDOW, (100, 0, 0), (0, 20, 40, 40))
                    pygame.draw.rect(WINDOW, (0, 255, 0), (0, 70, 40, 40))
                    pygame.draw.rect(WINDOW, (0, 100, 200), (0, 120, 40, 40))

                elif pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(70, 110):
                    pygame.draw.rect(WINDOW, (255, 0, 0), (0, 20, 40, 40))
                    pygame.draw.rect(WINDOW, (0, 100, 0), (0, 70, 40, 40))
                    pygame.draw.rect(WINDOW, (0, 100, 200), (0, 120, 40, 40))

                elif pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(170, 210):
                    pygame.draw.rect(WINDOW, (255, 0, 0), (0, 20, 40, 40))
                    pygame.draw.rect(WINDOW, (0, 255, 0), (0, 70, 40, 40))
                    pygame.draw.rect(WINDOW, (0, 100, 200), (0, 120, 40, 40))
                    pygame.draw.rect(WINDOW, (150, 150, 0), (0, 170, 40, 40))
                elif pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(220, 261):
                    pygame.draw.rect(WINDOW, (255, 0, 0), (0, 20, 40, 40))
                    pygame.draw.rect(WINDOW, (0, 255, 0), (0, 70, 40, 40))
                    pygame.draw.rect(WINDOW, (0, 100, 200), (0, 120, 40, 40))
                    pygame.draw.rect(WINDOW, (255, 255, 0), (0, 170, 40, 40))
                    pygame.draw.rect(WINDOW, (80, 0, 80), (0, 220, 40, 40))
                elif pygame.mouse.get_pos()[0] in range(0, 40) and pygame.mouse.get_pos()[1] in range(270, 310):
                    pygame.draw.rect(WINDOW, (255, 0, 0), (0, 20, 40, 40))
                    pygame.draw.rect(WINDOW, (0, 255, 0), (0, 70, 40, 40))
                    pygame.draw.rect(WINDOW, (0, 100, 200), (0, 120, 40, 40))
                    pygame.draw.rect(WINDOW, (255, 255, 0), (0, 170, 40, 40))
                    pygame.draw.rect(WINDOW, (128, 0, 128), (0, 220, 40, 40))
                    pygame.draw.rect(WINDOW, (100, 40, 0), (0, 270, 40, 40))

            else:
                paint = True

            if paint:
                if pygame.mouse.get_pressed()[0]:
                    pi = math.pi
                    x, y = pygame.mouse.get_pos()

                    pygame.draw.circle(WINDOW, paint_color, (x, y), paint_mode, index)

                    pygame.display.update()

        pygame.display.update()
