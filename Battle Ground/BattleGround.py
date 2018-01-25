import pygame
import time
import random

pygame.init()
displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Battle ground")

fire_sound = pygame.mixer.Sound("fire.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")

#pygame.mixer.music.load("fire.wav")
#pygame.mixer.music.play(1)


white = (255,255,255)
black = (0,0,0)
red = (220,30,30)
lred = (255,0,0)
green = (100,200,100)
lightgreen = (0,255,0)
dimyellow = (200,200,0)
yellow = (255,255,50)
blue = (100,100,200)

clock = pygame.time.Clock()
FPS = 30


tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5

ground = 35

barrier_width = 50

smallFont = pygame.font.SysFont("Comisansms", 28) #font size
medFont = pygame.font.SysFont("Comisansms", 50) #font size
largeFont = pygame.font.SysFont("Comisansms", 80) #font size


def score(score):
    text = smallFont.render("Score: "+str(score),True,black)
    gameDisplay.blit(text, [10,10])

def text_objects(text,color,size):
    if size=="small":
        textSurface = smallFont.render(text, True, color)
    elif size=="medium":
        textSurface = medFont.render(text, True, color)
    elif size=="large":
        textSurface = largeFont.render(text, True, color)
    return textSurface,textSurface.get_rect()

def text_to_button(msg , color, buttonX,buttonY,buttonWidth,buttonHeight, size="small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonX+(buttonWidth/2)), buttonY+(buttonHeight/2))
    gameDisplay.blit(textSurf, textRect)

def message_to_screen(msg,color, y_displace=0,size="small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(displayWidth/2), int(displayHeight/2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

def tank(x,y,turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x-27, y-2),
                       (x-26, y-5),
                       (x-25, y-8),
                       (x-23, y-12),
                       (x-20, y-14),
                       (x-18, y-16),
                       (x-15, y-17),
                       (x-13, y-19),
                       (x-11, y-21)]
    
    pygame.draw.circle(gameDisplay, black, (x,y),int(tankHeight/2))
    

    pygame.draw.line(gameDisplay, blue, (x,y),possibleTurrets[turPos], turretWidth)

    pygame.draw.circle(gameDisplay, red, (x-15,y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x-10,y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x-5,y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x,y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x+5,y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x+10,y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x+15,y+20), wheelWidth)
    pygame.draw.rect(gameDisplay, blue, (x-tankHeight, y, tankWidth, tankHeight))

    return possibleTurrets[turPos] 
    
def enemy_tank(x,y,turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x+27, y-2),
                       (x+26, y-5),
                       (x+25, y-8),
                       (x+23, y-12),
                       (x+20, y-14),
                       (x+18, y-16),
                       (x+15, y-17),
                       (x+13, y-19),
                       (x+11, y-21)]
    
    pygame.draw.circle(gameDisplay, dimyellow, (x,y),int(tankHeight/2))
    

    pygame.draw.line(gameDisplay, black, (x,y),possibleTurrets[turPos], turretWidth)

    pygame.draw.circle(gameDisplay, red, (x-15,y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x-10,y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x-5,y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x,y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x+5,y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x+10,y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, red, (x+15,y+20), wheelWidth)
    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight))

    return possibleTurrets[turPos] 
    
def game_controls():
    gcont = True
    while gcont:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
        gameDisplay.fill(white)
        version = smallFont.render("Game version: 0.0.1",True,red)
        gameDisplay.blit(version, [10,10])
        message_to_screen("Controls",
                          color=green,
                          y_displace=-150,
                          size="large")
        message_to_screen("Fire: Spacebar",
                          color=black,
                          y_displace=-30,
                          size="small",)
        message_to_screen("Move Turet: Up and Down",
                          color=black,
                          y_displace=20,
                          size="small",)
        message_to_screen("Move Tank: Left and Righ",
                          color=black,
                          y_displace=70,
                          size="small",)
        message_to_screen("Pause: P",
                          color=black,
                          y_displace=120,
                          size="small",)

        button("Play" , 150,500,100,50, green, lightgreen, action="play")
        button("Main Menu" , 350,500,100,50, dimyellow, yellow, action="main")
        button("Quit", 550,500,100,50, red, lred, action="Quit")
  
        pygame.display.update()
        clock.tick(15)
    

