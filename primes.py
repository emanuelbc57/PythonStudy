
def is_prime(number):
    """Diz se um numero é primo ou não"""
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def get_primes(number):
    """Encontra os numeros primos de 2 até o número solicitado"""
    primes = []
    if number <= 1:
        return primes
    for i in range(2, number):
        if is_prime(i):
            primes.append(i)
    return primes
