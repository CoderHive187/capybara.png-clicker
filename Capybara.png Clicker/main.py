import pygame
import random

pygame.display.set_caption("Capybara.png Clicker. (JUMPSCARE!1!)")

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
font = pygame.font.SysFont('Arial', 30)

# Set up the cookie image and rectangle
cookie_img = pygame.image.load('capybara.png').convert_alpha()
cookie_rect = cookie_img.get_rect()
cookie_rect.center = (screen_width / 2, screen_height / 2)

# Set up the cookie counter
cookies = 0

# Set up the cursor price and CPS (cookies per second)
cursor_price = 10
cursor_cps = 1

# Set up the cursor counter
cursors = 0

# Set up the background image
background_img = pygame.image.load('background.png').convert()

# Set up the game clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and cookie_rect.collidepoint(event.pos):
            cookies += 1
        elif event.type == pygame.MOUSEBUTTONDOWN and cookie_rect.collidepoint(event.pos):
            if cookies >= cursor_price:
                cookies -= cursor_price
                cursors += 1
                cursor_price *= 2
                cursor_cps += 1

    # Update cookie counter based on CPS
    cookies += cursor_cps * cursors

    # Draw background image
    screen.blit(background_img, [0, 0])

    # Draw cookies
    screen.blit(cookie_img, cookie_rect)
    cookies_text = font.render("Cookies: " + str(cookies), True, WHITE)
    screen.blit(cookies_text, [10, 10])

    # Draw cursors
    cursors_text = font.render("Cursors: " + str(cursors), True, WHITE)
    screen.blit(cursors_text, [10, 40])
    cursor_price_text = font.render("Price: " + str(cursor_price), True, GRAY)
    screen.blit(cursor_price_text, [10, 70])

    # Update the screen
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

# Quit the game
pygame.quit()
