import random
from collections import defaultdict

SEED=12345
random.seed(SEED)

ANNOTATORS = [
  "Yonglin Wang",
  "Zhuoran Huang",
  "Shiyi Shen",
  "Xiaoyu Lu"
]

CANDIDATES = [
  "Joe Biden",
  "Bernie Sanders",
  "Andrew Yang",
  "Elizabeth Warren",
  "Pete Buttigieg"
]

ASSIGNMENTS = defaultdict(list)
if __name__ == '__main__':
    random.shuffle(ANNOTATORS)
    random.shuffle(CANDIDATES)
    for ann, cand in zip(ANNOTATORS, CANDIDATES):
        ASSIGNMENTS[ann].append(cand)
    remaining_candidate = CANDIDATES[-1]
    random_annotator = random.choice(ANNOTATORS)
    ASSIGNMENTS[random_annotator].append(remaining_candidate)
    for ann, cands in ASSIGNMENTS.items():
        print(f"{ann}: {', '.join(cands)}")

