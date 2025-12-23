#!/usr/bin/env python3
"""
Configuração automática de DNS na Hostinger usando API Key do .env
"""
import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

class HostingerAPI:
    def __init__(self):
        self.api_key = os.getenv("HOSTINGER_API_KEY")
        self.base_url = "https://api.hostinger.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def test_connection(self):
        """Testa conexão com API"""
        try:
            response = requests.get(
                f"{self.base_url}/domains",
                headers=self.headers,
                timeout=10
            )
            return response.status_code == 200
        except:
            return False
    
    def get_domains(self):
        """Lista domínios"""
        response = requests.get(
            f"{self.base_url}/domains",
            headers=self.headers
        )
        return response.json()
    
    def get_dns_records(self, domain):
        """Obtém registros DNS"""
        response = requests.get(
            f"{self.base_url}/domains/{domain}/dns",
            headers=self.headers
        )
        return response.json()
    
    def add_dns_record(self, domain, record_type, name, value, ttl=3600):
        """Adiciona registro DNS"""
        data = {
            "type": record_type,
            "name": name,
            "content": value,
            "ttl": ttl
        }
        
        response = requests.post(
            f"{self.base_url}/domains/{domain}/dns",
            headers=self.headers,
            json=data
        )
        return response.json()
    
    def update_dns_record(self, domain, record_id, record_type, name, value, ttl=3600):
        """Atualiza registro DNS existente"""
        data = {
            "type": record_type,
            "name": name,
            "content": value,
            "ttl": ttl
        }
        
        response = requests.put(
            f"{self.base_url}/domains/{domain}/dns/{record_id}",
            headers=self.headers,
            json=data
        )
        return response.json()

def configure_vercel_dns(api, domain):
    """Configura DNS para Vercel"""
    print(f"\n🔧 Configurando DNS para {domain}...\n")
    
    # Verificar registros existentes
    print("📋 Verificando registros DNS atuais...")
    try:
        records = api.get_dns_records(domain)
        
        # Procurar registro A existente
        a_record_exists = False
        a_record_id = None
        
        for record in records.get("data", []):
            if record.get("type") == "A" and record.get("name") in ["@", ""]:
                a_record_exists = True
                a_record_id = record.get("id")
                print(f"   ✅ Registro A encontrado: {record.get('content')}")
                break
        
        # Procurar registro CNAME existente
        cname_record_exists = False
        cname_record_id = None
        
        for record in records.get("data", []):
            if record.get("type") == "CNAME" and record.get("name") == "www":
                cname_record_exists = True
                cname_record_id = record.get("id")
                print(f"   ✅ Registro CNAME encontrado: {record.get('content')}")
                break
        
        print()
        
    except Exception as e:
        print(f"⚠️  Não foi possível verificar registros existentes: {e}\n")
        records = {"data": []}
    
    # Configurar registro A
    print("📍 Configurando registro A...")
    try:
        if a_record_exists and a_record_id:
            # Atualizar existente
            result = api.update_dns_record(domain, a_record_id, "A", "@", "76.76.21.21")
            print(f"   ✅ Registro A atualizado: @ → 76.76.21.21")
        else:
            # Criar novo
            result = api.add_dns_record(domain, "A", "@", "76.76.21.21")
            print(f"   ✅ Registro A adicionado: @ → 76.76.21.21")
    except Exception as e:
        print(f"   ❌ Erro ao configurar registro A: {e}")
    
    print()
    
    # Configurar registro CNAME
    print("📍 Configurando registro CNAME...")
    try:
        if cname_record_exists and cname_record_id:
            # Atualizar existente
            result = api.update_dns_record(domain, cname_record_id, "CNAME", "www", "cname.vercel-dns.com")
            print(f"   ✅ Registro CNAME atualizado: www → cname.vercel-dns.com")
        else:
            # Criar novo
            result = api.add_dns_record(domain, "CNAME", "www", "cname.vercel-dns.com")
            print(f"   ✅ Registro CNAME adicionado: www → cname.vercel-dns.com")
    except Exception as e:
        print(f"   ❌ Erro ao configurar registro CNAME: {e}")
    
    print()
    return True

