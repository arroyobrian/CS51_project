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


def absearch(board, depth, a, b):
    """
    Minimax search to the specified depth on the specified board.
    Returns an integer, the column number that the search reccommends to add a pieve
    """

    tree = maketree(board, "MIN")

    if terminal(depth, board):
        return evaluate(tree.board.get_board_array)
    elif tree.node_type = "MAX":
        for i in tree.children[i]:
            a = (max(a, 
                absearch(tree.children[i].get_board_array, depth - 1, a, b)),
                tree.children[i]) 
            if b <= a:
                break #betacutoff, not max enough, throw out branch
            return a
    else:
        for i in tree.children[i]:
            b = (min(b, 
                absearch(tree.children[i].get_board_array, depth - 1, a, b)),
            tree.children[i])
            if b <= a:
                break #alphacutoff, not min enough, throw out branch
            return b


# sample inital absearch call:
# absearch(current_board, depth, -inf, inf)
            

        