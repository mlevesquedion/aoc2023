import collections
import itertools


lines = list(open('07.txt'))

rank_value = dict(zip('23456789TJQKA', itertools.count()))
joker_value = dict(zip('J23456789TQKA', itertools.count()))


def score(hand):
    rank_score = 0
    for i, c in enumerate(hand):
        rank_score = rank_score * 13 + rank_value[c]
    counts = [c for _, c in collections.Counter(hand).most_common()]
    if counts[0] == 5:
        return 6e10 + rank_score
    if counts[0] == 4:
        return 5e10 + rank_score
    if counts[0] == 3 and counts[1] == 2:
        return 4e10 + rank_score
    if counts[0] == 3:
        return 3e10 + rank_score
    if counts[0] == 2 and counts[1] == 2:
        return 2e10 + rank_score
    if counts[0] == 2:
        return 1e10 + rank_score
    return rank_score


def joker_score(hand):
    rank_score = 0
    for i, c in enumerate(hand):
        rank_score = rank_score * 13 + joker_value[c]
    joker_count = hand.count('J')
    hand = hand.replace('J', '')
    counts = [c for _, c in collections.Counter(hand).most_common()]
    if not counts or counts[0] + joker_count == 5:
        return 6e10 + rank_score
    if counts[0] + joker_count == 4:
        return 5e10 + rank_score
    if counts[0] + joker_count == 3 and counts[1] == 2:
        return 4e10 + rank_score
    if counts[0] + joker_count == 3:
        return 3e10 + rank_score
    if counts[0] == 2 and counts[1] + joker_count == 2:
        return 2e10 + rank_score
    if counts[0] + joker_count == 2:
        return 1e10 + rank_score
    return rank_score


def total_winnings(hand_bids, score):
    ranked = sorted(hand_bids, key=lambda parts: score(parts[0]))
    return sum([i*int(bid) for i, (_, bid) in enumerate(ranked, 1)])


hand_bids = [line.split() for line in lines]

assert total_winnings(hand_bids, score) == 251216224
assert total_winnings(hand_bids, joker_score) == 250825971
