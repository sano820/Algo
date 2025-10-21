import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    num, change_cnt = input().split()
    change_cnt = int(change_cnt)

    q = deque([(num, 0)])   # (현재 숫자 문자열, 교환 횟수)
    visited = set()         # (숫자, 교환횟수) 중복 방지
    max_value = 0

    while q:
        current, cnt = q.popleft()

        # 교환 횟수를 다 썼으면 최댓값 갱신
        if cnt == change_cnt:
            max_value = max(max_value, int(current))
            continue

        n = len(current)
        num_list = list(current)

        for i in range(n):
            for j in range(i + 1, n):
                # 두 자리 교환
                num_list[i], num_list[j] = num_list[j], num_list[i]
                new_num = ''.join(num_list)

                if (new_num, cnt + 1) not in visited:
                    visited.add((new_num, cnt + 1))
                    q.append((new_num, cnt + 1))

                # 원상 복구
                num_list[i], num_list[j] = num_list[j], num_list[i]

    print(f"#{test_case} {max_value}")