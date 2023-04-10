def gerar_email(nomes_completos, emailGerado):
    """
    Gera email com base nas iniciais dos nomes de um funcionario.

    Args:
        nome_completo (str): O nome completo do funcionário.

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
        i = 2
        while True:
            novo_email = emailPadrao + str(i) + '@empresa.com.br'
            email = novo_email
            break

    emailGerado.append(email)
    return email


nomes_completos = []
emailGerado = []
with open('text.txt', 'r') as arquivo:
    nomes_completos = arquivo.readlines()
for nome in nomes_completos:
    print(gerar_email([nome], emailGerado))


def test_gerar_email():
    nome = 'Guilherme Novais Lima Pereira'
    assert gerar_email(nome, emailGerado) == 'gnlp@empresa.com.br'
