numero = int(input("Digite um número: "))

fibonacci_anterior = 0
fibonacci_atual = 1

if numero == fibonacci_anterior or numero == fibonacci_atual:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:

    while fibonacci_atual < numero:
        fibonacci_proximo = fibonacci_anterior + fibonacci_atual
        fibonacci_anterior = fibonacci_atual
        fibonacci_atual = fibonacci_proximo

        if numero == fibonacci_atual:
            print(f"O número {numero} pertence à sequência de Fibonacci.")
            break
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")