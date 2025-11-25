import math

def mdc(a, b):
    """Calcula o Máximo Divisor Comum (Algoritmo de Euclides)."""
    while b:
        a, b = b, a % b
    return a

def inverso_modular(e, phi):
    """
    Calcula o inverso modular d, tal que (d * e) % phi == 1.
    Usa a função pow nativa do Python 3.8+ que suporta inverso modular.
    Isso é equivalente ao Algoritmo de Euclides Estendido.
    """
    try:
        return pow(e, -1, phi)
    except ValueError:
        raise ValueError("O inverso modular não existe (e não é coprimo de phi).")

def gerar_chaves(p, q):
    """
    Gera as chaves pública e privada com base nos primos p e q.
    Retorna: ((e, n), (d, n))
    """
    # 1. Calcular n (o módulo)
    n = p * q

    # 2. Calcular a função totiente de Euler phi(n)
    phi = (p - 1) * (q - 1)

    # 3. Escolher e (expoente público)
    # e deve ser: 1 < e < phi E coprimo de phi (mdc(e, phi) == 1)
    # Geralmente usamos primos pequenos como 3, 17, 65537 por eficiência.
    # Aqui, vamos buscar o menor 'e' possível que satisfaça a condição, começando de 3.
    e = 3
    while mdc(e, phi) != 1:
        e += 2

    # 4. Calcular d (expoente privado)
    # d é o inverso modular de e em relação a phi
    d = inverso_modular(e, phi)

    # Chave Pública: (e, n)
    # Chave Privada: (d, n)
    return ((e, n), (d, n))

def criptografar_rsa(mensagem_plain, chave_publica):
    """
    Criptografa uma mensagem usando a fórmula C = M^e mod n.
    Para fins didáticos, criptografamos caractere por caractere.
    
    Args:
        mensagem_plain (str): Texto original.
        chave_publica (tuple): (e, n)
    
    Returns:
        list: Lista de inteiros cifrados.
    """
    e, n = chave_publica
    mensagem_cifrada = []

    for char in mensagem_plain:
        # Converte char para inteiro (M)
        m = ord(char)
        
        # Verifica se o bloco (M) é menor que o módulo (n)
        # Se m >= n, a matemática do RSA falha para aquele bloco
        if m >= n:
            raise ValueError(f"Erro: O módulo n ({n}) é muito pequeno para cifrar o caractere '{char}' ({m}). Gere primos maiores.")

        # Aplica a fórmula: C = M^e mod n
        c = pow(m, e, n)
        mensagem_cifrada.append(c)

    return mensagem_cifrada

def descriptografar_rsa(mensagem_cifrada_lista, chave_privada):
    """
    Descriptografa uma lista de inteiros usando a fórmula M = C^d mod n.
    
    Args:
        mensagem_cifrada_lista (list): Lista de inteiros cifrados.
        chave_privada (tuple): (d, n)
    
    Returns:
        str: Mensagem original recuperada.
    """
    d, n = chave_privada
    mensagem_recuperada = ""

    for c in mensagem_cifrada_lista:
        # Aplica a fórmula: M = C^d mod n
        m = pow(c, d, n)
        
        # Converte inteiro de volta para char
        mensagem_recuperada += chr(m)

    return mensagem_recuperada