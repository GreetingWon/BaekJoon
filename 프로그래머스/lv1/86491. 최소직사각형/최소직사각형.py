def solution(sizes):
    answer = 0
    tmp = []
    imp = []
    
    for i in range(len(sizes)):
        tmp.append(0)
        imp.append(0)
        
        if(sizes[i][0] >= sizes[i][1]):
            tmp[i] = sizes[i][1]
            imp[i] = sizes[i][0]
        else:
            tmp[i] = sizes[i][0]
            imp[i] = sizes[i][1]
       
    answer = max(tmp)*max(imp)
    return answer