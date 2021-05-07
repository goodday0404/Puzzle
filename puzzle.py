import heapq


class State:
    rows = 5
    colums = 4

    def __init__(self, state):
        self.state = state
        self.parent = None
        self.f = 0
        self.g = 0
        self.h = 0
        self.row_pos_2x2 = -1
        self.col_pos_2x2 = -1
        self.empty1_pos = -1
        self.empty2_pos = -1
        self.init_state()

    def __repr__(self):
        return f'f({self.state}) = {self.f}'

    def __str__(self):
        print('board:')
        self.print_board()
        print()
        parent = self.parent.state if self.parent else 'None'
        return f'state: {self.state}\nparent state: {parent}\nf = {self.f}\ng = {self.g}\nh = {self.h}\nempty_pos1 = {self.empty1_pos}\nempty_pos2 = {self.empty2_pos}\n2x2_row = {self.row_pos_2x2}\n2x2_col = {self.col_pos_2x2}\n'

    def __lt__(self, other):
        return self.f < other.f

    def init_state(self):
        pos_2x2_left_top = self.find_2x2piece()
        self.row_pos_2x2 = pos_2x2_left_top // 4
        self.col_pos_2x2 = pos_2x2_left_top % 4
        self.empty1_pos, self.empty2_pos = [i for i, val in enumerate(self.state) if val == '0']

    def find_2x2piece(self):
        return self.state.index('1')

    def find_empty_cells(self):
        return [i for i, val in enumerate(self.state) if val == '0']

    def set_parent(self, parent):
        self.parent = parent

    def set_f(self, value):
        self.f = value

    def set_g(self, value):
        self.g = value

    def set_h(self, value):
        self.h = value

    def set_row_pos_2x2(self, row):
        self.row_pos_2x2 = row

    def set_col_pos_2x2(self, col):
        self.col_pos_2x2 = col

    def set_empty1(self, pos):
        self.empty1_pos = pos

    def set_empty2(self, pos):
        self.empty2_pos = pos

    def print_board(self):
        i = 0
        for s in self.state:
            if i >= State.colums:
                print()
                i = 0
            print(s, end='')
            i += 1
        print('\n')

    def write_state(self, outputfile):
        i = 0
        for s in self.state:
            if i >= State.colums:
                outputfile.write('\n')
                i = 0
            outputfile.write(s)
            i += 1
        outputfile.write('\n\n')


class Frontier:
    def __init__(self):
        self.frontier = []

    def push(self, state):
        heapq.heappush(self.frontier, (state.f, state))

    def pop(self):
        next_expand = heapq.heappop(self.frontier)
        return next_expand

    def is_empty(self):
        return len(self.frontier) == 0


class LIFO:
    def __init__(self):
        self.frontier = []

    def push(self, state):
        self.frontier.append(state)

    def pop(self):
        return self.frontier.pop()

    def is_empty(self):
        return len(self.frontier) == 0


def get_coordinate(n):
    row = n // 4
    col = n % 4
    # print(row, col)
    return [row, col]


def coordinate_to_index(p):
    return p[0] * 4 + p[1]


def str_to_list(str):
    lst = []
    lst[:0] = str
    return lst

    
def read_puzzle(id):
    state = ''
    with open(id) as file:
        for cnt, line in enumerate(file):
            line = line[:State.colums]
            state += line
            cnt += 0
    file.close()
    empty_pos1 = state.index('0')
    empty_pos2 = state.index('0', empty_pos1 + 1)
    init_state = State(state)
    init_state.set_empty1(empty_pos1)
    init_state.set_empty2(empty_pos2)
    return init_state


def is_goal(state):
    return state.state[13] == '1' and state.state[14] == '1' and \
        state.state[17] == '1' and state.state[18] == '1'


def create_successor(parent, successor_state):
    successor = State(successor_state)
    successor.set_parent(parent)
    cost_successor = get_cost(parent) + 1
    successor.set_g(cost_successor)
    h_value_successor = get_heuristic(successor)
    successor.set_h(h_value_successor)
    successor.set_f(cost_successor + h_value_successor)
    return successor
       

