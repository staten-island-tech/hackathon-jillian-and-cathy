Briefly describe the problem you're trying to solve or the task you're working on.

1. I want to add a background image to my python game
2. I need to make the background music stop when the game ends
3. Initally, the background image of my game was glitching and I was trying to fix it.
## 2. **Initial Approach/Code**

Describe the initial approach you took to solving the problem. If you started writing code, include it here.

1. background = pygame.image.load("images.png")
2. pygame.mixer.music.stop
- What was your plan for solving the problem?
- Did you have any initial thoughts or strategies before using ChatGPT?



## 3. **Interaction with ChatGPT**

### Questions/Requests to ChatGPT
Write down the questions or requests you made to ChatGPT. 
Also include what code from ChatGPT you are unsure of and craft a question that asks for further clarification. 

1. I asked ChatGPT how to fix my code in order for it to display an image 
2. I put my code into ChatGPT, asked how to fix it and why the code wasn't intially working
3. I put my whole code into ChatGPT and asked why the background image was glitching.






## 4. **ChatGPT's Suggestions/Code Changes**

Record the code or suggestions ChatGPT provided. Include any changes or improvements ChatGPT suggested and how it influenced your approach.


1. background = pygame.image.load('background.jpg') #replace with your image file
    background = pygame.transform.scale(background, (HEIGHT, WIDTH))
2. pygame.mixer.music.stop()

- What was ChatGPT's solution or suggestion?
- How did it differ from your original approach?

1. ChaptGPT's solution was to scale my image so it fit the pygame screen, it differed from my approach because
   I initally only wrote the first line of code and disregarded the image transformation scaling portion.
2. ChatGPT's solution was to actually call the function by adding the parentheses at the end
3. ChatGPT told me that I should call pygame.display.flip() AFTER all drawing operations are completed.
## 5. **Reflection on Changes**

Reflect on the changes made to your code after ChatGPT's suggestions. Answer the following questions:

- Why do you think ChatGPT's suggestions are helpful or relevant?
- Did the suggestions improve your code? How?
- Did you understand why the changes were made, or are you still uncertain about some parts?

1. I think ChatGPT's suggestions are helpful because it looks for things that are missing or code errors that aren't obvious to the human eye, 
   it is also a more effficent way of correcting stuff.
2. ChatGPT's suggestions were helpful because I missed a very simple step in my code that is necessary to make it run.
3. The suggestions were extremely helpful because I would have never though of moving the line of code, instead, I thought there was an issue in the code itself or I accidentally left an unecessary part.

## 6. **Testing and Results**

After making the changes, did you test your code? What were the results?

- Did you run any tests (e.g., unit tests, edge cases)?
- Did the code work as expected after incorporating ChatGPT's changes?
- Did you encounter any bugs or issues during testing?

1. After recieving help from chatGPT, I put the lines of code into my own, for example:
background = pygame.image.load('images.png')
background = pygame.transform.scale(background, (500, 800))
My code did end up working after a few adjustments to the image scaling.

2. After using chatGPT, I added the parentheses to the end of my code and it worked:
pygame.mixer.music.stop()

3. After using chatGPT, i moved pygame.display.flip() under if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: instead of while True:



## 7. **What Did You Learn?**

In this section, reflect on what you learned from this coding session. Did you gain any new insights, or were there areas you still struggled with? 

1. During this process, I learned to precisely recognize every factor when coding, in this case, image scaling/transforming which is important when creating a game.
2. Although this was a very small and silly mistake that I could have solved myself, I learned that I have to remember to call a function using parentheses in order for it to run.
3. From this I learned that there are small simple factors that could alter the code when running and I should be closely comprehending what is happening in my code during the coding process.