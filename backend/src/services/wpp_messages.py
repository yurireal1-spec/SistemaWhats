import os

class WhatsAppMessages:
    """
    Namespace para operações de Mensagens (Messages) e Status/Stories.
    """
    def __init__(self, client):
        self.client = client

    def enviar_mensagem(self, numero: str, texto: str, is_group: bool = False, options: dict = None) -> dict:
        """
        Envia uma mensagem de texto simples.
        Swagger: POST /api/{session}/send-message
        """
        payload = {
            "phone": numero,
            "message": texto,
            "isGroup": is_group,
            "options": options or {}
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-message", json=payload)

    def editar_mensagem(self, id_mensagem: str, novo_texto: str, options: dict = None) -> dict:
        """
        Edita o texto de uma mensagem enviada anteriormente.
        Swagger: POST /api/{session}/edit-message
        """
        payload = {
            "id": id_mensagem,
            "newText": novo_texto,
            "options": options or {}
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/edit-message", json=payload)

    def enviar_imagem(self, numero: str, path_ou_base64: str, legenda: str = None, is_group: bool = False, is_base64: bool = False) -> dict:
        """
        Envia uma imagem por caminho de arquivo local ou string base64.
        Swagger: POST /api/{session}/send-image / send-file
        """
        if is_base64:
            payload = {
                "phone": numero,
                "base64": path_ou_base64,
                "filename": "imagem.png",
                "caption": legenda or "",
                "isGroup": is_group
            }
            return self.client._executar_requisicao("POST", f"{self.client.session}/send-file-base64", json=payload)
        else:
            payload = {
                "phone": numero,
                "path": path_ou_base64,
                "caption": legenda or "",
                "isGroup": is_group
            }
            return self.client._executar_requisicao("POST", f"{self.client.session}/send-image", json=payload)

    def enviar_sticker(self, numero: str, path_ou_base64: str, is_group: bool = False, is_base64: bool = False) -> dict:
        """
        Envia uma imagem convertendo-a em sticker (figura).
        Swagger: POST /api/{session}/send-sticker
        """
        if is_base64:
            payload = {
                "phone": numero,
                "base64": path_ou_base64,
                "isGroup": is_group
            }
            return self.client._executar_requisicao("POST", f"{self.client.session}/send-file-base64", json=payload) # wppconnect supports base64 files
        else:
            payload = {
                "phone": numero,
                "path": path_ou_base64,
                "isGroup": is_group
            }
            return self.client._executar_requisicao("POST", f"{self.client.session}/send-sticker", json=payload)

    def enviar_resposta(self, numero: str, texto: str, id_mensagem_citada: str, is_group: bool = False) -> dict:
        """
        Responde a uma mensagem específica (marcando/citando a mensagem anterior).
        Swagger: POST /api/{session}/send-reply
        """
        payload = {
            "phone": numero,
            "message": texto,
            "isGroup": is_group,
            "options": {
                "quotedMsg": id_mensagem_citada
            }
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-message", json=payload)

    def enviar_arquivo(self, numero: str, path_ou_base64: str, legenda: str = None, nome_arquivo: str = "arquivo", is_group: bool = False, is_base64: bool = False) -> dict:
        """
        Envia qualquer tipo de documento ou arquivo.
        Swagger: POST /api/{session}/send-file / send-file-base64
        """
        if is_base64:
            payload = {
                "phone": numero,
                "base64": path_ou_base64,
                "filename": nome_arquivo,
                "caption": legenda or "",
                "isGroup": is_group
            }
            return self.client._executar_requisicao("POST", f"{self.client.session}/send-file-base64", json=payload)
        else:
            payload = {
                "phone": numero,
                "path": path_ou_base64,
                "caption": legenda or "",
                "isGroup": is_group
            }
            return self.client._executar_requisicao("POST", f"{self.client.session}/send-file", json=payload)

    def enviar_audio(self, numero: str, path_ou_base64: str, id_mensagem_citada: str = None, is_group: bool = False, is_base64: bool = False) -> dict:
        """
        Envia áudio gravado (formato PTT com microfone azul).
        Swagger: POST /api/{session}/send-voice / send-voice-base64
        """
        if is_base64:
            payload = {
                "phone": numero,
                "base64Ptt": path_ou_base64,
                "isGroup": is_group,
                "quotedMessageId": id_mensagem_citada
            }
            return self.client._executar_requisicao("POST", f"{self.client.session}/send-voice-base64", json=payload)
        else:
            payload = {
                "phone": numero,
                "path": path_ou_base64,
                "isGroup": is_group,
                "quotedMessageId": id_mensagem_citada
            }
            return self.client._executar_requisicao("POST", f"{self.client.session}/send-voice", json=payload)

    def enviar_status_texto(self, texto: str) -> dict:
        """
        Posta um status (Story) de texto.
        Swagger: POST /api/{session}/send-status
        """
        payload = {
            "message": texto
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-status", json=payload)

    def enviar_link_preview(self, numero: str, url: str, legenda: str, is_group: bool = False) -> dict:
        """
        Envia um link gerando a miniatura (preview).
        Swagger: POST /api/{session}/send-link-preview
        """
        payload = {
            "phone": numero,
            "url": url,
            "caption": legenda,
            "isGroup": is_group
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-link-preview", json=payload)

    def enviar_localizacao(self, numero: str, lat: str, lng: str, titulo: str, endereco: str, is_group: bool = False) -> dict:
        """
        Envia uma localização estática do Google Maps.
        Swagger: POST /api/{session}/send-location
        """
        payload = {
            "phone": numero,
            "lat": lat,
            "lng": lng,
            "title": titulo,
            "address": endereco,
            "isGroup": is_group
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-location", json=payload)

    def enviar_lista(self, numero: str, descricao: str, secoes: list, texto_botao: str, is_group: bool = False) -> dict:
        """
        Envia uma mensagem de lista interativa.
        Swagger: POST /api/{session}/send-list-message
        """
        payload = {
            "phone": numero,
            "description": descricao,
            "buttonText": texto_botao,
            "sections": secoes,
            "isGroup": is_group
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-list-message", json=payload)

    def enviar_enquete(self, numero: str, nome_enquete: str, opcoes: list, count_selecionavel: int = 1, is_group: bool = False) -> dict:
        """
        Envia uma enquete interativa.
        Swagger: POST /api/{session}/send-poll-message
        """
        payload = {
            "phone": numero,
            "name": nome_enquete,
            "choices": opcoes,
            "isGroup": is_group,
            "options": {
                "selectableCount": count_selecionavel
            }
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-poll-message", json=payload)

    def enviar_chave_pix(self, numero: str, chave: str, nome_recebedor: str, is_group: bool = False) -> dict:
        """
        Envia dados de pagamento Pix.
        Swagger: POST /api/{session}/send-pix-key
        """
        payload = {
            "phone": numero,
            "pixKey": chave,
            "merchantName": nome_recebedor,
            "isGroup": is_group
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-pix-key", json=payload)

    def baixar_midia(self, id_mensagem: str) -> dict:
        """
        Faz o download da mídia atrelada a uma mensagem específica.
        Swagger: POST /api/{session}/download-media
        """
        payload = {
            "messageId": id_mensagem
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/download-media", json=payload)

    def obter_midia_por_mensagem(self, id_mensagem: str) -> dict:
        """
        Obtém informações e o binário da mídia de uma mensagem.
        Swagger: GET /api/{session}/get-media-by-message/{messageId}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/get-media-by-message/{id_mensagem}")
