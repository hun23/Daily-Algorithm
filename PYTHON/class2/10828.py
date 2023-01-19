import sys

class new_stack:
    def __init__(self, arr):
        self.arr = arr
    
    def get_size(self):
        return len(self.arr)

    def is_empty(self):
        if self.get_size() == 0:
            return 1
        else:
            return 0

    def do_pop(self):
        if self.is_empty():
            return -1
        else:
            temp = self.arr[-1]
            del self.arr[-1]
            return temp

    def get_top(self):
        if self.is_empty():
            return -1
        else:
            return self.arr[-1]
    
    def do_push(self, num):
        self.arr.append(num)
        return None

def check_order(s):
    # push인 경우 order, num 분리
    if s[:2] == "pu":
        order = s.split()[0]
        num = int(s.split()[1])
        return order, num
    else:
        order = s
        return order ,None

def do_order(order ,stack, num):
    if order == "pop":
        return stack.do_pop()
    elif order == "size":
        return stack.get_size()
    elif order == "empty":
        return stack.is_empty()
    elif order == "top":
        return stack.get_top()
    elif order == "push":
        return stack.do_push(num)

n = int(input())
arr = []
for _ in range(n):
    # 입력
    inp = sys.stdin.readline().rstrip()
    #인스턴스 생성
    stack = new_stack(arr)
    # 어떤 명령인지 확인
    order, num = check_order(inp)
    # 해당 명령 stack에 수행
    out = do_order(order, stack, num)
    if out != None:
        print(out)
