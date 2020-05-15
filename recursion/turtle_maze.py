

def search_from(maze, start_row, start_col):
    maze.update_position(start_row, start_col)
    # Check for base case
    # 1. We run into a obstacle, return false
    if maze[start_row, start_col] == OBSTACLE:
        return False
    # 2. We have found a square that has already been explored
    if maze[start_row, start_col] == TRIED:
        return False
    # 3. success, an outside edge not occupied by an obstacle
    if maze.is_exit(start_row, start_col):
        maze.update_position(start_row, start_col, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_col, TRIED)

    # Otherwise, use logical short circuiting to try each
    # direction in turn (if needed)

    found = search_from(maze, start_row-1, start_col) or \
        search_from(maze, start_row+1, start_col) or \
        search_from(maze, start_row, start_col-1) or \
        search_from(maze, start_row, start_col+1)

    if found:
        maze.update_position(start_row, start_col, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_col, DEAD_END)
    return found