def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action =="play":
                gameLoop()
            if action == "controls":
                print("User clik controns")
                game_controls()
            if action == "Quit":
                print("User quit")
                pygame.quit()
                quit
            if action == "main":
                game_intro()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)

    
    
        
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

        clock.tick(5)

def barrier(xlocation,randomHeight, barrier_width):
    pygame.draw.rect(gameDisplay, black, [xlocation,displayHeight-randomHeight,barrier_width,randomHeight])
    
def explosion(x, y, size=50):
    pygame.mixer.Sound.play(explosion_sound)
    explode = True
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        startPoint = x,y

        colorChoices = [red, lred, dimyellow, yellow]

        magnitude = 1

        while magnitude < size:
            exloding_bit_x = x+ random.randrange(-1*magnitude,magnitude)
            exloding_bit_y = y+ random.randrange(-1*magnitude,magnitude)

            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,4)],
                               (exloding_bit_x,exloding_bit_y),
                               random.randrange(1,5))
            magnitude += 5
            clock.tick(100)
        explode =False
            


def fireShell(xy, tankx, tanky, turPos, gun_power,xlocation,barrier_width,randomHeight, enemyTankX, enemyTankY):
    pygame.mixer.Sound.play(fire_sound)
    damage = 0
    fire = True
    startingShell = list(xy)
    
    #print("Player fired!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        pygame.draw.circle(gameDisplay, green, (startingShell[0],startingShell[1]),5)

        startingShell[0] -= (12 - turPos)*2
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gun_power/50))**2)-(turPos+turPos/(12-turPos)))

        if startingShell[1] > displayHeight - ground:
            #print("Last shell: ",startingShell[0],startingShell[1])
            hit_x = int((startingShell[0]*displayHeight - ground)/startingShell[1])
            hit_y = int(displayHeight - ground)
            #print("Player impact position",hit_x, hit_y)
            if enemyTankX + 10 > hit_x > enemyTankX - 10:
                print("Player Criital Hit!")
                damage = 25
            elif enemyTankX + 15 > hit_x > enemyTankX - 15:
                print("Player Hard Hit!")
                damage = 18
            elif enemyTankX + 25 > hit_x > enemyTankX - 25:
                print("Player Medium Hit!")
                damage = 10
            elif enemyTankX + 35 > hit_x > enemyTankX - 35:
                print("Player Light Hit!")
                damage = 5

            explosion(hit_x,hit_y)
            fire = False

##            if etankx + 25 > hit_x > etankx - 25:
##                damage = 25 - (hit_x - etankx)
##                    if damage > 25:
##                         damage = 25 + (hit_x - etankx)
##                         print(damage)
##                        explosion(hit_x, hit_y)
##                        fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= displayHeight
        check_y_2 = startingShell[1] >= displayHeight - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            #print("Last shell: ",startingShell[0],startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            #print("play fired hit barrier",hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False
                     

        pygame.display.update()
        clock.tick(60)
    return damage

