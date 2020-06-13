
def formata_cpf_1(cpf):
    """ Retorna o CPF formatado, com pontos e um traço

    Esta implementação é ruim de propósito. Ela transforma o valor do CPF em
    uma string, adiciona zeros até que o tamanho seja de um CPF completo (onze
    números) e, por fim, adiciona os pontos e o traço separador do dígito
    verificador. E depois inverte toda a string, pois ela foi montada ao
    contrário.

    Parâmetros
    ----------
    cpf : number
          O CPF a ser formatado
    """

    # Transformando o CPF em uma string
    str_cpf = f"{cpf}"

    # Vetor onde será colocado o resultado.
    vec_cpf = []

    # Inserindo os algarismos do CPF, em ordem inversa.
    for c in str_cpf:
        vec_cpf.insert(0, c)

    # Adicionando o restante dos zeros, até que o vetor tenha tamanho 11.
    for i in range(1, 11-len(vec_cpf)):
        vec_cpf.append('0')
    
    # Montando a string final invertida
    rev_formatted_cpf = f"{''.join(vec_cpf[0:2])}-{''.join(vec_cpf[2:5])}.{''.join(vec_cpf[5:8])}.{''.join(vec_cpf[8:11])}"

    # Corrigindo a string
    formatted_cpf = ""
    for c in rev_formatted_cpf:
        formatted_cpf = c + formatted_cpf
    return formatted_cpf


def formata_cpf_3(cpf):
    """ Retorna o CPF formatado, com pontos e um traço

    Esta implementação tem uma abordagem diferente: ao invés de se operar em
    strings, um desenvolvedor incauto poderia pensar "ora, vou usar operadores
    matemáticos, já que trabalhar com strings é muito mais caro". Nesta função,
    cada dígito do valor do CPF é removido através de operadores matemáticos
    (módulo e divisão inteira). Para diminuir ainda mais a dependência de
    funções que envolvam string, esta função ainda tem um pequeno vetor
    contendo os dígitos "convertidos" para string. O único momento em que
    strings são necessárias é na geração do valor de retorno, em que todos os
    valores são agrupados.

    Parâmetros
    ----------
    cpf : number
          O CPF a ser formatado
    """
    cache = cpf

    # "Tabela" de conversão
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Vetor onde será colocado o resultado final. "Alocado estaticamente (R)"
    formatted_cpf = ['', '', '', '.', '', '', '', '.', '', '', '', '-', '', '']

    ix = 13
    while (ix >= 0):
        remainder = cache % 10
        cache = (cache - remainder) / 10
        # Percorre o vetor na ordem inversa (algarismo menos significativo)
        # para o mais significativo.
        formatted_cpf[ix] = digits[remainder]
        ix -= 1
        # Pula os caracteres especiais, pontos e traço.
        if ix == 11 or ix == 7 or ix == 3:
            ix -= 1
    # Por fim, cria uma string com todos os valores do vetor.
    return ''.join(formatted_cpf)


def formata_cpf_3(cpf):
    """ Retorna o CPF formatado, com pontos e um traço

    Esta implementação é um tanto mais otimizada - possui poucas instruções,
    faz uso de funções nativas do Python e é relativamente simples de entender.
    Ela transforma o CPF em string, adiciona os zeros faltantes e "fatia" a 
    string final para montar o CPF formatado.

    Parâmetros
    ----------
    cpf : number
          O CPF a ser formatado
    """
    str_cpf = f"{cpf}"
    str_cpf = '0' * (11-len(str_cpf)) + str_cpf
    return f"{str_cpf[0:3]}.{str_cpf[3:6]}.{str_cpf[6:9]}-{str_cpf[9:]}"


def formata_cpf_4(cpf):
    """ Retorna o CPF formatado, com pontos e um traço

    Esta implementação é bastante semelhante à anterior, com a diferença que
    a transformação do CPF para string não considera quantos zeros estão
    faltando. Basta apenas adicionar todos os onze e, quando a string formatada
    for gerada, os índices serem referentes ao fim. Assim não é necessário
    calcular o tamanho da string.

    Parâmetros
    ----------
    cpf : number
          O CPF a ser formatado
    """
    str_cpf = f"{'0' * 11}{cpf}"

    # Repare que todos os índices são negativos.
    return f"{str_cpf[-11:-8]}.{str_cpf[-8:-5]}.{str_cpf[-5:-2]}-{str_cpf[-2:]}"
