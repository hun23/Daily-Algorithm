import sys


class my_deque:
    def __init__(self, q):
        self.q = q

    def check_order(self, inp):
        if inp == "pop_front":
            return self.pop_front()
        elif inp == "pop_back":
            return self.pop_back()
        elif inp == "size":
            return self.size()
        elif inp == "empty":
            return self.empty()
        elif inp == "front":
            return self.front()
        elif inp == "back":
            return self.back()

    def push_front(self, n):
        self.q.insert(0, n)
        return n

    def push_back(self, n):
        self.q.append(n)
        return n

    def pop_front(self):
        if self.empty():
            return -1
        ret = self.q[0]
        del self.q[0]
        return ret

    def pop_back(self):
        if self.empty():
            return -1
        ret = self.q[-1]
        del self.q[-1]
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
q = my_deque([])
for _ in range(n):
    inp = sys.stdin.readline().rstrip().split()
    # 인자가 2개면 -> push명령어
    if len(inp) != 1:
        if inp[0][-1] == "t":  # push_fron"t"
            q.push_front(int(inp[1]))
        else:
            q.push_back(int(inp[1]))
    else:
        ret = q.check_order(inp[0])
        print(ret)
