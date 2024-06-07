import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1300, 700))
clock = pygame.time.Clock()

running = True
box_color = "purple"
random_x = random.randint(100,1200)
random_y = random.randint(100,600)

font1 = pygame.font.Font( None , 100)
fontSurface1 = font1.render(" You found the Chest " , False , "black" , "cadetblue2" )

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
found = False

class Box : 
    def __init__(self) : 
        self.x = random_x 
        self.y = random_y 
        self.height= 100 
        self.width = 100 
        self.color = "cadetblue3" 
 
        self.x = random_x 
        self.y = random_y 

    def random(self):
        self.x = random_x 
        self.y = random_y 
    
        
class Ball:
    def  __init__(self):
        self.x = 650
        self.y = 350
        self.speed = 10
        self.radius = 40
        self.color = "red"
        self.boost = 0


    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q] and self.boost == 0 :
                self.boost = 50

        if self.boost > 0 : 
            if keys[pygame.K_w]:
                if self.y >= 50 :
                    self.y -= self.boost
            if keys[pygame.K_s]:
                if self.y <= 650 :
                    self.y += self.boost
            if keys[pygame.K_a]:
                if self.x >= 50 :
                    self.x -= self.boost
            if keys[pygame.K_d]:
                if self.x <= 1250 :
                    self.x += self.boost
         
            self.boost -= 1

        else : 
            if keys[pygame.K_w]:
                if self.y >= 50 :
                    self.y -= self.speed
            if keys[pygame.K_s]:
                if self.y <= 650 :
                    self.y += self.speed
            if keys[pygame.K_a]:
                if self.x >= 50 :
                    self.x -= self.speed
            if keys[pygame.K_d]:
                if self.x <= 1250 :
                    self.x += self.speed
            if keys[pygame.K_q]:
                    self.boost = 50

    def boxCollision(self , box):

        if abs(self.x - box.x) < 100 and abs(self.y - box.y) < 100 : 
            box.color = "green"

box = Box()
ball1 = Ball()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    k = pygame.key.get_pressed()


    screen.fill("cadetblue3")

    pygame.draw.circle(screen, ball1.color, [ball1.x,ball1.y], ball1.radius,10)
    pygame.draw.rect(screen,box.color,[box.x , box.y , box.width , box.height ] ,0,10)

    ball1.move()
    ball1.boxCollision(box)

    if box.color == "green": text = screen.blit(fontSurface1 , [300,100,1000,1000])
   
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
