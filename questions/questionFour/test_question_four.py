import tkinter as tk


class Contato:
    """
    Classe que reprensenta um contato.

    Métodos:
    --------
    __init__(self, id: int, nome: str, email: str)
        Construtor da classe Contato.
    __str__(self)
        Retorna tudo o que foi passado pelo construtor da classe Contato.
    """

    def __init__(self, id, nome, telefone, email):
        """
        Construtor da classe Contato.

        Parâmetros:
        -----------
        id: int
            id do contato.
        nome: str
            nome do contato.
        telefone: str
            telefone do contato.
        email: str
            email do contato.
        """
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        """
        Retorna uma string que representa a classe Contato.

        Retorna:
        --------
        str
            String no formato "f'Id: {self.id} Nome: {self.nome} | Tel: {self.telefone} | email: {self.email}'"

        """
        return f'Id: {self.id} Nome: {self.nome} | Tel: {self.telefone} | email: {self.email}'


lista_ctt = []
id = 0


def adicionarCtt():
    """
    Função que adiciona um contato à lista 'lista_ctt'.

    Essa função lê os valores de entrada para nome, telefone e email, 
    cria um novo objeto 'Contato' com um id incrementado, adiciona-o à lista 'lista_ctt' e 
    atualiza o conteúdo do widget 'texto_contato' para exibir a nova lista de contatos. 

    Retorno: None.

    """
    global id
    nome = entrada_nome.get()
    telefone = entrada_telefone.get()
    email = entrada_email.get()
    id += 1
    contato = Contato(id, nome, telefone, email)
    lista_ctt.append(contato)
    texto_contato.config(state='normal')
    texto_contato.delete(1.0, tk.END)
    texto_contato.insert(tk.END, "\n".join(str(contato)
                         for contato in lista_ctt))
    texto_contato.config(state='disabled')


def deletarCtt():
    """
    Função que deleta um contato da lista 'lista_ctt'.

    Essa função lê o id de um contato e com base no mesmo deleta pelo index
    na lista ao qual ele pertence 'lista_ctt'.

    Retorno: None.

    """
    id = int(entrada_id.get())
    del lista_ctt[id - 1]
    texto_contato.config(state='normal')
    texto_contato.delete(1.0, tk.END)
    texto_contato.insert(tk.END, "\n".join(str(contato)
                         for contato in lista_ctt))
    texto_contato.config(state='disabled')


def atualizarCtt():
    """
    Função que atualiza um contato da lista 'lista_ctt'.

    Essa função percorre a 'lista_ctt' pelos contatos e faz alterações conforme a vontade do usuário
    pelo id lido e comparado na condição if.

    Retorno: None.

    """
    id = entrada_id.get()
    for contato in lista_ctt:
        if str(contato.id) == id:
            contato.nome = entrada_nome.get()
            contato.telefone = entrada_telefone.get()
            contato.email = entrada_email.get()
            break
    texto_contato.config(state='normal')
    texto_contato.delete(1.0, tk.END)
    texto_contato.insert(tk.END, "\n".join(str(contato)
                         for contato in lista_ctt))
    texto_contato.config(state='disabled')


janela = tk.Tk()
janela.title('Agenda')

rotulo_nome = tk.Label(janela, text='Nome: ')
rotulo_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()

rotulo_telefone = tk.Label(janela, text='Tel: ')
rotulo_telefone.pack()

entrada_telefone = tk.Entry(janela)
entrada_telefone.pack()

rotulo_email = tk.Label(janela, text='Email: ')
rotulo_email.pack()

entrada_email = tk.Entry(janela)
entrada_email.pack()

botao_adicionarCtt = tk.Button(janela, text='Adicionar', command=adicionarCtt)
botao_adicionarCtt.pack()

rotulo_id = tk.Label(janela, text='Remover/Atualizar pelo ID: ')
rotulo_id.pack(side=tk.LEFT)

entrada_id = tk.Entry(janela)
entrada_id.pack(side=tk.LEFT)

botao_deletarCtt = tk.Button(janela, text='Deletar', command=deletarCtt)
botao_deletarCtt.pack(side=tk.LEFT)

botao_atualizarCtt = tk.Button(janela, text='Atualizar', command=atualizarCtt)
botao_atualizarCtt.pack(side=tk.LEFT)

texto_contato = tk.Text(janela, height=5, state='disabled')
texto_contato.pack()

janela.mainloop()
