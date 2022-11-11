def find_p(p, n):
    while p[n] != n: #부모값이 자기 자신이면 root
        n = p[n]
    return n
    
def solution(n, costs):
    answer = 0
    parent = list(range(n)) #부모를 자기 자신으로 초기화
    c = sorted(costs, key = lambda x: x[2])
    
    for i in range(len(c)):
        p1 = find_p(parent, c[i][0])
        p2 = find_p(parent, c[i][1])
        if p1 != p2:
            parent[p2] = p1
            answer += c[i][2]
            
    return answer