def is_prime(num:int): # escrita auxiliada por IA para melhora de desempenho
    """
    Diz se um numero é primo.
    Obs.: Zero (0), um (1) e números negativos não são considerados números primos.
    
    ARGS
        num (int): numero a ser verificado

    RETURNS
        bool: True para numeros primos, False caso contrário

    EXEMPLOS:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
    """
    if num <= 1: #failsafe
        return False
    if num <= 3: #identifica 2 e 3
        return True
    if num % 2 == 0 or num % 3 == 0: # descarta multiplos de 2 e 3
        return False
    # Todo numero maior que 3 pode ser escrito:
    #   ou como um múltiplo de 2 (já descartados)
    #   ou como um múltiplo de 3 (já descartados)
    #   ou como 6k (já descartados nos multiplos de dois e 3)
    #   ou como (6k +/- 1), que são os numeros que serão iterados na proxima sessão
    i = 5 
    while i * i < num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_prime_sieve(num:int):
    return num in get_primes_sieve(num)

def get_primes(num:int):
    """
    Encontra os numeros primos até o número solicitado
    Obs: Para o caso de números menores que 2 (<2), a função retornará uma lista vazia

    ARGS:
        num(int): numero topo a ser verificado

    RETURNS:
        list: lista com os numeros primos encontrados até o numero topo
       
    EXEMPLOS:
        >>> get_primes(10)
        [2, 3, 5, 7]
        >>> get_primes(5)
        [2, 3, 5]
    """
    primes = []
    if num < 2: #failsafe
        return primes
    
    primes.append(2)

    for i in range(3, num+1, 2):
        if is_prime(i):
            primes.append(i)
    return primes

def get_primes_sieve(num:int): #escrita auxiliada por IA
    """
    Encontra os numeros primos até o número solicitado
    Obs: Para o caso de números menores que 2 (<2), a função retornará uma lista vazia

    ARGS:
        num(int): numero topo a ser verificado

    RETURNS:
        list: lista com os numeros primos encontrados até o numero topo
       
    EXEMPLOS:
        >>> get_primes(30)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        >>> get_primes(5)
        [2, 3, 5]"""
     # Cria uma lista chamada sieve com num + 1 elementos, todos inicializados como True
    sieve = [True] * (num+1) 
    sieve[0] = sieve[1] = False # 0 e 1 não são numeros primos

    # Marca os multiplos do numero primo como false
    for number in range(2, int(num**0.5) + 1):
        if sieve[number]: # identifica numero primo - valor inicial True)
            for multiple in range(number * number, num+1, number):
                sieve[multiple] = False
    
    # Extrai os primos da lista sieve pelo indice i
    primes = [i for i in range(num+1) if sieve[i]]
    return primes

def number_of_primes(num:int):
    """
    Retorna a quantidade de numeros primos de zero até o numero de entrada
    
    ARGS
        num(int): numero topo a ser verificado
        
    RETURNS
        int: numero de numeros primos de 0 até o numero limite
        
    EXEMPLOS
        >>> number_of_primes(10)
        4
        >>> number_of_primes(100)
        25
    """
    return len(get_primes_sieve(num))

def get_divisors(number:int):
    """Devolve um tupple (lista de divisores, quantidade de divisores)"""
    divisors = []
    for i in range(2, number+1):
        if number % i == 0:
            divisors.append(i)
    return (divisors, len(divisors))

# def gets_mdc():
# def gets_mmc():

print(number_of_primes(10))   # Deve retornar 4, pois os primos até 10 são [2, 3, 5, 7]
print(number_of_primes(100))  # Deve retornar 25, pois há 25 números primos até 100
print(number_of_primes(1000))

import timeit

def test_is_prime_performance():
    # Definir o intervalo de números para o teste
    test_range = [100, 1000, 10000, 100000, 1000000]
    
    for num in test_range:
        # Função de teste que chama is_prime para todos os números de 1 até num
        def test_is_prime():
            for i in range(1, num + 1):
                is_prime(i)

        # Medir o tempo de execução
        execution_time = timeit.timeit(test_is_prime, number=10)
        print(f"Tempo total para verificar números primos até {num}: {execution_time:.4f} segundos")


def test_is_prime_sieve_performance():
    # Definir o intervalo de números para o teste
    test_range = [100, 1000, 10000, 100000, 1000000]
    
    for num in test_range:
        # Função de teste que chama is_prime para todos os números de 1 até num
        def test_is_prime_sieve():
            for i in range(1, num + 1):
                is_prime_sieve(i)

        # Medir o tempo de execução
        execution_time = timeit.timeit(test_is_prime_sieve, number=10)
        print(f"Tempo total para verificar números primos até {num}: {execution_time:.4f} segundos")
# Chama o teste de desempenho
test_is_prime_performance()
test_is_prime_sieve_performance()