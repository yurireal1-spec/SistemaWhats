class WhatsAppGroup:
    """
    Namespace para operações de Grupos.
    """
    def __init__(self, client):
        self.client = client

    def obter_todas_listas_transmissao(self) -> dict:
        """
        Retorna todas as listas de transmissão ativas.
        Swagger: GET /api/{session}/all-broadcast-list
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/all-broadcast-list")

    def obter_todos_grupos(self) -> dict:
        """
        Retorna a lista de todos os grupos em que o usuário está inserido.
        Swagger: GET /api/{session}/all-groups
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/all-groups")

    def obter_membros_grupo(self, id_grupo: str) -> dict:
        """
        Retorna a lista de membros de um grupo específico.
        Swagger: GET /api/{session}/group-members/{groupId}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/group-members/{id_grupo}")

    def obter_grupos_comuns(self, wid: str) -> dict:
        """
        Obtém a lista de grupos em comum com um contato específico.
        Swagger: GET /api/{session}/common-groups/{wid}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/common-groups/{wid}")

    def obter_administradores_grupo(self, id_grupo: str) -> dict:
        """
        Retorna os administradores de um grupo específico.
        Swagger: GET /api/{session}/group-admins/{groupId}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/group-admins/{id_grupo}")

    def obter_informacoes_grupo(self, id_grupo: str) -> dict:
        """
        Retorna metadados e informações detalhadas de um grupo.
        Swagger: GET /api/{session}/group-info/{groupId}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/group-info/{id_grupo}")

    def obter_link_convite_grupo(self, id_grupo: str) -> dict:
        """
        Retorna o link de convite ativo do grupo.
        Swagger: GET /api/{session}/group-invite-link/{groupId}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/group-invite-link/{id_grupo}")

    def revogar_link_convite_grupo(self, id_grupo: str) -> dict:
        """
        Revoga o link de convite antigo e gera um novo para o grupo.
        Swagger: GET /api/{session}/group-revoke-link/{groupId}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/group-revoke-link/{id_grupo}")

    def obter_ids_membros_grupo(self, id_grupo: str) -> dict:
        """
        Retorna apenas os IDs serializados dos membros de um grupo.
        Swagger: GET /api/{session}/group-members-ids/{groupId}
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/group-members-ids/{id_grupo}")

    def criar_grupo(self, nome_grupo: str, participantes: list) -> dict:
        """
        Cria um novo grupo com um nome e uma lista de participantes.
        Swagger: POST /api/{session}/create-group
        """
        payload = {
            "groupname": nome_grupo,
            "phones": participantes
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/create-group", json=payload)

    def sair_do_grupo(self, id_grupo: str) -> dict:
        """
        Sai de um grupo de WhatsApp.
        Swagger: POST /api/{session}/leave-group
        """
        payload = {
            "groupId": id_grupo
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/leave-group", json=payload)

    def entrar_por_codigo_convite(self, codigo: str) -> dict:
        """
        Entra em um grupo usando o código identificador contido no link de convite.
        Swagger: POST /api/{session}/join-code
        """
        payload = {
            "inviteCode": codigo
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/join-code", json=payload)

    def adicionar_participante(self, id_grupo: str, participante: str) -> dict:
        """
        Adiciona um participante ao grupo.
        Swagger: POST /api/{session}/add-participant-group
        """
        payload = {
            "groupId": id_grupo,
            "phone": participante
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/add-participant-group", json=payload)

    def remover_participante(self, id_grupo: str, participante: str) -> dict:
        """
        Remove um participante do grupo.
        Swagger: POST /api/{session}/remove-participant-group
        """
        payload = {
            "groupId": id_grupo,
            "phone": participante
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/remove-participant-group", json=payload)

    def promover_participante(self, id_grupo: str, participante: str) -> dict:
        """
        Promove um participante a administrador do grupo.
        Swagger: POST /api/{session}/promote-participant-group
        """
        payload = {
            "groupId": id_grupo,
            "phone": participante
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/promote-participant-group", json=payload)

    def demover_participante(self, id_grupo: str, participante: str) -> dict:
        """
        Demove o cargo de administrador de um participante no grupo.
        Swagger: POST /api/{session}/demote-participant-group
        """
        payload = {
            "groupId": id_grupo,
            "phone": participante
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/demote-participant-group", json=payload)

    def obter_grupo_por_link_convite(self, link: str) -> dict:
        """
        Obtém metadados do grupo passando a URL de convite completa.
        Swagger: POST /api/{session}/group-info-from-invite-link
        """
        payload = {
            "inviteLink": link
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/group-info-from-invite-link", json=payload)

    def definir_descricao_grupo(self, id_grupo: str, descricao: str) -> dict:
        """
        Altera a descrição visível do grupo.
        Swagger: POST /api/{session}/group-description
        """
        payload = {
            "groupId": id_grupo,
            "description": descricao
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/group-description", json=payload)

    def definir_propriedade_grupo(self, id_grupo: str, propriedade: str, valor: bool) -> dict:
        """
        Define propriedades internas do grupo (ex: 'announcement', 'restrictOnlyAdmins').
        Swagger: POST /api/{session}/group-property
        """
        payload = {
            "groupId": id_grupo,
            "property": propriedade,
            "value": valor
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/group-property", json=payload)

    def definir_assunto_grupo(self, id_grupo: str, assunto: str) -> dict:
        """
        Altera o título/nome do grupo.
        Swagger: POST /api/{session}/group-subject
        """
        payload = {
            "groupId": id_grupo,
            "subject": assunto
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/group-subject", json=payload)

    def definir_mensagens_apenas_admin(self, id_grupo: str, apenas_admin: bool) -> dict:
        """
        Determina se apenas administradores podem enviar mensagens no grupo.
        Swagger: POST /api/{session}/messages-admins-only
        """
        payload = {
            "groupId": id_grupo,
            "value": apenas_admin
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/messages-admins-only", json=payload)

    def definir_foto_grupo(self, id_grupo: str, path: str) -> dict:
        """
        Altera a foto de perfil do grupo enviando a imagem correspondente.
        Swagger: POST /api/{session}/group-pic
        """
        payload = {
            "groupId": id_grupo,
            "path": path
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/group-pic", json=payload)

    def alterar_privacidade_grupo(self, id_grupo: str, privacidade: str) -> dict:
        """
        Altera as configurações de privacidade do grupo.
        Swagger: POST /api/{session}/change-privacy-group
        """
        payload = {
            "groupId": id_grupo,
            "privacy": privacidade
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/change-privacy-group", json=payload)
