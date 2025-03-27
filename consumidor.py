import datetime


def registrar_escolha(produto_nome):
    with open("historico_de_escolhas.txt", "a") as arquivo:
        arquivo.write(f"{datetime.datetime.now()}: {produto_nome}\n")


def escolher_produto(produto_nome):
    produtos_disponiveis = ['Arroz', 'Trigo', 'Milho', 'Cevada']
    
    if produto_nome not in produtos_disponiveis:
        raise ValueError(f"Produto '{produto_nome}' não é válido.")
    
    registrar_escolha(produto_nome)

    return produto_nome

   

