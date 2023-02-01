# 입력
T = int(input())
for tc in range(1, T + 1): # 1번부터 T번 테스트케이스까지
    N = int(input())
    boxes = list(map(int, input().split()))
    mx = 0 # 최대값 체크
    for (i, box) in enumerate(boxes):
        count = 0
        for right_box in boxes[i + 1:]: # 오른쪽 박스기둥 중에서
            if box > right_box: # 작은게 있으면
                count += 1 # 센다
        if count > mx: # 기존 max보다 크면
            mx = count # 바꾸기
    print(f"#{tc} {mx}")