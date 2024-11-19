import pygame
import random

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
TILE_WIDTH = WINDOW_WIDTH // 4
TILE_HEIGHT = WINDOW_HEIGHT // 6
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Piano Tiles Game")
clock = pygame.time.Clock()

# Game Variables
tiles = []
score = 0
game_over = False

# Function to create tiles
def create_tile():
    tile_x = random.randint(0, 3) * TILE_WIDTH
    return {'x': tile_x, 'y': 0}

# Function to draw the tiles
def draw_tiles():
    for tile in tiles:
        pygame.draw.rect(screen, BLACK, (tile['x'], tile['y'], TILE_WIDTH, TILE_HEIGHT))

# Main game loop
def run_game():
    global score, game_over
    tiles.append(create_tile())
    last_tile_time = pygame.time.get_ticks()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and len(tiles) > 0 and tiles[0]['x'] == 0 * TILE_WIDTH:
                    score += 1
                    tiles.pop(0)
                elif event.key == pygame.K_2 and len(tiles) > 0 and tiles[0]['x'] == 1 * TILE_WIDTH:
                    score += 1
                    tiles.pop(0)
                elif event.key == pygame.K_3 and len(tiles) > 0 and tiles[0]['x'] == 2 * TILE_WIDTH:
                    score += 1
                    tiles.pop(0)
                elif event.key == pygame.K_4 and len(tiles) > 0 and tiles[0]['x'] == 3 * TILE_WIDTH:
                    score += 1
                    tiles.pop(0)
                else:
                    # If the player pressed a wrong key
                    game_over = True
            
        screen.fill(WHITE)

        # Move tiles down
        for tile in list(tiles):
            tile['y'] += 5
            if tile['y'] > WINDOW_HEIGHT:
                game_over = True

        # Draw the tiles
        draw_tiles()
        
        # Create a new tile every half second
        if pygame.time.get_ticks() - last_tile_time > 500:
            tiles.append(create_tile())
            last_tile_time = pygame.time.get_ticks()

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    print(f"Game Over! Your score: {score}")
    pygame.quit()

if __name__ == "__main__":
    run_game()