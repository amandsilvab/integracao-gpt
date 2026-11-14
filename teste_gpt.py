
from services.gpt_service import analisar_duvida

pergunta = "Como configurar e instalar a VPN corporativa no meu computador?"

try:
    resultado = analisar_duvida(pergunta)

    print("\n========================================")
    print("TESTE DE INTEGRACAO GPT-OSS-20B")
    print("========================================")

    print("\nPERGUNTA:")
    print(pergunta)

    print("\nRESULTADO DA ANALISE:")
    print(f"Resolvido: {resultado['resolvido']}")
    print(f"Categoria: {resultado['categoria']}")
    print(f"Prioridade: {resultado['prioridade']}")

    print("\nRESPOSTA DA IA:")
    print(resultado["resposta"])

    print("\nMOTIVO DO ENCAMINHAMENTO:")
    print(resultado["motivo_encaminhamento"])

    print("\n========================================")

except Exception as erro:
    print(f"Erro no teste: {erro}")
