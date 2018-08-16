# INITIAL: a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], W)}, scores -> {([100, inf], W)}
scores: Dict[int, int] = input()     #dictinput()   # id -> score
# STATE: a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], W)}, scores -> {([100, inf], U)}
score_occurrences: Dict[int, int] = {}        # defaultdict(int)    # initialized to 0
# STATE: a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
for a, b in scores.items():
    # STATE: a -> U, b -> U, k -> N, scores_gt_10 -> N, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)} | a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
    a = a
    # STATE: a -> U, b -> U, k -> N, scores_gt_10 -> N, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)} | a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
    if a < 100:     # 'early adopter'
        # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
        weight: int = 3
        # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
    else:
        # STATE: a -> N, b -> U, k -> N, scores_gt_10 -> N, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
        weight: int = 1
        # STATE: a -> N, b -> U, k -> N, scores_gt_10 -> N, weight -> U, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
        if b not in score_occurrences.keys():        # workaround for defaultdict
            # STATE: a -> N, b -> U, k -> N, scores_gt_10 -> N, weight -> S, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)} | a -> N, b -> U, k -> N, scores_gt_10 -> N, weight -> U, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
            score_occurrences[b] = 0
            # STATE: a -> N, b -> S, k -> N, scores_gt_10 -> N, weight -> S, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> N, b -> U, k -> N, scores_gt_10 -> N, weight -> U, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
        # STATE: a -> N, b -> U, k -> N, scores_gt_10 -> N, weight -> U, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
        score_occurrences[b] += weight   # BUG B: wrong indentation
        # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
    # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
    a = a
    # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {([-inf, inf], S)}, scores -> {([100, inf], S)} | a -> W, b -> W, k -> W, scores_gt_10 -> W, weight -> W, score_occurrences -> {([-inf, inf], U)}, scores -> {([100, inf], U)}
# STATE: a -> N, b -> N, k -> W, scores_gt_10 -> W, weight -> N, score_occurrences -> {([11, inf], U)}, scores -> {}
scores_gt_10: int = 0
# STATE: a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([11, inf], U)}, scores -> {}
for k in score_occurrences.keys():
    # STATE: a -> N, b -> N, k -> U, scores_gt_10 -> U, weight -> N, score_occurrences -> {([11, inf], U)}, scores -> {} | a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([11, inf], U)}, scores -> {}
    a = a
    # STATE: a -> N, b -> N, k -> U, scores_gt_10 -> U, weight -> N, score_occurrences -> {([11, inf], U)}, scores -> {} | a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([11, inf], U)}, scores -> {}
    if k > 10:
        # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> U, weight -> N, score_occurrences -> {([11, inf], U)}, scores -> {} | a -> N, b -> N, k -> N, scores_gt_10 -> S, weight -> N, score_occurrences -> {([11, inf], S)}, scores -> {} | a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([11, inf], U)}, scores -> {}
        scores_gt_10 += score_occurrences[k]
        # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> S, weight -> N, score_occurrences -> {([11, inf], S)}, scores -> {} | a -> N, b -> N, k -> N, scores_gt_10 -> S, weight -> N, score_occurrences -> {([11, inf], S)}, scores -> {} | a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([11, inf], U)}, scores -> {}
    # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> S, weight -> N, score_occurrences -> {([11, inf], S)}, scores -> {} | a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([11, inf], U)}, scores -> {}
    a = a
    # STATE: a -> N, b -> N, k -> N, scores_gt_10 -> S, weight -> N, score_occurrences -> {([11, inf], S)}, scores -> {} | a -> N, b -> N, k -> W, scores_gt_10 -> U, weight -> N, score_occurrences -> {([11, inf], U)}, scores -> {}
# STATE: a -> N, b -> N, k -> N, scores_gt_10 -> U, weight -> N, score_occurrences -> {}, scores -> {}
print(scores_gt_10)
# FINAL: a -> N, b -> N, k -> N, scores_gt_10 -> N, weight -> N, score_occurrences -> {}, scores -> {}
