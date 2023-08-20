import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 400
screen_height = 300

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("exe example")

# Font for the text
font = pygame.font.Font(None, 36)

# Button dimensions and position
button_width = 100
button_height = 50
button_x = (screen_width - button_width) // 2
button_y = (screen_height - button_height) // 2

# Timing variables
show_hello = False
hello_timer = 0

# Main loop
running = True

while running:
    screen.fill(white)
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the mouse click is inside the button
            if button_x < event.pos[0] < button_x + button_width and \
            button_y < event.pos[1] < button_y + button_height:
                show_hello = True
                hello_timer = pygame.time.get_ticks()  # Get current time in milliseconds

    # Draw the button
    pygame.draw.rect(screen, black, (button_x, button_y, button_width, button_height))
    
    # Draw the button text
    button_text = font.render("Button", True, white)
    button_text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(button_text, button_text_rect)
    
    # Display "hello" if clicked and within the 3-second timeframe
    if show_hello:
        hello_text = font.render("executable demo for DTP", True, black)
        hello_text_rect = hello_text.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
        screen.blit(hello_text, hello_text_rect)
        
        if pygame.time.get_ticks() - hello_timer >= 3000:  # Check if 3 seconds have passed
            show_hello = False
    
    pygame.display.flip()

pygame.quit()
sys.exit()