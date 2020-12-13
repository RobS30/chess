
class Chess:
    """hold"""

    def __init__(self):
        """hold"""
        self._board = [] #creates a blank array to hold a copy of the board 
        for i in range(8):
            self._board.append([])
            for j in range(8):
                self._board[i].append([0])
        self._white_pieces = [w.R1,w.Kn1,w.B1,w.K,w.Q,w.B2,w.Kn2,w.R2,w.p1,w.p2,w.p3,w.p4,w.p5,w.p6,w.p7,w.p8]
        self._black_pieces = [b.R1,b.Kn1,b.B1,b.K,b.Q,b.B2,b.Kn2,b.R2,b.p1,b.p2,b.p3,b.p4,b.p5,b.p6,b.p7,b.p8]

    
    def print_board(self):
        """used for debugging- prints the board to console alng with key variable values"""
        current_board = self._board
        print(current_board[0])
        print(current_board[1])
        print(current_board[2])
        print(current_board[3])
        print(current_board[4])
        print(current_board[5])
        print(current_board[6])
        print(current_board[7])
        return True


game = Chess()
print(game.print_board())
