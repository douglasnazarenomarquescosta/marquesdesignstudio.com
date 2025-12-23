#!/usr/bin/env python3
"""Guia completo para configurar marquesdesignstudio.com na Hostinger"""
import requests
import json

BASE_URL = "http://localhost:8000"

print("="*70)
print("  🌐 CONFIGURAR marquesdesignstudio.com (HOSTINGER) NO VERCEL")
print("="*70)
print()

# Obter guia DNS
response = requests.post(f"{BASE_URL}/webbuilder/domain/guide", json={
    "domain_name": "marquesdesignstudio.com",
    "hosting_platform": "vercel"
})

result = response.json()

print("📋 PASSOS PARA CONFIGURAR:")
print()
for i, step in enumerate(result['steps'], 1):
    print(f"  {i}. {step}")

print()
print("="*70)
print("📊 REGISTROS DNS PARA ADICIONAR NA HOSTINGER:")
print("="*70)
print()

for record in result['dns_records']:
    print(f"  ✅ Tipo: {record['type']:6} | Nome: {record['name']:5} | Valor: {record['value']}")

print()
print("="*70)
print("⏱️  INFORMAÇÕES ADICIONAIS")
print("="*70)
print()
print(f"  🕐 Tempo estimado: {result['estimated_time']}")
print(f"  🔒 SSL: {result['ssl_certificate']}")
print()
print("  📍 Como acessar DNS na Hostinger:")
print("     1. Login: https://hpanel.hostinger.com")
print("     2. Menu: Domínios")
print("     3. Selecione: marquesdesignstudio.com")
print("     4. Aba: DNS / Name Servers → DNS Zone Editor")
print("     5. Clique: + Adicionar Registro")
print()
print("  🔗 Ferramentas úteis:")
print("     - Verificar DNS: https://dnschecker.org/?domain=marquesdesignstudio.com")
print("     - Testar SSL: https://www.ssllabs.com/ssltest/")
print()
print("="*70)
print("✅ Seu site já está criado em:")
print(f"   G:\\Projeto de IA\\generated_sites\\marques-design-studio")
print()
print("🚀 Próximo passo: Deploy no Vercel")
print("   cd \"G:\\Projeto de IA\\generated_sites\\marques-design-studio\"")
print("   vercel")
print("="*70)
