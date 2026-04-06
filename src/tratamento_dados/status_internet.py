#---------------Aqui verificamos o status Internet---------------

statusInternet = {
    1: "Ativo",
    2: "Desativado",
    3: "Bloqueio Manual",
    4: "Bloqueio Automático",
    5: "Financeiro em Atraso",
    6: "Aguardando Assinatura",
}

def traduzir(valor):
    valor = int(valor)
    return statusInternet.get(valor, "Desconhecido")
