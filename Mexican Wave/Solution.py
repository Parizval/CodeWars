def wave(str):
    ans = []
    for i in range(len(str)):
        if str[i] == " ": continue
        ans.append(str[:i] + str[i].upper() + str[i+1:])
    return ans