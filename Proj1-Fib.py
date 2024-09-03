numero = input("Digite um número para verificar se ele pertence à sequência de Fibonacci: ")

if numero.isdigit():
    numero = int(numero)
    
    a, b = 0, 1
    
    if numero == a or numero == b:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:

        while b < numero:
            a, b = b, a + b
        if b == numero:
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")
else:
    print("Por favor, digite um número inteiro válido.")



#O número é informado pelo input do usuário, a condição é verificada com a estrutura if else.
#Incluí também uma verificação para inputs inválidos.
