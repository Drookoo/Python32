import pygame

pygame.init() 

BLCK = (0  , 0  , 0)
WHT  = (255, 255, 255)

size = (1400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("shift.py")

done = False

clock = pygame.time.Clock()

rect_x = 0
rect_y = 200

# change the rect_change_x value around. Can't achieve the effect you're looking for
rect_change_x = 300

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill(BLCK)
	
	pygame.draw.rect(screen, WHT, [rect_x,rect_y,50,50])
	
	rect_x += rect_change_x
	
	
	if rect_x >= 650:
		rect_change_x = 0
	if rect_x <= 650:
		rect_change_x = 1 /rect_change_x
		rect_change_x = rect_change_x + 1
	
	
	pygame.display.flip()
	clock.tick(60)
pygame.quit()
