import pygame
import random
import sys

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
TILE_WIDTH = SCREEN_WIDTH // 4
TILE_HEIGHT = 100
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TILE_COLOR = (49, 140, 231)
HIT_COLOR = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Piano Tiles")
clock = pygame.time.Clock()

# Tile Class
class Tile:
    def __init__(self, column):
        self.rect = pygame.Rect(column * TILE_WIDTH, 0, TILE_WIDTH, TILE_HEIGHT)

    def move(self):
        self.rect.y += 5  # Move tile downwards

    def draw(self, surface):
        pygame.draw.rect(surface, TILE_COLOR, self.rect)

# Game Variables
tiles = []
score = 0
game_over = False

def reset_game():
    global tiles, score, game_over
    tiles = []
    score = 0
    game_over = False

# Main Game Loop
while True:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos
            column = mouse_x // TILE_WIDTH
            
            # Check if a tile was clicked
            for tile in tiles:
                if tile.rect.collidepoint(event.pos):
                    tiles.remove(tile)
                    score += 1
                    break

    if not game_over:
        # Add new tiles
        if random.randint(1, 20) == 1:  # Randomly spawn tiles
            tiles.append(Tile(random.randint(0, 3)))

        # Move existing tiles
        for tile in tiles:
            tile.move()
            if tile.rect.top > SCREEN_HEIGHT:  # Check for game over condition
                game_over = True

        # Redraw the screen
        screen.fill(WHITE)
        for tile in tiles:
            tile.draw(screen)

        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    else:
        # Game Over Screen
        screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        end_text = font.render('Game Over', True, BLACK)
        score_text = font.render(f'Score: {score}', True, BLACK)
        restart_text = font.render('Click to Restart', True, BLACK)

        screen.blit(end_text, (SCREEN_WIDTH // 2 - end_text.get_width() // 2, SCREEN_HEIGHT // 2 - end_text.get_height()))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + end_text.get_height()))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + end_text.get_height() + score_text.get_height() + 10))

        pygame.display.flip()

        # Wait for click to restart
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                reset_game()
