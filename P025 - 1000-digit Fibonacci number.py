cache = {0:1, 1:1}

def get_nth_fibonacci(nth: int) -> int:
    
    # We're going to store results in our cache!
    global cache
    if nth not in cache.keys():
        cache[nth] = get_nth_fibonacci(nth - 2) + get_nth_fibonacci(nth - 1)
    
    return cache[nth]

def get_digit_count(n: int) -> int:
    return len(str(n))

# Where stuff happens
index = 0
while True:
    f = get_nth_fibonacci(index)
    if get_digit_count(f) >= 1000:
        break
    index += 1
    
print(f"Index = {index + 1}")
