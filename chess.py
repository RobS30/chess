
class Chess:
    """hold"""

    def __init__(self):
        """hold"""
        self._board = [] #creates a blank array to hold a copy of the board 
        for i in range(8):
            self._board.append([])
            for j in range(8):
                self._board[i].append([0])
        self._players_turn = []
        self._white_pieces = [w_R1,w_Kn1,w_B1,w_K,w_Q,w_B2,w_Kn2,w_R2,w_p1,w_p2,w_p3,w_p4,w_p5,w_p6,w_p7,w_p8]
        self._black_pieces = [w_R1,w_Kn1,w_B1,w_K,w_Q,w_B2,w_Kn2,w_R2,w_p1,w_p2,w_p3,w_p4,w_p5,w_p6,w_p7,w_p8]
        return True
    
    def make_move(self,start,end):
        """hold"""
        #check to make sure correct player is playing
        #check to see if piece belongs to player 
        return True

    def is_legal(self):
        """hold"""
        #valid move for pawn
        #valid move for knight
        #valid move for bishop
        #valid move for rook
        #valid move for queen
        #valid move for king
        return True

    def is_draw(self):
        """hold"""
        return True
    
    def is_win(self):
        """hold"""
        return True

    def new_game(self):
        """hold"""
        return True

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
game.print_board()
