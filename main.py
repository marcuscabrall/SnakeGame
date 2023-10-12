import pygame
import random
import time

pygame.init()

pygame.display.set_caption("Snake Game")
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_green = (0, 255, 0)

hit_box = 20
update_speed = 15

def generate_food():
    food_x = round(random.randrange(0, width - hit_box) / float(hit_box)) * float(hit_box)
    food_y = round(random.randrange(0, height - hit_box) / float(hit_box)) * float(hit_box)
    return food_x, food_y

def draw_food(size, food_x, food_y):
    pygame.draw.rect(screen, color_green, [food_x, food_y, size, size])

def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, color_white, [pixel[0], pixel[1], size, size])

def draw_score(score):
    font = pygame.font.SysFont("Helvetica", 30)
    text = font.render("Score: {}".format(score), True, color_red)
    screen.blit(text, [2, 2])

def end_of_game():
    font = pygame.font.SysFont("Helvetica", 60)
    text = font.render("GAME OVER!", True, color_red)
    text_width, text_height = text.get_width(), text.get_height()
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    screen.blit(text, (x, y))

def select_speed(keyboard_in):
    if keyboard_in == pygame.K_DOWN:
        speed_x = 0
        speed_y = hit_box
    elif keyboard_in == pygame.K_UP:
        speed_x = 0
        speed_y = -hit_box
    elif keyboard_in == pygame.K_RIGHT:
        speed_x = hit_box
        speed_y = 0
    elif keyboard_in == pygame.K_LEFT:
        speed_x = -hit_box
        speed_y = 0
    return speed_x, speed_y

def run_game():
    game_over = False

    x = width / 2
    y = height / 2

    speed_x = 0
    speed_y = 0

    size_snake = 1
    pixels = []

    food_x, food_y = generate_food()

    while not game_over:
        screen.fill(color_black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                end_of_game()

            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = select_speed(event.key)

        draw_food(hit_box, food_x, food_y)

        if x < 0 or x >= width or y < 0 or y >= height:
            game_over = True
            end_of_game()

        x += speed_x
        y += speed_y

        pixels.append([x, y])
        if len(pixels) > size_snake:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                game_over = True
                end_of_game()

        draw_snake(hit_box, pixels)

        draw_score(size_snake - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            size_snake += 1
            food_x, food_y = generate_food()

        clock.tick(update_speed)
    time.sleep(5)

run_game()