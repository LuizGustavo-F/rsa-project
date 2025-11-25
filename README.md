# 🔐 Implementação do Algoritmo RSA

**Disciplina:** Segurança em Sistemas de Computação  
**Linguagem:** Python 3

Este repositório contém uma implementação completa e didática do algoritmo de criptografia assimétrica RSA (Rivest-Shamir-Adleman). O projeto foi desenvolvido para demonstrar a geração de chaves, a matemática modular e o processo de cifragem/decifragem, cumprindo todos os requisitos propostos no trabalho acadêmico.

---

## 📋 Tabela de Conteúdos

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Estrutura de Arquivos](#estrutura-de-arquivos)
- [Pré-requisitos e Instalação](#pré-requisitos-e-instalação)
- [Como Executar](#como-executar)
- [Exemplo de Uso](#exemplo-de-uso)
- [Fundamentação Teórica](#fundamentação-teórica)
- [Autores](#autores)
 

---

## 📖 Sobre o Projeto
O objetivo deste software é simular o funcionamento real do RSA. Diferente de bibliotecas prontas que escondem a matemática, este projeto implementa cada etapa "do zero", incluindo a geração de números primos e o cálculo de inverso modular.

O sistema permite que o usuário digite uma mensagem de texto, converte-a para hexadecimal, cifra caractere por caractere utilizando chaves geradas dinamicamente e, por fim, descriptografa para provar a integridade da mensagem.

---

## 🚀 Funcionalidades

- **Geração de Primos (Crivo de Eratóstenes):** Implementação do algoritmo clássico para encontrar números primos reais para `p` e `q`.
- **Geração de Chaves Automática:**
  - Cálculo do módulo `n` e do totiente `φ(n)`
  - Seleção automática do expoente público `e`
  - Cálculo do expoente privado `d` (Inverso Modular)
- **Conversão Hexadecimal:** Exibição da mensagem em formato hexadecimal antes da cifragem.
- **Criptografia:** Aplicação da fórmula `C = M^e mod n`
- **Descriptografia:** Recuperação da mensagem via `M = C^d mod n`

---

## 📂 Estrutura de Arquivos

```
rsa_project/
│
├── src/
│   ├── primes.py      # Lógica do Crivo de Eratóstenes (Geração de p e q)
│   ├── rsa_core.py    # Núcleo matemático (MDC, Inverso Modular, Gerar Chaves)
│   └── utils.py       # Funções auxiliares (Texto <-> Hexadecimal)
│
├── main.py            # Arquivo principal (Menu Interativo e Execução)
├── .gitignore         # Arquivos ignorados pelo Git
└── README.md          # Documentação do projeto
```

---

## 🛠 Pré-requisitos e Instalação

Este projeto foi desenvolvido utilizando apenas as bibliotecas padrão do Python 3.  
Não é necessário instalar pacotes externos via pip.

### Requisitos:
- Python **3.8** ou superior

### Instalação:

Clone o repositório:

```
git clone https://github.com/SEU-USUARIO/rsa-project.git
```

Acesse a pasta:

```
cd rsa-project
```

---

## ▶️ Como Executar

Execute o programa:

```
python main.py
```

O programa gerará automaticamente as chaves e solicitará a mensagem para criptografar.

---

## 📊 Exemplo de Uso

```
=== IMPLEMENTAÇÃO DO ALGORITMO RSA ===
Disciplina: Segurança em Sistemas de Computação
------------------------------------------

[1] Gerando números primos p e q via Crivo de Eratóstenes...
    -> Primo p gerado: 151
    -> Primo q gerado: 313

[2] Calculando chaves RSA...
    -> Módulo n (p*q): 47263
    -> Função Totiente phi(n): 46800
    -> Chave Pública (e, n): (7, 47263)
    -> Chave Privada (d, n): (26743, 47263)

------------------------------------------
Digite a mensagem para criptografar: carro

[3] Representação Hexadecimal da mensagem:
    -> 636172726f

[4] Criptografando (C = M^e mod n)...
    -> Mensagem Cifrada (Lista de Inteiros): [18566, 17100, 1807, 1807, 33736]
    -> Visualização Hex dos Blocos Cifrados: 4886 42CC 70F 70F 83C8

[5] Descriptografando (M = C^d mod n)...
    -> Mensagem Recuperada: carro

✔ SUCESSO: A mensagem recuperada é idêntica à original.
```

---

## 🧠 Fundamentação Teórica

O algoritmo baseia-se na dificuldade computacional de fatorar grandes números inteiros. Suas etapas incluem:

### 1. Escolha de Primos:
Seleção de dois números primos `p` e `q`.

### 2. Cálculo do Módulo:
$$
n = p \times q
$$


### 3. Função Totiente de Euler:
$$
\phi(n) = (p - 1)(q - 1)
$$


### 4. Chave Pública:
Escolher `e` tal que:
- `1 < e < φ(n)`
- `mdc(e, φ(n)) = 1`

### 5. Chave Privada:
Encontrar `d` tal que:
Encontrar \( d \) tal que:

$$
d \times e \equiv 1 \pmod{\phi(n)}
$$


### 6. Cifragem:
$$
C = M^e \bmod n
$$
### 7. Decifragem:
$$
M = C^d \bmod n
$$

---

## 👥 Autores

- **Luiz G. F. Carvalho**  

---

> **Aviso:** Este projeto é puramente acadêmico e não deve ser utilizado para proteger dados sensíveis em produção, pois utiliza primos pequenos para fins de demonstração.


