import requests
from .wpp_messages import WhatsAppMessages
from .wpp_chat import WhatsAppChat
from .wpp_contact import WhatsAppContact
from .wpp_group import WhatsAppGroup
from .wpp_profile import WhatsAppProfile
from .wpp_status import WhatsAppStatus
from .wpp_labels import WhatsAppLabels
from .wpp_catalog import WhatsAppCatalog
from .wpp_misc import WhatsAppMisc

class WhatsAppClient:
    """
    O Cliente Central do WppConnect.
    
    Responsável por gerenciar o ciclo de vida da conexão, autenticação,
    e centralizar as chamadas dos endpoints da tag 'Auth' do Swagger.
    """
        
    def __init__(self, session: str, secret_key: str):
        """
        Inicializa o cliente base configurando o endereço e as credenciais.
        
        :param session: Nome da sessão/instância do WhatsApp (ex: 'yuri').
        :param secret_key: Chave secreta de autenticação configurada no servidor.
        """
        self.base_url = "http://localhost:21465/api"
        self.session = session
        self.secret_key = secret_key
        self._token = None 
        self.headers = {"Content-Type": "application/json"}

        # Instanciar os submódulos correspondentes às tags do Swagger
        self.messages = WhatsAppMessages(self)
        self.chat = WhatsAppChat(self)
        self.contact = WhatsAppContact(self)
        self.group = WhatsAppGroup(self)
        self.profile = WhatsAppProfile(self)
        self.status = WhatsAppStatus(self)
        self.labels = WhatsAppLabels(self)
        self.catalog = WhatsAppCatalog(self)
        self.misc = WhatsAppMisc(self)

    def _executar_requisicao(self, metodo: str, endpoint: str, **kwargs) -> dict:
        """
        Método auxiliar para realizar requisições automáticas e autenticadas para o servidor.
        
        :param metodo: Método HTTP (GET, POST, PUT, DELETE).
        :param endpoint: O caminho relativo da API (ex: 'yuri/send-message').
        :return: JSON retornado pelo servidor ou dicionário contendo o erro.
        """
        if not self._token:
            if not self.autenticar():
                return {"erro": "Falha na autenticação (geração de token)"}

        # Sincroniza e garante o token atualizado nos headers
        self.headers["Authorization"] = f"Bearer {self._token}"
        
        # Remove headers passados em kwargs se houver para evitar conflitos
        headers = kwargs.pop("headers", self.headers)
        
        url = f"{self.base_url}/{endpoint}"
        try:
            resposta = requests.request(metodo, url, headers=headers, **kwargs)
            if resposta.status_code in [200, 201]:
                try:
                    return resposta.json()
                except ValueError:
                    return {"sucesso": True, "resposta": resposta.text}
            try:
                return {"erro": resposta.json(), "status_code": resposta.status_code}
            except ValueError:
                return {"erro": resposta.text, "status_code": resposta.status_code}
        except Exception as e:
            return {"erro": str(e)}

    def autenticar(self) -> bool:
        """
        Gera um Token JWT usando a secret_key e atualiza os cabeçalhos globais.
        
        Swagger: POST /api/{session}/{secretkey}/generate-token
        
        :return: True se a autenticação foi bem-sucedida, False caso contrário.
        """
        url = f"{self.base_url}/{self.session}/{self.secret_key}/generate-token"
        
        try:
            resposta = requests.post(url)
            if resposta.status_code in [200, 201]:
                self._token = resposta.json().get("token")
                self.headers["Authorization"] = f"Bearer {self._token}"
                return True
            return False
        except Exception as e:
            print(f"💥 Erro ao autenticar: {e}")
            return False

    def mostrar_todas_sessoes(self) -> dict:
        """
        Lista todas as sessões ativas e configuradas no servidor WppConnect.
        
        Swagger: GET /api/{secretkey}/show-all-sessions
        
        :return: Dicionário JSON com a lista de sessões ou mensagem de erro.
        """
        url = f"{self.base_url}/{self.secret_key}/show-all-sessions"
        
        try:
            resposta = requests.get(url) 
            if resposta.status_code == 200:
                return resposta.json()
            return {"erro": resposta.text}
        except Exception as e:
            return {"erro": str(e)}

    def iniciar_todos(self) -> dict:
        """
        Dispara a inicialização em massa de todas as sessões do servidor.
        
        Swagger: POST /api/{secretkey}/start-all
        
        :return: Dicionário informando o sucesso do disparo e o corpo da resposta.
        """
        url = f"{self.base_url}/{self.secret_key}/start-all?session={self.session}"
        
        try:
            resposta = requests.post(url)
            return {
                "sucesso": resposta.status_code in [200, 201],
                "corpo": resposta.json() if resposta.status_code == 200 else resposta.text
            }
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}

    def verificar_conexao(self) -> bool:
        """
        Verifica se a sessão atual está conectada à internet e ao WhatsApp.
        
        Swagger: GET /api/{session}/check-connection-session (Requer Bearer Token)
        
        :return: True se estiver conectado com sucesso, False se houver falha.
        """
        if not self._token:
            if not self.autenticar():
                return False

        url = f"{self.base_url}/{self.session}/check-connection-session"
        
        try:
            resposta = requests.get(url, headers=self.headers)
            if resposta.status_code == 200:
                dados = resposta.json()
                
                # ✨ Validação robusta: aceita se 'status' for True, se 'connected' for True 
                # ou se a mensagem contiver "Connected"
                is_status_true = dados.get("status") is True
                is_connected_true = dados.get("connected") is True
                is_message_connected = "connected" in str(dados.get("message", "")).lower()
                
                return is_status_true or is_connected_true or is_message_connected
                
            return False
            
        except Exception as e:
            print(f"💥 Erro ao verificar conexão do WhatsApp: {e}")
            return False
            
        
    def iniciar_sessao(self) -> bool:
        """
        Inicia a sessão atual abrindo o navegador interno (Puppeteer) no servidor.
        
        Swagger: POST /api/{session}/start-session (Requer Bearer Token)
        
        :return: True se o comando de inicialização foi aceito pelo servidor.
        """
        if not self._token:
            if not self.autenticar():
                return False

        url = f"{self.base_url}/{self.session}/start-session"
        payload = {"waitQrCode": False}
        
        try:
            resposta = requests.post(url, json=payload, headers=self.headers)
            if resposta.status_code in [200, 201]:
                print(f"🚀 Chamada para iniciar sessão '{self.session}' enviada!")
                return True
            print(f"❌ Falha ao iniciar sessão '{self.session}': {resposta.text}")
            return False
        except Exception as e:
            print(f"💥 Erro de conexão ao iniciar sessão '{self.session}': {e}")
            return False
        
    def obter_qrcode(self) -> dict:
        """
        Recupera o estado atual do QR Code da sessão em formato de imagem/base64.
        
        Swagger: GET /api/{session}/qrcode-session (Requer Bearer Token)
        
        :return: JSON contendo os dados de imagem do QR Code ou bloco de erro.
        """
        if not self._token:
            if not self.autenticar():
                return {"erro": "Falha na autenticação"}

        url = f"{self.base_url}/{self.session}/qrcode-session"
        try:
            resposta = requests.get(url, headers=self.headers)
            if resposta.status_code == 200:
                return resposta.json()
            return {"erro": resposta.text, "status_code": resposta.status_code}
        except Exception as e:
            return {"erro": str(e)}

    def deslogar_sessao(self) -> bool:
        """
        Desconecta e desvincula o WhatsApp do servidor (Equivalente a 'Sair' no celular).
        Apaga os dados de sessão salvos localmente.
        
        Swagger: POST /api/{session}/logout-session (Requer Bearer Token)
        
        :return: True se o logout foi concluído com sucesso.
        """
        if not self._token:
            if not self.autenticar():
                return False

        url = f"{self.base_url}/{self.session}/logout-session"
        try:
            resposta = requests.post(url, headers=self.headers)
            return resposta.status_code in [200, 201]
        except Exception as e:
            print(f"💥 Erro ao deslogar sessão: {e}")
            return False

    def fechar_sessao(self) -> bool:
        """
        Fecha o navegador virtual da sessão para liberar memória RAM.
        Mantém os dados de login intactos para o próximo login.
        
        Swagger: POST /api/{session}/close-session (Requer Bearer Token)
        
        :return: True se a sessão foi fechada corretamente no servidor.
        """
        if not self._token:
            if not self.autenticar():
                return False

        url = f"{self.base_url}/{self.session}/close-session"
        try:
            resposta = requests.post(url, headers=self.headers)
            return resposta.status_code in [200, 201]
        except Exception as e:
            print(f"💥 Erro ao fechar sessão: {e}")
            return False

    def status_da_sessao(self) -> dict:
        """
        Retorna o estado operacional em tempo real da sessão (ex: CONNECTED, QRCODE).
        
        Swagger: GET /api/{session}/status-session (Requer Bearer Token)
        
        :return: JSON contendo a string de status do servidor.
        """
        if not self._token:
            if not self.autenticar():
                return {"status": "NOT_AUTHENTICATED"}

        url = f"{self.base_url}/{self.session}/status-session"
        try:
            resposta = requests.get(url, headers=self.headers)
            if resposta.status_code == 200:
                return resposta.json()
            return {"erro": resposta.text}
        except Exception as e:
            return {"erro": str(e)}