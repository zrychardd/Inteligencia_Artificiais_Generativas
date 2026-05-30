from openai import OpenAI

cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)
personalidade =(
    "aja como treinador motivacional"
)
print("--DIgite 'sair' para fechar o programa--")
print("\nMe diga como vc esta se sentido hoje:")
while True:
    palavra = input("\nR: \n")
    if palavra.lower() == "sair" :
        print("Programa Encerrado")
        break

    resposta = cliente.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",

        messages=[
            {
                "role": "system",
                "content": personalidade
            },

            {
                "role": "user",
                "content": palavra
            }
        ]
    )

    print("IA couch:")
    print(resposta.choices[0].message.content)

# achei interresante as resposta ele realmente agiu como um couch, e ainda armazenou dados das minhas resposta anteriores com dominio