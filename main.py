from services.google_docs import ler_documentacao


def main():

    print("=" * 50)
    print("SISTEMA DE SUPORTE DE TI")
    print("=" * 50)

    try:

        print("\nConectando ao Google Docs...")

        documentacao = ler_documentacao()

        print("\nDocumentação carregada com sucesso!")

        print("\nCONTEÚDO DO DOCUMENTO:")
        print("-" * 50)

        print(documentacao)

        print("-" * 50)

    except Exception as erro:

        print("\nErro durante a execução:")
        print(erro)


if __name__ == "__main__":
    main()