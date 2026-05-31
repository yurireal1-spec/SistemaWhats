class WhatsAppProfile:
    """
    Namespace para operações de Perfil e Aparelho/Sessão (Profile).
    """
    def __init__(self, client):
        self.client = client

    def alterar_username(self, novo_nome: str) -> dict:
        """
        Altera o nome de exibição (username) da sessão ativa.
        Swagger: POST /api/{session}/change-username
        """
        payload = {
            "name": novo_nome
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/change-username", json=payload)

    def alterar_foto_perfil(self, path: str) -> dict:
        """
        Altera a foto de perfil do número conectado.
        Swagger: POST /api/{session}/change-profile-image
        """
        payload = {
            "path": path
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/change-profile-image", json=payload)
