class WhatsAppMisc:
    """
    Namespace para operações diversas (Misc).
    """
    def __init__(self, client):
        self.client = client

    def limpar_dados_sessao(self, secret_key: str) -> dict:
        """
        Limpa todos os arquivos e dados de cache locais salvos para a sessão.
        Swagger: POST /api/{session}/{secretkey}/clear-session-data
        """
        return self.client._executar_requisicao("POST", f"{self.client.session}/{secret_key}/clear-session-data")

    def inscrever_presenca(self, numero: str, is_group: bool = False, all: bool = False) -> dict:
        """
        Inscreve-se para monitorar a presença (online/digitando) de um contato ou de todos.
        Swagger: POST /api/{session}/subscribe-presence
        """
        payload = {
            "phone": numero,
            "isGroup": is_group,
            "all": all
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/subscribe-presence", json=payload)

    def definir_presenca_online(self, is_online: bool) -> dict:
        """
        Define o status de presença online da própria sessão.
        Swagger: POST /api/{session}/set-online-presence
        """
        payload = {
            "isOnline": is_online
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/set-online-presence", json=payload)

    def obter_plataforma_mensagem(self, id_mensagem: str) -> dict:
        """
        Obtém a plataforma de origem da mensagem pelo ID.
        Swagger: GET /api/{session}/get-platform-from-message/{messageId}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/get-platform-from-message/{id_mensagem}")
