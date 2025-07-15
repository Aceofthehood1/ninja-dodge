import pygame #use pip3 install pygame to install pygame
import time
import random

#Creating the window
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #window
pygame.display.set_caption("Ninja Dodge")#caption

BG = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT)) #background image setup

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

def draw(player): 
    WIN.blit(BG,(0,0)) #Method used to draw an image or surface use(0,0) to cover the whole page
    
    pygame.draw.rect(WIN, "red", player)  #Used to draw player onto the window
    
    pygame.display.update() # refresh the display

#Main game loop - Loop that runs while the game runs so its alive.
def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock() #Loop runs too fast so create clock object to regulate the speed of the game actions

    while run:
        clock.tick(60)
        for event in pygame.event.get():  #Checks for events
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >=0: #Limit the players movement so they dont go off screen
            player.x -= PLAYER_VEL  #Used to control player movement (Subtract 5 from the current x axis)
        if keys[pygame.K_RIGHT] and player.x + player.width + PLAYER_VEL <= WIDTH: #adding the player width because the x coordinate starts from the top left of the player so adding the player width allows the command to take into account the full width of the player before moving.
            player.x += PLAYER_VEL

        draw(player)
    
    pygame.quit() #Allows the close button to quit the application when it is clicked on

if __name__ =="__main__": #To make sure the game is being run directly from this file. In the case this file is imported it would be checked
    main()