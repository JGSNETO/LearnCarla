import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Pygame Example")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Rectangle settings
rect_x, rect_y = 50, 50
rect_speed_x, rect_speed_y = 2, 2

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update rectangle position
    rect_x += rect_speed_x
    rect_y += rect_speed_y
    
    # Bounce off edges
    if rect_x < 0 or rect_x > 800 - 50:
        rect_speed_x = -rect_speed_x
    if rect_y < 0 or rect_y > 600 - 50:
        rect_speed_y = -rect_speed_y
    
    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (rect_x, rect_y, 50, 50))
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)
