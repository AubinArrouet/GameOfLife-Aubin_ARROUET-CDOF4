def initialize():
    """
    Initializes the Game of Life simulation with a predefined starting state.
    Prints each generation's grid to the console for 1,000 generations.

    The grid is a list of strings where:
    - '#' represents a live cell
    - ' ' represents a dead cell
    """
    current_state = [
        '                                              ',
        '                                              ',
        '                                              ',
        '                                              ',
        '                                              ',
        '                                              ',
        '                                              ',
        '                                              ',
        '                                 #            ',
        '                                ##            ',
        '                                 ##           ',
        '                                              ',
        '                                              ',
        '                                              ',
        '                                              ',
        '                                              ',
        '                                              ',
        '                                              '
    ]

    for generation in range(1000):  # Stops at 1,000 generations
        print(f"Generation {generation}:")
        for row in current_state:
            print(row)
        print("\n")
        current_state = iteration(current_state)


def iteration(current_state):
    """
    Computes the next generation of the grid based on the current state.

    Args:
        current_state (list of str): The current state of the grid.

    Returns:
        list of str: The next state of the grid after applying the Game of Life rules.
    """
    rows = len(current_state)
    cols = len(current_state[0])
    new_state = []

    for i in range(rows):
        new_row = ''
        for j in range(cols):
            alive_neighbors = count_alive_neighbors(current_state, i, j,rows,cols)
            if current_state[i][j] == '#' and alive_neighbors in [2, 3]:
                new_row += '#'
            elif current_state[i][j] == ' ' and alive_neighbors == 3:
                new_row += '#'
            else:
                new_row += ' '
        new_state.append(new_row)

    return new_state 

def count_alive_neighbors(current_state, x, y,rows,cols):
    """
    Counts the number of live ('#') neighbors around a given cell.

    Args:
        current_state (list of str): The current state of the grid.
        x (int): The row index of the cell.
        y (int): The column index of the cell.
        rows (int): Total number of rows in the grid.
        cols (int): Total number of columns in the grid.

    Returns:
        int: The number of live neighbors around the cell.
    """
    alive_neighbors = 0
    uselesss_variable=None #this is a useless variable to remove, it is put so that I can test issues

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue

            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and current_state[nx][ny] == '#':
                alive_neighbors += 1

    return alive_neighbors

if __name__ == "__main__":
    initialize()
