
from services.atendimento import atender_colaborador


# Dados de teste
colaborador = "Amanda"
pergunta = "Como configurar e instalar a VPN corporativa no meu computador?"

try:
    resultado = atender_colaborador(colaborador, pergunta)

    print("\n========================================")
    print("SISTEMA DE ATENDIMENTO AUTOMATIZADO")
    print("========================================")

    print(f"\nColaborador: {colaborador}")
    print(f"Pergunta: {pergunta}")

    print("\nRESULTADO:")

    if resultado["status"] == "respondido":

        print("Status: Duvida resolvida pela IA")
        print(f"Resposta: {resultado['resposta']}")

    elif resultado["status"] == "chamado_aberto":

        print("Status: Chamado registrado automaticamente")
        print(f"Identificador: {resultado['identificador']}")
        print(f"Categoria: {resultado['categoria']}")
        print(f"Prioridade: {resultado['prioridade']}")
        print(f"Orientacao: {resultado['resposta']}")

    print("\n========================================")

except Exception as erro:
    print(f"Erro no atendimento: {erro}")
