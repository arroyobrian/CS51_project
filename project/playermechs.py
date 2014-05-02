import searcher

def evaluate(board):
    """
    this is the minimax function
    it evaluates a board based on link length
    and board centricity
    """
    me = board.get_current_player_id
    enemy = board.get_other_player_id

    score = 0

    # this is a smarter evaluate: by subtracting the number of cells 
    # in the board from a winning board or adding to a losing board,
    # the AI tries to win as fast as possible or 
    # lose as slowly as possible
    # it also prefers to put tokens not on the sides, where there is
    # more room and greater ability to make plays

    if board.longest_tokechain_from_anywhere(me) >= 4:
        score = 5000 - board.cell_count
    elif board.longest_tokechain_from_anywhere(enemy) >= 4:
        score = -5000 + board.cell_count
    else:
        mechains = list(set(board.chain_cells(me)))
        mecenterchains = filter(lambda (x,y): y == 0 or y == board.width - 1, chains)
        for length in range(1,3):
            temp = filter(lambda x: len(x) == length)
            score = score + (len(temp) * length)

        yochains = list(set(board.chain_cells(enemy)))
        yocenterchains = filter(lambda (x,y): y == 0 or y == board.width - 1, chains)
        for length in range(1,3):
            temp = filter(lambda x: len(x) == length)
            score = score - (len(temp) * length)

    return score


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
    elif tree.node_type == "MAX":
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
# absearch(current_board, depth, (-inf, None), (inf, None))
            

        
