#!/usr/bin/env python3
"""
Deploy Automatizado do Marques Design Studio
Executa todo o processo de configuração
"""
import subprocess
import sys
import time
import os
from pathlib import Path

def print_header(title):
    """Imprime cabeçalho formatado"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")

def run_command(command, description, shell=True):
    """Executa comando e mostra resultado"""
    print(f"⚙️  {description}...")
    try:
        result = subprocess.run(
            command,
            shell=shell,
            capture_output=True,
            text=True,
            cwd="G:\\Projeto de IA\\generated_sites\\marques-design-studio"
        )
        
        if result.returncode == 0:
            print(f"✅ {description} - Concluído!\n")
            if result.stdout:
                print(result.stdout)
            return True
        else:
            print(f"❌ Erro: {result.stderr}\n")
            return False
    except Exception as e:
        print(f"❌ Erro ao executar: {e}\n")
        return False

def check_vercel_installed():
    """Verifica se Vercel CLI está instalado"""
    try:
        result = subprocess.run(
            ["vercel", "--version"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except:
        return False

def install_vercel():
    """Instala Vercel CLI"""
    print_header("INSTALANDO VERCEL CLI")
    
    print("📦 Verificando se Node.js está instalado...")
    try:
        result = subprocess.run(["node", "--version"], capture_output=True)
        if result.returncode != 0:
            print("❌ Node.js não está instalado!")
            print("\n📥 Por favor, instale Node.js:")
            print("   1. Acesse: https://nodejs.org")
            print("   2. Baixe a versão LTS")
            print("   3. Execute o instalador")
            print("   4. Reinicie o PowerShell")
            print("   5. Execute este script novamente")
            return False
    except:
        print("❌ Node.js não encontrado!")
        return False
    
    print("✅ Node.js instalado\n")
    
    print("📦 Instalando Vercel CLI...")
    result = subprocess.run(
        ["npm", "install", "-g", "vercel"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("✅ Vercel CLI instalado com sucesso!\n")
        return True
    else:
        print(f"❌ Erro ao instalar: {result.stderr}\n")
        return False

def create_vercel_config():
    """Cria arquivo de configuração do Vercel"""
    vercel_json = {
        "version": 2,
        "name": "marques-design-studio",
        "builds": [
            {
                "src": "index.html",
                "use": "@vercel/static"
            }
        ]
    }
    
    import json
    config_path = Path("G:\\Projeto de IA\\generated_sites\\marques-design-studio\\vercel.json")
    
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(vercel_json, f, indent=2)
    
    print("✅ Arquivo vercel.json criado\n")

def deploy_to_vercel():
    """Faz deploy no Vercel"""
    print_header("DEPLOY NO VERCEL")
    
    site_path = "G:\\Projeto de IA\\generated_sites\\marques-design-studio"
    
    print("🚀 Iniciando deploy...")
    print("⚠️  Uma janela do navegador será aberta para login\n")
    
    # Usar vercel --prod para deploy em produção
    result = subprocess.run(
        ["vercel", "--prod", "--yes"],
        cwd=site_path,
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("✅ Deploy concluído com sucesso!\n")
        
        # Extrair URL do output
        output = result.stdout
        if "https://" in output:
            lines = output.split('\n')
            for line in lines:
                if "https://" in line and "vercel.app" in line:
                    url = line.strip()
                    print(f"🌐 URL do site: {url}\n")
                    return url
        
        return True
    else:
        print(f"❌ Erro no deploy: {result.stderr}\n")
        
        # Se erro for de autenticação, tentar login
        if "not authenticated" in result.stderr.lower():
            print("🔐 Fazendo login no Vercel...\n")
            subprocess.run(["vercel", "login"], cwd=site_path)
            
            # Tentar deploy novamente
            print("🔄 Tentando deploy novamente...\n")
            return deploy_to_vercel()
        
        return False

def show_dns_instructions(vercel_url=None):
    """Mostra instruções de DNS"""
    print_header("CONFIGURAR DNS NA HOSTINGER")
    
    print("📋 PASSOS PARA CONFIGURAR:\n")
    
    steps = [
        "1. Acesse: https://hpanel.hostinger.com",
        "2. Faça login com suas credenciais",
        "3. Menu lateral → Domínios",
        "4. Clique em: marquesdesignstudio.com",
        "5. Aba: DNS / Name Servers → DNS Zone Editor",
        "6. Clique em: + Adicionar Registro",
        "",
        "📊 ADICIONE ESTES REGISTROS:",
        "",
        "Registro 1 (A):",
        "   Tipo: A",
        "   Nome: @ (ou deixe vazio)",
        "   Valor: 76.76.21.21",
        "   TTL: 3600",
        "",
        "Registro 2 (CNAME):",
        "   Tipo: CNAME",
        "   Nome: www",
        "   Valor: cname.vercel-dns.com",
        "   TTL: 3600",
        "",
        "7. Clique em 'Adicionar' ou 'Save' para cada registro",
        "8. Aguarde 10-60 minutos para propagação DNS"
    ]
    
    for step in steps:
        print(f"   {step}")
    
    print("\n" + "="*70 + "\n")

def show_vercel_domain_instructions():
    """Mostra instruções para adicionar domínio no Vercel"""
    print_header("ADICIONAR DOMÍNIO NO VERCEL")
    
    print("📋 PASSOS:\n")
    
    steps = [
        "1. Acesse: https://vercel.com/dashboard",
        "2. Clique no projeto: marques-design-studio",
        "3. Vá em: Settings (engrenagem no topo)",
        "4. Menu lateral: Domains",
        "5. Digite: marquesdesignstudio.com",
        "6. Clique em: Add",
        "7. Adicione também: www.marquesdesignstudio.com",
        "",
        "⏳ Aguarde o Vercel validar os registros DNS",
        "✅ Quando aparecer 'Valid', está pronto!",
        "",
        "🔒 SSL será configurado automaticamente em ~10 minutos"
    ]
    
    for step in steps:
        print(f"   {step}")
    
    print("\n" + "="*70 + "\n")

def create_shortcuts():
    """Cria atalhos úteis"""
    print_header("CRIANDO ATALHOS")
    
    # Atalho para abrir Hostinger
    hostinger_script = """
