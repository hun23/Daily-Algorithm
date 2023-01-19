import random


def making_card_list() -> list:
    card_list = []

    for shape in ["spade", "heart", "diamond", "clover"]:

        for number in [
            "A",
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            "J",
            "Q",
            "K",
        ]:

            card_list.append((shape, number))

    return card_list


def to_num(a):
    if a == "spade":
        return 4
    elif a == "diamond":
        return 3
    elif a == "heart":
        return 2
    elif a == "clover":
        return 1
    elif a == "A":
        return 14
    elif a == "K":
        return 13
    elif a == "Q":
        return 12
    elif a == "J":
        return 11
    return a


def get_winner(c1, c2):
    # 알파벳 및 문양 숫자로 변환
    p1 = tuple(map(to_num, c1))
    p2 = tuple(map(to_num, c2))
    # 후 숫자비교
    if p1[1] > p2[1]:
        return 1
    elif p1[1] < p2[1]:
        return 2
    if p1[0] > p2[0]:
        return 1
    else:
        return 2


# 같으면 문양비교

trump_card_list = making_card_list()
# 카드 섞기
random.shuffle(trump_card_list)
player1 = []
player2 = []
score1 = 0
score2 = 0
index = 0
while score1 < 6 and score2 < 6:
    # 카드뽑기
    card1 = trump_card_list.pop()
    card2 = trump_card_list.pop()
    player1.append(card1)
    player2.append(card2)
    # 승자비교
    winner = get_winner(card1, card2)
    if winner == 1:
        score1 += 1
    else:
        score2 += 1
    print(f"{card1} {card2} player{winner} win!")
print(
    f"{score1}:{score2} Finally player{1 if score1>score2 else 2} win"
)