def get_successors(state):
    # get positions of empty cells
    empty1 = get_coordinate(state.empty1_pos)
    empty2 = get_coordinate(state.empty2_pos)
    # find neighbours of empty cells
    empty1_neighbours = find_neighbours(state, empty1)
    empty2_neighbours =find_neighbours(state, empty2)
    for successor_str in empty1_neighbours:
        try:
            empty2_neighbours.remove(successor_str)
        except:
            pass
    empty1_neighbours.extend(empty2_neighbours)
    successors = []
    for successor_str in empty1_neighbours:
        successor = create_successor(state, successor_str)
        successors.append(successor)  
    return successors


def find_neighbours(state, empty_cell):
    row = empty_cell[0]
    col = empty_cell[1]
    neighbours = []
    if row > 0:
        # check up
        neighour = get_new_state(state, row - 1, col, row, col)
        if neighour:
            neighbours.append(neighour)
    if row < 4:
        #check down
        neighour = get_new_state(state, row + 1, col, row, col)
        if neighour:
            neighbours.append(neighour)
    if col > 0:
        # check left
        neighour = get_new_state(state, row, col - 1, row, col)
        if neighour:
            neighbours.append(neighour)
    if col < 3:
        # check right
        neighour = get_new_state(state, row, col + 1, row, col)
        if neighour:
            neighbours.append(neighour)
    return neighbours


def swap_position(pieces, row, col, erow, ecol):
    index_piece = coordinate_to_index([row,col])
    index_empty = coordinate_to_index([erow,ecol])
    temp = pieces[index_piece]
    pieces[index_piece] = pieces[index_empty]
    pieces[index_empty] = temp
   

def movwe_2x2_vertical(state, row, col, erow, ecol, direction):
    successor = str_to_list(state.state)
    vertical_neighbour_col = -1
    row_to_swap = row + 1 if direction == 'u' else row - 1
    if col > 0 and is_same_piece(state, row, col-1, 1):
        vertical_neighbour_col = col-1
    else:
        vertical_neighbour_col = col+1
    swap_position(successor, row_to_swap, col, erow, ecol)
    swap_position(successor, row_to_swap, vertical_neighbour_col, erow, vertical_neighbour_col)
    return "".join(successor)


def movwe_2x2_horizontal(state, row, col, erow, ecol, direction):
    successor = str_to_list(state.state)
    vertical_neighbour_row = -1
    col_to_swap = col + 1 if direction == 'l' else col - 1
    if row > 0 and is_same_piece(state, row-1, col, 1):
        vertical_neighbour_row = row-1
    else:
        vertical_neighbour_row = row+1
    swap_position(successor, row, col_to_swap, erow, ecol)
    swap_position(successor, vertical_neighbour_row, col_to_swap, vertical_neighbour_row, ecol)
    return "".join(successor)


def movwe_2x1_vertical(state, row, col, erow, ecol, direction,piece):
    successor = str_to_list(state.state)
    piece = int(piece)
    if direction == 'd':
        if row > 0 and is_same_piece(state, row-1, col, piece):
            swap_position(successor, row-1, col, erow, ecol)
            return "".join(successor) 
    else:
        if row < 4 and is_same_piece(state, row+1, col, piece):
            swap_position(successor, row+1, col, erow, ecol)
            return "".join(successor)

    horizontal_neighbour_col = -1
    if col > 0 and is_same_piece(state, row, col-1, piece):
        horizontal_neighbour_col = col-1
    else:
        horizontal_neighbour_col = col+1
    swap_position(successor, row, col, erow, ecol)
    swap_position(successor, row, horizontal_neighbour_col, erow, horizontal_neighbour_col)
    return "".join(successor)


def movwe_2x1_horizontal(state, row, col, erow, ecol, direction, piece):
    successor = str_to_list(state.state)
    piece = int(piece)
    if direction == 'r':
        if col > 0 and is_same_piece(state, row, col-1, piece):
            swap_position(successor, row, col-1, erow, ecol)
            return "".join(successor) 
    else:
        if col < 3 and is_same_piece(state, row, col+1, piece):
            swap_position(successor, row, col+1, erow, ecol)
            return "".join(successor)

    vertical_neighbour_row = -1
    if row > 0 and is_same_piece(state, row-1, col, piece):
        vertical_neighbour_row = row-1
    else:
        vertical_neighbour_row = row+1
    swap_position(successor, row, col, erow, ecol)
    swap_position(successor, vertical_neighbour_row, col, vertical_neighbour_row, ecol)
    return "".join(successor)


