import sys


class my_queue:
    def __init__(self, q):
        self.q = q

    def check_order(self, inp):
        if inp == "pop":
            return self.pop()
        elif inp == "size":
            return self.size()
        elif inp == "empty":
            return self.empty()
        elif inp == "front":
            return self.front()
        elif inp == "back":
            return self.back()

    def push(self, n):
        self.q.append(n)
        return n

    def pop(self):
        if self.empty():
            return -1
        ret = self.q[0]
        del self.q[0]
        return ret

    def size(self):
        return len(self.q)

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def front(self):
        if self.empty():
            return -1
        return self.q[0]

    def back(self):
        if self.empty():
            return -1
        return self.q[-1]


n = int(input())
# my_queue 클래스 생성
q = my_queue([])
for _ in range(n):
    inp = sys.stdin.readline().rstrip().split()
    # 인자가 2개면 -> push명령어
    if len(inp) != 1:
        q.push(int(inp[1]))
    else:
        ret = q.check_order(inp[0])
        print(ret)
