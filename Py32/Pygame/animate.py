import pygame
# Fixes executive file error
import pygame._view
pygame.init() 

# Color
BLCK = (0  , 0  , 0)
WHT  = (255, 255, 255)
GRN  = (0  , 225, 0)
RD   = (255, 0  , 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Loop Until User Ends 
done = False

# How Fast Screen Updates
clock = pygame.time.Clock()

# Rectangle Start Position 
rect_x = 50 
rect_y = 50

# Rectangle Speed and Direction 
rect_change_x = 5
rect_change_y = 5

# ---------- Main Program Loop ----------
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill(BLCK)
	
	# Our Rectangle 
	pygame.draw.rect(screen, WHT, [rect_x,rect_y,50,50])
	
	# Change in Rectangle Speed
	rect_x += rect_change_x
	rect_y += rect_change_y
	
	# Bounce
	if rect_y > 450 or rect_y < 0:
		rect_change_y = rect_change_y * -1 
	if rect_x > 650 or rect_x < 0:
		rect_change_x = rect_change_x * -1
	
	
	pygame.display.flip()
	clock.tick(60)
pygame.quit()