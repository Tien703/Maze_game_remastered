# Maze Game

A simple Python-based maze game built with `pygame`. The game features randomized maze generation using the Depth-First Search (DFS) algorithm, a playable character, and an exit gate.

## Features

- **Randomized Maze Generation:** Uses a randomized DFS algorithm to create unique mazes every time.
- **Animation Mode:** Watch the maze being generated in real-time.
- **Playable Character:** Move through the maze to find the exit.
- **Responsive Design:** Resizable game window and adjustable tile sizes.
- **Win Condition:** Reaching the exit gate (blue) wins the game.

## Requirements

- Python 3.x
- `pygame`
- `numpy`

## Installation

1.  **Clone the repository (or download the files):**
    ```bash
    git clone <repository-url>
    cd maze-game
    ```

2.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Play

Run the game using the following command:

```bash
python game.py
```

### Controls

- **`1`**: Start the game immediately with a pre-generated maze.
- **`2`**: Watch the maze generation animation before playing.
- **`R`**: Reset and generate a new maze.
- **Arrow Keys (Up, Down, Left, Right)**: Move the player through the maze.
- **Close Window**: Quit the game.

### Objective

Navigate your player (represented by the character/square) from the starting position to the **Exit Gate** to win the game.

## Project Structure

- `game.py`: Main entry point of the game.
- `src/system/`: Core logic including Player, Maze, and configuration.
- `generator/`: Algorithms for maze generation (e.g., Randomized DFS).
- `requirements.txt`: List of required Python packages.
