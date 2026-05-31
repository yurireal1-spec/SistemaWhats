class WhatsAppStatus:
    """
    Namespace para operações de Stories/Status do WhatsApp.
    """
    def __init__(self, client):
        self.client = client

    def enviar_status_texto(self, texto: str) -> dict:
        """
        Publica um novo status (Story) contendo apenas texto.
        Swagger: POST /api/{session}/send-text-storie
        """
        payload = {
            "text": texto
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-text-storie", json=payload)

    def enviar_status_imagem(self, path: str, legenda: str = None) -> dict:
        """
        Publica uma imagem nos Status.
        Swagger: POST /api/{session}/send-image-storie
        """
        payload = {
            "path": path,
            "caption": legenda or ""
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-image-storie", json=payload)

    def enviar_status_video(self, path: str, legenda: str = None) -> dict:
        """
        Publica um vídeo nos Status.
        Swagger: POST /api/{session}/send-video-storie
        """
        payload = {
            "path": path,
            "caption": legenda or ""
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-video-storie", json=payload)
