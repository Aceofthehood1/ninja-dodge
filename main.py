import pygame #use pip3 install pygame to install pygame
import time
import random
pygame.font.init() #initialize font module

#Creating the window
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #window
pygame.display.set_caption("Ninja Dodge")#caption

BG = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT)) #background image setup

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5
SHURIKEN_WIDTH = 10
SHURIKEN_HEIGHT = 20
SHURIKEN_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30) #assigning font style and size

def draw(player, elapsed_time, shurikens): 
    WIN.blit(BG,(0,0)) #Method used to draw an image or surface use(0,0) to cover the whole page

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white") #create font object and pass the text to be rendered
    WIN.blit(time_text, (10,10))
    
    pygame.draw.rect(WIN, "red", player)  #Used to draw player onto the window

    for shuriken in shurikens:
        pygame.draw.rect(WIN, "white", shuriken)
    
    pygame.display.update() # refresh the display

#Main game loop - Loop that runs while the game runs so its alive.
def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock() #Loop runs too fast so create clock object to regulate the speed of the game actions
    start_time = time.time() #this will get the current time
    elapsed_time = 0 

    shuriken_add_increment = 2000 #amount of miliseconds before a shuriken is added
    shuriken_count = 0 #when a shuriken should be added after a certain time

    shurikens = []
    hit = False

    while run:
        shuriken_count += clock.tick(60)
        elapsed_time = time.time() - start_time # this will get the amount of time the user has spent since the window was open in this case since the loop was running 
        
        if shuriken_count > shuriken_add_increment:
            for _ in range(3):
                shuriken_x = random.randint(0, WIDTH - SHURIKEN_WIDTH) #setting up 3 shurikens to be on random possions on the screen
                shuriken = pygame.Rect(shuriken_x, -SHURIKEN_HEIGHT, SHURIKEN_WIDTH, SHURIKEN_HEIGHT) #to make the shuriken move down on the screen but its starting position is off of the screen(not visible)
                shurikens.append(shuriken)
            
            shuriken_add_increment = max(200, shuriken_add_increment - 50) #make the increment value 200
            shuriken_count = 0

        for event in pygame.event.get():  #Checks for events
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >=0: #Limit the players movement so they dont go off screen
            player.x -= PLAYER_VEL  #Used to control player movement (Subtract 5 from the current x axis)
        if keys[pygame.K_RIGHT] and player.x + player.width + PLAYER_VEL <= WIDTH: #adding the player width because the x coordinate starts from the top left of the player so adding the player width allows the command to take into account the full width of the player before moving.
            player.x += PLAYER_VEL

        for shuriken in shurikens[:]: #making copy of the shurikens list since it could cause errors later on
            shuriken.y += SHURIKEN_VEL
            if shuriken.y > HEIGHT: #to check if the shuriken has left the window 
                shurikens.remove(shuriken)
            elif shuriken.y + shuriken.height >= player.y and shuriken.colliderect(player): #when a shuriken hits a player or the ground it dissapears 
                shurikens.remove(shuriken)
                hit = True
                break
        
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2)) #place text in the middle of the screen
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, shurikens)
    
    pygame.quit() #Allows the close button to quit the application when it is clicked on

if __name__ =="__main__": #To make sure the game is being run directly from this file. In the case this file is imported it would be checked
    main()