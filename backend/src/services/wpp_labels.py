class WhatsAppLabels:
    """
    Namespace para operações de Etiquetas (Labels) do WhatsApp Business.
    """
    def __init__(self, client):
        self.client = client

    def criar_nova_etiqueta(self, nome: str, cor: str) -> dict:
        """
        Cria uma nova etiqueta com cor personalizada.
        Swagger: POST /api/{session}/add-new-label
        """
        payload = {
            "name": nome,
            "color": cor
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/add-new-label", json=payload)

    def adicionar_ou_remover_etiqueta(self, id_etiqueta: str, target_id: str, adicionar: bool) -> dict:
        """
        Vincula ou desvincula uma etiqueta a um chat ou mensagem específico.
        Swagger: POST /api/{session}/add-or-remove-label
        """
        payload = {
            "labelId": id_etiqueta,
            "chatId": target_id,
            "value": adicionar
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/add-or-remove-label", json=payload)

    def obter_todas_etiquetas(self) -> dict:
        """
        Retorna todas as etiquetas cadastradas no celular.
        Swagger: GET /api/{session}/get-all-labels
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/get-all-labels")

    def deletar_todas_etiquetas(self) -> dict:
        """
        Remove todas as etiquetas.
        Swagger: PUT /api/{session}/delete-all-labels
        """
        return self.client._executar_requisicao("PUT", f"{self.client.session}/delete-all-labels")

    def deletar_etiqueta(self, id_etiqueta: str) -> dict:
        """
        Apaga uma etiqueta do sistema pelo ID.
        Swagger: PUT /api/{session}/delete-label/{id}
        """
        return self.client._executar_requisicao("PUT", f"{self.client.session}/delete-label/{id_etiqueta}")