def movwe_1x1(state, row, col, erow, ecol):
    successor = str_to_list(state.state)
    swap_position(successor, row, col, erow, ecol)
    return "".join(successor) 


def get_new_state(state, row, col, erow, ecol):
    neigbour_pos = coordinate_to_index([row, col])
    piece = state.state[neigbour_pos]
    direction = ''
    if piece == '0':
        return None
    if row == erow and isMovable_horizontal(state, row, col, erow, ecol, piece):
        # move to left if True. Otherwise to right
        direction = 'l' if col - ecol > 0 else 'r'
        if piece == '1':
            return movwe_2x2_horizontal(state, row, col, erow, ecol, direction)
        elif piece == '7':
            return movwe_1x1(state, row, col, erow, ecol)
        else:
            return movwe_2x1_horizontal(state, row, col, erow, ecol, direction, piece)
    elif col == ecol and isMovable_vertical(state, row, col, erow, ecol, piece):
        # move to up if True. Otherwise to down
        direction = 'u' if row - erow > 0 else 'd'           
        if piece == '1':
            return movwe_2x2_vertical(state, row, col, erow, ecol, direction)
        elif piece == '7':
            return movwe_1x1(state, row, col, erow, ecol)
        else:
            return movwe_2x1_vertical(state, row, col, erow, ecol, direction,piece)
    else:
        return None

def find_fragment(state, row, col, erow, ecol, piece):
    # find pos of anther piece
    if row > 0 and is_same_piece(state, row-1, col, piece):
        return [row-1, col]
    elif row < 4 and is_same_piece(state, row+1, col, piece):
        return [row+1, col]
    elif col > 0 and is_same_piece(state, row, col-1, piece):
        return [row, col-1]
    return [row, col+1]


def isMovable_horizontal(state, row, col, erow, ecol, piece):
    piece = int(piece)
    if piece == 1:
        return isMovable2x2_horizontal(state, row, col, erow, ecol, piece)
    elif piece == 7:
        return True
    else:
        return isMovable1x2_horizontal(state, row, col, erow, ecol, piece)


def isMovable2x2_horizontal(state, row, col, erow, ecol, piece):
    row_2nd_piece = -1
    # find pos of anther piece
    if row > 0 and is_same_piece(state, row-1, col, piece):
        row_2nd_piece = row - 1
    else:
        row_2nd_piece = row + 1
    # check if whole piece can move
    destination = coordinate_to_index([row_2nd_piece, ecol])
    if state.state[destination] == '0':
        return True
    return False


def isMovable1x2_horizontal(state, row, col, erow, ecol, piece):
    row_2nd_piece = -1
    # find pos of anther piece
    if row > 0 and is_same_piece(state, row-1, col, piece):
        row_2nd_piece = row - 1
    elif row < 4 and is_same_piece(state, row+1, col, piece):
        row_2nd_piece = row + 1
    elif col > 0 and is_same_piece(state, row, col-1, piece):
        row_2nd_piece = row
    else:
        row_2nd_piece = row
    # check if whole piece can move
    if row_2nd_piece == row:
        return True
    destination = coordinate_to_index([row_2nd_piece, ecol])
    if state.state[destination] == '0':
        return True
    return False


def isMovable_vertical(state, row, col, erow, ecol, piece):
    piece = int(piece)
    if piece == 1:
        return isMovable2x2_vertical(state, row, col, erow, ecol, piece)
    elif piece == 7:
        return True
    else:
        return isMovable1x2_vertical(state, row, col, erow, ecol, piece)


def isMovable2x2_vertical(state, row, col, erow, ecol, piece):
    col_2nd_piece = -1
    # find pos of anther piece
    if col > 0 and is_same_piece(state, row, col-1, piece):
        col_2nd_piece = col - 1
    else:
        col_2nd_piece = col + 1
    # check if whole piece can move
    destination = coordinate_to_index([erow, col_2nd_piece])
    if state.state[destination] == '0':
        return True
    return False


