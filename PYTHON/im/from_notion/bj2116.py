import sys


def get_otherside(dice, side):
    idx = dice.index(side)
    if idx == 0:
        return dice[5]
    elif idx == 5:
        return dice[0]
    elif idx == 1:
        return dice[3]
    elif idx == 3:
        return dice[1]
    elif idx == 2:
        return dice[4]
    elif idx == 4:
        return dice[2]


def get_max_side(dice, side):
    idx = dice.index(side)
    sides = []
    if idx == 0 or idx == 5:
        sides += dice[1:5]
    elif idx == 1 or idx == 3:
        sides += dice[0] + dice[2:4] + dice[5]
    elif idx == 2 or idx == 4:
        sides += dice[:2] + dice[3] + dice[5]
    return max(sides)


n = int(input())
dices = []
for _ in range(n):
    dice = list(map(int, sys.stdin.readline().rstrip().split()))
    dices.append(dice)
_sum = 0
for side in dices[0]:
    _sum += get_max_side(dices[0], side)
# 위에 쌓기...?
