from abc import ABC, abstractmethod
from .orcamento import OrcamentoProcessado

class TemplateMensagem(ABC):
    """
    Classe Abstrata (Fôrma Base). 
    Garante que qualquer novo template SEJA OBRIGADO a ter o método 'gerar'.
    """
    @abstractmethod
    def gerar(self, orcamento: OrcamentoProcessado) -> str:
        pass


class TemplatePadrao(TemplateMensagem):
    """Modelo 1: O seu texto atual, focado em listar os procedimentos."""
    def gerar(self, orcamento: OrcamentoProcessado) -> str:
        msg = (
            f"Olá, *{orcamento.nome_cliente}*! Tudo bem?\n\n"
            f"Aqui estão os detalhes do seu planejamento clínico *#{orcamento.numero_orcamento}*:\n"
            f"🩺 *Dentista:* {orcamento.dentista_responsavel}\n\n"
            f"📋 *Procedimentos Recomendados:*\n"
        )
        for item in orcamento.tratamentos:
            msg += f"▪️ {item.nome} ({item.regiao_dente}) - Qtd: {item.quantidade}\n"
            
        msg += f"\n💰 *Investimento Total:* R$ {orcamento.valor_final:,.2f}"
        if orcamento.valor_desconto > 0:
            msg += f"\n🎉 *Desconto Especial Aplicado:* R$ {orcamento.valor_desconto:,.2f}"
            
        msg += "\n\nPodemos agendar o seu início?"
        return msg


class TemplateUrgencia(TemplateMensagem):
    """Modelo 2: Texto focado em escassez/urgência para fechar logo."""
    def gerar(self, orcamento: OrcamentoProcessado) -> str:
        msg = (
            f"🚨 Olá, *{orcamento.nome_cliente}*, conseguimos uma condição de urgência!\n\n"
            f"O Dr(a). {orcamento.dentista_responsavel} separou um horário nesta semana para iniciar "
            f"o seu tratamento de *{orcamento.tratamentos[0].nome if orcamento.tratamentos else 'Planejamento'}*.\n\n"
            f"Conseguimos segurar o valor de **R$ {orcamento.valor_final:,.2f}** apenas até sexta-feira.\n\n"
            f"Vamos garantir a sua vaga?"
        )
        return msg


class TemplateCondicaoEspecial(TemplateMensagem):
    """Modelo 3: Texto focado em parcelamento ou facilidades."""
    def gerar(self, orcamento: OrcamentoProcessado) -> str:
        msg = (
            f"Olá, *{orcamento.nome_cliente}*! Sabia que facilitamos o seu tratamento?\n\n"
            f"O seu planejamento *#{orcamento.numero_orcamento}* ficou no total de R$ {orcamento.valor_final:,.2f}.\n"
            f"Conseguimos parcelar esse valor para que você não adie o cuidado com o seu sorriso! 😁\n\n"
            f"Quer que eu simule as opções de parcelamento para você?"
        )
        return msg