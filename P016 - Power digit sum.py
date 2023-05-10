# Theoretically, I would have to write a bignum library myself...
# but I don't need to do that as I'm working with Python.

n = 2**1000
d = [int(k) for k in str(n)]
print(sum(d))