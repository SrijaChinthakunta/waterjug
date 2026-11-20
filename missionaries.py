from collections import deque

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    rm, rc = 3 - m, 3 - c

    if rm > 0 and rm < rc:
        return False

    return True

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = set()

    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            for step in path + [state]:
                print(step)
            print("Solution Found!")
            return

        if state in visited:
            continue

        visited.add(state)
        m, c, boat = state

        for dm, dc in moves:
            if boat == 1:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)

            if is_valid(new_state[0], new_state[1]):
                if new_state not in visited:
                    queue.append((new_state, path + [state]))

    print("No solution found!")

solve()
