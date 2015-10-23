#the most basic of pygame programs 
import pygame
from colors import *
pygame.init() 

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame. display.set_caption("My Game")

# Loop Until User Ends 
done = False

# How Fast Screen Updates
clock = pygame.time.Clock()

# ---------- Main Program Loop ----------
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill(WHITE)
	pygame.display.flip()
	clock.tick(60)
pygame.quit()