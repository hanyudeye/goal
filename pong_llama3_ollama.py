import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BALL_SIZE = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the title of the window
pygame.display.set_caption("Pong")

# Set up some variables to store the state of the game
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

score1 = 0
score2 = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle1_y -= 5
    if keys[pygame.K_DOWN]:
        paddle1_y += 5
    if keys[pygame.K_w]:
        paddle2_y -= 5
    if keys[pygame.K_s]:
        paddle2_y += 5

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Collision detection
    if ball_y < 0 or ball_y > HEIGHT - BALL_SIZE:
        ball_speed_y *= -1
    if ball_x < 0 or ball_x > WIDTH - BALL_SIZE:
        ball_speed_x *= -1
    if ball_y + BALL_SIZE > paddle1_y and ball_y < paddle1_y + PADDLE_HEIGHT:
        if ball_x + BALL_SIZE > paddle1_y and ball_x < paddle1_y + PADDLE_WIDTH:
            ball_speed_x *= -1
    if ball_y + BALL_SIZE > paddle2_y and ball_y < paddle2_y + PADDLE_HEIGHT:
        if ball_x + BALL_SIZE > paddle2_y and ball_x < paddle2_y + PADDLE_WIDTH:
            ball_speed_x *= -1

    # Draw everything
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    pygame.draw.rect(screen, (0, 0, 0), (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, (0, 0, 0), (WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Update the score
    if ball_x < 0:
        score2 += 1
    elif ball_x > WIDTH:
        score1 += 1

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render(str(score1) + " - " + str(score2), True, (0, 0, 0))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)

    # Update the display
    pygame.display.flip()