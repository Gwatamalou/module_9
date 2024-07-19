
def is_prime(func):
    def wrapper():
        n = func()
        dn = 2
        while dn*dn <= n and n % dn == 0: dn += 1
        return n, dn
    return wrapper
def sum_three(*number: int) -> int:
    return sum(number)
