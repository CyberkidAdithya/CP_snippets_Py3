def gcd_iter(a, b):
    while(b):
        a, b = b, a % b
    return a
# gcd_iter(13, 19)

def gcd_recur(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
# gcd_recur(13, 19)
