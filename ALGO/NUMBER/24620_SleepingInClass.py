T = int(input())
for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    # 일단 합치기
    total = sum(numbers)
    # 예외처리
    if total == 0:
        print(0)
        continue
    
    # 약수찾기
    divs = []
    for i in range(1, int(total**0.5) + 1):
        quo, rem = divmod(total, i)
        if rem == 0:
            divs.append(i)
            divs.append(quo)
    divs.sort(reverse=True)  # 역순으로 정렬하여 최대한 많은 칸을 가지도록(=최소 수정 횟수)
    
    # d 만큼의 칸을 가진 경우 각 칸의 숫자는 total//d이다
    for d in filter(lambda x:x<=N, divs):  # 시작 칸수 이하인 경우(=가능한경우)만 고려
        is_possible = True
        # 각 칸을 total//d로 채울 수 있는지 판단
        # 어떻게?
        # numbers를 돌면서 일단 합치기
        # total//d보다 큰게 있으면 종료
        target = total//d
        idx, temp_sum = 0, 0
        for num in numbers:
            temp_sum += num
            if temp_sum == target:  # 목표값 달성시 temp_sum 초기화 후 계속 합치기
                temp_sum = 0
            elif temp_sum > target:  # 커지면 불가능한 경우이므로 넘어가기
                is_possible = False
                break
            else:  # 작으면 그냥 계속 합치기
                pass
        if is_possible:
            print(N - d)  # 답은 원래 칸수(N)와 목표 칸수(d)와의 차이
            break
        