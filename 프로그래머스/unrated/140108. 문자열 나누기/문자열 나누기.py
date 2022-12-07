def solution(s):
    answer = 0
    
    same = 0 #같은 알파벳 카운트
    diff = 0 #다른 알파벳 카운트
    start = True 
    
    for i in range(len(s)):
        if start == True:
            tmp = s[i]
            same += 1
            start = False
        else :
            if tmp == s[i] :
                same += 1
            else :
                diff += 1
        
            if same == diff :
                start = True
                answer += 1
                
        if i == (len(s) - 1) :
            if start == False :
                answer += 1
                
    return answer