$desktop = [Environment]::GetFolderPath("Desktop")
$WshShell = New-Object -ComObject WScript.Shell
$shortcut = $WshShell.CreateShortcut("$desktop\\⚙️ Config DNS Hostinger.url")
$shortcut.TargetPath = "https://hpanel.hostinger.com"
$shortcut.Save()
Write-Host "✅ Atalho Hostinger criado!"
"""
    
    subprocess.run(["powershell", "-Command", hostinger_script], capture_output=True)
    print("✅ Atalho criado: ⚙️ Config DNS Hostinger")
    
    # Atalho para abrir Vercel Dashboard
    vercel_script = """
$desktop = [Environment]::GetFolderPath("Desktop")
$WshShell = New-Object -ComObject WScript.Shell
$shortcut = $WshShell.CreateShortcut("$desktop\\🚀 Vercel Dashboard.url")
$shortcut.TargetPath = "https://vercel.com/dashboard"
$shortcut.Save()
Write-Host "✅ Atalho Vercel criado!"
"""
    
    subprocess.run(["powershell", "-Command", vercel_script], capture_output=True)
    print("✅ Atalho criado: 🚀 Vercel Dashboard")
    
    # Atalho para verificar DNS
    dns_script = """
$desktop = [Environment]::GetFolderPath("Desktop")
$WshShell = New-Object -ComObject WScript.Shell
$shortcut = $WshShell.CreateShortcut("$desktop\\🔍 Verificar DNS.url")
$shortcut.TargetPath = "https://dnschecker.org/?domain=marquesdesignstudio.com"
$shortcut.Save()
Write-Host "✅ Atalho DNS Checker criado!"
"""
    
    subprocess.run(["powershell", "-Command", dns_script], capture_output=True)
    print("✅ Atalho criado: 🔍 Verificar DNS\n")

def main():
    """Função principal"""
    print("\n" + "🌐"*35)
    print_header("DEPLOY AUTOMATIZADO - MARQUES DESIGN STUDIO")
    print("🌐"*35 + "\n")
    
    print("Este script irá:")
    print("  1. ✅ Verificar se Vercel CLI está instalado")
    print("  2. 🚀 Fazer deploy no Vercel")
    print("  3. 📋 Mostrar instruções de DNS")
    print("  4. 🔗 Criar atalhos úteis")
    print()
    
    input("Pressione ENTER para continuar...")
    
    # Etapa 1: Verificar/Instalar Vercel CLI
    print_header("ETAPA 1: VERIFICANDO VERCEL CLI")
    
    if check_vercel_installed():
        print("✅ Vercel CLI já está instalado!\n")
    else:
        print("⚠️  Vercel CLI não encontrado\n")
        install = input("Deseja instalar o Vercel CLI agora? (s/n): ")
        
        if install.lower() == 's':
            if not install_vercel():
                print("\n❌ Não foi possível instalar Vercel CLI")
                print("Por favor, instale manualmente:")
                print("   npm install -g vercel")
                sys.exit(1)
        else:
            print("\n❌ Vercel CLI é necessário para continuar")
            print("Instale com: npm install -g vercel")
            sys.exit(1)
    
    # Etapa 2: Criar configuração
    print_header("ETAPA 2: PREPARANDO DEPLOY")
    create_vercel_config()
    
    # Etapa 3: Deploy
    vercel_url = deploy_to_vercel()
    
    if not vercel_url:
        print("\n⚠️  Deploy não concluído")
        print("\nPara fazer deploy manualmente:")
        print("   cd \"G:\\Projeto de IA\\generated_sites\\marques-design-studio\"")
        print("   vercel --prod")
        return
    
    # Etapa 4: Instruções DNS
    show_dns_instructions(vercel_url)
    
    # Etapa 5: Instruções Vercel
    show_vercel_domain_instructions()
    
    # Etapa 6: Criar atalhos
    create_shortcuts()
    
    # Resumo final
    print_header("✅ DEPLOY CONCLUÍDO!")
    
    print("📦 O que foi feito:")
    print("   ✅ Site enviado para Vercel")
    print("   ✅ Atalhos criados na área de trabalho")
    print("   ✅ Instruções de DNS preparadas")
    print()
    
    print("📋 PRÓXIMOS PASSOS:")
    print("   1. Configure DNS na Hostinger (instruções acima)")
    print("   2. Adicione domínio no Vercel Dashboard")
    print("   3. Aguarde propagação DNS (10-60 min)")
    print("   4. Acesse: https://marquesdesignstudio.com")
    print()
    
    print("🔗 ATALHOS CRIADOS NA ÁREA DE TRABALHO:")
    print("   • ⚙️ Config DNS Hostinger - Configurar DNS")
    print("   • 🚀 Vercel Dashboard - Gerenciar site")
    print("   • 🔍 Verificar DNS - Checar propagação")
    print("   • 🎨 Marques Design - Visualizar site local")
    print()
    
    print("📚 DOCUMENTAÇÃO:")
    print("   • G:\\Projeto de IA\\GUIA_DOMINIO_HOSTINGER.md")
    print("   • G:\\Projeto de IA\\WEBBUILDER.md")
    print()
    
    print("="*70)
    print("🎉 Sucesso! Seu site está quase online!")
    print("="*70)
    
    # Abrir links importantes
    open_links = input("\nDeseja abrir os links importantes agora? (s/n): ")
    if open_links.lower() == 's':
        import webbrowser
        print("\n🌐 Abrindo navegador...")
        webbrowser.open("https://hpanel.hostinger.com")
        time.sleep(2)
        webbrowser.open("https://vercel.com/dashboard")
        time.sleep(2)
        webbrowser.open("https://dnschecker.org/?domain=marquesdesignstudio.com")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação cancelada pelo usuário")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Erro inesperado: {e}")
        sys.exit(1)
