def count_primes(a, b):
    count = 0
    for num in range(a, b+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            count += 1
    return(count)