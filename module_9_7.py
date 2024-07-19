
def is_prime(func):
    def wrapper(*number):
        n = func(*number)
        dn = 2
        while dn*dn <= n and n % dn == 0: dn += 1
        print("Составное") if dn*dn > n else print("Простое")
        return n
    return wrapper


@is_prime
def sum_three(*number):
    return sum(number)


result = sum_three(2, 3, 6)
print(result)
