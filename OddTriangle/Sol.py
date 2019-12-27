def odd_row(n):
    ans = []
    start = n**2 - (n-1)
    ans.append(start)
    for i in range(n-1):
        start += 2
        ans.append(start)
    return ans