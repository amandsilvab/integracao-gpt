
from services.atendimento import atender_colaborador


def main():

    print("=" * 50)
    print("SISTEMA DE SUPORTE DE TI")
    print("=" * 50)

    try:
        colaborador = input("\nInforme seu nome: ").strip()

        pergunta = input("\nDescreva sua dúvida ou problema: ").strip()

        if not colaborador or not pergunta:
            print("\nErro: informe seu nome e sua dúvida.")
            return

        print("\nAnalisando sua solicitação...")
        resultado = atender_colaborador(colaborador, pergunta)

        print("\n" + "=" * 50)
        print("RESULTADO DO ATENDIMENTO")
        print("=" * 50)

        if resultado["status"] == "respondido":

            print("\nStatus: Dúvida resolvida pela IA")
            print(f"\nOrientação:\n{resultado['resposta']}")

        elif resultado["status"] == "chamado_aberto":

            print("\nStatus: Chamado registrado automaticamente")
            print(f"Identificador: {resultado['identificador']}")
            print(f"Categoria: {resultado['categoria']}")
            print(f"Prioridade: {resultado['prioridade']}")
            print(f"\nOrientação: {resultado['resposta']}")

        print("\n" + "=" * 50)

    except Exception as erro:
        print(f"\nErro durante o atendimento: {erro}")


if __name__ == "__main__":
    main()
