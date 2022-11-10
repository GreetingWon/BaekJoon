def dfs(x, computers, visited): #dfs 정의, x는 노드
    visited[x] = True #x 노드에 대한 방문 처리
    for a, b in enumerate(computers[x]): #a는 x 노드의 index, b는 x 노드의 value
        if(b == 1 and (visited[a] == False)): #x 노드에 대해 연결되어있으면서, 방문한 적 없다면
           dfs(a, computers, visited) #해당 노드를 새로운 x 노드로 dfs 한다

def solution(n, computers):
    visited = n * [False] 
    answer = 0
    
    for i in range(len(computers)):
        if(visited[i] == False):
            dfs(i, computers, visited)
            answer += 1
            
    return answer