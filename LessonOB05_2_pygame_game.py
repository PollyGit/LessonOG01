#Это игра-аркада, пинг-понг на одного

import pygame
import sys
from pygame.locals import *

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

# Класс для платформы
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = (SCREEN_WIDTH - self.width) // 2  #ставим по центру по коорд х
        self.y = SCREEN_HEIGHT - 50 # по у смещаем на 50 выше чем нижняя точка
        self.speed = 10  #скорость платформы

    #ф-ция движения платформы + проверка, чтобы не заходила за пределы экрана
    def move(self, direction):
        if direction == 'left' and self.x > 0:
            self.x -= self.speed
        elif direction == 'right' and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE,
                         (self.x, self.y, self.width, self.height))

# Класс для мяча
class Ball:
    def __init__(self):
        self.radius = 10    #радиус мяча
        self.x = SCREEN_WIDTH // 2  #координаты по центру
        self.y = SCREEN_HEIGHT // 2 #координаты по центру
        self.speed_x = 5
        self.speed_y = -5

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Отражение от стен
        if self.x <= 0 or self.x >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.y <= 0:
            self.speed_y *= -1

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
    paddle = Paddle()
    ball = Ball()
    bricks = []

    # Создание кирпичей
    for i in range(5):
        for j in range(8):
            brick = Brick(j * 70 + 35, i * 30 + 35)
            bricks.append(brick)

    clock = pygame.time.Clock()

    #Обработка событий
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #Считываются нажатия на левую и правую клавишу
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            paddle.move('left')
        if keys[K_RIGHT]:
            paddle.move('right')

        ball.move()

        # Проверка столкновения мяча с платформой
        if (paddle.y < ball.y + ball.radius < paddle.y + paddle.height
                and paddle.x < ball.x < paddle.x + paddle.width):
            ball.speed_y *= -1

        # Проверка столкновения мяча с кирпичами
        for brick in bricks:
            if brick.visible:
                if (brick.x < ball.x < brick.x + brick.width
                        and brick.y < ball.y < brick.y + brick.height):
                    ball.speed_y *= -1
                    brick.visible = False

        # Проверка проигрыша
        if ball.y > SCREEN_HEIGHT:
            print("Game Over")
            pygame.quit()
            sys.exit()

        #заливка экрана
        screen.fill(BLACK)
        #отрисовка объектов: платформа и мяч
        paddle.draw(screen)
        ball.draw(screen)
        # отрисовка объектов: кирпичи
        for brick in bricks:
            brick.draw(screen)

        #обновление экрана
        pygame.display.update()
        #контроль ФПС (60 кадров в секунду), чтобы не было больше,
        # тк кол-во кадров влияет на скорость игры
        clock.tick(30)

# def ask_play_again():
#     while True:
#         choice = input("Хотите сыграть снова? (да/нет): ").strip().lower()
#         if choice == 'да':
#             return True
#         elif choice == 'нет':
#             print("Спасибо за игру! До свидания!")
#             return False
#         else:
#             print("Пожалуйста, введите 'да' или 'нет'.")




if __name__ == '__main__':
    main()