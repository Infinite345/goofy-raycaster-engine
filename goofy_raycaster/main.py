import pygame
pygame.init()

running = True

x = 0 #config
y = 0
xres = 1920
yres = 1080
speed = 5
color = (255, 255, 255)
surface = pygame.display.set_mode((xres, yres))
pygame.display.set_caption("goofy raycaster")
#pygame.display.set_icon("")

while running:
    
    if event.type == pygame.QUIT: #quit
        running = False
        
    keys = pygame.key.get_pressed() #keypresses
    
    if keys[pygame.K_W]:
        y = y + speed
    if keys[pygame.K_S]:
        y = y - speed
    if keys[pygame.K_A]:
        x = x - speed
    if keys[pygame.K_d]:
        x = x + speed
        
    pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60)) #render
    pygame.display.flip()
    
pygame.quit()