def e_fireShell(xy, tankx, tanky, turPos, gun_power,xlocation,barrier_width,randomHeight, ptankX, ptankY):
    pygame.mixer.Sound.play(fire_sound)
    damage = 0 
    currentPower = 1
    power_found = False

    while not power_found:
        currentPower += 1
        if currentPower > 100:
            power_found = True
        #print("Enemy current power", currentPower)

        fire = True
        startingShell = list(xy)


        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #pygame.draw.circle(gameDisplay, red, (startingShell[0],startingShell[1]),5)

            startingShell[0] += (12 - turPos)*2
            startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(currentPower/50))**2) - (turPos+turPos/(12-turPos)))

            if startingShell[1] > displayHeight-ground:
                hit_x = int((startingShell[0]*displayHeight-ground)/startingShell[1])
                hit_y = int(displayHeight-ground)
                #explosion(hit_x,hit_y)
                if ptankX+15 > hit_x > ptankX - 15:
                    #print("target acquired!")
                    power_found = True
                fire = False

            check_x_1 = startingShell[0] <= xlocation + barrier_width
            check_x_2 = startingShell[0] >= xlocation

            check_y_1 = startingShell[1] <= displayHeight
            check_y_2 = startingShell[1] >= displayHeight - randomHeight

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((startingShell[0]))
                hit_y = int(startingShell[1])
                #explosion(hit_x,hit_y)
                fire = False
    

    
    fire = True
    startingShell = list(xy)
    #print("Enemy FIRE!",xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay, red, (startingShell[0],startingShell[1]),5)


        startingShell[0] += (12 - turPos)*2



        # y = x**2

        gun_power = random.randrange(int(currentPower *0.90), int(currentPower*1.10))            
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))

        if startingShell[1] > displayHeight-ground:
            #print("Last shell:",startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]*displayHeight-ground)/startingShell[1])
            hit_y = int(displayHeight-ground)
            #print("Enemy Ground Impact:", hit_x,hit_y)
            
            if ptankX + 10 > hit_x > ptankX - 10:
                print("Enemy Criital Hit!")
                damage = 25
            elif ptankX + 15 > hit_x > ptankX - 15:
                print("Enemy Hard Hit!")
                damage = 18
            elif ptankX + 25 > hit_x > ptankX - 25:
                print("Enemy Medium Hit!")
                damage = 10
            elif ptankX + 35 > hit_x > ptankX - 35:
                print("Enemy Light Hit!")
                damage = 5
            
            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= displayHeight
        check_y_2 = startingShell[1] >= displayHeight - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            #print("Last shell:",startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            #print("Impact:", hit_x,hit_y)
            explosion(hit_x,hit_y)
            fire = False
            

        pygame.display.update()
        clock.tick(60)
    return damage
        

def power(level):
    text = smallFont.render("Power: " +str(level)+"%", True, black)
    gameDisplay.blit(text, [displayWidth/2,0])

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
        version = smallFont.render("Game version: 0.0.1",True,red)
        gameDisplay.blit(version, [10,10])
        message_to_screen("Welcome to Battle ground",
                          color=green,
                          y_displace=-150,
                          size="large")
        message_to_screen("- Shoot em all",
                          color=black,
                          y_displace=-30,
                          size="medium",)
        message_to_screen("- Dodge bullet",
                          color=black,
                          y_displace=20,
                          size="medium",)
        message_to_screen("- Fun with fight",
                          color=black,
                          y_displace=70,
                          size="medium",)

        button("Play" , 150,500,100,50, green, lightgreen, action="play")
        button("Controls" , 350,500,100,50, dimyellow, yellow, action="controls")
        button("Quit", 550,500,100,50, red, lred, action="Quit")
  
        pygame.display.update()
        clock.tick(15)

def game_over():
    gameOver = True
    while gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
        gameDisplay.fill(white)
        version = smallFont.render("Game version: 0.0.1",True,red)
        gameDisplay.blit(version, [10,10])
        message_to_screen("Game Over",
                          color=green,
                          y_displace=-150,
                          size="large")
        message_to_screen("You ran out of health",
                          color=black,
                          y_displace=-30,
                          size="medium",)

        button("Play Again" , 150,500,150,50, green, lightgreen, action="play")
        button("Controls" , 350,500,100,50, dimyellow, yellow, action="controls")
        button("Quit", 550,500,100,50, red, lred, action="Quit")
  
        pygame.display.update()
        clock.tick(15)


def you_win():
    Win = True
    while Win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
        gameDisplay.fill(white)
        version = smallFont.render("Game version: 0.0.1",True,red)
        gameDisplay.blit(version, [10,10])
        message_to_screen("You Won",
                          color=green,
                          y_displace=-150,
                          size="large")
        message_to_screen("Congratulations",
                          color=black,
                          y_displace=-30,
                          size="medium",)

        button("Play Again" , 150,500,150,50, green, lightgreen, action="play")
        button("Controls" , 350,500,100,50, dimyellow, yellow, action="controls")
        button("Quit", 550,500,100,50, red, lred, action="Quit")
  
        pygame.display.update()
        clock.tick(15)

