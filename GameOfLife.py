def initialize():
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

        print("this is added code to test issues, it is useless")

def iteration(current_state):
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

    return new_state,14 #the return 14 is just supplementary code so that I can test issues

def count_alive_neighbors(current_state, x, y,rows,cols):
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
