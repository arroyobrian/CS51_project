
class NonexistentMove(Exception):
    """ if player makes an illegal request """
    """ we will need a way to store the offending
        column (and possibly the board itself) """


    
class ConnectFourBoard(board_matrix, current_player):
    """ Store a Connect-Four Board

    Board columns fill from the bottom (ie., row 6).
    """

    # The horizontal width of the board
    board_width = 7
    # The vertical height of the board
    board_height = 6

    
    def __init__():
        """ new ConnectFourBoard
        """

   
    def get_current_player_id():
        """ id of the player whose turn it is """

    def get_other_player_id():
        """ id of the opponent of the player who should be moving now """
   
    def top_elt_column(column):
        """
        id# of player who is in the topmost token in the column.
        Return 0 if the column is empty.
        So a way to link a column with a player is needed. maybe
        if we create a column id for each column and store the information
        as an array?"""

    def height_column(column):
        """
        Return the index of the first cell in the specified column that is filled.
        """

    def cell(column, row):
        """
        Get the id# of the player owning the taker in the specified cell.
        Return 0 if it is unclaimed.
        """
    
    def move(column):
        """
        Make the move as the player.
        Raise 'InvalidMoveException' if move is illegal.
        Takes in the column the player wants to change and 
        their id to store their move
        """
        
    def win():
        """
        Return the id# of winner.
        Return 0 if it has not yet been won.
        """

    def game_over():
        """ Return True if the game has been won, False otherwise """


 
    

    
