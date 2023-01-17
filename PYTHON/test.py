orders = "아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또"
orders = orders.split(",")
ice = 0
di = dict()
for menu in orders:
    if menu[:3] == "아이스":
        ice += 1
    if di.get(menu) == None:
        di[menu] = 1
    else:
        di[menu] += 1
print(ice)
print(di)
