# 입력
n, k = map(int, input().split())
students = []
for _ in range(n):
    s, y = map(int, input().split())
    students.append((s, y))
# 성별, 학년 순서로 정렬
students.sort(key=lambda x: (x[0], x[1]))
temp_stud = students[0]  # 첫번째 학생 저장
k_count = 0  # 한 방에 들어가는 학생 수 카운트
room_count = 0  # 방 개수 카운트
for stud in students[1:]:  # 첫번째 & 두번째 학생부터 비교
    if temp_stud != stud:  # 성별이나 학년이 다르면
        k_count = 0  # 한 방 학생 수 초기화
        room_count += 1  # 방 개수 추가
    else:
        k_count += 1  # 성별,학년이 같으면 한 방 학생수 추가

    if k_count == k:  # 한 방 학생수가 한계이면
        room_count += 1  # 방 개수 추가
        k_count = 0  # 한 방 학생수 초기화
    temp_stud = stud
print(room_count + 1)
