# Задача 2

import sys

import pygame
import requests

pygame.init()
screen = pygame.display.set_mode((1920, 1080))

coords = input().split()
zoom = input().split()
zoom = list(map(float, zoom))


def map_show():
    map_request = f"http://static-maps.yandex.ru/1.x/" \
                  f"?ll={float(coords[0])},{float(coords[1])}&spn={float(zoom[0])},{float(zoom[1])}&l=sat"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    map = pygame.image.load(map_file)
    map = pygame.transform.scale(map, (1920, 1080))
    screen.blit(map, (0, 0))
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_PAGEUP:
                if zoom[0] != 1 and zoom[1] != 1:
                    zoom[0] -= 1
                    zoom[1] -= 1
            if event.key == pygame.K_PAGEDOWN:
                if zoom[0] != 19 and zoom[1] != 19:
                    zoom[0] += 1
                    zoom[1] += 1

    map_show()
    pygame.display.update()