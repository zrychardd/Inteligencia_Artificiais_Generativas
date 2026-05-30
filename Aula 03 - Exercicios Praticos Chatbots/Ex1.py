from openai import OpenAI

cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

pergunta = input("Digite a sua pergunta para a IA:\n")

resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": "Você é um assistente inteligente."
        },

        {
            "role": "user",
            "content": pergunta
        }
    ]
)
print("\nResposta da IA:\n")
print(resposta.choices[0].message.content)