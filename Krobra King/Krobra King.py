import pygame
#import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,255)

displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Krobra King")

#icon = pygame.image.load('snake.png')
#pygame.display.set_icon(icon)

img = pygame.image.load('snakehead.png')
appleimg = pygame.image.load('apple.png')


clock = pygame.time.Clock()

appleThickness = 30
block_size = 20
FPS = 20

direction ="right"

smallFont = pygame.font.SysFont(None, 25) #size
medFont = pygame.font.SysFont(None, 50) #size
largeFont = pygame.font.SysFont(None, 80) #size

score=0


def pause():
    paused = True
    while paused:
        message_to_screen("Pause",
                              color=red,
                              y_displace=-50,
                              size="large")
        message_to_screen("Press P to continue or Q to quite",
                                color=black,
                                y_displace=50,
                                size="medium")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
    
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #gameDisplay.fill(white)

        clock.tick(5)
    

def score(score):
    text = smallFont.render("Score: "+str(score),True,black)
    gameDisplay.blit(text, [10,10])

def scoreTotal(score):
    text = largeFont.render("Total Score: "+str(score),True,green)
    gameDisplay.blit(text, [220,170])

def randAppleGen():
    randAppleX = round(random.randrange(0,displayWidth-appleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0,displayHeight-appleThickness))#/10.0)*10.0
    return randAppleX,randAppleY

def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_SPACE:
                    intro = False
                    
        gameDisplay.fill(white)
        message_to_screen("Welcome to Krobra King",
                          color=green,
                          y_displace=-150,
                          size="large")
        message_to_screen("- Just eat apple to grow",
                          color=black,
                          y_displace=-30,
                          size="medium",)
        message_to_screen("- Do not hit the wall",
                          color=black,
                          y_displace=20,
                          size="medium",)
        message_to_screen("- Do not run into yourself",
                          color=black,
                          y_displace=70,
                          size="medium",)
        message_to_screen("press Space bar to start, P to pause, Q to quit",
                          color=red,
                          y_displace=150,
                          size="small")
        version = smallFont.render("Game version: 0.0.1",True,red)
        gameDisplay.blit(version, [10,10])
        
        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakeList):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size=="small":
        textSurface = smallFont.render(text, True, color)
    elif size=="medium":
        textSurface = medFont.render(text, True, color)
    elif size=="large":
        textSurface = largeFont.render(text, True, color)
        
    return textSurface,textSurface.get_rect()

def message_to_screen(msg,color, y_displace=0,size="small"):
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [displayWidth/2,displayHeight/2])
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (displayWidth/2),(displayHeight/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction
    gameExit = False
    gameOver = False
    
    lead_x = displayWidth/2
    lead_y = displayHeight/2
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    
    randAppleX,randAppleY = randAppleGen()
    
    while not gameExit:
        
        if gameOver == True:
            gameDisplay.fill(white)
            scoreTotal(snakeLength-1)
            message_to_screen("Game over",
                              red,
                              y_displace=0,
                              size="large")
            message_to_screen("Press C to play again or Q to exit",
                              black,
                              y_displace=100,
                              size="medium")
            pygame.display.update()
            
        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_SPACE:
                        gameLoop()
                        
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                    
                elif event.key == pygame.K_p:
                    pause()
                    
                
        if  lead_x>=displayWidth or lead_x<0 or lead_y>=displayHeight or lead_y<0:
                gameOver = True

        #lead_x = (lead_x + lead_x_change) % 800
        #lead_y = (lead_y + lead_y_change) % 600﻿

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)


        #pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,appleThickness,appleThickness])
        gameDisplay.blit(appleimg, (randAppleX,randAppleY))
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        
        snake(block_size, snakeList)

        score(snakeLength-1)
        
        pygame.display.update()

##        if lead_x == randAppleX and lead_y == randAppleY:
##            randAppleX = round(random.randrange(0,displayWidth-block_size)/10.0)*10.0
##            randAppleY = round(random.randrange(0,displayHeight-block_size)/10.0)*10.0
##            snakeLength +=1
##        if lead_x >= randAppleX and lead_x <= randAppleX+appleThickness:
##            if lead_y >= randAppleY and lead_y <= randAppleY+appleThickness:
##                randAppleX = round(random.randrange(0,displayWidth-block_size))#/10.0)*10.0
##                randAppleY = round(random.randrange(0,displayHeight-block_size))#/10.0)*10.0
##                snakeLength +=1
        if lead_x > randAppleX and lead_x < randAppleX+appleThickness or lead_x+block_size > randAppleX and lead_x+block_size < randAppleX+appleThickness:
            if lead_y > randAppleY and lead_y < randAppleY+appleThickness or lead_y+block_size > randAppleY and lead_y+block_size < randAppleY+appleThickness:
                randAppleX,randAppleY = randAppleGen()
                snakeLength +=1
        

        

        clock.tick(FPS)

    #message_to_screen("You Lose",red)
    #time.sleep(2)
    #pygame.display.update()
    pygame.quit()
    quit()

gameIntro()
gameLoop()
