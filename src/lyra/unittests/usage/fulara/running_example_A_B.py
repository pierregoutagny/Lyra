# INITIAL: a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], W)}, scores -> {}
scores: Dict[int, int] = input()     #dictinput()   # id -> score
# STATE: a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], W)}, scores -> {}
score_occurrences: Dict[int, int] = {}        # defaultdict(int)    # initialized to 0
# STATE: a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
for a, b in scores.items():
    # STATE: a -> U, b -> N, k -> N, scores_gt_10 -> N, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {} | a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
    a = a
    # STATE: a -> U, b -> N, k -> N, scores_gt_10 -> N, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {} | a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
    if a < 100:     # 'early adopter'
        # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
        weight: int = 3
        # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
    else:
        # STATE: a -> U, b -> N, k -> N, scores_gt_10 -> N, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
        weight: int = 1
        # STATE: a -> U, b -> N, k -> N, scores_gt_10 -> N, weight -> U, score_occurrences -> {([100, inf], U)}, scores -> {} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
        if a not in score_occurrences.keys():        # workaround for defaultdict
            # STATE: a -> U, b -> N, k -> N, scores_gt_10 -> N, weight -> S, score_occurrences -> {([100, inf], U)}, scores -> {} | a -> U, b -> N, k -> N, scores_gt_10 -> N, weight -> U, score_occurrences -> {([100, inf], U)}, scores -> {} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
            score_occurrences[a] = 0
            # STATE: a -> S, b -> N, k -> N, scores_gt_10 -> N, weight -> S, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> U, b -> N, k -> N, scores_gt_10 -> N, weight -> U, score_occurrences -> {([100, inf], U)}, scores -> {} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
        # STATE: a -> U, b -> N, k -> N, scores_gt_10 -> N, weight -> U, score_occurrences -> {([100, inf], U)}, scores -> {} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
        score_occurrences[a] += weight   # BUG A: should be indexed by b & BUG B: wrong indentation
        # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
    # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
    a = a
    # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> W, b -> N, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([100, inf], U)}, scores -> {}
# STATE: a -> N, b -> N, k -> W, scores_gt_10 -> W, weight -> N, score_occurrences -> {([100, inf], U)}, scores -> {}
scores_gt_10: int = 0
# STATE: a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([100, inf], U)}, scores -> {}
for k in score_occurrences.keys():
    # STATE: a -> N, b -> N, k -> U, scores_gt_10 -> U, weight -> N, score_occurrences -> {([100, inf], U)}, scores -> {} | a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([100, inf], U)}, scores -> {}
    a = a
    # STATE: a -> N, b -> N, k -> U, scores_gt_10 -> U, weight -> N, score_occurrences -> {([100, inf], U)}, scores -> {} | a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([100, inf], U)}, scores -> {}
    if k > 10:
        # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> U, weight -> N, score_occurrences -> {([100, inf], U)}, scores -> {} | a -> N, b -> N, k -> N, scores_gt_10 -> S, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([100, inf], U)}, scores -> {}
        scores_gt_10 += score_occurrences[k]
        # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> S, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> N, b -> N, k -> N, scores_gt_10 -> S, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([100, inf], U)}, scores -> {}
    # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> S, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([100, inf], U)}, scores -> {}
    a = a
    # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> S, weight -> N, score_occurrences -> {([100, inf], S)}, scores -> {} | a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([100, inf], U)}, scores -> {}
# STATE: a -> N, b -> N, k -> N, scores_gt_10 -> U, weight -> N, score_occurrences -> {}, scores -> {}
print(scores_gt_10)
# FINAL: a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {}, scores -> {}
