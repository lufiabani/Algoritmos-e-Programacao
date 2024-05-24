import itertools

# Funções Lógicas
def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def IMPLIES(a, b):
    return (not a) or b

def BICOND(a, b):
    return a == b

# Mapeamento de operadores para funções
operators = {
    '^': 'AND',
    'v': 'OR',
    '->': 'IMPLIES',
    '<=>': 'BICOND',
    '~': 'NOT'
}

# Função para substituir os operadores por funções correspondentes
def replace_operators(expression):
    # Substituir operadores de 2 caracteres primeiro para evitar substituição parcial
    expression = expression.replace('->', ' IMPLIES ')
    expression = expression.replace('<=>', ' BICOND ')
    # Substituir operadores de 1 caractere
    expression = expression.replace('~', 'NOT ')
    expression = expression.replace('^', ' AND ')
    expression = expression.replace('v', ' OR ')
    return expression

# Função para avaliar uma expressão lógica
def evaluate_expression(expression, variables):
    local_vars = {var: variables[var] for var in variables}
    local_vars.update({
        'AND': AND,
        'OR': OR,
        'NOT': NOT,
        'IMPLIES': IMPLIES,
        'BICOND': BICOND
    })
    return eval(expression, {"__builtins__": None}, local_vars)

# Função para gerar a tabela verdade
def truth_table(expression, variables):
    num_vars = len(variables)
    table = []

    # Gerar todas as combinações possíveis de valores de verdade
    combinations = list(itertools.product([False, True], repeat=num_vars))

    for combination in combinations:
        # Mapear os valores de verdade para as variáveis
        var_values = dict(zip(variables, combination))

        # Avaliar a expressão lógica com os valores de verdade atuais
        result = evaluate_expression(expression, var_values)

        # Adicionar a combinação e o resultado à tabela
        table.append((combination, result))

    return table

# Função para imprimir a tabela verdade de forma legível
def print_truth_table(expression, variables):
    table = truth_table(expression, variables)

    # Imprimir cabeçalho
    header = variables + ["Result"]
    print(" | ".join(header))

    # Imprimir linhas da tabela
    for row in table:
        values = [str(int(value)) for value in row[0]] + [str(int(row[1]))]
        print(" | ".join(values))

# Função principal para receber a entrada do usuário e gerar a tabela verdade
def main():
    expression = input("Digite a expressão lógica: ")

    # Substituir operadores pelos nomes das funções
    expression = replace_operators(expression)

    # Extraindo variáveis únicas da expressão
    variables = sorted(set(filter(str.isalpha, expression)))

    if not variables:
        print("Nenhuma variável encontrada na expressão.")
        return

    print("\nTabela Verdade:")
    print_truth_table(expression, variables)

if __name__ == "__main__":
    main()
