#---------------Primeiro e segundo nome---------------

def atualizar_nomes(nome):

    if len(nome) == 1:
        return nome
    
    nome_separado = str(nome).split()

    primeiro = nome_separado[0]
    ultimo = nome_separado[-1]

    return primeiro + " " + ultimo

