# this handles the rules of the game; it will generate all possible moves and then filter the mvoes down to valid moves

from urllib.parse import non_hierarchical


class Chess:
    """hold"""

    def __init__(self):
        """hold"""


        self._board = [
        ['bp1','bp2','bp3','bp4','bp5','bp6','bp7','bp8'],
        ['wp1','wp2','wp3','wp4','wp5','wp6','wp7','wp8'],
        ['---','---','---','---','---','---','---','---'],
        ['---','---','---','---','---','---','---','---'],
        ['---','---','---','---','---','---','---','---'],
        ['---','---','---','---','---','---','---','---'],
        ['wp1','wp2','wp3','wp4','wp5','wp6','wp7','wp8'],
        ['wR1','wKn1','wB1','wK','wQ','wB2','wKn2','wR2'],
        ]

        self._white_pieces = ['wR1','wKn1','wB1','wK','wQ','wB2','wKn2','wR2','wp1','wp2','wp3','wp4','wp5','wp6','wp7','wp8']
        self._black_pieces = ['wR1','wKn1','wB1','wK','wQ','wB2','wKn2','wR2','wp1','wp2','wp3','wp4','wp5','wp6','wp7','wp8']
        self._players_turn = "white"
        return None

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

    def make_move(self,start,end):
        """hold"""
        #check to make sure correct player is playing
        #check to see if piece belongs to player 
        return True

    def undo_move(self):
        return None

    def can_castle(self):
        return None

    def get_valid_moves(self):
        return None

    def is_in_check(self):
        return None

    def get_squares_under_attack(self):
        return None

    def valid_moves(self):
        """outlines possible moves for selected piece and returns and array of valid moves"""
        #valid move for pawn- Moves forward one or two squares on first move, then only one square forward after that.  Attacks on the diagnal.  Cannot move over pieces.
        #valid move for knight- Moves two vertical and one horizontal, or one vertical and two horizontal.  Can move over pieces.  
        #valid move for bishop- Moves diagnally forward or backwards.  Cannot move over pieces. 
        #valid move for rook- Moves vertically or horizontally.  Cannot pass over pieces 
        #valid move for queen- Can move like a bishop or rook.  Cannot move over pieces.  
        #valid move for king- Can only move one square in any direction.  Cannot move over pieces
        #special cases- en passant and castling--king side and queen side
        return None

    def is_draw(self):
        """hold"""
        return None
    
    def is_win(self):
        """hold"""
        return None

    def new_game(self):
        """hold"""
        return None
        
    def get_pawn_moves(self):
        return None

    def get_rook_moves(self):
        return None

    def get_knight_moves(self):
        return None

    def get_bishop_moves(self):
        return None

    def get_king_moves(self):
        return None
    
    def get_queen_moves(self):
        return None



game = Chess()
game.print_board()

