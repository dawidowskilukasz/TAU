import random
import sys

class MazeGame:
    def __init__(self, size=5, obstacles=None, start=None, end=None):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.start = (random.randint(0, size - 1), 0)
        self.end = (random.randint(0, size - 1), size - 1)

        self.current_position = self.start
        self.board[self.start[0]][self.start[1]] = 'S'
        self.board[self.end[0]][self.end[1]] = 'E'

        self.obstacles = obstacles if obstacles is not None else self.generate_obstacles()
        for obstacle in self.obstacles:
            if obstacle not in {self.start, self.end}:
                self.board[obstacle[0]][obstacle[1]] = 'X'

    def generate_obstacles(self):
        obstacles = []
        for _ in range(self.size):
            obstacle = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            if obstacle not in obstacles and obstacle not in {self.start, self.end}:
                obstacles.append(obstacle)
        return obstacles

    def display(self):
        for row in self.board:
            print(' '.join(row))
        print("\n")

    def move(self, direction):
        x, y = self.current_position
        if direction == 'w':
            x -= 1
        elif direction == 's':
            x += 1
        elif direction == 'd':
            y += 1
        elif direction == 'a':
            y -= 1
        if 0 <= x < self.size and 0 <= y < self.size:
            if self.board[x][y] != 'X':
                self.board[self.current_position[0]][self.current_position[1]] = '.'
                self.current_position = (x, y)
                self.board[x][y] = 'S'
            else:
                print("!! You cannot move onto an obstacle.\n")
        else:
            print("!! You cannot leave the board.\n")

    def play(self):
        print("Objective: reach E try to avoid X,\nInstructions: Move with w, s, a, d, confirm choice with ENTER\n"
              "Quit game with q and confirm with ENTER")
        self.display()

        while True:
            if self.current_position == self.end:
                print("\nCongratulations! You successfully completed the maze!\n")
                break
            direction = input("Which direction would you like to go? ")
            if direction.lower() == 'q':
                print("\nYou exited the game.\n")
                break
            self.move(direction.lower())
            self.display()

if len(sys.argv) > 1:
    if sys.argv[1] == 'start':
        game = MazeGame()
        game.play()
