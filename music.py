import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piano Tiles")
background = pygame.image.load('images.png')
background = pygame.transform.scale(background, (500, 800))
# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TILE_COLOR = (0, 128, 0)

# Game variables
tile_width = WIDTH // 4
tile_height = HEIGHT // 20
tile_speed = 8
level_speed_up = 20 
title_drop_speed = 5
tiles = []
score = 0
game_over = False

# Define tile class
class Tile:
    def __init__(self):
        self.x = random.randint(0, 3) * tile_width
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, tile_width, HEIGHT // 3.5)

    def fall(self):
        self.y += tile_speed
        self.rect.y = self.y

    def reset(self):
        self.__init__()

    def draw(self):
        pygame.draw.rect(screen, TILE_COLOR, self.rect)

# Main game loop
def main():
    global score, game_over
    clock = pygame.time.Clock()
    
    # Generate initial tiles
    for _ in range(2):
        tiles.append(Tile())

    while True:
        screen.blit(background, (0, 0))
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                for tile in tiles:
                    if tile.rect.collidepoint(mouse_x, mouse_y):
                        score += 1
                        tile.reset()

        # Update tiles
        for tile in tiles:
            tile.fall()
            if tile.y > HEIGHT:
                game_over = True

        # Drawing tiles
        for tile in tiles:
            tile.draw()

        # Draw score
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(text, (10, 10))

        if game_over:
            game_over_font = pygame.font.Font(None, 74)
            game_over_text = game_over_font.render("Game Over", True, BLACK)
            game_over_score = game_over_font.render()
            screen.blit(game_over_text, (WIDTH // 6, HEIGHT // 3))
            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.quit()
            return

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()

