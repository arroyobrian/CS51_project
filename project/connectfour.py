
class NonexistentMove(Exception):
    """ if player makes an illegal request """
    """ we will need a way to store the offending
        column (and possibly the board itself) """


class IllegalMove(Exception):
    """
    Move is not allowed by standard rules of 
    connect Connect-Four
    """


    
class ConnectFourBoard:
    """ Store a Connect-Four Board

    Board columns fill from the bottom (ie., row 6).
    """

    # The horizontal width of the board
    board_width = 7
    # The vertical height of the board
    board_height = 6

    
    def __init__(self, board_array = None, last_column = None, current_player = 1, last_move = -1):
        """ new ConnectFourBoard
            takes in a actual board (as lists of lists or tuples)
            winning state (initially none),
            the first player to move,
            the last changed column (to be able to undo moves and check for victory)
            we should make the board immutable so that our search tree will use copies of the board
            instead of modifying the board in memory
        """

        if board_array == None:
            self._board_array = ((0,) * self.board_width) * self.board_height

        self.current_player = current_player

   
    def get_current_player_id():
        return current_player

    def get_other_player_id():
        if current_player == 1:
            return 2
        else:
            return 1
   
    def top_elt_column(self,column):
        """
        id# of player who is in the topmost token in the column.
        Return 0 if the column is empty.
        So a way to link a column with a player is needed. maybe
        if we create a column id for each column and store the information
        as an array?"""

        for row in self[column]:
            if row[column] != 0:
                return row[column]

        return 0

    def height_column(column):
        """
        Return the index of the first cell in the specified column that is filled.
        """

        for row in self[column]:
            if row[column] = 0:
                return row - 1

        return self.board_height


    def cell(self, column, row):
        """
        Get the id# of the player owning the taker in the specified cell.
        Return 0 if it is unclaimed.
        """
        self._board_array[row][column]
    
    def move(column):
        """
        Make the move as the player.
        Raise 'InvalidMoveException' if move is illegal.
        Takes in the column the player wants to change and 
        their id to store their move
        a list of lists stores the board as a list of the rows
        but move inserts by columns, so we need to take a 
        """
        
    def win():
        """
        Return the id# of winner.
        Return 0 if it has not yet been won.
        """

    def game_over():
        """ Return True if the game has been won, False otherwise """


 
    

    
