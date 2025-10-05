import pygame
from sys import *
def locate(number,relative_angle):
    number+=1
    if number==60 :
        number=0
    mouse_pos = pygame.mouse.get_pos()
    mouse_x=mouse_pos[0]
    mouse_y=mouse_pos[1]
    text_surface=test_font.render(str(number),False,"White")
    text_surface2=test_font.render("mouse x:"+str(mouse_x),False,"White")
    text_surface3=test_font.render("mouse y:"+str(mouse_y),False,"White")
    player_x=player.x
    player_y=player.y

    relative_mouse_x=mouse_x-player_x
    relative_mouse_y=mouse_y-player_y

    if relative_mouse_x==0:
        relative_angle=0
    else:
        if relative_mouse_x>0 and relative_mouse_y>0:
            relative_angle=math.atan(abs(relative_mouse_y)/abs(relative_mouse_x))
        elif relative_mouse_x<0 and relative_mouse_y>0:
            relative_angle=math.atan(relative_mouse_y/relative_mouse_x)+3.14159265
        elif relative_mouse_x<0 and relative_mouse_y<0:
            relative_angle=math.atan(relative_mouse_y/relative_mouse_x)+3.14159265
        elif relative_mouse_x>0 and relative_mouse_y<0:
            relative_angle=math.atan(relative_mouse_y/relative_mouse_x)+6.28318531
    text_surface5=test_font.render("player x:"+str(player_x),False,"White")
    text_surface6=test_font.render("player y:"+str(player_y),False,"White")
    text_surface7=test_font.render("mouse/player_angle:"+str(relative_angle),False,"White")
    screen.blit(menu_surface,(0,0))
    screen.blit(menu_surface2,(100,150))
    screen.blit(text_surface,(0,0))
    screen.blit(text_surface2,(0,30))
    screen.blit(text_surface3,(0,50))
    screen.blit(text_surface5,(0,120))
    screen.blit(text_surface6,(0,140))
    screen.blit(text_surface7,(0,160))
    return relative_angle

