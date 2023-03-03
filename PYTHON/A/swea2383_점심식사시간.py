def get_min_len(st, stair_num):
    # stair
    wait_list, on_stair = [], []
    for person in st:
        pr, pc = peoples[person]
        sr, sc, v = stairs[stair_num]
        d = abs(sr - pr) + abs(sc - pc) + 1  # len + wait to start(1)
        wait_list.append(d)
    wait_list.sort()

    # until on_stair and wait_list is empty
    time_sum = 0
    while on_stair or wait_list:
        if len(on_stair) < 3 and wait_list:  # wait_list to on_stair
            on_stair.append(wait_list.pop(0) + v)
        # if on_stair is full or wait_list is empty
        else:
            # min time to delete at least one item on on_stair
            time_passed = min(on_stair) 
            time_sum += time_passed
            for i in range(len(on_stair)):
                on_stair[i] -= time_passed

            # delete passed one
            while on_stair:
                if on_stair[0] <= 0:
                    del on_stair[0]
                else:
                    break
            
            # update time remaining on wait_list
            for j in range(len(wait_list)):
                wait_list[j] -= time_passed
                if wait_list[j] < 0:
                    wait_list[j] = 0
    return time_sum


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # get people / stair coordinates
    peoples, stairs = {}, {}
    p_idx, s_idx = 0, 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                peoples[p_idx] = (r, c)
                p_idx += 1
            elif arr[r][c]:
                stairs[s_idx] = (r, c, arr[r][c])
                s_idx += 1

    # recursion / backtasking
    answer = 2147483647
    for i in range(1<<p_idx):
        st1, st2 = [], []
        # set person - stair pair
        for j in range(p_idx):
            if i & (1<<j):
                st1.append(j) # first stair
            else:
                st2.append(j)  # second stair
        temp = max(get_min_len(st1, stair_num=0), get_min_len(st2, stair_num=1))
        answer = min(answer, temp)
    print(f"#{tc} {answer}")
