"""
🔹 O que é um algoritmo?

Um algoritmo é simplesmente um passo a passo lógico para resolver um problema.
Tipo uma receita de bolo 🍰:

Pegue os ingredientes
Misture
Asse
Sirva

Na programação é a mesma lógica, só que usando comandos.
"""
# 🔹 Comandos e Entrada de Dados
"""
Aqui você aprende a:
Mostrar informações → print()
Receber dados do usuário → input()
Exemplo simples:

"""
name = input("Digite seu nme: ") # Recebe o nome do usuário
print("Olá", name) # Mostra uma saudação com o nome

# 🔹 Operadores
"""
Usados para comparar valores (retornam True ou False):
> maior
< menor
>= maior ou igual
<= menor ou igual
== igual
!= diferente
"""
print (5 > 3) # True
print (5 == 3) # False

# 🔹 Operadores Lógicos
"""
Sevem para combinar condições:
and → e
or → ou
not → não
"""
idade = 18
print(idade >= 18) and idade < 65 ) 

# 🔹 Operadores
"""
Eles servem para fazer contas e comparações.

➕ Operadores Aritméticos

+ soma
- subtração
* multiplicação
/ divisão
"""
a = 10
b = 2
print(a + b)

# ➖ Subtração (-) Subtrai um valor do outro.

a = 10
b = 5
resultado = a - b
print(resultado)  # 5

# ✖️ Multiplicação (*) Multiplica valores.

a = 10
b = 5
resultado = a * b
print(resultado)  # 50

# ➗ Divisão (/) Sempre retorna float (número com decimal).

a = 10
b = 4
resultado = a / b
print(resultado)  # 2.5

# ➗ Divisão inteira (//) Retorna só a parte inteira da divisão.

a = 10
b = 4
resultado = a // b
print(resultado)  # 2

# 🔺 Exponenciação (**) Um número elevado a outro.

a = 2
b = 3
resultado = a ** b
print(resultado)  # 8

# 🔁 Módulo / Resto (%) Retorna o resto da divisão.

a = 10
b = 3
resultado = a % b
print(resultado)  # 1

# 🧠 Exemplo juntando tudo

a = 7
b = 2

print(a + b)   # 9
print(a - b)   # 5
print(a * b)   # 14
print(a / b)   # 3.5
print(a // b)  # 3
print(a ** b)  # 49
print(a % b)   # 1

#✅ Ordem de precedência
"""
1️⃣ Parênteses  ( ) 👉 Sempre vêm primeiro

2️⃣ Exponenciação **

3️⃣ Multiplicação e divisão *   /   //   % 👉 Todos têm a mesma prioridade

4️⃣ Adição e subtração +   -



# 📦 Variáveis em Python
"""
Variável é um espaço na memória para guardar um valor.
🔹 Criando variáveis
"""
idade = 18
nome = "Maria"
altura = 1.65
aprovado = True
print(nome, "tem", idade , "anos.", "sua altura é", altura, "metros" )

"""
👉 Python descobre o tipo sozinho:
int → números inteiros
float → números decimais
str → texto
bool → verdadeiro ou falso
"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Nome:", nome)
print("Idade:", idade)

#⚠️ Importante: input() sempre vem como texto, por isso usamos int() ou float().