def heuristic(a, b):
    '''
    The heuristic function of the A*
    '''
    x = b[0]-a[0]
    y = b[1]-a[1]
    return (x*x + y*y)

def get_neighbors(case,obstacles) :
    '''
    Returns the list of each cell which is adjacent to the (i, j) cell
    '''
    i, j = case
    neighbors = []
    if j > 0 and obstacles[i, j-1]:
        neighbors.append((i, j-1))
    if j < 20 and obstacles[i, j+1]:
        neighbors.append((i, j+1))
    if i > 0 and obstacles[i-1, j]:
        neighbors.append((i-1, j))
    if i < 31 and obstacles[i+1, j]:
        neighbors.append((i+1, j))
    return neighbors
