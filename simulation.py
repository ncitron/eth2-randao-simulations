from random import random

def get_proposals_epoch(percentage: float) -> int:
    props = 0
    for _ in range(32):
        if random() < percentage:
            props += 1
    return props

def should_skip(percentage: float) -> bool:
    props_no_skip = get_proposals_epoch(percentage)
    props_skip = get_proposals_epoch(percentage)
    return props_skip > props_no_skip + 1

def get_percentage_skip(percentage: float, rounds: int) -> float:
    total_skips = 0
    for _ in range(rounds):
        if should_skip(percentage):
            total_skips += 1
    return total_skips / rounds

for p in range (100):
    percent_skips = get_percentage_skip(p / 100, 100000)
    print(f"validator_percentage: {p}, skip_percentage: {percent_skips}")
