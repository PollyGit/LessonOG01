import pygame
import time

#автоматически инициализирует все модули, доступные
# для работы. Без нее не будет работать.
pygame.init()

#Создание окна, в котором будем работать
#размеры окна в виде кортежа
window_size = (800, 600)
#устанавливаем окно с определенным размером
screen = pygame.display.set_mode(window_size)
#установка названия для окна
pygame.display.set_caption('Тестовая игра')

#картинка
image = pygame.image.load('OB05_python_pic1.png')
#Рамка для изображения, хитбокс
image_rect = image.get_rect()
#скорость передвижения картинки при нажатии на клавишу
speed = 5

#Добавляем 2й объект в игру
image2 = pygame.image.load('OB05_python_pic2.png')
image_rect2 = image2.get_rect()


#Самая главная часть - игровой цикл.
# Будет упроавляться одной переменной.
run = True
#Все события прогоняем через цикл
while run:
    for event in pygame.event.get():
        #что происхдит при нажатии на крестик
        if event.type == pygame.QUIT:
            run = False
        #что происходит при движении мышкой
        if event.type == pygame.MOUSEMOTION:
            #значения позиции мышки
            mouseX, mouseY = pygame.mouse.get_pos()
            #координатам рамки присваиваем координаты мышки
            #вычитаем 40 (тк 80 - размер изображения), чтобы мышь была посередине
            image_rect.x = mouseX - 40
            image_rect.y = mouseY - 40

    #Проверка: касается ли image и image2 друг друга
    if image_rect.colliderect(image_rect2):
        print('Произошло столкновение')
        #Задержка, чтобы сообщение выводилось 1 раз
        time.sleep(1)

    # #нажатие на клавишу, Перемещение с помощью клавиатуры
    # keys = pygame.key.get_pressed()
    # #условие,  что происходит при нажатии на разные клавиши
    # if keys[pygame.K_LEFT]: #нажатие на левую стрелку
    #     image_rect.x -= speed   #перемещение рамки влево на величину скорости
    # if keys[pygame.K_RIGHT]:  # нажатие на правую стрелку
    #     image_rect.x += speed  # перемещение рамки вправо на величину скорости
    # if keys[pygame.K_UP]: #нажатие настрелку вверх
    #     image_rect.y -= speed   #перемещение рамки вверх на величину скорости
    # if keys[pygame.K_DOWN]:  # нажатие настрелку вниз
    #     image_rect.y += speed  # перемещение рамки вниз на величину скорости

    #залить цветом окно
    screen.fill((0, 0, 0))
    #после заливки добавляем изображение. blit() - что именно будем отображать
    screen.blit(image, image_rect)
    screen.blit(image2, image_rect2)  #добавляем 2е изображение
    #обновление экрана
    pygame.display.flip()

pygame.quit()