from openai import OpenAI
from gtts import gTTS

# Sua chave da NVIDIA
cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

palavra = input("Digite o Texto que deseja converter em audio:\n")


# Converter texto em voz
tts = gTTS(
    text=palavra,
    lang="pt"
)

tts.save("ex9.mp3")

print("\nÁudio salvo como ex9.mp3")
