
class Node:
    """
    Representation of game tree node.
    Each node holds
    1. a label
    2. a value 
    3. node type MIN or MAX
    4. list of child nodes.
    (board state, initial None value, Min or Max (whether you want this move to be a max gain or min loss), child nodes in list, last move made)
    """
    def __init__(self, board, valued, node_type, children, colmove):
        self.board = board
        self.valued = valued
        self.node_type = node_type
        self.children = children
        self.colmove = colmove


    def make_tree(self, board, mnmx, depth):
        childs = []

        if mnmx == "MAX":
            counter = "MIN"
        else:
            counter = "MAX"


        if board.win_yet or depth = 0:
            return Node(self, board, None, counter, [], board.last_column)
        else:
            for i in board.move(i):
                try:
                    childs.append(board.move(i))
                except IllegalMove:
                    pass




        mochild = []
        for j in childs:
            mochild.append(make_tree(childs[j], board.get_other_player_id(), depth - 1))


        return Node(self, board, None, counter, mochild, board.last_column)
                
        
    def is_at_depth(self, depth):

        return depth <= 0

    def tree_get_next_move(node):
        """
        Returns next moves for traversing the tree
        """

    def tree_eval(self, node):
        """
        Returns the value of a node by evalutating the board state
        is a minimax function
        """
        if node.value:
            if node.node_type == "MIN":
                return -node.value
            elif node.node_type == "MAX":
                return node.value
        else:
            return None


