# ==============================================================================
# EXERCÍCIO 8: Extração de Função (Extract Method)
# Enunciado: O método processar_dados está fazendo muitas coisas. Refatore-o 
# extraindo partes da lógica para métodos auxiliares menores e mais focados.
# ==============================================================================

# --- CÓDIGO ANTES DA REFATORAÇÃO ---
# class ProcessadorDeDados:
#     def __init__(self, dados):
#         self.dados = dados
#     def processar_dados(self):
#         if not self.dados or not isinstance(self.dados, list):
#             print("Erro: Dados inválidos.")
#             return []
#         dados_filtrados = []
#         for item in self.dados:
#             if isinstance(item, int) and item > 0:
#                 dados_filtrados.append(item)
#         dados_transformados = []
#         for item in dados_filtrados:
#             dados_transformados.append(item * 10)
#         print("--- Relatório de Processamento ---")
#         print(f"Total de itens processados: {len(dados_transformados)}")
#         print(f"Dados transformados: {dados_transformados}")
#         print("----------------------------------")
#         return dados_transformados


# --- CÓDIGO DEPOIS DA REFATORAÇÃO ---
class ProcessadorDeDados:
    def __init__(self, dados):
        self.dados = dados

    def processar_dados(self):
        # O método principal agora atua como um coordenador claro do fluxo
        if not self._dados_sao_validos():
            print("Erro: Dados inválidos.")
            return []

        dados_filtrados = self._filtrar_dados()
        dados_transformados = self._transformar_dados(dados_filtrados)
        
        self._gerar_relatorio(dados_transformados)
        
        return dados_transformados

    # --- Métodos Auxiliares Extraídos (Privados por convenção com '_') ---
    def _dados_sao_validos(self):
        return bool(self.dados and isinstance(self.dados, list))

    def _filtrar_dados(self):
        return [item for item in self.dados if isinstance(item, int) and item > 0]

    def _transformar_dados(self, dados_para_transformar):
        return [item * 10 for item in dados_para_transformar]

    def _gerar_relatorio(self, dados_finais):
        print("--- Relatório de Processamento ---")
        print(f"Total de itens processados: {len(dados_finais)}")
        print(f"Dados transformados: {dados_finais}")
        print("----------------------------------")


# Teste do Exercício 8
proc = ProcessadorDeDados([1, 2, -3, 4, "a", 5])
proc.processar_dados()

# --- O QUE MUDOU? ---
# 1. Princípio da Responsabilidade Única (SRP): O método original fazia tudo. 
#    Agora, cada parte da lógica ganhou sua própria subfunção especialista.
#
# 2. Legibilidade e Testabilidade: O fluxo principal do método `processar_dados` 
#    agora pode ser lido e compreendido em segundos. Além disso, cada operação 
#    pode ser testada ou modificada isoladamente.
# ==============================================================================
