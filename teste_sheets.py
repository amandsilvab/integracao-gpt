
from services.google_sheets import registrar_chamado


# Dados fictícios para testar a integração
chamado_teste = {
    "colaborador": "João da Silva",
    "categoria": "Hardware",
    "descricao": "O computador não está ligando.",
    "resposta_ia": "",
    "motivo_encaminhamento": (
        "O problema não possui procedimento "
        "suficiente na documentação."
    ),
    "prioridade": "Média"
}


# Executa o registro
try:

    identificador = registrar_chamado(chamado_teste)

    print("\nTeste concluído!")
    print("ID do chamado:", identificador)

except Exception as erro:

    print("\nErro ao registrar chamado:")
    print(erro)
