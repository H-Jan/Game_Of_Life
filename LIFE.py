import sys
import pygame
import pygame.draw
import random



class CellularAutomata:

    def __init__(self, grid_width = 1100, grid_height = 900, Cell_Size = 10, Cell_Color_Alive = (225, 225, 225),
            Cell_Color_Dead = (100, 100, 100), maximum_fps = 15):

        pygame.init()
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.Cell_Size = Cell_Size
        self.Cell_Color_Alive = Cell_Color_Alive
        self.Cell_Color_Dead = Cell_Color_Dead
            #The above code cleans up the overall parameters of the  code. 
            #The parameters reference width, height, Cell Size (blocks) and the colors of living and dead cells (blocks)
        self.screen = pygame.display.set_mode((self.grid_width, self.grid_height))
        self.clear_screen()
        pygame.display.flip()

        self.maximum_fps = maximum_fps
            #This, as I learned, is integral to preventing the program from running all at once

        self.active_grid = 0
        self.number_columns = int(self.grid_width / self.Cell_Size)
        self.number_rows = int(self.grid_height / self.Cell_Size)
            #Initializes the grids on which our generations will be displayed
            # Moved from init grid 
            # int function to prevent float and int type error
        self.grids = []
        self.init_grid()
            #Initializes the screen
        self.set_grid()

        self.paused = False
        self.game_over = False
    
    def init_grid(self):
        def create_grid():
            rows = []
            for row_number in range(self.number_rows):
                list_of_columns = [0] * self.number_columns
                rows.append(list_of_columns)
                #This function erases the issue of having the rows non-randomly generated
                # And resulting in a long line of cells alive and dead rather than our desired pattern
            return rows
        self.grids.append(create_grid())
        self.grids.append(create_grid())
            #This double append erases our issue of an immutable tuple 
            # within our previous list and our randomization issue. 


        
    def set_grid(self, value=None, grid=0): 
            #Allows the "zeroing" of the grid with one function through set_grid
            # Now, set_grid() or set_grid(None) will be random, as with our previous function
            # set_grid with a value of 1 is all alive, and a value of 0 will kill off all cells
            # The grid = 0 will determine if active or inactive 
        for r in range(self.number_rows):
            for c in range(self.number_columns):
                    #Weird issue if reversed order for rows and columns. Need to look into
                if value is None:
                    cell_value = random.randint(0, 1)
                else: 
                    cell_value = value
                self.grids[grid][r][c] = cell_value

    


    def draw_grid(self):
            #This function draws the "cells" onto our screen. Progress.
        self.clear_screen()
        for c in range(self.number_columns):
            for r in range(self.number_rows):
                if self.grids[self.active_grid][r][c] == 1:
                    color = self.Cell_Color_Alive
                else: 
                    color = self.Cell_Color_Dead
                pygame.draw.circle(self.screen, 
                    color, 
                    (int(c * self.Cell_Size + (self.Cell_Size / 2)), 
                    int(r * self.Cell_Size + (self.Cell_Size / 2))), 
                    int(self.Cell_Size / 2), 
                    0)
                #All elements of a circle in Pygame
        pygame.display.flip()


    def clear_screen(self):
        self.screen.fill(self.Cell_Color_Dead)
            # ERROR1: This is displaying after the points on the function?
            # Error was unrelated to order of function, resolved from redefinition of grid
            #Gets rid of previous game display


    def get_cell(self, row_number, column_number):
        #This should find the state of the cell during our active grid
        try: 
            cell_value = self.grids[self.active_grid][row_number][column_number]
        except:
            cell_value = 0
        return cell_value
            # This try/except was found on Stack Overflow - learn more of function

    def cell_neighbors(self, row_index, column_index):
        #This will get number of alive/dead neighbors and determine path of next generation 
        #As per the rules of a Cellular Automata
        number_alive_neighbors = 0
        number_alive_neighbors += self.get_cell(row_index - 1, column_index -1)
        number_alive_neighbors += self.get_cell(row_index - 1, column_index)
        number_alive_neighbors += self.get_cell(row_index - 1, column_index + 1)
        number_alive_neighbors += self.get_cell(row_index, column_index - 1)
        number_alive_neighbors += self.get_cell(row_index, column_index + 1)
        number_alive_neighbors += self.get_cell(row_index + 1, column_index - 1)
        number_alive_neighbors += self.get_cell(row_index + 1, column_index)
        number_alive_neighbors += self.get_cell(row_index + 1, column_index + 1)
        #The neighboring cells of any automata grid

        if self.grids[self.active_grid][row_index][column_index] == 1:
            #This should mean if alive
            if number_alive_neighbors > 3:
                return 0
                #First rule of Game of Life, representative of overpopulation
            if number_alive_neighbors < 2:
                return 0
                #Second rule of Game of Life, representative of underpopulation
            if number_alive_neighbors == 2:
                return 1
            if number_alive_neighbors == 3:
                return 1
                #These two represent perfect conditions for growth
        elif self.grids[self.active_grid][row_index][column_index] == 0:
            #This should be if they are dead
            if number_alive_neighbors == 3:
                return 1
                #This is the condition that a untouched environmnet from dead cells sprouts new ones
        return self.grids[self.active_grid][row_index][column_index]
            

    def update_generation(self):
            # Inspect current active generation
            # update inactive grid to store next generation
            # swap out the active grid
            # Loops it to the next generation
        self.set_grid(0, self.inactive_grid())
        for r in range(self.number_rows - 1):
            for c in range(self.number_columns - 1):
                next_generation_state = self.cell_neighbors(r, c)
                self.grids[self.inactive_grid()][r][c]  = next_generation_state
        self.active_grid = self.inactive_grid()

    def inactive_grid(self):
        #This function will help with indexing the active grid, changing 0 to 1 and 1 to 0
        return (self.active_grid + 1) % 2
        #Good old simple Algebra
 
    def handle_events(self):
        for event in pygame.event.get():
                # if event is keypress of "s" then stop the game
                # if the event is keypress "r" then we will randomize grid
                # if event is keypress of "q" then we will quit
            if event.type == pygame.KEYDOWN:
                print("pressed keys")
                if event.unicode == 's':
                    print("Pausing")
                    if self.paused:
                        self.paused = False
                    else:
                        self.paused = True
                elif event.unicode == 'r':
                    print("Randomization")
                    self.active_grid = 0
                    self.set_grid(None, self.active_grid)
                    self.set_grid(0, self.inactive_grid())
                    self.draw_grid()
                elif event.unicode == 'q':
                    print("Exit")
                    self.game_over = True
            if event.type == pygame.QUIT:
                sys.exit()
        #This function was created through extensive Stack Overflow/Googling.
        # Keydown determines if a key is pressed down. 
        # pygame.Quit was taken from starter practice code on Pygame page 
        # Unicode lists individual characters of language as strings. Again, taken 
        # from Stack Overflow examples. 


    def run(self):
            #The main game loop, where everything comes together. This is indicative of the 
            # multiple passing generations with Cellular Automata
        clock = pygame.time.Clock()

        while True:
            if self.game_over:
                return
            
            self.handle_events()

            if not self.paused:
                self.update_generation()
                self.draw_grid()

            clock.tick(self.maximum_fps)
            #Timer for rate of appearnce
            


if __name__ == '__main__':
    game = CellularAutomata()
    game.run()
