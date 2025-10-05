import pygame
def move_player(player,keys):#Permite mover el sol
    if keys[pygame.K_d]:#Input de tecka
        player.x+=3#Cambio de la coordenada
    if keys[pygame.K_a]:
        player.x-=3
    if keys[pygame.K_s]:
        player.y+=3
    if keys[pygame.K_w]:
        player.y-=3
    return player