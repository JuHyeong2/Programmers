def solution(s):
    answer = []
    for i, c1 in enumerate(s):
        s_indexing = s[:i]
        same_count = 0
        index_count = 0
        for j, c2 in enumerate(s_indexing):
            if c1 == c2:
                same_count = same_count + 1
                index_count = len(s_indexing) - j

        if same_count == 0:
            answer.append(-1)
        else:
            answer.append(index_count)
    return answer

print(solution('banana'))