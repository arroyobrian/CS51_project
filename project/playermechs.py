import searcher



def evaluate(board):

    chains = list(board.chain_cells(board.get_current_player_id))

    fours = filter(lambda x: len(x) = 4, chains)
    threes = filter(lambda x: len(x) = 3, chains)
    twos = filter(lambda x: len(x) = 2, chains)

    return (len(fours) * 99999999 + len(threes) * 1000 + len(twos) * 10)



def next_moves(board):
    """ Figures out legal moves the player can make from this position """
    childs = []
    for i in range(0,7):
        try:
            childs.append(board.move(i))
        except IllegalMove:
            pass
    return childs

def terminal(depth, board):
    """
    True when maximum depth is reached or
    the game is over.
    """
    return depth >= 0 or board.is_game_over


def minimax(board, depth):
    """
    Minimax search to the specified depth on the specified board.
    Returns an integer, the column number that the search reccommends to add a pieve
    """

    tree = maketree(board, "MIN")

    cvals = []
    if depth = 1:
        for i in tree.children[i]:
            cvals.append(evaluate(tree.children[i].get_board_array))
            if tree.node_type = "MIN":
                return min(cvals) 
            else:
                return max (cvals)
    elif depth = 0:
        raise Exception('Search Depth Too Far')
    else:
        for i in tree.children[i]:
            cvals.append(tree.children[i].get_board_array)
        if tree.node_type = "MIN"

        