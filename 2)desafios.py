def fib(n):
    # Verifica se o número é menor que 0, pois Fibonacci não é definido para números negativos
    if n < 0:
        return "O número informado é inválido. Digite um número positivo."
    # Se o número for 0, retorna a sequência de Fibonacci como [0]
    elif n == 0:
        return [0]
    # Se o número for 1, retorna a sequência de Fibonacci como [0, 1]
    elif n == 1:
        return [0, 1]
    else:
        # Inicializa a lista com os dois primeiros valores da sequência de Fibonacci
        fib_list = [0, 1]
        # Enquanto o último valor da lista for menor que n, continua adicionando valores à lista
        while fib_list[-1] < n:
            # Adiciona o próximo valor à lista como a soma dos dois valores anteriores
            next_value = fib_list[-1] + fib_list[-2]
            fib_list.append(next_value)
        # Verifica se o número informado pertence à sequência de Fibonacci
        if n in fib_list:
            return f"O número {n} pertence à sequência de Fibonacci: {fib_list}"
        else:
            return f"O número {n} não pertence à sequência de Fibonacci."

# Exemplo de uso:
print(fib(13))
