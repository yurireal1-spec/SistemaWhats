import os
import sys
from dotenv import load_dotenv

# Garante que o diretório src está no path de importação
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.wpp_client import WhatsAppClient

# Carrega as variáveis de ambiente
load_dotenv()

def testar_inicializacao():
    print("====== 🧪 INICIANDO TESTE DOS MÓDULOS INTEGRADOS ======\n")
    
    SESSION_NAME = "yuri"
    SECRET_KEY = os.getenv("SECRET_KEY", "Wpp15324@")
    
    print(f"🔄 Instanciando WhatsAppClient com a sessão '{SESSION_NAME}'...")
    wpp = WhatsAppClient(session=SESSION_NAME, secret_key=SECRET_KEY)
    
    print("\n🔍 Verificando os namespaces compostos:")
    
    namespaces = {
        "Messages (messages)": wpp.messages,
        "Chat (chat)": wpp.chat,
        "Contact (contact)": wpp.contact,
        "Group (group)": wpp.group,
        "Profile (profile)": wpp.profile,
        "Status Stories (status)": wpp.status,
        "Labels (labels)": wpp.labels,
        "Catalog & Business (catalog)": wpp.catalog,
        "Misc (misc)": wpp.misc
    }
    
    sucesso_geral = True
    for nome, instancia in namespaces.items():
        if instancia is not None:
            print(f"   ✅ Namespace {nome} carregado: {instancia.__class__.__name__}")
            # Verifica se o cliente interno está apontando de volta para a mesma instância wpp
            if instancia.client == wpp:
                print(f"      👉 Cliente referenciado corretamente!")
            else:
                print(f"      ❌ Erro: Referência cruzada inválida para o cliente base!")
                sucesso_geral = False
        else:
            print(f"   ❌ Namespace {nome} NÃO carregado!")
            sucesso_geral = False
            
    print("\n🕵️‍♂️ Verificando se o import direto via pacote 'services' funciona:")
    try:
        import services
        classes = [
            'WhatsAppClient', 'WhatsAppMessages', 'WhatsAppChat',
            'WhatsAppContact', 'WhatsAppGroup', 'WhatsAppProfile',
            'WhatsAppStatus', 'WhatsAppLabels', 'WhatsAppCatalog', 'WhatsAppMisc'
        ]
        for cls_name in classes:
            getattr(services, cls_name)
        print("   ✅ Importações bem-sucedidas através do services/__init__.py!")
    except Exception as e:
        print(f"   ❌ Falha ao importar do pacote services: {e}")
        sucesso_geral = False
        
    print("\n=======================================================")
    if sucesso_geral:
        print("🎉 TODOS OS SERVIÇOS E NAMESPACES FORAM INTEGRADOS COM SUCESSO!")
    else:
        print("❌ HOUVE FALHA NA INTEGRAÇÃO DOS SERVIÇOS.")
    print("=======================================================")

if __name__ == "__main__":
    testar_inicializacao()
