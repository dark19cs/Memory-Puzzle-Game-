def use_hint(cards, revealed):
    seen = {}
    for i, c in enumerate(cards):
        if revealed[i]: continue
        if c in seen:
            return seen[c], i
        seen[c] = i
    return None