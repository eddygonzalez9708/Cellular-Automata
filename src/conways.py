import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
WIN_SIZE = 500

# 1. Create an initial set of states with simiple pattern (Ex. blinker)

cur_state = [00] * 500
cur_state[10] = 1
cur_state[20] = 1
cur_state[30] = 1
cur_state[40] = 1
cur_state[50] = 1

next_state = []

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
 
  # --- Transition logic should go here

  # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
  # Any live cell with two or three live neighbours lives on to the next generation.
  # Any live cell with more than three live neighbours dies, as if by overpopulation.
  # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

  # 3. Work on rules that 1) look at all neighbors, 2) save new state in next state

  # --- Screen-clearing code goes here
 
  # Here, we clear the screen to gray. Don't put other drawing commands
  # above this, or they will be erased with this command.

  screen.fill(GRAY)

  # --- Drawing code should go here 
  cur_index = 0

  for left in range(0, 500, 42):
    for top in range(0, 500, 42):
      # 2. Draw based on the values in current state
      state = cur_state[cur_index]
      # 4. Draw based on values in next state
      if state:
        color = BLACK
      else:
        color = WHITE
      
      pygame.draw.rect(screen, color, pygame.Rect(left, top, 40, 40))
      cur_index += 1
   
  # --- Go ahead and update the screen with what we've drawn.
  pygame.display.flip()
 
  # --- Limit to 5 frames per second
  clock.tick(5)
 
# Close the window and quit.
pygame.quit()