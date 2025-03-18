import pygame
from constants import *

#this allows us to use code from
#the open-source pygame library
#throughout this file 

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	clock = pygame.time.Clock()
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 
		screen.fill("black") #Fill the screen with black
		pygame.display.flip() #Refresh the display

		dt = clock.tick(60) / 1000 #Limit to 60 FPS and calculate delta time

if __name__=="__main__":
	main()

