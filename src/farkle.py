from collections.abc import Iterable

triple_score: dict[int, int] = dict(zip((1, 2, 3, 4, 5, 6), (1000, 200, 300, 400, 500, 600)))


def best_score(dice: Iterable[int]) -> tuple[int, ...]:
    die_counts: list[int] = [0] * 6

    num_dice = 0
    for die in dice:
        die_counts[die - 1] += 1
        num_dice += 1

    score = 0
    extra_dice: list[int] = []
    if all(count == 1 for count in die_counts):
        score = 1200
    elif all(count == 2 for count in die_counts if count != 0):
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
        try:
            extra_dice.append(die_counts.index(1) + 1)
        except ValueError:
            pass
    elif 4 <= num_dice <= 6 and die_counts.count(4) == 1:
        for die, count in enumerate(die_counts):
            if count == 4:
                score = triple_score[die + 1] * 2
                break
        for die, count in enumerate(die_counts):
            if 1 <= count <= 2:
                extra_dice.append(die + 1)
    elif 3 <= num_dice <= 6 and 0 < die_counts.count(3) <= 2:
        for die, count in enumerate(die_counts):
            if count == 3:
                score = triple_score[die + 1]
                break
        for die, count in enumerate(die_counts):
            if 1 <= count <= 2:
                extra_dice.append(die + 1)
    else:
        score = 0

    if score == 0:
        return 0, *dice

    return score, *extra_dice
