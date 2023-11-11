import pygame
pygame.init()
size=width,height=(800,800)
screen=pygame.display.set_mode(size)
ball=pygame.image.load("ball.gif")
x,y=width/2-50,height-110
man=pygame.Rect(x,y-100,50,100)
vel=10
clock=pygame.time.Clock()
run=True
start=False
c=0
while run:
        clock.tick(60)
        screen.fill((255,0,0))
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        run=False
        c+=1
        if c>=100:
                start=True
        if start:
                y-=vel
                vel-=0.1
                if vel<=-10:
                        vel=10
        screen.blit(ball,(x,y))
        pygame.display.update()
pygame.quit()
