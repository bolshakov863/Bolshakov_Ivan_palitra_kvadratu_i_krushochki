def draw_palette():
    palette.fill(background_color)
    for i in range(12):
        color_rect = pygame.Rect(i * sizes, 0, sizes, sizes)
        pygame.draw.rect(palette, COLORS[i], color_rect)
    border_rect = pygame.Rect(CUR_INDEX * sizes, 0, sizes, sizes)
    pygame.draw.rect(palette, BORDER_COLOR, border_rect, width=3)
    screen.blit(palette, palette_rect.topleft)

import pygame
pygame.init()
from all_colors import *
from random import choice

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
background_color = (255, 255, 255)
brush_color = (0, 0, 0)
brush_width = 5


BORDER_COLOR = (0, 0, 0)
CUR_INDEX = 0

canvas = pygame.Surface(screen.get_size())
canvas.fill(background_color)

RECTANGLE_COLOR = (255, 0, 0)
top_left = 0,0
size = 0,0
dragging = False
rectangles = []


sizes = 50
palette_rect = pygame.Rect(10, 10, sizes * 12, sizes)
palette = pygame.Surface(palette_rect.size)
dragging_palette = False

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if palette_rect.collidepoint(event.pos):
                print('потащили')
                dragging_palette = True
                offset = (event.pos[0] - palette_rect.left,
                          event.pos[1] - palette_rect.top)
            else:
                print('не тащим')
                dragging_palette = False

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            print('не тащим')
            dragging_palette = False

    if dragging_palette:
        new_pos = (mouse_pos[0] - offset[0],
                    mouse_pos[1] - offset[1])
        palette_rect.topleft = new_pos

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed[0]:
        print(mouse_pos)
        if palette_rect.collidepoint(mouse_pos):
            selected_color_index = ((mouse_pos[0] - palette_rect.left) // sizes)
            CUR_INDEX = selected_color_index
            brush_color = COLORS[CUR_INDEX]
        else:
            pygame.draw.circle(canvas, brush_color, mouse_pos, brush_width)

    elif event.type == pygame.MOUSEBUTTONDOWN:
        top_left = event.pos
        size = 0,0
        dragging = True

    elif event.type == pygame.MOUSEMOTION and dragging:
        right_bottom = event.pos
        size = (right_bottom[0] - top_left[0],
                right_bottom[1] - top_left[1])

    elif event.type == pygame.MOUSEBUTTONUP:
        right_bottom = event.pos
        size = (right_bottom[0] - top_left[0],
                 right_bottom[1] - top_left[1])
        dragging = False
        rect = pygame.Rect(top_left, size)
        color = choice(COLORS)
        rectangles.append((rect, color))

#        elif event.type == pygame.K_SPACE:
#            pygame.rect(screen, RECTANGLE_COLOR, (top_left, size))

    screen.blit(canvas, (0, 0))
    draw_palette()
    screen.fill(background_color)
    pygame.draw.rect(screen, RECTANGLE_COLOR, (top_left, size), 1)
    for rectangle, color in rectangles:
        pygame.draw.rect(screen, color, rectangle, 1)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()