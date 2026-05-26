import pandas as pd
import os
import shutil

def carregar_dados_entrada():
    '''
        Função reservada para ler e organizar asquivos de planilhas  nos podrões (.csv), (.xlsx);
        o arquivo deve ser colocado na pasta (src/'entrada_planilhas') pós processamento 
        será encaminhada para (src/'planilha_processada')
    '''
    # Descobre o caminho da pasta onde este arquivo (leitor.py) está
    caminho_do_script = os.path.dirname(os.path.abspath(__file__))
    # Sobe um nível ou define a pasta a partir da raiz do script
    dir_in = os.path.join(caminho_do_script, "../entrada_planilhas")
    dir_out = os.path.join(caminho_do_script, "../planilha_processada")
    

    for arquivo in os.listdir(dir_in):
        if arquivo.endswith(".xlsx") or arquivo.endswith(".csv"):
            caminho_arquivo = os.path.join(dir_in, arquivo)
            
            print(f"Lendo arquivo: {arquivo}")
            
            try:
                # 1. Leitura do arquivo
                if arquivo.endswith(".xlsx"):
                    db = pd.read_excel(caminho_arquivo, dtype= {'telefone':str})
                else:
                    # Tenta ler CSV (ajuste o sep se necessário)
                    db = pd.read_csv(caminho_arquivo, sep=';', encoding='uft-8', dtype= {'telefone':str})

                # 2. Move o arquivo original para não processar repetido
                #caminho_destino = os.path.join(dir_out, arquivo)
                #shutil.move(caminho_arquivo, caminho_destino)
                
                return db # Retorna o DataFrame assim que encontrar o primeiro arquivo
                
            except Exception as e:
                print(f"Erro ao processar {arquivo}: {e}")
                return None

    print("Nenhum arquivo novo para processar.")
    return None

