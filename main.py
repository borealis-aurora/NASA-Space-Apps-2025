import pygame
from sys import exit
import math 
import numpy as np
import pygame.camera

def Weather(O):
    match O:
        case"a":
            weather="plague"
        case"b":
            weather="clear"
    playing=False
    return weather,playing

def music_state(playing,weather):
    if playing==False and weather=="clear":
        pygame.mixer.music.load("Music/Ground.mp3")
        pygame.mixer.music.play(loops=100,fade_ms=50)
    if playing==False and weather=="plague":
        pygame.mixer.music.load("Music/Plague.mp3")
        pygame.mixer.music.play(loops=100,fade_ms=50)
    playing=True
    return playing

class invisible_wall:
    def __init__(self):
        self.col_reference=pygame.image.load("Graphics/Coliision_reference.png")
        self.pos_x=300
        self.pos_y=300
        self.surface=self.col_reference.get_rect(topleft=(self.pos_x,self.pos_y))
def interactions_check():
    red.interaction(player.x, player.y)

class device:
    def __init__(self,x0,y0):
        self.col_reference=pygame.image.load("Graphics/Girasol.png")
        self.player_sprite1=pygame.image.load("Graphics/Girasol.png")
        self.player_sprite2=pygame.image.load("Graphics/Girasol_contorno.png")
        self.player_sprite3=pygame.image.load("Graphics/Button_E.png")
        #device=pygame.draw.circle(screen, "red", (offset_x,offset_y), 25)
        self.pos_x=x0+offset_x
        self.pos_y=y0+offset_y
        self.text_surface10=test_font.render("Hay zombis en tu jardin",False,"White")
        self.surface=self.col_reference.get_rect(topleft=(self.pos_x,self.pos_y))
    def return_surface(self): return self.surface
    def return_pos(self): return self.pos_x,self.pos_y
    def interaction(self,player_x,player_y):
        if np.sqrt((-player_x+self.pos_x)**2 + (-player_y+self.pos_y)**2) <80:
            text_surface9=test_font.render("device nearby: press E to interact:",False,"White")
            screen.blit(self.player_sprite1,(self.pos_x-30,self.pos_y-30))
            screen.blit(self.player_sprite3,(self.pos_x-20,self.pos_y-90))
            screen.blit(text_surface9,(10,200))
        else:
            screen.blit(self.player_sprite2,(self.pos_x-30,self.pos_y-30))
        if np.sqrt((-player_x+self.pos_x)**2 + (-player_y+self.pos_y)**2) < 80:
            screen.blit(self.text_surface10,(self.pos_x,self.pos_y+40))
            
class device2:
    def __init__(self,x0,y0):
        self.col_reference=pygame.image.load("Graphics/Girasol.png")
        self.player_sprite1=pygame.image.load("Graphics/Girasol.png")
        self.player_sprite2=pygame.image.load("Graphics/Girasol_contorno.png")
        self.player_sprite3=pygame.image.load("Graphics/Button_E.png")
        #device=pygame.draw.circle(screen, "red", (offset_x,offset_y), 25)
        self.pos_x=x0+offset_x
        self.pos_y=y0+offset_y
        self.text_surface10=test_font.render("Hay zombis en tu jardin",False,"White")
        self.surface=self.col_reference.get_rect(topleft=(self.pos_x,self.pos_y))
    def return_surface(self): return self.surface
    def return_pos(self): return self.pos_x,self.pos_y
    def interaction(self,player_x,player_y):
        if np.sqrt((-player_x+self.pos_x)**2 + (-player_y+self.pos_y)**2) <80:
            text_surface9=test_font.render("device nearby: press E to interact:",False,"White")
            screen.blit(self.player_sprite1,(self.pos_x-30,self.pos_y-30))
            screen.blit(self.player_sprite3,(self.pos_x-20,self.pos_y-90))
            screen.blit(text_surface9,(10,200))
        else:
            screen.blit(self.player_sprite2,(self.pos_x-30,self.pos_y-30))
        if np.sqrt((-player_x+self.pos_x)**2 + (-player_y+self.pos_y)**2) < 80:
            screen.blit(self.text_surface10,(self.pos_x,self.pos_y+40))
