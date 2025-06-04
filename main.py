import pygame
import random
import sys
import os

# Инициализация Pygame
try:
    pygame.init()
except pygame.error as e:
    print(f"Ошибка инициализации Pygame: {e}")
    sys.exit()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
try:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Игра Тир")
except pygame.error as e:
    print(f"Ошибка создания окна: {e}")
    sys.exit()

# Проверка папки с изображениями
if not os.path.exists("img"):
    print("Папка 'img' не найдена! Создайте папку и добавьте изображения.")
    sys.exit()


# Функция загрузки изображения с созданием заглушки при ошибке
def load_image(name, size=None):
    try:
        img = pygame.image.load(f"img/{name}")
        if size:
            img = pygame.transform.scale(img, size)
        return img.convert_alpha()
    except:
        print(f"Изображение img/{name} не найдено, создана заглушка")
        surf = pygame.Surface((80, 80), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, 0, 0), (40, 40), 40)
        pygame.draw.circle(surf, (255, 255, 255), (40, 40), 30)
        pygame.draw.circle(surf, (255, 0, 0), (40, 40), 20)
        return surf


# Загрузка ресурсов
icon = load_image("icon.jpg")
target_img = load_image("target.png", (80, 80))
pygame.display.set_icon(icon)

# Игровые параметры
target_x = random.randint(0, SCREEN_WIDTH - 80)
target_y = random.randint(0, SCREEN_HEIGHT - 80)
target_speed_x = random.choice([-3, -2, 2, 3])
target_speed_y = random.choice([-3, -2, 2, 3])

score = 0
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 32)

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка попадания
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (target_x <= mouse_x <= target_x + 80 and
                    target_y <= mouse_y <= target_y + 80):
                score += 1
                # Новая позиция и цвет
                target_x = random.randint(0, SCREEN_WIDTH - 80)
                target_y = random.randint(0, SCREEN_HEIGHT - 80)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                # Новая скорость
                target_speed_x = random.choice([-3, -2, 2, 3])
                target_speed_y = random.choice([-3, -2, 2, 3])

    # Движение мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Отскок от границ
    if target_x <= 0 or target_x >= SCREEN_WIDTH - 80:
        target_speed_x *= -1
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - 80:
        target_speed_y *= -1

    # Отрисовка
    screen.fill(color)
    screen.blit(target_img, (target_x, target_y))

    # Отображение счета
    score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()