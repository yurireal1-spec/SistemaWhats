import os
import sys
import pandas as pd

# Garante que o Python encontre os módulos locais
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import carregar_dados_entrada, limpar_tela,pausar
from services import TemplatePadrao, TemplateCondicaoEspecial, TemplateUrgencia, WhatsAppClient, OrcamentoProcessado

def meng():
    # 1. Carrega a planilha do Excel
    df = carregar_dados_entrada()
    wpp = WhatsAppClient('yuri')
    
    # 🔄 Tenta autenticar e verificar conexão com o WhatsApp
    print("\n🔄 Conectando ao serviço do WhatsApp...")
    if not wpp.verificar_conexao():
        print("⚠️ WhatsApp não está conectado. Tentando iniciar sessão...")
        if wpp.iniciar_sessao():
            print("⏳ Aguarde a inicialização da sessão. Se for a primeira vez,")
            print("   escaneie o QR Code no terminal do wppconnect-server.")
            import time
            time.sleep(3)
        else:
            print("❌ Não foi possível iniciar a sessão do WhatsApp.")
            pausar()
            return
            
    if df is not None:
        while True:
            print('Dados carregados com sucesso\n')
            
            # 📋 2. MAPEA E APRESENTA O MENU DE OPÇÕES
            opcoes_templates = {
                "1": TemplatePadrao(),
                "2": TemplateUrgencia(),
                "3": TemplateCondicaoEspecial()
            }

            # 🛡️ NOVO LOOP INTERNO: Exclusivo para garantir a validação do menu
            while True:
                limpar_tela()
                print("=== ESCOLHA O MODELO DE MENSAGEM PARA ESTE REPIQUE ===")
                print("1 - Padrão (Detalhado)")
                print("2 - Urgência (Escassez)")
                print("3 - Condição Especial (Financeiro)")
                
                escolha = input("Digite o número do modelo desejado: ")
                
                #fecha o sistema iginorando os loops.
                if escolha =="0":
                    return

                if escolha in opcoes_templates:
                    template_selecionado = opcoes_templates[escolha]
                    print(f"\n✅ Sucesso! Template selecionado com sucesso.\n")
                    break  # 👈 AGORA SIM: Quebra apenas o loop do menu e avança!
                else:
                    print(f"\n❌ Erro: '{escolha}' não é uma opção válida!")
                    print("👉 Por favor, digite apenas um dos números do menu (1, 2 ou 3).\n")
                    print("-" * 50)
                    pausar()
                    

            print("\nIniciando o processamento dos clientes...\n")

            # 👥 3. LAÇO PRINCIPAL DE CLIENTES
            for index, linha in df.iterrows():
                # Defesa: ignora linhas onde o nome do cliente está em branco
                if pd.isna(linha['cliente']): 
                    continue 

                # Constrói o objeto dinâmico tratando os Nans e colunas infinitas
                orcamento = OrcamentoProcessado.construir_da_linha(linha)
                
                print('_' * 50)
                print(f"{index}º Cliente: {orcamento.nome_cliente}\n")

                # (Seu laço antigo comentado mantido de forma limpa)
                '''
                for i, tratamento in enumerate(orcamento.tratamentos):
                    print(
                        f"  {i}. Procedimento: {tratamento.nome}\n"
                        f"     Região/Dente: ({tratamento.regiao_dente})\n"
                        f"     Quantidade: {tratamento.quantidade}\n"
                    )
                '''
                
                # 🌟 A MÁGICA DO POLIMORFISMO:
                # O template escolhido gera o texto customizado para este orçamento
                texto_final = template_selecionado.gerar(orcamento)
                
                print("📝 MENSAGEM PRONTA PARA ENVIO:")
                #print(texto_final)
                
                print(f"📤 Enviando mensagem para {orcamento.nome_cliente} ({orcamento.telefone})...")
                resultado = wpp.enviar_mensagem(orcamento.telefone, texto_final)
                
                if resultado.get("sucesso"):
                    print("✅ Mensagem enviada com sucesso!")
                else:
                    print(f"❌ Falha ao enviar mensagem: {resultado.get('erro') or resultado.get('corpo')}")
                
                print('_' * 50)
            
            # Pergunta se deseja repetir todo o processo (reler menu) ou encerrar o script
            if input("\nGostaria de rodar o disparador novamente (s/n): ").lower() != 's': 
                break
    else:
        print("Nenhum dado encontrado na planilha.")

# Ponto de entrada padrão do Python
if __name__ == "__main__":
    meng()