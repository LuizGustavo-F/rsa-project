import sys
from src.primes import selecionar_primos_distintos
from src.rsa_core import gerar_chaves, criptografar_rsa, descriptografar_rsa
from src.utils import texto_para_hex

def main():
    print("=== IMPLEMENTAÇÃO DO ALGORITMO RSA ===")
    print("Disciplina: Segurança em Sistemas de Computação")
    print("------------------------------------------")

    try:
        # 1. Geração de Primos (Crivo de Eratóstenes)
        print("\n[1] Gerando números primos p e q via Crivo de Eratóstenes...")
        p, q = selecionar_primos_distintos()
        print(f"    -> Primo p gerado: {p}")
        print(f"    -> Primo q gerado: {q}")

        # 2. Geração de Chaves
        print("\n[2] Calculando chaves RSA...")
        public_key, private_key = gerar_chaves(p, q)
        e, n = public_key
        d, _ = private_key
        
        print(f"    -> Módulo n (p*q): {n}")
        print(f"    -> Função Totiente phi(n): {(p-1)*(q-1)}")
        print(f"    -> Chave Pública (e, n): ({e}, {n})")
        print(f"    -> Chave Privada (d, n): ({d}, {n})")

        # 3. Entrada do Usuário
        print("\n------------------------------------------")
        msg_original = input("Digite a mensagem para criptografar: ")
        
        # 4. Conversão Hexadecimal (Pré-requisito do PDF)
        msg_hex = texto_para_hex(msg_original)
        print(f"\n[3] Representação Hexadecimal da mensagem:")
        print(f"    -> {msg_hex}")

        # 5. Criptografia
        print("\n[4] Criptografando (C = M^e mod n)...")
        # Nota: O RSA opera sobre números. Convertemos cada char para seu valor ASCII e ciframos.
        msg_cifrada = criptografar_rsa(msg_original, public_key)
        print(f"    -> Mensagem Cifrada (Lista de Inteiros): {msg_cifrada}")
        
        # Exibição bonita dos dados cifrados em Hex
        cifrada_hex = ' '.join([hex(c)[2:].upper() for c in msg_cifrada])
        print(f"    -> Visualização Hex dos Blocos Cifrados: {cifrada_hex}")

        # 6. Descriptografia
        print("\n[5] Descriptografando (M = C^d mod n)...")
        msg_recuperada = descriptografar_rsa(msg_cifrada, private_key)
        print(f"    -> Mensagem Recuperada: {msg_recuperada}")

        # Validação
        if msg_original == msg_recuperada:
            print("\n✅ SUCESSO: A mensagem recuperada é idêntica à original.")
        else:
            print("\n❌ ERRO: A mensagem recuperada difere da original.")

    except ValueError as ve:
        print(f"\nErro de configuração: {ve}")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()