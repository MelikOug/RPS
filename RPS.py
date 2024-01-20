import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, MultipleLocator


class Cell():

    def __init__(self, num, x, y):
        self.num = num
        self.state = moves[num-1]
        self.xpos = x
        self.ypos = y
        self.wins = 0
        self.draws = 0
        self.losses = 0

    def __repr__(self):
        'Access by writing population.cells[x][y] in console'
        return ('State: {}, Position: ({},{}), W/D/L: {}/{}/{}'.format(self.state, self.xpos, self.ypos, self.wins, self.draws, self.losses))

    def get_score(self):
        'Play with 8 nearest neighbours from left to right, bottom to top'
        for j in range(-1, 2):
            for i in range(-1, 2):
                if i != 0 or j != 0:
                    neighbour = population.cells[self.xpos+i][self.ypos+j]
                    if wins[self.state] == neighbour.state:
                        self.wins += 1
                    elif wins[neighbour.state] == self.state:
                        self.losses += 1
                    else:
                        self.draws += 1
        return


class Population():

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate_cells(self):
        '''
        Ensures periodic boundary conditions'
        Cell in population.cells accessed by [column][row] or [x][y]
        '''
        self.cells = [[Cell(num=np.random.randint(1, 4), x=j, y=i)
                      for i in range(width+1)] for j in range(height+1)]
        return

    def plot(self):
        fig = plt.figure(figsize=(10, 10), dpi=100)
        ax = fig.add_subplot()
        ax.tick_params(axis='both', labelsize=10, direction='out',
                       top=True, right=True, which='both')

        # Set axes limits
        ax.set_xlim(0-1.5, self.width+1.5)
        ax.set_ylim(0-1.5, self.height+1.5)

        # Set major ticks
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(1))

        # Set minor ticks with an offset of 0.5
        x_minor_ticks = np.arange(-0.5, self.width+1, 1)
        y_minor_ticks = np.arange(-0.5, self.height+1, 1)
        ax.xaxis.set_minor_locator(plt.FixedLocator(x_minor_ticks))
        ax.yaxis.set_minor_locator(plt.FixedLocator(y_minor_ticks))

        # Have grid line up with minor ticks
        ax.grid(which='minor', linewidth=2)

        for row in population.cells:
            for cell in row:
                ax.scatter(cell.xpos, cell.ypos, marker='s',
                           s=600, color=colours[cell.state])
        return


width, height = 20, 20
moves = ['Rock', 'Paper', 'Scissors']
colours = {moves[0]: 'red', moves[1]: 'blue', moves[2]: 'green'}
wins = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}

population = Population(width, height)
population.generate_cells()
population.plot()
