import pygame
import sys

#State class'ı durumların özelliklerini bulunduran class
class state:
    def __init__(self,text,x,y,start,end,screen,color,textcolor):
        self.x=x
        self.y=y
        self.Ea=None
        self.Eb=None
        self.color=color
        self.start=start
        self.end=end
        self.title=text
        self.screen=screen
        self.r=25
        self.textcolor=textcolor
        self.font=pygame.font.SysFont(None, 20)
        self.name=self.font.render(text, True, textcolor, { 0,0,0})
        self.drawsatate();
        self.writename()
        #statelerin ciziminin yapırdıgı fonsiyon
    def drawsatate(self):
        pygame.draw.circle(self.screen,self.color, (self.x,self.y), self.r,2)
        if(self.end==True):
            
            pygame.draw.circle(self.screen,self.color, (self.x,self.y), self.r-5,1)
        if(self.start==True):
         pygame.draw.line(self.screen,self.color,[self.x-50,self.y],[self.x-30,self.y])
         pygame.draw.line(self.screen,self.color,[self.x-30-3,self.y+9],[self.x-30,self.y])
         pygame.draw.line(self.screen,self.color,[self.x-30-3,self.y-9],[self.x-30,self.y])
        
            
         
        #state isminin cizindiği fonksiyon
    def writename(self):
        textrect =self.name.get_rect()
        textrect.centerx = self.x
        textrect.centery = self.y
        self.screen.blit(self.name, textrect)
        
        pygame.display.update()
textcolor =   (255, 0,  0)        
WHITE = (255, 255, 255)
color =  (0,   0, 0)
#stateler arası iliskini cizirdiği fonksiyon
def draw(screen,x,y,text):
  pi=3.141592653
  font=pygame.font.SysFont(None, 12)
  alfabe=font.render(text, True,textcolor,{ 0,0,0} )
  if(x[0]==y[0]):
         
        pygame.draw.arc(screen, color,[y[0],y[1], 45,50], pi, 5*pi/2, 2)
        
        pygame.draw.line(screen,color,[y[0]-9,y[1]+9+25],[y[0],y[1]+25],2)
        pygame.draw.line(screen,color,[y[0]+9,y[1]+9+25],[y[0],y[1]+25],2)
        textdraw=alfabe.get_rect()
        textdraw.centerx=y[0]+45
        textdraw.centery=y[1]+50
        screen.blit(alfabe,textdraw)
        pygame.display.update()
  else:     
    
    if(x[0]>y[0]):
        i=10*(y[0]-x[0])/100
        
        textdraw=alfabe.get_rect()
        textdraw.centerx=y[0]+(x[0]-y[0])/2
        textdraw.centery=y[1]+75
        screen.blit(alfabe,textdraw)
        pygame.draw.arc(screen, color,[y[0], y[1],x[0]-y[0]-i,80+i], pi, 2*pi, 2)
        pygame.draw.line(screen,color,[y[0]-9,y[1]+9+25],[y[0],y[1]+25],2)
        pygame.draw.line(screen,color,[y[0]+9,y[1]+9+25],[y[0],y[1]+25],2)
        pygame.display.update()
    else:
       i=10*(y[0]-x[0])/100
       textdraw1=alfabe.get_rect()
       textdraw1.centerx=x[0]+(y[0]-x[0])/2
       textdraw1.centery=y[1]-50
       screen.blit(alfabe,textdraw1)
       pygame.draw.arc(screen,color,[x[0],x[1]-60, y[0]-x[0], 100-i], 0, pi, 2)
       #pygame.draw.polygon(screen,color,[[y[0]-12,y[1]-12-25],[y[0]+12,y[1]-12-25],[y[0],y[1]-25]])
       pygame.draw.line(screen,color,[y[0]-12,y[1]-12-25],[y[0],y[1]-25],2)
       pygame.draw.line(screen,color,[y[0]+12,y[1]-12-25],[y[0],y[1]-25],2)
       pygame.display.update()


