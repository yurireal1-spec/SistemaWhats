class WhatsAppCatalog:
    """
    Namespace para operações de Catálogo de Produtos e Carrinho (Business).
    """
    def __init__(self, client):
        self.client = client

    def obter_produtos(self) -> dict:
        """
        Retorna a lista de produtos cadastrados no catálogo.
        Swagger: GET /api/{session}/get-products
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/get-products")

    def obter_produto_por_id(self, id_produto: str) -> dict:
        """
        Obtém os detalhes de um produto específico.
        Swagger: GET /api/{session}/get-product-by-id
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/get-product-by-id?productId={id_produto}")

    def adicionar_produto(self, payload: dict) -> dict:
        """
        Adiciona um novo produto ao catálogo.
        Swagger: POST /api/{session}/add-product
        """
        return self.client._executar_requisicao("POST", f"{self.client.session}/add-product", json=payload)

    def editar_produto(self, payload: dict) -> dict:
        """
        Edita as informações de um produto existente.
        Swagger: POST /api/{session}/edit-product
        """
        return self.client._executar_requisicao("POST", f"{self.client.session}/edit-product", json=payload)

    def deletar_produtos(self, ids_produtos: list) -> dict:
        """
        Exclui múltiplos produtos do catálogo de uma vez.
        Swagger: POST /api/{session}/del-products
        """
        payload = {
            "productsId": ids_produtos
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/del-products", json=payload)

    def obter_colecoes(self) -> dict:
        """
        Retorna as coleções do catálogo.
        Swagger: GET /api/{session}/get-collections
        """
        return self.client._executar_requisicao("GET", f"{self.client.session}/get-collections")

    def criar_colecao(self, nome: str, ids_produtos: list) -> dict:
        """
        Cria uma nova coleção agrupando produtos específicos.
        Swagger: POST /api/{session}/create-collection
        """
        payload = {
            "name": nome,
            "productsId": ids_produtos
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/create-collection", json=payload)

    def editar_colecao(self, id_colecao: str, nome: str, ids_produtos: list) -> dict:
        """
        Edita a coleção passando os produtos que a compõem.
        Swagger: POST /api/{session}/edit-collection
        """
        payload = {
            "collectionId": id_colecao,
            "name": nome,
            "productsId": ids_produtos
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/edit-collection", json=payload)

    def deletar_colecao(self, id_colecao: str) -> dict:
        """
        Exclui uma coleção do catálogo.
        Swagger: POST /api/{session}/del-collection
        """
        payload = {
            "collectionId": id_colecao
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/del-collection", json=payload)

    def enviar_link_catalogo(self, numero: str) -> dict:
        """
        Envia o link do catálogo de produtos para um cliente.
        Swagger: POST /api/{session}/send-link-catalog
        """
        payload = {
            "phone": numero
        }
        return self.client._executar_requisicao("POST", f"{self.client.session}/send-link-catalog", json=payload)