def health_bars(player_health, enemy_health):
    if player_health > 75:
        player_health_color = lightgreen
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red

    if enemy_health > 75:
        enemy_health_color = lightgreen
    elif enemy_health > 50:
        enemy_health_color = yellow
    else:
        enemy_health_color = red

    pygame.draw.rect(gameDisplay, player_health_color, (680, 25, player_health, 25))
    pygame.draw.rect(gameDisplay, enemy_health_color, (20, 25, enemy_health, 25))


def gameLoop():
    gameExit = False
    gameOver = False
    #FPS = 15

    player_health = 100
    enemy_health = 100
    
    barrier_width = 50

    mainTankX = displayWidth * 0.9 #initial position not the edge
    mainTankY = displayHeight * 0.9 #initial position not the edge
    tankMove = 0
    currentTurpos = 0
    changeTur = 0

    enemyTankX = displayWidth * 0.1
    enemyTankY = displayHeight * 0.9

    fire_power = 50
    power_change = 0

    xlocation = (displayWidth/2) + random.randint(-0.1*displayWidth,0.1*displayWidth)
    randomHeight = random.randrange(displayHeight*0.1,displayHeight*0.6)
     
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
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5
                
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5
                
                elif event.key == pygame.K_UP:
                    changeTur = 1
                
                elif event.key == pygame.K_DOWN:
                    changeTur = -1
                    
                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_SPACE:
                
                    damage = fireShell(gun, mainTankX,mainTankY,currentTurpos,fire_power,
                              xlocation,barrier_width,randomHeight,
                              enemyTankX, enemyTankY)
                    enemy_health -= damage

                    possibleMovement = ['f','r']
                    moveIndex = random.randrange(0,2)

                    for x in range(random.randrange(0,10)):
                        if displayWidth * 0.3 > enemyTankX > displayWidth * 0.03:
                            if possibleMovement[moveIndex] == "f":
                                enemyTankX +=5
                            elif possibleMovement[moveIndex] == "r":
                                enemyTankX -=5
                            gameDisplay.fill(white)
                            health_bars(player_health, enemy_health)
                            gun = tank(mainTankX,mainTankY, currentTurpos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change
                            power(fire_power)
                            barrier(xlocation,randomHeight,barrier_width)
                            gameDisplay.fill(green, rect=[0, displayHeight - ground, displayWidth, ground])
                            pygame.display.update()           
                    
                    damage = e_fireShell(enemy_gun, enemyTankX,enemyTankY,8,50,
                              xlocation,barrier_width,randomHeight,
                                mainTankX,mainTankY)
                    player_health -= damage
                elif event.key == pygame.K_a:
                    power_change = -1

                elif event.key == pygame.K_d:
                    power_change = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0

      
        mainTankX += tankMove
        
        currentTurpos += changeTur

        #move gun
        if currentTurpos > 8:
             currentTurpos = 8
        elif currentTurpos < 0:
             currentTurpos = 0

    
        #[positonX - (40/2)] which is upperleft < righ edge of barirer   
        if mainTankX - (tankWidth/2) < xlocation+barrier_width:
            mainTankX += 5
            print("hit barrier")
            #offest with tankMove = -5
            #if(0-4) pullback
            #if >5 bounch

        gameDisplay.fill(white)
        health_bars(player_health, enemy_health)
        gun = tank(mainTankX,mainTankY, currentTurpos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)

        fire_power += power_change
        if fire_power > 100:
            fire_power = 100
        elif fire_power < 1:
            fire_power = 1
        
        power(fire_power)
        
        
        
        barrier(xlocation,randomHeight,barrier_width)
        gameDisplay.fill(green, rect=[0, displayHeight - ground, displayWidth, ground])
        pygame.display.update()

        if player_health < 1:
            game_over()
        elif enemy_health < 1:
            you_win()
        clock.tick(FPS)

    pygame.quit()
    quit()

gameIntro()
gameLoop()
