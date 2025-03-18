import pygame

#Base class for game objects 
class CircleShape(pygame.sprite.Sprite):
	def __init__(self, x, y, radius):
		super().__init__()
		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0, 0)
		self.radius = radius

		#we will be using this later
		#if hasattr(self, "containers"):
			#super().__init__(self.containers)
		#else:
			#super().__init__()

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		#sub-classes must override
		pass
