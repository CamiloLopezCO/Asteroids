import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		#Always kill the asteroid first
		self.kill()
		
		#If it's the smallest, no splitting
		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		#Compute new radius 
		new_radius = self.radius - ASTEROID_MIN_RADIUS

		#Generate random angle for split
		random_angle = random.uniform(20, 50)

		#General two new velocities
		direction1 = self.velocity.rotate(random_angle) * 1.2
		direction2 = self.velocity.rotate(-random_angle) * 1.2

		#Spawn two new asteroids
		from asteroid import Asteroid #Avoid circular import issues
		Asteroid(self.position.x, self.position.y, new_radius).velocity = direction1
		Asteroid(self.position.x, self.position.y, new_radius).velocity = direction2
