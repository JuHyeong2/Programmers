

def solution(today, terms, privacies):
    answer = []
    terms_value_list = [] # term의 약관종류
    terms_month_list = [] # term의 유효기간
    privacy_month_list = [] # privacies의 유효기간
    today_year = int(today.split('.')[0])
    today_month = int(today.split('.')[1])
    today_day = int(today.split('.')[2])
    for i, term in enumerate(terms):
        term_value = term.split(' ')
        terms_value_list.append(term_value[0])
        terms_month_list.append(term_value[1])

    for i, privacy in enumerate(privacies):
        privacy_list = privacy.split(' ')
        privacy_value = privacy_list[1]
        for j, terms_value in enumerate(terms_value_list):
            if privacy_value == terms_value:
                privacy_month_list.append(terms_month_list[j])
        privacy_year, privacy_month, privacy_day = map(int, privacy_list[0].split('.'))

        # privacies의 날짜에 해당하는 유효기간(월) 을 더해준다.
        privacy_date_plus_term = privacy_month + int(privacy_month_list[i])

        # 유효기간(월)이 12를 넘어갈 경우 12이하가 될때 까지 유효기간(년)에 +1을 해주고 유효기간(월)에 -12를 해준다.
        while privacy_date_plus_term > 12:
            privacy_year = privacy_year + 1
            privacy_date_plus_term = privacy_date_plus_term - 12

        # 유효기간(일)에 -1을 해주고 0이 될경우 28로 바꿔주고 유효기간(월)에 -1을 해준다.
        privacy_day = privacy_day - 1
        if privacy_day == 0:
            privacy_day = 28
            privacy_date_plus_term = privacy_date_plus_term - 1

            # 유효기간(월)이 0이 될경우 유효기간(년)에 -1을 해주고 유효기간(월)을 12로 바꿔준다.
            if privacy_date_plus_term == 0:
                privacy_year = privacy_year - 1
                privacy_date_plus_term = 12

        # 유효기간과 오늘날짜를 년 -> 월 -> 일 순으로 비교한다.
        if today_year > privacy_year:
            answer.append(i + 1)
        elif today_year < privacy_year:
            continue
        else:
            if today_month > privacy_date_plus_term:
                answer.append(i + 1)
            elif today_month < privacy_date_plus_term:
                continue
            else:
                if today_day > privacy_day:
                    answer.append(i + 1)
                elif today_day < privacy_day:
                    continue
    return answer
