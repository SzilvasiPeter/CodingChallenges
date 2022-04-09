import math

def pos_to_coords(pos):
    """
    Converts a position [0..63] into a pair of coord (x, y)
    """
    x = int(math.floor(pos/8))
    y = int(pos%8)
    return (x, y)


def coords_to_pos(x, y):
    """
    Converts a pair of coord (x, y) into a position [0..63]
    """
    return x + y * 8


def get_possible_moves(x, y):
    """
    Returns a list of valid coordinates for next move
    """
    all_moves = []
    all_moves.append((x+2, y+1))
    all_moves.append((x+2, y-1))
    all_moves.append((x-2, y+1))
    all_moves.append((x-2, y-1))
    all_moves.append((x+1, y+2))
    all_moves.append((x+1, y-2))
    all_moves.append((x-1, y+2))
    all_moves.append((x-1, y-2))

    valid_moves = []
    for (x, y) in all_moves:
        if(x >= 0 and x < 8 and y >= 0  and y < 8):
            valid_moves.append((x, y))

    return valid_moves

# Bruteforce solution O(n^2): working
def solution1(src, dest):
    if src == dest:
        return 0

    # Get the current and target tile
    src_x, src_y = pos_to_coords(src)
    dst_x, dst_y = pos_to_coords(dest)
    
    # Create a queue with all the positions I need to check
    queue = get_possible_moves(src_x, src_y)
    depth_queue = []

    # the depth, or solution
    depth = 0 

    while True:
        depth += 1

        # We check each move available at this depth
        for move in queue:
            # Let's see if we arrived to destination
            if move[0] == dst_x and move[1] == dst_y:
                return depth

            # we build the next depth queue, which will replace the queue after we tested them all
            # this is necessary to test one level at a time
            depth_queue.extend(get_possible_moves(move[0], move[1]))

        queue = depth_queue
        depth_queue = []

# Divider solution O(1): not working
def solution2(src, dest):
    x = [src//8, src%8]
    y = [dest//8, dest%8]
    
    a = abs(x[0] - y[0])
    b = abs(x[1] - y[1])
    
    z = a+b
    
    steps = 0
    remainder = z % 3
    quotient = z // 3
    
    # Same
    if x[0] == y[0] and x[1] == y[1]:
        return 0
    # Diagonal
    elif a > 2 and b > 2 and a == b:
        if z % 4 == 0:
            steps += 4
        else:
            steps += (z // 4)*2
    # Parallel
    elif x[0] == y[0] or x[1] == y[1]:
        if z % 2 == 0:
            steps += 2
        else:
            steps += 3

        if z // 6 == 1:
            steps += 2
    # elif z % 4 == 0:
    #     steps += (z // 4) * 2 
    # Otherwise
    else:
        if remainder == 1: 
            steps += 3 
        elif remainder == 2: 
            steps += 2 

        steps += quotient
        
    return steps

# Pattern solution O(1): working
def solution3(src, dest):
    x = [src//8, src%8]
    y = [dest//8, dest%8]

    a = abs(x[0] - y[0])
    b = abs(x[1] - y[1])

    z = a + b

    even_pattern = [0, 3, 2, 3, 2, 3, 4, 5]
    odd_pattern = [0, 1, 2, 3, 4, 3, 4]
    diagonal_corner_pattern = [4, 4, 2, 4, 4, 4, 6]
    diagonal_pattern = [2, 4, 2, 4, 4, 4, 6]

    idx = z // 2
    
    # Same
    if x[0] == y[0] and x[1] == y[1]:
        return 0

    # Diagonal
    elif a == b:
        # Corner
        if  (x[0] == 0 and x[1] == 0) or \
            (x[0] == 0 and x[1] == 7) or \
            (x[0] == 7 and x[1] == 0) or \
            (x[0] == 7 and x[1] == 7) or \
            (y[0] == 0 and y[1] == 0) or \
            (y[0] == 0 and y[1] == 7) or \
            (y[0] == 7 and y[1] == 0) or \
            (y[0] == 7 and y[1] == 7):
            return diagonal_corner_pattern[idx-1]
        else:
            return diagonal_pattern[idx-1]
    else:
        if a == 0 or b == 0:
            return even_pattern[a+b]
        if a == 1 or b == 1:
            return odd_pattern[a+b-2]
        if a == 2 or b == 2:
            return even_pattern[a+b-4+2]
        if a == 3 or b == 3:
            return odd_pattern[a+b-6+2]
        if a == 4 or b == 4:
            return even_pattern[a+b-8+4]
        if a == 5 or b == 5:
            idx = a+b-10+4
            if idx == 5:
                return odd_pattern[idx] + 2 
            return odd_pattern[idx]
        if a == 6 or b == 6:
            return even_pattern[a+b-12+6]


if __name__ == '__main__':
    for i in range(0, 63):
        for j in range(0, 63):
            sol2 = solution1(i, j)
            sol3 = solution3(i, j)
            if  sol3 != sol2:
                print(i, j)
                print("sol3: " + str(sol3) + " sol2: " + str(sol2))
