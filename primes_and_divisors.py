def is_prime(number:int):
    """Diz se um numero é primo ou não"""
    if number <= 1: #failsafe
        return False
    for i in range(2, (number+1)//2):
        print(i)
        if number % i == 0:
            return False
    return True

def get_primes(number:int):
    """Encontra os numeros primos até o número solicitado"""
    primes = []
    if number <= 1: #failsafe
        return primes
    for i in range(2, number):
        if is_prime(i):
            primes.append(i)
    return primes

def number_of_primes(number:int):
    """Devolve a  quantidade de numeros primos entre 1 e o numero desejado"""
    nprimes = 0
    if number <= 1: #failsafe
        return nprimes
    for i in range(2, number):
        if is_prime(i):
            nprimes += 1
    return nprimes

def get_divisors(number:int):
    """Devolve um tupple (lista de divisores, quantidade de divisores)"""
    divisors = []
    for i in range(2, number+1):
        if number % i == 0:
            divisors.append(i)
    return (divisors, len(divisors))

# def gets_mdc():
# def gets_mmc():
print(is_prime(29))