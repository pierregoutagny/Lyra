# INITIAL: i -> [-inf, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [-inf, inf]; v2 -> [-inf, inf], d -> {([-inf, inf], [-inf, inf])}, d -> {([-inf, inf], True)}, {}
v1: int = 0
# STATE: i -> [-inf, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [-inf, inf], d -> {([-inf, inf], [-inf, inf])}, d -> {([-inf, inf], True)}, {}
i: int = int(input())
# STATE: i -> [-inf, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [-inf, inf], d -> {([-inf, inf], [-inf, inf])}, d -> {([-inf, inf], True)}, {}
d: Dict[int, int] = {3: 2}
# STATE: i -> [-inf, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [-inf, inf], d -> {([3, 3], [2, 2])}, d -> {([-inf, 2], True), ([4, inf], True)}, {}
d[4]: int = 1
# STATE: i -> [-inf, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [-inf, inf], d -> {([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, 2], True), ([5, inf], True)}, {}
d[v1]: int = 7
# STATE: i -> [-inf, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [-inf, inf], d -> {([0, 0], [7, 7]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([1, 2], True), ([5, inf], True)}, {}
d[1]: int = v1
# STATE: i -> [-inf, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [-inf, inf], d -> {([0, 0], [7, 7]), ([1, 1], [0, 0]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([2, 2], True), ([5, inf], True)}, {}
v2: int = d[3]
# STATE: i -> [-inf, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [2, 2], d -> {([0, 0], [7, 7]), ([1, 1], [0, 0]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([2, 2], True), ([5, inf], True)}, {}
d[2]: int = 3 + v2
# STATE: i -> [-inf, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [2, 2], d -> {([0, 0], [7, 7]), ([1, 1], [0, 0]), ([2, 2], [5, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {}
if i >= 2:
    # STATE: i -> [2, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [2, 2], d -> {([0, 0], [7, 7]), ([1, 1], [0, 0]), ([2, 2], [5, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {}
    i: int = i
    # STATE: i -> [2, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [2, 2], d -> {([0, 0], [7, 7]), ([1, 1], [0, 0]), ([2, 2], [5, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {}
    if i in d.keys():
        # STATE: i -> [2, 4]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [2, 2], d -> {([0, 0], [7, 7]), ([1, 1], [0, 0]), ([2, 2], [5, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {(d, i, None)}
        v2: int = d[i]
        # STATE: i -> [2, 4]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [1, 5], d -> {([0, 0], [7, 7]), ([1, 1], [0, 0]), ([2, 2], [5, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {(d, i, None)}
    # STATE: i -> [2, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [1, 5], d -> {([0, 0], [7, 7]), ([1, 1], [0, 0]), ([2, 2], [5, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {}
    i: int = i
    # STATE: i -> [2, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 0]; v2 -> [1, 5], d -> {([0, 0], [7, 7]), ([1, 1], [0, 0]), ([2, 2], [5, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {}
    for k, v in d.items():
        # STATE: i -> [2, inf]; k -> [0, 4]; len(d) -> [-inf, inf]; v -> [0, 7]; v1 -> [0, 2]; v2 -> [1, 5], d -> {([0, 0], [7, 7]), ([1, 1], [0, 2]), ([2, 2], [1, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {(d, k, v)}
        i: int = i
        # STATE: i -> [2, inf]; k -> [0, 4]; len(d) -> [-inf, inf]; v -> [0, 7]; v1 -> [0, 2]; v2 -> [1, 5], d -> {([0, 0], [7, 7]), ([1, 1], [0, 2]), ([2, 2], [1, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {(d, k, v)}
        if k >= 3:
            # STATE: i -> [2, inf]; k -> [3, 4]; len(d) -> [-inf, inf]; v -> [1, 2]; v1 -> [0, 2]; v2 -> [1, 5], d -> {([0, 0], [7, 7]), ([1, 1], [0, 2]), ([2, 2], [1, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {(d, k, v)}
            v1: int = v
            # STATE: i -> [2, inf]; k -> [3, 4]; len(d) -> [-inf, inf]; v -> [1, 2]; v1 -> [1, 2]; v2 -> [1, 5], d -> {([0, 0], [7, 7]), ([1, 1], [0, 2]), ([2, 2], [1, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {(d, k, v), (d, k, v1)}
            d[k-2]: int = v1        # weak update without partitioning
            # STATE: i -> [2, inf]; k -> [3, 4]; len(d) -> [-inf, inf]; v -> [1, 2]; v1 -> [1, 2]; v2 -> [1, 5], d -> {([0, 0], [7, 7]), ([1, 1], [0, 2]), ([2, 2], [1, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {(d, k, v), (d, k, v1)}
        # STATE: i -> [2, inf]; k -> [0, 4]; len(d) -> [-inf, inf]; v -> [0, 7]; v1 -> [0, 2]; v2 -> [1, 5], d -> {([0, 0], [7, 7]), ([1, 1], [0, 2]), ([2, 2], [1, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {(d, k, v)}
        i: int = i
        # STATE: i -> [2, inf]; k -> [0, 4]; len(d) -> [-inf, inf]; v -> [0, 7]; v1 -> [0, 2]; v2 -> [1, 5], d -> {([0, 0], [7, 7]), ([1, 1], [0, 2]), ([2, 2], [1, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {(d, k, v)}
    # STATE: i -> [2, inf]; k -> [0, 4]; len(d) -> [-inf, inf]; v -> [0, 7]; v1 -> [0, 2]; v2 -> [1, 5], d -> {([0, 0], [7, 7]), ([1, 1], [0, 2]), ([2, 2], [1, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {}
    i: int = i
# FINAL: i -> [-inf, inf]; k -> [-inf, inf]; len(d) -> [-inf, inf]; v -> [-inf, inf]; v1 -> [0, 2]; v2 -> [1, 5], d -> {([0, 0], [7, 7]), ([1, 1], [0, 2]), ([2, 2], [1, 5]), ([3, 3], [2, 2]), ([4, 4], [1, 1])}, d -> {([-inf, -1], True), ([5, inf], True)}, {}
