def generate_hashtag(s):
    ans = "#"
    check = False
    if len(s) == 0 : return False
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] == " " :continue
        ans += s[i].capitalize()
    if len(ans) > 140 : return False
    return ans