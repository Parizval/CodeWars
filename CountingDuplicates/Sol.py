def duplicate_count(text):
    text = text.lower()
    ans = 0 
    extra = list(set(text))
    ans = 0 
    for i in extra:
        if text.count(i) > 1 : 
            ans += 1
    return ans 