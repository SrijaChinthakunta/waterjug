from collections import deque

def water_jug(cap1, cap2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        print(a, b)

        if a == target or b == target:
            print("Solution Found!")
            return

        next_states = [
            (cap1, b),
            (a, cap2),
            (0, b),
            (a, 0),
            (a - min(a, cap2 - b), b + min(a, cap2 - b)),
            (a + min(b, cap1 - a), b - min(b, cap1 - a))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("No solution found!")

water_jug(4, 3, 2)
