from services.google_docs import ler_documento_faq

try:
    faq = ler_documento_faq()

    print("Conexão com Google Docs realizada!")
    print("\nCONTEÚDO DO FAQ:\n")
    print(faq)

except Exception as erro:
    print("Erro ao acessar o Google Docs:")
    print(erro)