def check_player(relative_angle,player):
    player_x=player.x-30
    player_y=player.y-30
    pi=np.pi
    player_rect=player_sprite1.get_rect(topleft= (player.x,player.y))
    if relative_angle>(0) and relative_angle<(pi/6):
        screen.blit(player_sprite1,(player_x,player_y))
    if relative_angle>(pi/6) and relative_angle<(pi/3):
        screen.blit(player_sprite2,(player_x,player_y))
    if relative_angle>(pi/3) and relative_angle<(pi/4):
        screen.blit(player_sprite3,(player_x,player_y))
    if relative_angle>(pi/4) and relative_angle<(pi/2):
        screen.blit(player_sprite4,(player_x,player_y))
    if relative_angle>(pi/2) and relative_angle<(3*pi/4):
        screen.blit(player_sprite10,(player_x,player_y))
    if relative_angle>(3*pi/4) and relative_angle<(pi):
        screen.blit(player_sprite8,(player_x,player_y))
    if relative_angle>(pi) and relative_angle<(5*pi/4):
        screen.blit(player_sprite11,(player_x,player_y))
    if relative_angle>(5*pi/4) and relative_angle<(7*pi/4):
        screen.blit(player_sprite7,(player_x,player_y))
    if relative_angle>(7*pi/4) and relative_angle<(2*pi):
        screen.blit(player_sprite5,(player_x,player_y))
    return player_rect

def colission(player,keys,offset_x,offset_y,player_state,player_rect,object_rect,dt,object_x,object_y):
    player_rect=check_player(relative_angle,player)
    if player_rect.colliderect(object_rect):
        text_surface11=test_font.render("Colision detectada",False,"White")
        screen.blit(text_surface11,(10,220))
        player_rect.right = object_rect.left
        player.x = player_rect.x
    if player_rect.colliderect(object_rect):
        text_surface11=test_font.render("Colision detectada",False,"White")
        screen.blit(text_surface11,(10,220))
        player_rect.left = object_rect.right
        player.x = player_rect.x
    if player_rect.colliderect(object_rect):
        text_surface11=test_font.render("Colision detectada",False,"White")
        screen.blit(text_surface11,(10,220))
        player_rect.bottom = object_rect.top
        player.y = player_rect.y
    if player_rect.colliderect(object_rect):
        text_surface11=test_font.render("Colision detectada",False,"White")
        screen.blit(text_surface11,(10,220))
        player_rect.top = object_rect.bottom
        player.y = player_rect.y
def move_player(player,keys,offset_x,offset_y,player_state,player_rect,object_rect,dt,object_x,object_y):
    player_state="idle"
    speed=10
    player_rect=check_player(relative_angle,player)
    if keys[pygame.K_d]:
        player.x += speed
        player_rect.x =player.x
        if player_rect.colliderect(object_rect):
            text_surface11=test_font.render("Colision detectada",False,"White")
            screen.blit(text_surface11,(10,220))
            player_rect.right = object_rect.left
            player.x = player_rect.x
        else:
            player_state = "moving"
    if keys[pygame.K_a]:
        player.x -= speed
        player_rect.x=player.x
        if player_rect.colliderect(object_rect):
            text_surface11=test_font.render("Colision detectada",False,"White")
            screen.blit(text_surface11,(10,220))
            player_rect.left = object_rect.right
            player.x = player_rect.x
        else:
            player_state = "moving"
    if keys[pygame.K_s]:
        player.y += speed
        player_rect.y=player.y
        if player_rect.colliderect(object_rect):
            text_surface11=test_font.render("Colision detectada",False,"White")
            screen.blit(text_surface11,(10,220))
            player_rect.bottom = object_rect.top
            player.y = player_rect.y
        else:
            player_state = "moving"
    if keys[pygame.K_w]:
        player.y -= speed
        player_rect.y=player.y
        if player_rect.colliderect(object_rect):
            text_surface11=test_font.render("Colision detectada",False,"White")
            screen.blit(text_surface11,(10,220))
            player_rect.top = object_rect.bottom
            player.y = player_rect.y
        else:
            player_state = "moving"
    if player.x>740:
        player.x=740
        player_state="moving"
        offset_x-=10
    if player.x<540:
        player_state="moving"
        player.x=540
        offset_x+=10
        player_state="moving"
    if player.y>400:
        player.y=400
        player_state="moving"
        offset_y-=10
    if player.y<200:
        player_state="moving"
        player.y=200
        offset_y+=10
        player_state="moving"
    return player,offset_x,offset_y,player_state

