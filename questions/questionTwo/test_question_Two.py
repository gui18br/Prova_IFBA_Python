def gerar_email(nomes_completos, emailGerado):
    """
    Gera email com base nas iniciais dos nomes de um funcionario e armazena dentro de uma lista de strings.
    Se já houver um email dentro da lista é acrescentado com um número 2.

    Args:
        nomes_completos (list): Lista de nomes completos dos funcionários.
        emailGerado (list): Lista de emails já gerados dos funcionarios.

    Returns:
        str: O email conforme gerado.
    """
    # ira dividir o nome em uma lista de palavras
    nomes_funcionarios = ''
    for nome in nomes_completos:
        nomes_funcionarios = nome.split()

    # lista de nomes a serem ignorados
    ignorados = ['da', 'de', 'do', 'das', 'dos']

    primeiras_letras = []
    for nome in nomes_funcionarios:
        # verifica se o nome esta na lista para ser ignorado
        if nome.lower() in ignorados:
            # ignora o nome se estiver
            continue
        primeira_letra = nome[0].lower()
        primeiras_letras.append(primeira_letra)

    emailPadrao = ''.join(primeiras_letras)
    email = emailPadrao + '@empresa.com.br'

    # verifica se o email ja existe
    if email in emailGerado:
        novo_email = emailPadrao + str(2) + '@empresa.com.br'
        email = novo_email

    emailGerado.append(email)
    return email


nomes_completos = []
emailGerado = []
try:
    with open('text.txt', 'r') as arquivo:
        nomes_completos = arquivo.readlines()
except IOError:
    print('Erro ao abrir arquivo')

try:
    with open('emailsFuncionarios.txt', 'w') as arquivo:
        if not nomes_completos:
            raise ValueError('Lista de nomes vazia')
        for nome in nomes_completos:
            email = gerar_email([nome], emailGerado)
            arquivo.write(
                f'Nome: {nome.strip()} | E-mail: {email}\n')
except IOError:
    print('Erro ao escrever no arquivo')


def test_gerar_email():
    emailGerado = []
    nomes_completos = ['Carlos Souza Silva', 'Cassio Silva dos Santos',
                       'Maria da Silva Castro', 'Antonio dos Santos Cardoso']
    assert gerar_email([nomes_completos[0]],
                       emailGerado) == 'css@empresa.com.br'
    assert gerar_email([nomes_completos[1]],
                       emailGerado) == 'css2@empresa.com.br'
    assert gerar_email([nomes_completos[2]],
                       emailGerado) == 'msc@empresa.com.br'
    assert gerar_email([nomes_completos[3]],
                       emailGerado) == 'asc@empresa.com.br'
