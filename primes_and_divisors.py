def is_prime(num:int): # escrita auxiliada por IA para melhora de desempenho
    """
    Diz se um numero é primo.
    
    ARGS
        num (int): numero a ser verificado

    RETURNS
        bool: True para numeros primos, False caso contrário

    EXEMPLOS:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
    
    NOTE:
        Zero, um, e números negativos não são considerados números primos e a função retornará False
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

def get_primes(num:int):
    """
    Encontra os numeros primos até o número solicitado
    
    ARGS:
        num(int): numero topo a ser verificado

    RETURNS:
        list: lista com os numeros primos encontrados até o numero topo
       
    EXEMPLOS:
        >>> get_primes(10)
        [2, 3, 5, 7]
        >>> get_primes(5)
        [2, 3, 5]
    NOTE:
        Se um numero menor que 2 for passado, a função retornará uma lista vazia
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
    
    ARGS:
        num(int): numero topo a ser verificado

    RETURNS:
        list: lista com os numeros primos encontrados até o numero topo
       
    EXEMPLOS:
        >>> get_primes(30)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        >>> get_primes(5)
        [2, 3, 5]
        
    NOTE:
        Se um numero menor que 2 for passado, a função retornará uma lista vazia
"""
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

def get_divisors(num:int):
    """
    Retorna os divisores de um numero e o sua quantidade
    
    ARGS
        num(int): numero a ser avaliado
        
    RETURNS
        tuple: Uma tupla contendo:
            - list: Uma lista com todos os divisores de `number`, em ordem crescente.
            - int: A quantidade total de divisores encontrados.

    EXEMPLOS:
        >>> get_divisors(28)
        ([1, 2, 4, 7, 14, 28], 6)
        
        >>> get_divisors(16)
        ([1, 2, 4, 8, 16], 5)
    
    NOTE:
        Se um número não positivo for passado, a função retornará uma lista vazia e 0 como quantidade de divisores.
        """
    
    divisors = []
    for i in range(1, int(num**0.5 + 1)):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num//i)
    divisors.sort()
    return (divisors, len(divisors))

# def gets_mdc():
# def gets_mmc():


