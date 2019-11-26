def score_hand(cards):
    score = 0 
    ace = 0 
    for i in cards:
        if i == 'A' : ace += 1 ; score += 1 
        elif i in ['K','Q','J'] : score += 10 
        else: 
            score += int(i)
    for i in range(1,ace+1,1):
        if score + 10 <= 21 : score += 10
        else: 
            break
    return score