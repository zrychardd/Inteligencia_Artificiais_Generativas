from openai import OpenAI

cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)
personalidade = (
    "Você é um robô super inteligente vindo do ano 3025. "
    "Você responde de forma divertida, usa termos tecnológicos, "
    "faz piadas sobre computadores e sempre chama as pessoas de humano. "
    "Apesar de ser um robô, você é amigável e gosta de ajudar."
)


print("Para sair do programa digite: sair\n")
while True:
    pergunta = input("Digite a sua pergunta :\n")
    if pergunta.lower() == "sair":
        print("Encerrando o programa. Até mais!")
        break
    else:
        resposta = cliente.chat.completions.create(
            model="meta/llama-3.1-8b-instruct",

            messages=[
             {
                "role": "system",
                "content": personalidade
            },

            {
                "role": "user",
                "content": pergunta
            }
        ]
    )
    print("\nResposta da IA:\n")
    print("Ela agira como um:"+ " Ninja da aldeia da folha")
    print(resposta.choices[0].message.content)

