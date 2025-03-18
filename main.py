import pygame
from constants import *
from player import Player

#this allows us to use code from
#the open-source pygame library
#throughout this file 

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	
	#Create groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	#Set containers for the Player class
	Player.containers = updatable, drawable 

	#Instantiate the player at the center of the screen
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
 
		screen.fill("black") #Fill the screen with black
		player.update(dt) #Update all updatables
		
		#Draw all drawables
		for sprite in drawable:
			sprite.draw(screen)

		pygame.display.flip() #Refresh the display
		dt = clock.tick(60) / 1000 #Limit to 60 FPS and calculate delta time

if __name__=="__main__":
	main()

