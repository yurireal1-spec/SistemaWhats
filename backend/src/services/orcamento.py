from dataclasses import dataclass, field
import pandas as pd

@dataclass
class ItemTratamento:
    """Representa um único procedimento clínico dentro de um orçamento."""
    nome: str
    regiao_dente: str
    quantidade: int

@dataclass
class OrcamentoProcessado:
    """Representa um orçamento totalmente processado e pronto para o sistema."""
    # Dados do Cliente
    nome_cliente: str
    telefone: str
    
    # Dados Clínicos
    numero_orcamento: str
    dentista_responsavel: str
    
    # Dados Financeiros Calculados
    valor_bruto: float
    valor_desconto: float
    percentual_desconto: int
    valor_final: float
    
    # 🌟 AQUI ENTROU A COMPOSIÇÃO: Substituímos as 3 variáveis fixas antigas por uma lista dinâmica
    tratamentos: list[ItemTratamento] = field(default_factory=list)

    @classmethod  # ⬅️ Agora devidamente indentado para dentro da classe
    def construir_da_linha(cls, linha):
        """Fábrica 100% dinâmica que se adapta a qualquer número de colunas de tratamento."""
        
        # 1. Tratamento de dados básicos
        nome = linha['cliente'] if pd.notna(linha['cliente']) else "Sem Nome"
        tel = linha['telefone'] if pd.notna(linha['telefone']) else ""
        numero = str(linha['orçamento']) if pd.notna(linha['orçamento']) else "0"
        dentista = linha['dentista'] if pd.notna(linha['dentista']) else "Não Informado"
        
        v_bruto = float(linha['valor bruto']) if pd.notna(linha['valor bruto']) else 0.0
        v_final = float(linha['valor final']) if pd.notna(linha['valor final']) else 0.0
        v_desc = v_bruto - v_final
        perc_desc = int((v_desc / v_bruto) * 100) if v_bruto > 0 and v_desc > 0 else 0

        lista_tratamentos = []
        
        # 2. Descobrindo os números das colunas dinamicamente
        for coluna in linha.index:
            if coluna.startswith('Tratamento_'):
                try:
                    numero_sufixo = coluna.split('_')[1]
                except IndexError:
                    continue 
                
                col_tratamento = f'Tratamento_{numero_sufixo}'
                col_dentes = f'Dentes/Arcada_{numero_sufixo}'
                col_quantidade = f'Quantidade_{numero_sufixo}'
                
                if pd.notna(linha[col_tratamento]):
                    nome_proc = str(linha[col_tratamento]).strip()
                    if not nome_proc:
                        continue
                        
                    regiao = str(linha[col_dentes]) if col_dentes in linha.index and pd.notna(linha[col_dentes]) else "Geral"
                    
                    try:
                        qtd = int(linha[col_quantidade]) if col_quantidade in linha.index and pd.notna(linha[col_quantidade]) else 1
                    except ValueError:
                        qtd = 1
                    
                    # Guarda o tratamento válido instanciando a sub-classe
                    item = ItemTratamento(nome=nome_proc, regiao_dente=regiao, quantidade=qtd)
                    lista_tratamentos.append(item)

        # 3. Retorna a classe montada passando a lista de tratamentos gerada
        return cls(
            nome_cliente=nome,
            telefone=tel,
            numero_orcamento=numero,
            dentista_responsavel=dentista,
            valor_bruto=v_bruto,
            valor_desconto=v_desc,
            percentual_desconto=perc_desc,
            valor_final=v_final,
            tratamentos=lista_tratamentos
        )