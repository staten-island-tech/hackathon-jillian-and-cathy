
# ChatGPT Coding Diary

## Project Name: Piano Tiles Game

### Date: 11/22/24

---
1. I need to write a code to add Jingle Bells music to a piano tiles game

Initial approach:
pygame.mixer.music.load('jingle-bells-music-holiday-christmas-new-year-background-intro-theme-265845.mp3')
pygame.mixer.music.play(-1)

I asked "Whats wrong with this code? [insert code]"
ChatGPT sugggested to initialize the mixer.
This worked because if the mixer is not initialized, the mixer will not be able to control the source of the audio.
The result was:
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('jingle-bells-music-holiday-christmas-new-year-background-intro-theme-265845.mp3')
pygame.mixer.music.play(-1)

I learned that when using an audio source, you have to initialize the mixer, otherwise there will be an error.

2. I need to write a code to add a christmas background to the game.

Initial approach:
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

background_image = pygame.image.load('pianotilesbackground.jpg')  # Add your own background image
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

I asked "What's wrong with this code? [insert code]"
ChatGPT suggested that the names for width and height were not the same so the code would not work.
It also suggested that the width and height might not have matched the images width and height
This worked because if names for the width and height are not the same, they will not be known as the same thing, therefore the code will not work
And if the images dimensions do not fit the dimensions written, the image will not fit.
The result was:
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 856

background_image = pygame.image.load('pianotilesbackground.jpg')  # Add your own background image
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

I learned that when uploading a background image in a code, you cannot make mistakes such as writing the wrong names for dimensions.
You also cannot expect the background image to fit into any dimensions, you have to find the exact dimensions of the image and write it.

3. I need to write a code to pause and unpause the music.

I asked "How to pause the music [insert code]"
ChatGPT wrote a slightly different code in certain areas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

        if tile.rect.top > SCREEN_HEIGHT:  # Check for game over condition
                game_over = True
                pygame.mixer.music.pause()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            reset_game()
            pygame.mixer.music.unpause()

I learned how to modify certain areas in a code to pause and unpause

