import binascii

def texto_para_hex(texto):
    """
    Converte uma string de texto para sua representação hexadecimal.
    Ex: 'A' -> '41'
    """
    # Converte string para bytes, depois para hex bytes, depois decodifica para string
    return binascii.hexlify(texto.encode('utf-8')).decode('utf-8')

def hex_para_texto(hex_string):
    """
    Converte uma string hexadecimal de volta para texto.
    Ex: '41' -> 'A'
    """
    try:
        return binascii.unhexlify(hex_string).decode('utf-8')
    except Exception as e:
        return f"[Erro na conversão: {e}]"

def caractere_para_int(char):
    """Converte um caractere em seu valor inteiro (ASCII/Unicode)."""
    return ord(char)

def int_para_caractere(codigo):
    """Converte um valor inteiro de volta para caractere."""
    try:
        return chr(codigo)
    except:
        return '?'