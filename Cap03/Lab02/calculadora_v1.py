# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

def soma(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mult(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

print("\nSelecione o número da operação desejada: ")

print("\n1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("\nDigite sua opção (1/2/3/4): "))
n1 = int(input("\nDigite o primeiro número: "))
n2 = int(input("\nDigite o segundo número: "))

if opcao == 1:
    print(n1, "+", n2, "=", soma(n1,n2))
elif opcao == 2:
    print(n1, "-", n2, "=", sub(n1,n2))
elif opcao == 3:
    print(n1, "x", n2, "=", mult(n1,n2))
elif opcao == 4:
    print(n1, "/", n2, "=", div(n1,n2))
else:
    print("Opção inválida")



