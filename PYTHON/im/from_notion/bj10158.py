w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

pp = p + t % (w * 2)
qq = q + t % (h * 2)
print(min(pp, w * 2 - pp), min(qq, h * 2 - qq))
