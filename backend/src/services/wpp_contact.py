class WhatsAppContact:
    """
    Namespace para operações de Contatos (Contact e Blocklist).
    """
    def __init__(self, client):
        self.client = client

    def verificar_status_numero(self, numero: str) -> dict:
        """
        Verifica se um número existe no WhatsApp e retorna informações de status.
        Swagger: GET /api/{session}/check-number-status/{phone}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/check-number-status/{numero}")

    def obter_todos_contatos(self) -> dict:
        """
        Retorna todos os contatos salvos e conversas ativas.
        Swagger: GET /api/{session}/all-contacts
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/all-contacts")

    def obter_contato(self, numero: str) -> dict:
        """
        Obtém informações de um contato específico do WhatsApp.
        Swagger: GET /api/{session}/contact/{phone}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/contact/{numero}")

    def obter_contato_pn_lid(self, pn_lid: str) -> dict:
        """
        Obtém informações do contato através do PN Lid.
        Swagger: GET /api/{session}/contact/pn-lid/{pnLid}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/contact/pn-lid/{pn_lid}")

    def obter_perfil_numero(self, numero: str) -> dict:
        """
        Retorna os detalhes de perfil público de um número de celular.
        Swagger: GET /api/{session}/profile/{phone}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/profile/{numero}")

    def obter_foto_perfil(self, numero: str) -> dict:
        """
        Retorna a URL e os metadados da imagem de perfil de um contato.
        Swagger: GET /api/{session}/profile-pic/{phone}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/profile-pic/{numero}")

    def obter_status_perfil(self, numero: str) -> dict:
        """
        Retorna a mensagem de status (antigo recado/frase) do perfil do contato.
        Swagger: GET /api/{session}/profile-status/{phone}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/profile-status/{numero}")

    def obter_lista_bloqueados(self) -> dict:
        """
        Retorna a lista de contatos bloqueados na sessão.
        Swagger: GET /api/{session}/blocklist
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/blocklist")

    def bloquear_contato(self, numero: str) -> dict:
        """
        Bloqueia um contato no WhatsApp.
        Swagger: POST /api/{session}/block-contact
        """
        payload = {
            "phone": numero
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/block-contact", json=payload)

    def desbloquear_contato(self, numero: str) -> dict:
        """
        Desbloqueia um contato no WhatsApp.
        Swagger: POST /api/{session}/unblock-contact
        """
        payload = {
            "phone": numero
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/unblock-contact", json=payload)
