import random

def crivo_de_eratostenes(limite=1000):
    """
    Implementa o algoritmo do Crivo de Eratóstenes para encontrar
    todos os números primos até um determinado limite.
    Retorna uma lista de números primos.
    """
    # 1. Cria uma lista de booleanos (True = Primo, False = Não Primo)
    # Inicialmente, assumimos que todos são primos.
    # Índices 0 e 1 são marcados como False.
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False

    # 2. O algoritmo iterativo
    p = 2
    while (p * p <= limite):
        # Se primos[p] não foi alterado, então é um primo
        if primos[p] == True:
            # Atualiza todos os múltiplos de p
            for i in range(p * p, limite + 1, p):
                primos[i] = False
        p += 1

    # 3. Coleta os índices que permaneceram True
    lista_primos = [p for p in range(limite + 1) if primos[p]]
    return lista_primos

def selecionar_primos_distintos():
    """
    Gera uma lista de primos usando o Crivo e seleciona 
    aleatoriamente dois primos distintos (p e q).
    Usamos um limite razoável (ex: 500) para garantir que n = p*q
    seja maior que o valor de um caractere ASCII padrão (255).
    """
    # Geramos primos até 1000 para ter uma boa variedade
    lista = crivo_de_eratostenes(1000)
    
    # Filtramos primos muito pequenos para evitar problemas de segurança trivial
    # (n deve ser maior que o maior caractere possível, ex: 255)
    lista = [p for p in lista if p > 50] 

    if len(lista) < 2:
        raise ValueError("Intervalo muito pequeno para encontrar dois primos distintos.")

    p = random.choice(lista)
    q = random.choice(lista)

    # Garante que p e q sejam distintos
    while p == q:
        q = random.choice(lista)

    return p, q