def locate(number,relative_angle,player_state):
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
            relative_angle=math.atan(relative_mouse_y/relative_mouse_x)+np.pi
        elif relative_mouse_x<0 and relative_mouse_y<0:
            relative_angle=math.atan(relative_mouse_y/relative_mouse_x)+np.pi
        elif relative_mouse_x>0 and relative_mouse_y<0:
            relative_angle=math.atan(relative_mouse_y/relative_mouse_x)+(2*np.pi)
    text_surface5=test_font.render("player x:"+str(player_x),False,"White")
    text_surface6=test_font.render("player y:"+str(player_y),False,"White")
    text_surface7=test_font.render("mouse/player_angle:"+str(relative_angle),False,"White")
    text_surface8=test_font.render("state:"+player_state,False,"White")
    screen.blit(menu_surface,(10,0))
    screen.blit(menu_surface3,(offset_x,offset_y))
    screen.blit(text_surface,(10,0))
    screen.blit(text_surface2,(10,30))
    screen.blit(text_surface3,(10,50))
    screen.blit(text_surface5,(10,120))
    screen.blit(text_surface6,(10,140))
    screen.blit(text_surface7,(10,160))
    screen.blit(text_surface8,(10,180))
    return number,relative_angle


Matriz_de_colision=[[1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2],
                    [1,1,1,1,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2],
                    [1,1,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2],
                    [1,1,0,0,0,0,0,1,0,0,0,1,2,2,2,2,2,2,2,2,2],
                    [1,1,0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2],
                    [1,1,0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
"""
0: sin colisión
1: con colisión
2: no colisión (pero aquí es por que ya es espacio vacío)
"""
Matriz_de_colision=np.array(Matriz_de_colision)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 600))
pygame.display.set_caption('GAME')
clock = pygame.time.Clock()
number=1
mouse_pos = pygame.mouse.get_pos()
mouse_x=mouse_pos[0]
mouse_y=mouse_pos[1]
pygame.mixer.init()
menu_surface= pygame.image.load("Graphics/background.png")
menu_surface3= pygame.image.load("Graphics/map3.png")
player_sprite1=pygame.image.load("Graphics/player_placeholder1.png")
player_sprite2=pygame.image.load("Graphics/player_placeholder2.png")
player_sprite3=pygame.image.load("Graphics/player_placeholder3.png")
player_sprite4=pygame.image.load("Graphics/player_placeholder4.png")
player_sprite5=pygame.image.load("Graphics/player_placeholder5.png")
player_sprite6=pygame.image.load("Graphics/player_placeholder6.png")
player_sprite7=pygame.image.load("Graphics/player_placeholder7.png")
player_sprite8=pygame.image.load("Graphics/player_placeholder8.png")
player_sprite9=pygame.image.load("Graphics/player_placeholder9.png")
player_sprite10=pygame.image.load("Graphics/player_placeholder10.png")
player_sprite11=pygame.image.load("Graphics/player_placeholder11.png")
player_sprite12=pygame.image.load("Graphics/player_placeholder12.png")


test_font=pygame.font.Font(None,25)
text_surface=test_font.render(str(number),False,"White")
text_surface2=test_font.render("mouse x:"+str(mouse_x),False,"White")
text_surface3=test_font.render("mouse y"+str(mouse_y),False,"White")
player = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player_x=player.x
player_y=player.y
player_still=True

relative_mouse_x=mouse_x-player_x
relative_mouse_y=mouse_y-player_y

relative_angle=math.atan(relative_mouse_y/relative_mouse_x)

offset_x=0
offset_y=0
playing=False
player_state="idle"



weather="clear"
dt=1
text_surface5=test_font.render("player x:"+str(player_x),False,"White")
text_surface6=test_font.render("player y:"+str(player_y),False,"White")
text_surface7=test_font.render("mouse/player_angle:"+str(relative_angle),False,"White")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    playing=music_state(playing,weather)
    number,relative_angle=locate(number,relative_angle,player_state)
    keys = pygame.key.get_pressed()#Variable que corresponde al inpu
    player_rect=check_player(relative_angle, player)
    
    """
    OBJETOS
    """
    red=device(255,255)
    object_rect=red.return_surface()
    object_x,object_y=red.return_pos()
    
    red2=device2(400,255)
    object_rect2=red2.return_surface()
    object_x2,object_y2=red2.return_pos()
    """
    OBJETOS
    """
    WALL=invisible_wall()
    player,offset_x,offset_y,player_state=move_player(player, keys,offset_x,offset_y,player_state,player_rect,object_rect,dt,object_x,object_y)
    
    interactions_check()
    if keys[pygame.K_p]:#Input de tecla
        O="a"
        weather,playing=Weather(O)
    if keys[pygame.K_o]:#Input de teclab
        O="b"
        weather,playing=Weather(O)
    pygame.display.update()
    clock.tick(60)