def isMovable1x2_vertical(state, row, col, erow, ecol, piece):
    col_2nd_piece = -1
    # find pos of anther piece
    if row > 0 and is_same_piece(state, row-1, col, piece):
        col_2nd_piece = col
    elif row < 4 and is_same_piece(state, row+1, col, piece):
        col_2nd_piece = col
    elif col > 0 and is_same_piece(state, row, col-1, piece):
        col_2nd_piece = col - 1
    else:
        col_2nd_piece = col + 1
    # check if whole piece can move
    if col_2nd_piece == col:
        return True
    destination = coordinate_to_index([erow, col_2nd_piece])
    if state.state[destination] == '0':
        return True
    return False
            

def is_same_piece(state, row, col, piece):
    index = coordinate_to_index([row, col])
    if int(state.state[index]) == piece:
        return True
    return False

    
def get_cost(state):
    return state.g


def get_heuristic(state):
    return abs(state.row_pos_2x2 - 3) + abs(state.col_pos_2x2 - 1)


def is_explored(explored, expanding_state):
    try:
        result = explored[expanding_state.state]
        return result
    except:
        return False 


def print_path(state, num_expanded):
    path = []
    total_cost = get_cost(state)
    while state:
        path.append(state)
        state = state.parent
    path = path[::-1]
    print("Initial State:")
    path[0].print_board()
    print(f'Cost of the solution: {total_cost}\n')
    print(f'Number of states expanded: {num_expanded}\n')
    print('Solution:\n')
    count = 0
    for state in path:
        print(count)
        state.print_board()
        count += 1


def a_star(initial_state):
    initial_state.set_h(get_heuristic(initial_state))
    frontier = Frontier()
    frontier.push(initial_state)
    explored = {}
    num_expanded = 0
    while not frontier.is_empty():
        popped = frontier.pop()
        expanding_state = popped[1]
        if is_goal(expanding_state):
            num_expanded += 1
            return [expanding_state, num_expanded]
        successors = get_successors(expanding_state)
        for successor in successors:
            if is_explored(explored, successor):
                continue
            frontier.push(successor)
            explored[successor.state] = True
        num_expanded += 1
    return [0,0]

def dfs(initial_state):
    frontier = LIFO()
    frontier.push(initial_state)
    explored = {}
    num_expanded = 0
    while not frontier.is_empty():
        expanding_state = frontier.pop()
        if is_goal(expanding_state):
            num_expanded += 1
            return [expanding_state, num_expanded]
        successors = get_successors(expanding_state)
        for successor in successors:
            if is_explored(explored, successor):
                continue
            frontier.push(successor)
            explored[successor.state] = True
        num_expanded += 1
    return [0,0]


def write_path(state, num_expanded, filename):
    path = []
    total_cost = get_cost(state)
    while state:
        path.append(state)
        state = state.parent
    path = path[::-1]
    output_file = None
    try:
        output_file = open(filename, 'x')
    except FileExistsError:
        output_file = open(filename, 'w')
    
    output_file.write("Initial State:\n")
    path[0].write_state(output_file)
    output_file.write(f'Cost of the solution: {total_cost}\n\n')
    output_file.write(f'Number of states expanded: {num_expanded}\n\n')
    output_file.write('Solution:\n\n')
    count = 0
    for state in path:
        output_file.write(f'{count}\n')
        state.write_state(output_file)
        count += 1


def solve_puzzle():
    input = ['puzzle1.txt', 'puzzle2.txt']
    output_astar = ['puzzle1sol_astar.txt', 'puzzle2sol_astar.txt']
    output_dfs = ['puzzle1sol_dfs.txt', 'puzzle2sol_dfs.txt']

    for i in range(2):
        initial_state = read_puzzle(input[i])
        expanding_state, num_expanded = a_star(initial_state)
        write_path(expanding_state, num_expanded, output_astar[i])

    for i in range(2):
        initial_state = read_puzzle(input[i])
        expanding_state, num_expanded = dfs(initial_state)
        write_path(expanding_state, num_expanded, output_dfs[i])



if __name__ == "__main__":
    solve_puzzle()
