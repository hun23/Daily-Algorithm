xlen, ylen = map(int, input().split())
N = int(input())
shops = []
for n in range(N):
    a, b = map(int, input().split())
    shops.append((a, b))
    # if a <= 2:
    #     shops.append((b, (2 - a) * ylen))
    # else:
    #     shops.append(((a - 3) * xlen, ylen - b))
dga, dgb = map(int, input().split())
# print(shops)
dis = 0
for (a, b) in shops:
    temp = 0
    if dga == a:  # 같은 쪽
        temp += abs(b - dgb)
    elif dga <= 2 and 2 < a <= 4:  # 양쪽 중 하나
        if a == 3:
            temp += dgb + (ylen - b) if dga == 2 else b
        else:
            temp += xlen - dgb + (ylen - b) if dga == 2 else b
    elif 2 < dga <= 4 and a <= 2:  # 양쪽 중 하나
        if a == 1:
            temp += dgb + (xlen - b) if dga == 4 else b
        else:
            temp += (ylen - b) + (xlen - b) if dga == 4 else b
    else:  # 반대쪽
        temp += min(dgb, xlen - dgb) * 2 + abs(b - dgb) + ylen
    dis += temp
    # print(temp)
print(dis)
