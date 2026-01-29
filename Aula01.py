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