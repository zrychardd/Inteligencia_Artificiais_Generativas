from openai import OpenAI
from gtts import gTTS

# Sua chave da NVIDIA
cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

palavra = input("Qual a sua duvida de hoje?\n")

# Gera resposta da IA
resposta = cliente.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",

    messages=[
        {
            "role": "system",
            "content": "Seja fiel ao texto para ser narrado em voz alta"
        },

        {
            "role": "user",
            "content": palavra
        }
    ]
)

texto = resposta.choices[0].message.content

print("\nResposta:\n")
print(texto)
# Converter texto em voz
tts = gTTS(
    text=texto,
    lang="pt"
)

tts.save("ex10.mp3")

print("\nÁudio salvo como ex10.mp3")