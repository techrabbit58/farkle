from typing import Iterable

triple_score: dict[int, int] = dict(zip((1, 2, 3, 4, 5, 6), (1000, 200, 300, 400, 500, 600)))


def best_score(dice: Iterable[int], initial_score: int = 0) -> tuple[int, ...]:

    score = 0
    extra_dice: list[int] = []
    num_dice, die_counts = count_dice(dice)

    if num_dice == 6 and all(count == 1 for count in die_counts):
        score = 1200
    elif num_dice == 6 and all(count == 2 for count in die_counts if count != 0):
        score = 800
    elif die_counts.count(0) == 5 and die_counts.count(6) == 1:
        for die, count in enumerate(die_counts):
            if count != 0:
                score = triple_score[die + 1] * 8
                break
    elif 5 <= num_dice <= 6 and die_counts.count(5) == 1:
        for die, count in enumerate(die_counts):
            if count == 5:
                score = triple_score[die + 1] * 4
                break
        extra_dice = add_to_extra_dice(die_counts, extra_dice)
    elif 4 <= num_dice <= 6 and die_counts.count(4) == 1:
        for die, count in enumerate(die_counts):
            if count == 4:
                score = triple_score[die + 1] * 2
                break
        extra_dice = add_to_extra_dice(die_counts, extra_dice)
    elif 3 <= num_dice <= 6 and 0 < die_counts.count(3) <= 2:
        for die, count in enumerate(die_counts):
            if count == 3:
                score += triple_score[die + 1]
        extra_dice = add_to_extra_dice(die_counts, extra_dice)
    else:
        score = 0

    if score == 0:
        extra_dice += dice

    ones, fives, extra_dice = count_single_ones_and_fives(extra_dice)

    score += ones * 100 + fives * 50

    return initial_score + score, *sorted(extra_dice)


def count_single_ones_and_fives(extra_dice: list[int]) -> tuple[int, int, list[int]]:
    ones = extra_dice.count(1)
    fives = extra_dice.count(5)
    extra_dice = [die for die in extra_dice if die not in (1, 5)]
    return ones, fives, extra_dice


def count_dice(dice: Iterable[int]) -> tuple[int, list[int]]:
    die_counts = [0] * 6
    num_dice = 0
    for die in dice:
        die_counts[die - 1] += 1
        num_dice += 1
    return num_dice, die_counts


def add_to_extra_dice(die_counts: list[int], extra_dice: list[int]) -> list[int]:
    for die, count in enumerate(die_counts):
        if 1 <= count <= 2:
            extra_dice += [die + 1] * die_counts[die]
    return extra_dice
