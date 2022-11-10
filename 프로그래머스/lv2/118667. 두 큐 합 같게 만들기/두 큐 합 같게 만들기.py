def solution(q1, q2):
    import collections
    n = len(q1)
    q1, q2 = collections.deque(q1), collections.deque(q2)
    sum1, sum2 = sum(q1), sum(q2)
    ans = 0

    while sum1 != sum2:
        if sum1 > sum2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum1 -= tmp
            sum2 += tmp

        elif sum2 > sum1:
            tmp = q2.popleft()
            q1.append(tmp)
            sum1 += tmp
            sum2 -= tmp

        ans += 1

        if ans > 4 * n:
            return -1
    return ans
