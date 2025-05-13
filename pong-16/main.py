import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle setup
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_a = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(WIDTH - 60, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball setup
BALL_SIZE = 20
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_dx, ball_dy = 4, 4

# Score
score_a = 0
score_b = 0
font = pygame.font.SysFont("Courier", 30)

# Sounds (Optional)
# bounce_sound = pygame.mixer.Sound("bounce.wav")  # Uncomment if you have sound

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= 6
    if keys[pygame.K_s] and paddle_a.bottom < HEIGHT:
        paddle_a.y += 6
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= 6
    if keys[pygame.K_DOWN] and paddle_b.bottom < HEIGHT:
        paddle_b.y += 6

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Border collision
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1
        # bounce_sound.play()

    # Score update
    if ball.right >= WIDTH:
        score_a += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_dx *= -1

    if ball.left <= 0:
        score_b += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_dx *= -1

    # Paddle collision
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_dx *= -1
        # bounce_sound.play()

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw middle line
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Draw score
    score_text = font.render(f"Player A: {score_a}    Player B: {score_b}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    # Update the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
