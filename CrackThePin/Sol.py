import hashlib
def crack(hash):
    for i in range(1000000):
        string = str(i) 
        string = "0"*(5-len(string)) + string
        res = hashlib.md5(string.encode())
        if res.hexdigest() == hash:
            return string