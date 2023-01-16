def solution(t, p):
    answer = 0
    p_len = len(p)
    p_int = int(p)
    start_i = -1

    for i in range(len(t)+1):
        if i >= p_len:
            start_i = start_i + 1
            t_substring = t[start_i:i]
            t_subint = int(t_substring)
            if t_subint <= p_int:
                answer = answer + 1
    return answer

print(solution("10203", "15"))