def main():
    print("="*70)
    print("  🤖 CONFIGURAÇÃO AUTOMÁTICA DE DNS - HOSTINGER API")
    print("="*70)
    print()
    
    # Verificar se API key existe
    api_key = os.getenv("HOSTINGER_API_KEY")
    
    if not api_key:
        print("❌ HOSTINGER_API_KEY não encontrada no .env!")
        print()
        print("Por favor, adicione no arquivo .env:")
        print("   HOSTINGER_API_KEY=sua_chave_aqui")
        return
    
    print("✅ API Key carregada do .env")
    print()
    
    # Inicializar API
    api = HostingerAPI()
    
    # Testar conexão
    print("🔌 Testando conexão com API Hostinger...")
    
    if not api.test_connection():
        print("❌ Não foi possível conectar à API Hostinger")
        print()
        print("Possíveis causas:")
        print("   1. API Key inválida")
        print("   2. Hostinger pode não ter API pública disponível")
        print("   3. Problema de rede")
        print()
        print("📋 SOLUÇÃO: Configuração manual")
        print()
        print("Siga estas instruções:")
        print("   1. Acesse: https://hpanel.hostinger.com")
        print("   2. Domínios → marquesdesignstudio.com")
        print("   3. DNS Zone Editor")
        print("   4. Adicione:")
        print("      - Tipo A: @ → 76.76.21.21")
        print("      - Tipo CNAME: www → cname.vercel-dns.com")
        print()
        
        # Abrir link
        import webbrowser
        open_panel = input("🌐 Abrir painel Hostinger agora? (s/n): ")
        if open_panel.lower() == 's':
            webbrowser.open("https://hpanel.hostinger.com")
        
        return
    
    print("✅ Conexão estabelecida com sucesso!")
    print()
    
    # Listar domínios
    print("📋 Buscando domínios...")
    try:
        domains_data = api.get_domains()
        domains = domains_data.get("data", [])
        
        print(f"✅ {len(domains)} domínio(s) encontrado(s):")
        for domain in domains:
            print(f"   • {domain.get('name', 'N/A')}")
        print()
        
    except Exception as e:
        print(f"❌ Erro ao buscar domínios: {e}")
        return
    
    # Verificar se marquesdesignstudio.com existe
    target_domain = "marquesdesignstudio.com"
    domain_found = any(d.get("name") == target_domain for d in domains)
    
    if not domain_found:
        print(f"❌ Domínio {target_domain} não encontrado!")
        print()
        print("Domínios disponíveis:")
        for domain in domains:
            print(f"   • {domain.get('name')}")
        return
    
    print(f"✅ Domínio {target_domain} encontrado!")
    print()
    
    # Configurar DNS
    success = configure_vercel_dns(api, target_domain)
    
    if success:
        print("="*70)
        print("  ✅ CONFIGURAÇÃO DNS CONCLUÍDA!")
        print("="*70)
        print()
        print("📊 Registros DNS configurados:")
        print("   ✅ A: @ → 76.76.21.21")
        print("   ✅ CNAME: www → cname.vercel-dns.com")
        print()
        print("⏰ Próximos passos:")
        print("   1. Aguarde 10-60 minutos para propagação DNS")
        print("   2. Verifique em: https://dnschecker.org")
        print("   3. Adicione domínio no Vercel Dashboard")
        print()
        print("🔗 Links úteis:")
        print("   • Hostinger: https://hpanel.hostinger.com")
        print("   • Vercel: https://vercel.com/dashboard")
        print("   • DNS Checker: https://dnschecker.org/?domain=marquesdesignstudio.com")
        print()
        
        # Abrir links
        open_links = input("🌐 Deseja abrir os links agora? (s/n): ")
        if open_links.lower() == 's':
            import webbrowser
            import time
            print("\n🌐 Abrindo navegador...")
            webbrowser.open("https://dnschecker.org/?domain=marquesdesignstudio.com&type=A")
            time.sleep(2)
            webbrowser.open("https://vercel.com/dashboard")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação cancelada pelo usuário")
    except Exception as e:
        print(f"\n\n❌ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
