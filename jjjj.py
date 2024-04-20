import pygame
import sys

pygame.init()


screen = pygame.display.set_mod((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Menu")
font = pygame.font.Font(none,36)


menu_options =['start','settings','exit']
selected_option =0


FPS = 30
BLACK=(0,0,0)
WHITE=(225,225,225)
RED=(225,0,0)
GREEN = (0,225,0)
                       

class Button():
  def _init_(self,text,x,y wight,hight color,hover_color):
    self.text=text
  def draw(self,screen):
    mouse_pos = ougame.mouse.get_pos()
    if self.x < mouse_pos[0] < self.x+ self.widght  \
    and self.y < mouse_pos[1],self.y + self height:
    pygame.draw.rect(screen, self.hover.color,(self.x,self.y,self.width,self.hight))
else:
    pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
text = font.render(self.text,True,WHITE)
text_rect = text.get_rect( centre=(self.x +selfwidht/2,self.y =self.height/2))
screen.blit(text,text_rect)


buttons =[]
    for i,option in enumerate(menu_options):
    button = Button(ortion,400 -100,200+ i*50,200,50,BLACK,RED)
    buttons append(button)


