import pygame
import sys
import random


pygame.init()
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH = 800
HEIGHT = 800
direction = 1


win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.vel = 10
        self.bumper_surface = pygame.Surface((100, 10))
        self.bumper_surface.fill(self.color)
        self.bumper_rect = pygame.Rect(self.x, self.y, 100, 10)


class PlayerOne(Player):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)


class PlayerTwo(Player):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = random.randint(2, 10) * 0.95
        self.vel_y = random.randint(8, 10) * 0.95
        self.direction_x = 1
        self.direction_y = 1
        self.factor_x = 1
        self.factor_y = 1
        self.ball_surface = pygame.Surface((10, 10))
        self.ball_surface.fill(GREEN)
        self.ball_rect = pygame.Rect(self.x, self.y, 10, 10)

    def move_ball(self):
        self.y += self.vel_y * self.direction_y * self.factor_y
        self.x += self.vel_x * self.direction_x * self.factor_x
        if self.x < 0 or self.x + 10 >= 800:
            self.direction_x *= -1
        if self.y <= 10:
            if self.x + 10 >= bumper_1.x and self.x <= bumper_1.x + 100:
                self.direction_y *= -1

            else:
                print("Blue lost a point")
                self.x = 395
                self.y = 11
                bumper_1.x = 350
                bumper_2.x = 350
                pygame.time.delay(100)
        if self.y >= 780:
            if self.x + 10 >= bumper_2.x and self.x <= bumper_2.x + 100:
                self.direction_y *= -1
            else:
                print("Red lost a point")
                self.x = 395
                self.y = 779
                bumper_1.x = 350
                bumper_2.x = 350
                pygame.time.delay(100)


def draw():
    win.fill(BLACK)
    win.blit(bumper_2.bumper_surface, (bumper_2.x, bumper_2.y))
    win.blit(bumper_1.bumper_surface, (bumper_1.x, bumper_1.y))
    win.blit(bol.ball_surface, (bol.x, bol.y))
    pygame.display.update()


bumper_2 = PlayerTwo(350, 790, RED)
bumper_1 = PlayerOne(350, 0, BLUE)
bol = Ball(395, 10)


def main():

    run = True
    while run:
        clock.tick(60)
        bol.move_ball()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.key.set_repeat(1, 10)
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if key[pygame.K_z] and bumper_1.x > 0:
                    bumper_1.x -= bumper_1.vel
                if key[pygame.K_x] and bumper_1.x < 700:
                    bumper_1.x += bumper_1.vel
                if key[pygame.K_KP1] and bumper_2.x > 0:
                    bumper_2.x -= bumper_2.vel
                if key[pygame.K_KP2] and bumper_2.x < 700:
                    bumper_2.x += bumper_2.vel
        draw()


main()

pygame.quit()
