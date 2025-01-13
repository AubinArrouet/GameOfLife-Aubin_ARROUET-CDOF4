# Conway's Game of Life - Python Implementation

# Description

This project is a simple Python implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The game is played on a grid of cells, where each cell can be either alive (#) or dead ( ). The state of the grid evolves in discrete time steps according to a set of rules based on the number of alive neighbors of each cell.

The purpose of this project is to provide an educational demonstration of the Game of Life, showcasing how simple rules can produce complex patterns and behaviors. It is implemented in plain Python and outputs the evolving grid states to the console.

How to Run the Project

# Prerequisites:

Ensure you have Python 3.x installed on your system.

Steps:

Download or clone this repository to your local machine.

Navigate to the directory containing the script.

Run the script using the following command:

python game_of_life.py

The program will simulate 1,000 generations of the Game of Life, printing each generation to the console.

Contribution Guide

We welcome contributions to improve this project! Here's how you can get involved:

Fork the Repository:

Click the "Fork" button at the top of the repository page to create your own copy.

Clone the Repository:

Clone your forked repository to your local machine using:

git clone https://github.com/your-username/game_of_life.git

Make Your Changes:

Create a new branch for your changes:

git checkout -b feature-name

Implement your improvements or features.

Test Your Changes:

Run the script and ensure your changes work as expected.

Commit and Push:

Commit your changes with a meaningful message:

git commit -m "Add feature: description"

Push your changes to your forked repository:

git push origin feature-name

Create a Pull Request:

Navigate to the original repository and click "New Pull Request."

Provide a clear description of your changes and submit the pull request.

We appreciate all contributions, whether it's fixing a bug, improving documentation, or adding new features!

Rules of the Game

Any live cell (#) with fewer than 2 live neighbors dies (underpopulation).

Any live cell (#) with 2 or 3 live neighbors survives to the next generation.

Any live cell (#) with more than 3 live neighbors dies (overpopulation).

Any dead cell ( ) with exactly 3 live neighbors becomes a live cell (reproduction).

How It Works

Initialization

The initialize() function sets up the initial grid state. The grid is represented as a list of strings, where each string represents a row of the grid. In the provided implementation, a small pattern is pre-defined to demonstrate the evolution of the game.

Iteration

The iteration() function computes the next state of the grid based on the rules of the game. It:

Counts the number of alive neighbors for each cell using the count_alive_neighbors() function.

Applies the game rules to determine the state of each cell in the next generation.

Neighbor Counting

The count_alive_neighbors() function checks the 8 surrounding cells of a given cell to calculate the number of alive neighbors. It ensures boundary conditions are handled correctly to avoid accessing out-of-bounds cells.

Example Output

Generation 0:
                                              
                                              
                                              
                                              
                                              
                                              
                                              
                                              
                                 #            
                                ##            
                                 ##           
                                              
                                              
                                              
                                              
                                              
                                              
                                              

Generation 1:
...

Customization

You can customize the initial grid state by modifying the current_state variable in the initialize() function. Each row should be a string of equal length, with # representing live cells and spaces ( ) representing dead cells.

Requirements

Python 3.x

Limitations

The grid size is fixed and defined by the dimensions of the initial current_state list. To handle larger grids dynamically, additional modifications are required.

The game outputs to the console, which may not be ideal for visualizing complex patterns. Consider integrating a graphical interface for better visualization.

License

This code is provided as-is for educational purposes. Feel free to modify and use it as needed.

