#Это игра-аркада, пинг-понг на двоих

import pygame
import sys
from pygame.locals import *
import random

# Размеры экрана
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Инициализация Pygame
pygame.init()

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Arkanoid')

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)

y2 = SCREEN_HEIGHT-40

# Класс для платформы
class Paddle:
    def __init__(self, y, color):
        self.width = 100
        self.height = 10
        self.x = (SCREEN_WIDTH - self.width) // 2  #ставим по центру по коорд х
        self.y = y
        self.speed = 10  #скорость платформы
        self.color = color

    #ф-ция движения платформы + проверка, чтобы не заходила за пределы экрана
    def move(self, direction):
        if direction == 'left' and self.x > 0:
            self.x -= self.speed
        elif direction == 'right' and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))

# Класс для мяча
class Ball:
    def __init__(self):
        self.radius = 10    #радиус мяча
        self.reset()

    def reset(self):
        self.x = SCREEN_WIDTH // 2  #координаты по центру
        self.y = SCREEN_HEIGHT // 2 #координаты по центру
        self.speed_x = 5
        self.speed_y = random.randint(-5, 5)
        if self.speed_y == 0:
            self.speed_y = 3


    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Отражение от стен
        if self.x <= 0 or self.x >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        # if self.y <= 0 or self.y >= SCREEN_HEIGHT:
        # if self.y <=0:
        #     self.speed_y = -self.speed_y
        if self.y >= SCREEN_HEIGHT or self.y <= 0:
            self.reset()


    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)


# Класс для кирпичей
class Brick:
    def __init__(self, x, y):
        self.width = 60
        self.height = 20
        self.x = x
        self.y = y
        self.color = GREEN
        self.visible = True

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.color,
                             (self.x, self.y, self.width, self.height))



# Основная функция игры
def main():
    paddle1 = Paddle(40, (0, 0, 255))
    paddle2 = Paddle(y2, (255, 255, 255))
    ball = Ball()
    bricks = []

    # Создание кирпичей
    for i in range(3):
        for j in range(3):
            brick = Brick(j * 70 + 235, i * 30 + 255)
            bricks.append(brick)

    clock = pygame.time.Clock()

    # Переменные для хранения очков
    score_paddle1 = 0
    score_paddle2 = 0


    #Обработка событий
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #Считываются нажатия на левую и правую клавишу
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            paddle1.move('left')
        if keys[K_RIGHT]:
            paddle1.move('right')
        if keys[K_a]:
            paddle2.move('left')
        if keys[K_d]:
            paddle2.move('right')

        ball.move()

        # Проверка столкновения мяча с платформой
        # if (paddle1.y <= ball.y + ball.radius <= paddle1.y + paddle1.height
        #         and paddle1.x <= ball.x <= paddle1.x + paddle1.width):
        if (paddle1.y <= ball.y <= paddle1.y + paddle1.height
                and paddle1.x <= ball.x <= paddle1.x + paddle1.width):
            ball.speed_y = -ball.speed_y
            ball.speed_x = -ball.speed_x
            score_paddle1 += 1   # Увеличиваем очки paddle1

        if (paddle2.y <= ball.y + ball.radius <= paddle2.y + paddle2.height
                and paddle2.x <= ball.x <= paddle2.x + paddle2.width):
            ball.speed_y = -ball.speed_y
            ball.speed_x = -ball.speed_x
            score_paddle2 += 1  # Увеличиваем очки paddle2

        # if ball.x <= 0 or ball.x >= SCREEN_WIDTH:
        #     ball.speed_x *= -1
        # if ball.y <= 0 or ball.y >= SCREEN_HEIGHT:
        #     ball.reset()

        # Проверка столкновения мяча с кирпичами
        for brick in bricks:
            if brick.visible:
                if (brick.x < ball.x < brick.x + brick.width
                        and brick.y < ball.y < brick.y + brick.height):
                    ball.speed_y *= -1
                    brick.visible = False

        # # Проверка проигрыша
        # if ball.y > SCREEN_HEIGHT:
        #     print("Game Over")
        #     pygame.quit()
        #     sys.exit()

        #заливка экрана
        screen.fill(BLACK)
        #отрисовка объектов: платформа и мяч
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)
        # отрисовка объектов: кирпичи
        for brick in bricks:
            brick.draw(screen)

        # Отображение очков
        score_text = font.render(f'Синий: {score_paddle1}  Белый: {score_paddle2}', True, WHITE)
        screen.blit(score_text, (20, 20))


        #обновление экрана
        pygame.display.flip()

        #контроль ФПС (60 кадров в секунду), чтобы не было больше,
        # тк кол-во кадров влияет на скорость игры
        clock.tick(60)


if __name__ == '__main__':
    main()