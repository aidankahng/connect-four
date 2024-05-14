import numpy

# Game board is 7 across and 6 tall
# Each column can be stored as an array along with a counter showing how many pucks have been played in it
# Each move will alternate colors
# Make / Train an AI to play the game later

class ConnectFour:
    def __init__(self):
        self.board = Board()
    
    def start_game(self):
        print("Welcome to Connect 4!")
        print("Here is the initial Board")
        self.board.show_board()
        while not self.board.finished:
            print(f"It is currently Player {self.board.player}'s turn")
            str_input = input(f"Which column would you like to play on? [1-7] ")
            if str_input.isdigit():
                int_input = int(str_input)
                if int_input > 0 and int_input < 8:
                    self.board.play(int_input-1)
                else:
                    print("Not in valid range [1-7]")
            else:
                print("Invalid input...")
        print("Program complete.")



class Board:
    def __init__(self):
        self.b = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        # use .count(0) and indexing to replace correct value
        self.player = 1
        self.finished = False

    def change_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def show_board(self):
        br = numpy.transpose(self.b)
        print("*******BOARD*******")
        for row in range(1, len(br)+1):
            for col in br[len(br)-row]:
                spaces = 2
                print(col, end=" " * spaces)
            print()
        print()
        print()
        

    # Attempts to play player's token on a given column
    # Returns True if success, False if failed to place there
    def play(self, col):
        if self.finished:
            print("Game is already finished")
            print(f"Unable to play {col} for player {self.player}")
            return False
        c = self.b[col].count(0)
        if c > 0:
            self.b[col][6-c] = self.player
            self.change_player()
            self.show_board()
            self.check_win()
            return True
        return False
    
    # Checks all possible win conditions
    def check_win(self):
        if self.check_cols() or self.check_rows() or self.check_diags():
            self.finished = True
            print("GAME OVER!")
        elif not self.has_empty_space():
            print("No One Wins!")

    
    def check_cols(self):
        for col in self.b:
            for i in range(3):
                mult_check = col[i] * col[i+1] * col[i+2] * col[i+3]
                if self.check_helper(mult_check):
                    print(f"4 connected in a column")
                    return True
        return False
    
    def check_rows(self):
        for j in range(6):
            for i in range(4):
                mult_check = self.b[i][j] * self.b[i+1][j] * self.b[i+2][j] * self.b[i+3][j]
                if self.check_helper(mult_check):
                    print(f"4 connected in a row")
                    return True
        return False
    
    def check_diags(self):
        for i in range(4):
            for j in range(3):
                mult_check = self.b[i][j] * self.b[i+1][j+1] * self.b[i+2][j+2] * self.b[i+3][j+3]
                if self.check_helper(mult_check):
                    print(f"Connected Diagonally!")
                    return True
                mult_check = self.b[i][j+3] * self.b[i+1][j+2] * self.b[i+2][j+1] * self.b[i+3][j]
                if self.check_helper(mult_check):
                    print(f"Connected Diagonally!")
                    return True
        return False

    # Checks if value is an end condition
    def check_helper(self, mult_check):
        if mult_check == 1:
            print("Player 1 has won the game")
            return True
        elif mult_check == 16:
            print("Player 2 has won the game")
            return True
        else:
            return False
    
    def has_empty_space(self):
        for col in self.b:
            for item in col:
                if item == 0:
                    return True
        return False

# This class will look at a board, and play a move
# 

# To run the loop
if __name__ == "__main__":
    haha = ConnectFour()
    haha.start_game()