def findpow_iter(a, b, m = int(1e9 + 7)):    #iterative
    res = 1 
    while b > 0:
        if b & 1:
            res = res * a % m
        a = a * a % m
        b >>= 1
    return res % m

def findpow_recur(a, b, m = int(1e9 + 7)):    #recursive
    if a == 0:
        return 0
    if b == 0:
        return 1
    tmp = findpow_recur(a, b // 2, m)
    if b % 2 == 0:
        return tmp * tmp % m
    else:
        return ((tmp * tmp % m) * a) % m
