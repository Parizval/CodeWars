def is_valid_walk(walk):
    if len(walk) != 10 : return False
    if walk.count('n') - walk.count('s') == 0 and walk.count('e') - walk.count('w') == 0 : 
        return True
    return False