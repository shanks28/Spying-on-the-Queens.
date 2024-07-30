# N-Queens Visualization

This project provides a visualization of various algorithms solving the N-Queens problem, implemented in Python using Pygame. The N-Queens problem is a classic problem in computer science and mathematics. It involves placing N queens on an N×N chessboard such that no two queens threaten each other.

## Features

- **Interactive Visualization**: Watch in real-time as different algorithms attempt to solve the N-Queens problem.
- **Multiple Algorithms**: Includes Backtracking, Brute Force, and Heuristic Hill Climbing algorithms.
- **Algorithm Comparison**: Easily compare the efficiency of algorithms based on execution time and steps taken.

## Algorithms

### Backtracking
Backtracking is a recursive, depth-first approach. It places a queen in a column, then moves to the next row and attempts to find a safe spot for the next queen. If no spot is safe, it backtracks to the previous row to move the queen to the next possible spot and proceeds again.

### Brute Force
The Brute Force method generates all possible configurations of queens on the board and checks each configuration to see if it's a solution. This method is not efficient for larger values of N but is included for educational purposes.

### Heuristic Hill Climbing
Heuristic Hill Climbing is an optimization technique which starts with an arbitrary solution and iteratively makes small changes to the solution, trying to improve it. In the context of the N-Queens problem, it adjusts the positions of the queens to reduce the number of conflicting queens.

## Getting Started

### Prerequisites
- Python 3.x
- Pygame
- Tkinter

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/n-queens-visualization.git
Navigate to the project directory:

bash

cd n-queens-visualization

Install the required packages:

```bash

pip install pygame tkinter

2.Running the Application:

To run the application, execute:

bash

python main.py

Replace main.py with the path to your script if different.
Usage

Upon launching, the application will prompt you to select an algorithm. The visualization will start automatically and display each step the algorithm takes to solve the N-Queens problem.
Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your features or fixes.
License

This project is licensed under the MIT License - see the LICENSE.md file for details.
Acknowledgments

    Thanks to all contributors who have helped in refining the algorithms and enhancing the application.
