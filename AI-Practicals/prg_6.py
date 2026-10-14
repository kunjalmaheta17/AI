'''
What is a Heuristic Function?
A heuristic function is a function used in Artificial Intelligence (AI)
to estimate how close a current state is to the goal state.
In simple words, a heuristic function helps an AI program decide which
option looks most promising to reach the goal.

What is Manhattan Distance?
Manhattan distance is the total number of horizontal and vertical steps
required to move from one position to another on a grid. Diagonal
movement is not counted.

Mathematical formula

d=|r_1-r_2|+|c_1-c_2|

'''
import heapq

# Define the goal state (0 represents the blank space)
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Define the valid positions where the blank tile can move
moves = {
    0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
    3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
    6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
}


# Heuristic function: Calculate Manhattan distance
def heuristic(state):
    distance = 0

    # Check the position of each tile
    for index, tile in enumerate(state):

        # Ignore the blank tile
        if tile == 0:
            continue

        # Find the tile's correct position in the goal state
        goal_index = goal.index(tile)

        # Convert positions into row and column numbers
        row1, col1 = divmod(index, 3)
        row2, col2 = divmod(goal_index, 3)

        # Add horizontal and vertical distances
        distance += abs(row1 - row2) + abs(col1 - col2)

    # Return the total distance from the goal
    return distance


# Solve the puzzle using Greedy Best-First Search
def solve(start):

    # Initialize the priority queue with the starting state
    # Each entry contains: heuristic, counter, state, path
    counter = 0
    queue = [(heuristic(start), counter, start, [])]

    # Store states already discovered to avoid duplicates
    visited = set([start])

    while queue:

        # Select the state with the smallest heuristic value
        h, _, state, path = heapq.heappop(queue)

        # Check whether the goal state has been reached
        if state == goal:
            return path + [state]

        # Find the current position of the blank tile
        zero = state.index(0)

        # Generate all valid moves of the blank tile
        for move in moves[zero]:

            # Create a new state by swapping the blank tile
            new_state = list(state)
            new_state[zero], new_state[move] = (
                new_state[move], new_state[zero]
            )
            new_state = tuple(new_state)

            # Process only states that have not been discovered
            if new_state not in visited:
                visited.add(new_state)
                counter += 1

                # Calculate the heuristic and add the new state
                # to the priority queue for future exploration
                heapq.heappush(
                    queue,
                    (heuristic(new_state), counter,
                     new_state, path + [state])
                )

    # Return None if the search cannot find a solution
    return None


# Define the initial puzzle state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

# Execute the search
solution = solve(start)

# Display the solution path and heuristic value of each state
if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")

    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print("Heuristic value =", heuristic(step))
        print()
else:
    print("No solution found")
