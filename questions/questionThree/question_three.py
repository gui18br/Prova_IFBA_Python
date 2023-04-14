import tkinter as tk


def gerar_email(nome_completo):
    """
    Gera email com base nas iniciais dos nomes de um funcionario.

    Args:
        nome_completo (str): O nome completo do funcionário.
        emailGerado (str, optional): O email gerado anteriormente. Default é vazio.

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


def criar_email():
    """
    Função que cria um email com base no nome completo passado pelo usuário.

    Essa função pega o nome completo passado pelo usuário e faz o chamado da função
    'gerar_email()', na qual gera um email com base nas iniciais dos nomes passados
    pelo usuário.

    Retorno: None.

    """
    nome_completo = entrada_nome.get()
    email = gerar_email(nome_completo)
    texto_email.config(state='normal')
    texto_email.delete(1.0, tk.END)
    texto_email.insert(tk.END, email)
    texto_email.config(state='disabled')


# Criacao  da janela principal
janela = tk.Tk()
janela.title("Gerador de E-mail")

# texto
rotulo_nome = tk.Label(janela, text="Nome completo:")
rotulo_nome.pack()

# campo de entrada
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

# botao
botao_gerar = tk.Button(janela, text="Gerar E-mail", command=criar_email)
botao_gerar.pack()

# Caixa de texto para exibição do email
texto_email = tk.Text(janela, state='disabled', width=30, height=1)
texto_email.pack()


janela.mainloop()
