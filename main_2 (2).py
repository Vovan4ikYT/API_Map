import os
import sys

import pygame
import requests

coords = input().split()
zoom = input().split()

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

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
map = pygame.image.load(map_file)
map = pygame.transform.scale(map, (1920, 1080))

while True:
    screen.blit(map, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os.remove(map_file)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                os.remove(map_file)
                sys.exit()

    pygame.display.update()