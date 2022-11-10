def solution(survey, choices):
    scores = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(survey)):
        choice = choices[i]
        element = survey[i]
        if choice == 1:
            scores[element[0]] += 3
        elif choice == 2:
            scores[element[0]] += 2
        elif choice == 3:
            scores[element[0]] += 1
        elif choice == 4:
            scores[element[0]] += 0
        elif choice == 5:
            scores[element[1]] += 1
        elif choice == 6:
            scores[element[1]] += 2
        else:
            scores[element[1]] += 3
    print(scores)
    answer = ""
    if scores['R'] < scores['T']:
        answer += 'T'
    else:
        answer += 'R'
    if scores['C'] < scores['F']:
        answer += 'F'
    else:
        answer += 'C'
    if scores['J'] < scores['M']:
        answer += 'M'
    else:
        answer += 'J'
    if scores['A'] < scores['N']:
        answer += 'N'
    else:
        answer += 'A'
    return answer