
from services.google_docs import ler_documento_faq

try:
    print("=" * 60)
    print("TESTE DE INTEGRACAO COM GOOGLE DOCS")
    print("=" * 60)

    faq = ler_documento_faq()

    print("\nCONEXAO REALIZADA COM SUCESSO!")
    print(f"\nQuantidade de caracteres: {len(faq)}")

    print("\n" + "=" * 60)
    print("CONTEUDO COMPLETO DO FAQ")
    print("=" * 60)

    print(faq)

    print("\n" + "=" * 60)
    print("FIM DO DOCUMENTO")
    print("=" * 60)

except Exception as erro:
    print(f"\nERRO AO ACESSAR O GOOGLE DOCS: {erro}")
