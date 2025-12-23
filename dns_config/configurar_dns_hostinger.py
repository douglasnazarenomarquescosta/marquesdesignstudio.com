#!/usr/bin/env python3
"""
Configuração Automática de DNS via Hostinger API
"""
import requests
import json

class HostingerDNS:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.hostinger.com/dns/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def list_domains(self):
        """Lista todos os domínios"""
        response = requests.get(
            f"{self.base_url}/domains",
            headers=self.headers
        )
        return response.json()
    
    def get_dns_records(self, domain):
        """Obtém registros DNS de um domínio"""
        response = requests.get(
            f"{self.base_url}/domains/{domain}/records",
            headers=self.headers
        )
        return response.json()
    
    def add_a_record(self, domain, name, value, ttl=3600):
        """Adiciona registro A"""
        data = {
            "type": "A",
            "name": name,
            "content": value,
            "ttl": ttl
        }
        
        response = requests.post(
            f"{self.base_url}/domains/{domain}/records",
            headers=self.headers,
            json=data
        )
        return response.json()
    
    def add_cname_record(self, domain, name, value, ttl=3600):
        """Adiciona registro CNAME"""
        data = {
            "type": "CNAME",
            "name": name,
            "content": value,
            "ttl": ttl
        }
        
        response = requests.post(
            f"{self.base_url}/domains/{domain}/records",
            headers=self.headers,
            json=data
        )
        return response.json()
    
    def configure_vercel_dns(self, domain):
        """Configura DNS para Vercel automaticamente"""
        print(f"🔧 Configurando DNS para {domain}...")
        
        # Adicionar registro A
        print("📍 Adicionando registro A...")
        a_result = self.add_a_record(domain, "@", "76.76.21.21")
        
        if "error" not in a_result:
            print("✅ Registro A adicionado: @ → 76.76.21.21")
        else:
            print(f"❌ Erro ao adicionar registro A: {a_result['error']}")
        
        # Adicionar registro CNAME
        print("📍 Adicionando registro CNAME...")
        cname_result = self.add_cname_record(domain, "www", "cname.vercel-dns.com")
        
        if "error" not in cname_result:
            print("✅ Registro CNAME adicionado: www → cname.vercel-dns.com")
        else:
            print(f"❌ Erro ao adicionar CNAME: {cname_result['error']}")
        
        print("\n✅ Configuração DNS concluída!")
        print("⏳ Aguarde 10-60 minutos para propagação")
        
        return True

def main():
    print("="*70)
    print("  🔧 CONFIGURAÇÃO AUTOMÁTICA DE DNS - HOSTINGER")
    print("="*70)
    print()
    
    # Pedir API Key
    print("Para configurar automaticamente, você precisa de uma API Key da Hostinger.")
    print()
    print("📋 Como obter API Key da Hostinger:")
    print("   1. Login: https://hpanel.hostinger.com")
    print("   2. Menu: Avançado → API")
    print("   3. Clique: Gerar Nova Chave")
    print("   4. Copie a chave")
    print()
    
    api_key = input("Cole sua API Key aqui (ou ENTER para pular): ").strip()
    
    if not api_key:
        print("\n⚠️  Sem API Key. Mostrando instruções manuais...\n")
        show_manual_instructions()
        return
    
    # Configurar DNS
    dns = HostingerDNS(api_key)
    
    try:
        # Listar domínios
        print("\n📋 Buscando seus domínios...")
        domains = dns.list_domains()
        
        if "marquesdesignstudio.com" in domains:
            dns.configure_vercel_dns("marquesdesignstudio.com")
        else:
            print("❌ Domínio marquesdesignstudio.com não encontrado")
            print(f"📋 Domínios encontrados: {domains}")
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("\n⚠️  Configuração automática falhou. Use o método manual.")
        show_manual_instructions()

def show_manual_instructions():
    """Mostra instruções manuais detalhadas"""
    print("="*70)
    print("  📋 CONFIGURAÇÃO MANUAL DE DNS")
    print("="*70)
    print()
    
    print("🌐 Acesse: https://hpanel.hostinger.com")
    print()
    
    print("📍 PASSO A PASSO:")
    print()
    print("1. Faça login no painel Hostinger")
    print("2. Menu lateral → Domínios")
    print("3. Clique em: marquesdesignstudio.com")
    print("4. Aba superior → DNS / Name Servers")
    print("5. Clique em: DNS Zone Editor ou Gerenciar DNS")
    print()
    
    print("6. ADICIONAR REGISTRO A:")
    print("   ┌─────────────────────────────┐")
    print("   │ Tipo: A                     │")
    print("   │ Nome: @                     │")
    print("   │ Valor: 76.76.21.21          │")
    print("   │ TTL: 3600                   │")
    print("   └─────────────────────────────┘")
    print("   Clique em: Adicionar ou Save")
    print()
    
    print("7. ADICIONAR REGISTRO CNAME:")
    print("   ┌─────────────────────────────┐")
    print("   │ Tipo: CNAME                 │")
    print("   │ Nome: www                   │")
    print("   │ Valor: cname.vercel-dns.com │")
    print("   │ TTL: 3600                   │")
    print("   └─────────────────────────────┘")
    print("   Clique em: Adicionar ou Save")
    print()
    
    print("8. ✅ Pronto! Aguarde 10-60 minutos para propagação")
    print()
    
    print("🔍 VERIFICAR PROPAGAÇÃO:")
    print("   https://dnschecker.org/?domain=marquesdesignstudio.com")
    print()
    
    print("="*70)

if __name__ == "__main__":
    main()
