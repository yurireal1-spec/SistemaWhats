class WhatsAppChat:
    """
    Namespace para operações de Chat.
    """
    def __init__(self, client):
        self.client = client

    def listar_chats(self, options: dict = None) -> dict:
        """
        Retorna a lista de chats da sessão ativa.
        Swagger: POST /api/{session}/list-chats
        """
        payload = options or {}
        return self.client._executar_requisicao("POST", f"{self.client.session}/list-chats", json=payload)

    def todos_chats_arquivados(self) -> dict:
        """
        Retorna todos os chats arquivados.
        Swagger: GET /api/{session}/all-chats-archived
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/all-chats-archived")

    def todos_chats_com_mensagens(self) -> dict:
        """
        Retorna todas as conversas com suas respectivas mensagens carregadas.
        Swagger: GET /api/{session}/all-chats-with-messages
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/all-chats-with-messages")

    def todas_mensagens_chat(self, numero: str) -> dict:
        """
        Obtém todas as mensagens dentro de uma conversa específica.
        Swagger: GET /api/{session}/all-messages-in-chat/{phone}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/all-messages-in-chat/{numero}")

    def todas_novas_mensagens(self) -> dict:
        """
        Obtém todas as novas mensagens.
        Swagger: GET /api/{session}/all-new-messages
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/all-new-messages")

    def mensagens_nao_lidas(self) -> dict:
        """
        Retorna mensagens não lidas.
        Swagger: GET /api/{session}/unread-messages
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/unread-messages")

    def todas_mensagens_nao_lidas(self) -> dict:
        """
        Retorna todas as mensagens marcadas como não lidas.
        Swagger: GET /api/{session}/all-unread-messages
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/all-unread-messages")

    def buscar_chat_por_id(self, numero: str) -> dict:
        """
        Retorna os detalhes de um chat específico.
        Swagger: GET /api/{session}/chat-by-id/{phone}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/chat-by-id/{numero}")

    def buscar_mensagem_por_id(self, id_mensagem: str) -> dict:
        """
        Obtém os metadados de uma mensagem específica via ID.
        Swagger: GET /api/{session}/message-by-id/{messageId}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/message-by-id/{id_mensagem}")

    def verificar_chat_online(self, numero: str) -> dict:
        """
        Verifica se um determinado contato está online.
        Swagger: GET /api/{session}/chat-is-online/{phone}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/chat-is-online/{numero}")

    def ultimo_visto(self, numero: str) -> dict:
        """
        Retorna o timestamp do 'Visto por Último' do contato.
        Swagger: GET /api/{session}/last-seen/{phone}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/last-seen/{numero}")

    def obter_silenciados(self, tipo: str = "all") -> dict:
        """
        Lista chats silenciados. Tipo pode ser 'all', 'chat', 'group'.
        Swagger: GET /api/{session}/list-mutes/{type}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/list-mutes/{tipo}")

    def carregar_e_obter_mensagens(self, numero: str) -> dict:
        """
        Carrega conversas antigas do banco local e retorna as mensagens.
        Swagger: GET /api/{session}/load-messages-in-chat/{phone}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/load-messages-in-chat/{numero}")

    def obter_mensagens(self, numero: str, limite: int = 100) -> dict:
        """
        Retorna o histórico de mensagens de uma conversa.
        Swagger: GET /api/{session}/get-messages/{phone}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/get-messages/{numero}?limit={limite}")

    def arquivar_chat(self, numero: str, arquivar: bool = True) -> dict:
        """
        Arquiva ou desarquiva um chat.
        Swagger: POST /api/{session}/archive-chat
        """
        payload = {
            "phone": numero,
            "value": arquivar
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/archive-chat", json=payload)

    def arquivar_todos_chats(self, arquivar: bool = True) -> dict:
        """
        Arquiva todas as conversas ativas.
        Swagger: POST /api/{session}/archive-all-chats
        """
        payload = {
            "value": arquivar
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/archive-all-chats", json=payload)

    def limpar_chat(self, numero: str) -> dict:
        """
        Limpa todo o histórico visível de mensagens de uma conversa específica.
        Swagger: POST /api/{session}/clear-chat
        """
        payload = {
            "phone": numero
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/clear-chat", json=payload)

    def limpar_todos_chats(self) -> dict:
        """
        Limpa as mensagens de todas as conversas do celular.
        Swagger: POST /api/{session}/clear-all-chats
        """
        return self.client._executar_requisicao("POST", f"{self.client.session}/clear-all-chats")

    def deletar_chat(self, numero: str) -> dict:
        """
        Apaga um chat inteiro.
        Swagger: POST /api/{session}/delete-chat
        """
        payload = {
            "phone": numero
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/delete-chat", json=payload)

    def deletar_todos_chats(self) -> dict:
        """
        Apaga todas as conversas.
        Swagger: POST /api/{session}/delete-all-chats
        """
        return self.client._executar_requisicao("POST", f"{self.client.session}/delete-all-chats")

    def deletar_mensagem(self, numero: str, id_mensagem: str, apenas_para_mim: bool = False) -> dict:
        """
        Apaga uma mensagem específica do histórico.
        Swagger: POST /api/{session}/delete-message
        """
        payload = {
            "phone": numero,
            "id": id_mensagem,
            "onlyLocal": apenas_para_mim
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/delete-message", json=payload)

    def reagir_mensagem(self, id_mensagem: str, reacao: str) -> dict:
        """
        Reage a uma mensagem com um emoji.
        Swagger: POST /api/{session}/react-message
        """
        payload = {
            "msgId": id_mensagem,
            "reaction": reacao
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/react-message", json=payload)

    def encaminhar_mensagens(self, numero: str, ids_mensagens: list) -> dict:
        """
        Encaminha uma lista de mensagens para outro contato.
        Swagger: POST /api/{session}/forward-messages
        """
        payload = {
            "phone": numero,
            "responses": ids_mensagens
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/forward-messages", json=payload)

    def marcar_nao_lido(self, numero: str) -> dict:
        """
        Marca um chat como não lido.
        Swagger: POST /api/{session}/mark-unseen
        """
        payload = {
            "phone": numero
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/mark-unseen", json=payload)

    def fixar_chat(self, numero: str, fixar: bool = True) -> dict:
        """
        Fixa ou desafixa um chat no topo.
        Swagger: POST /api/{session}/pin-chat
        """
        payload = {
            "phone": numero,
            "value": fixar
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/pin-chat", json=payload)

    def enviar_vcard_contato(self, numero: str, numero_vcard: str, nome_vcard: str) -> dict:
        """
        Envia um cartão de contato (VCard).
        Swagger: POST /api/{session}/contact-vcard
        """
        payload = {
            "phone": numero,
            "contactsId": numero_vcard,
            "name": nome_vcard
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/contact-vcard", json=payload)

    def silenciar_chat(self, numero: str, silenciar: bool = True, tempo: str = "8h") -> dict:
        """
        Silencia ou desilencia um chat. Tempo pode ser "8h", "1w", "always" etc.
        Swagger: POST /api/{session}/send-mute
        """
        # Trata tempo para segundos no wppconnect
        # O wppconnect aceita parâmetros como '8h' ou número de segundos diretamente
        payload = {
            "phone": numero,
            "value": silenciar,
            "time": tempo
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-mute", json=payload)

    def marcar_como_lido(self, numero: str) -> dict:
        """
        Marca todas as mensagens do chat como lidas.
        Swagger: POST /api/{session}/send-seen
        """
        payload = {
            "phone": numero
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-seen", json=payload)

    def definir_estado_chat(self, numero: str, estado: str) -> dict:
        """
        Define o estado da conversa (0 para pausado, 1 para digitando, 2 para gravando).
        Swagger: POST /api/{session}/chat-state
        """
        payload = {
            "phone": numero,
            "chatstate": estado # 'typing', 'recording', 'paused'
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/chat-state", json=payload)

    def definir_mensagens_temporarias(self, numero: str, duracao: int) -> dict:
        """
        Define mensagens temporárias em segundos (ex: 86400 para 24 horas, 0 para desativar).
        Swagger: POST /api/{session}/temporary-messages
        """
        payload = {
            "phone": numero,
            "value": duracao
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/temporary-messages", json=payload)

    def definir_digitando(self, numero: str, digitando: bool) -> dict:
        """
        Ativa ou desativa a exibição de "digitando..." para o contato.
        Swagger: POST /api/{session}/typing
        """
        payload = {
            "phone": numero,
            "value": digitando
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/typing", json=payload)

    def definir_gravando(self, numero: str, gravando: bool) -> dict:
        """
        Ativa ou desativa a exibição de "gravando áudio..." para o contato.
        Swagger: POST /api/{session}/recording
        """
        payload = {
            "phone": numero,
            "value": gravando
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/recording", json=payload)

    def favoritar_mensagem(self, id_mensagem: str, favoritar: bool = True) -> dict:
        """
        Favorita ou desfavorita uma mensagem.
        Swagger: POST /api/{session}/star-message
        """
        payload = {
            "messageId": id_mensagem,
            "value": favoritar
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/star-message", json=payload)

    def obter_reacoes(self, id_mensagem: str) -> dict:
        """
        Retorna as reações aplicadas em uma mensagem.
        Swagger: GET /api/{session}/reactions/{id}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/reactions/{id_mensagem}")

    def obter_votos(self, id_mensagem: str) -> dict:
        """
        Retorna os votos aplicados a uma enquete (mensagem de poll).
        Swagger: GET /api/{session}/votes/{id}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/votes/{id_mensagem}")

    def rejeitar_chamada(self, id_chamada: str) -> dict:
        """
        Rejeita uma chamada de voz/vídeo recebida pelo ID.
        Swagger: POST /api/{session}/reject-call
        """
        payload = {
            "callId": id_chamada
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/reject-call", json=payload)
