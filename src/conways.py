import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
WIN_SIZE = 500
AREA = 40

# 1. Fill current state with random states

# Stretch 1: Allow users to choose between several predefined initial states.
# Stretch 2: Allows users to set the number of squares.

curr_state = [None] * WIN_SIZE

for i in range(len(curr_state)):
  curr_state[i] = random.randint(0, 1)

next_state = []

pygame.init()
 
# Set the width and height of the screen [width, height]

size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title

pygame.display.set_caption("Conway's Game of Life")
 
# Loop until the user clicks the close button.

done = False
 
# Used to manage how fast the screen updates.

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

  # 3. Work on rules that 
  # 3.1) look at all neighbors
  # 3.2) save new state in next state

  # --- Screen-clearing code goes here
 
  # Here, we clear the screen to gray.
  # Don't put other drawing commands above this, or they will be erased with this command.

  screen.fill(GRAY)

  # --- Drawing code should go here 

  curr_index = 0
  width = WIN_SIZE // AREA

  if len(next_state):
    state = next_state[:]
  else:
    state = curr_state[:]
  
  next_state = []

  for left in range(0, 500, AREA + 2):
    for top in range(0, 500, AREA + 2):
      # 2. Draw based on the values in current state
      status = state[curr_index]

      # 1. Calculate the number of live neighbors
      # 1.2 Find the indexes of all neighbors

      # Example:
      ##########
      '''
      -------
      |0|3|6|
      |1|4|7|
      |2|5|8|
      -------
      '''
      
      neighbors = {
        'n': curr_index - 1,
        'e': curr_index + width,
        'w': curr_index - width,
        's': curr_index + 1,
        'ne': curr_index - 1 + width,
        'nw': curr_index - 1 - width,
        'se': curr_index + 1 + width,
        'sw': curr_index + 1 - width
      }

      column_one = curr_index in range(0, width)
      row_one = curr_index % width == 0
      last_column = curr_index in range(width * (width - 1), width ** 2)
      last_row = (curr_index + 1) % width == 0

      if column_one and row_one:
        del neighbors['n']
        del neighbors['w']
        del neighbors['ne']
        del neighbors['nw']
        del neighbors['sw'] 
      elif column_one and last_row:
        del neighbors['s']
        del neighbors['w']
        del neighbors['nw']
        del neighbors['sw']
        del neighbors['se']
      elif last_column and row_one:
        del neighbors['n']
        del neighbors['e']
        del neighbors['ne']
        del neighbors['nw']
        del neighbors['se']
      elif last_column and last_row:
        del neighbors['s']
        del neighbors['e']
        del neighbors['ne']
        del neighbors['se']
        del neighbors['sw']
      elif column_one: 
        del neighbors['w']
        del neighbors['nw']
        del neighbors['sw']
      elif row_one: 
        del neighbors['n']
        del neighbors['ne']
        del neighbors['nw']
      elif last_column:
        del neighbors['e']
        del neighbors['ne']
        del neighbors['se']
      elif last_row:
        del neighbors['s']
        del neighbors['se']
        del neighbors['sw']
      
      live_neighbors = 0

      for key in neighbors:
        index = neighbors[key]

        if state[index] == 1:
          live_neighbors += 1
      
      if live_neighbors < 2 or live_neighbors > 3:
        next_state.append(0)
      elif status == 0 and live_neighbors == 2:
        next_state.append(0)
      else:
        next_state.append(1)
      
      # 4. Draw based on values in next state
      if status:
        color = BLACK
      else:
        color = WHITE
      
      pygame.draw.rect(screen, color, pygame.Rect(left, top, AREA, AREA))
      curr_index += 1
   
  # --- Go ahead and update the screen with what we've drawn.
  pygame.display.flip()
 
  # --- Limit to 5 frames per second
  clock.tick(5)
 
# Close the window and quit.
pygame.quit()