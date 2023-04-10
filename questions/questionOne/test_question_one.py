def gerar_email(nome_completo):
    """
    Gera email com base nas iniciais dos nomes de um funcionario.

    Args:
        nome_completo (str): O nome completo do funcionário.

    Returns:
        str: O email conforme gerado.
    """
    # ira dividir o nome em uma lista de palavras
    nomes = nome_completo.split()

    # lista de nomes a serem ignorados
    ignorados = ['da', 'de', 'do', 'das', 'dos']

    primeiras_letras = []
    for nome in nomes:
        # verifica se o nome esta na lista para ser ignorado
        if nome.lower() in ignorados:
            # ignora o nome se estiver
            continue
        primeira_letra = nome[0].lower()
        primeiras_letras.append(primeira_letra)

    email = ''.join(primeiras_letras) + '@empresa.com.br'
    return email


def test_gerar_email():
    nome = 'Guilherme Novais Lima Pereira'
    assert gerar_email(nome) == 'gnlp@empresa.com.br'
