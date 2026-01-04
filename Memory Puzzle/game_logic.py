import random

DIFFICULTY = {
    "Easy":   {"time": [40, 60, 80, 100, 120], "hints": 2},
    "Medium": {"time": [30, 45, 60, 75, 90], "hints": 1},
    "Hard":   {"time": [20, 35, 50, 65, 80], "hints": 0},
}

def create_cards(level):
    symbols = ["A","A","B","B","C","C","D","D","E","E","F","F"]
    # Use (level + 1) pairs for level scaling so level 1 has 2 pairs (4 cards)
    pairs = min(level + 1, len(symbols)//2)
    cards = symbols[: pairs * 2 ]
    random.shuffle(cards)
    return cards
