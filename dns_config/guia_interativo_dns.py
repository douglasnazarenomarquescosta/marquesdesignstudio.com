#!/usr/bin/env python3
"""
Guia Interativo para Configuração DNS - Hostinger
"""
import webbrowser
import time

def print_step(number, title, details):
    """Imprime passo formatado"""
    print(f"\n{'='*70}")
    print(f"  {number} {title}")
    print('='*70)
    for detail in details:
        print(f"   {detail}")
    print()

def main():
    print("\n" + "🌐"*35)
    print("="*70)
    print("  GUIA INTERATIVO - CONFIGURAÇÃO DNS MARQUESDESIGNSTUDIO.COM")
    print("="*70)
    print("🌐"*35 + "\n")
    
    input("Pressione ENTER para começar...")
    
    # Passo 1
    print_step(
        "1️⃣",
        "ABRIR PAINEL HOSTINGER",
        [
            "Vou abrir o painel Hostinger no seu navegador...",
            "🔗 https://hpanel.hostinger.com",
            "",
            "✅ Faça login com seu email e senha"
        ]
    )
    
    input("Pressione ENTER para abrir o painel...")
    webbrowser.open("https://hpanel.hostinger.com")
    
    input("\nFez login? Pressione ENTER para continuar...")
    
    # Passo 2
    print_step(
        "2️⃣",
        "ENCONTRAR O DOMÍNIO",
        [
            "No painel da Hostinger:",
            "",
            "📂 Procure no menu lateral esquerdo:",
            "   → Clique em 'Domínios' ou 'Domains'",
            "",
            "📋 Você verá uma lista de domínios",
            "   → Procure: marquesdesignstudio.com",
            "   → Clique nele"
        ]
    )
    
    input("Clicou no domínio? Pressione ENTER...")
    
    # Passo 3
    print_step(
        "3️⃣",
        "ACESSAR CONFIGURAÇÕES DNS",
        [
            "Na página do domínio, procure por:",
            "",
            "🔧 Opções possíveis (depende da interface):",
            "   • 'DNS / Name Servers'",
            "   • 'Gerenciar DNS' ou 'Manage DNS'",
            "   • 'DNS Zone'",
            "   • 'DNS Records'",
            "",
            "👉 Clique nessa opção"
        ]
    )
    
    input("Encontrou as configurações DNS? Pressione ENTER...")
    
    # Passo 4
    print_step(
        "4️⃣",
        "LOCALIZAR DNS ZONE EDITOR",
        [
            "Agora você deve estar na página de DNS.",
            "",
            "🔍 Procure por:",
            "   • Botão 'DNS Zone Editor'",
            "   • Ou 'Gerenciar Registros DNS'",
            "   • Ou uma lista de registros DNS",
            "",
            "✅ Você deve ver registros como:",
            "   • Tipo A, CNAME, MX, TXT, etc.",
            "",
            "👉 Procure um botão: '+ Adicionar' ou 'Add Record'"
        ]
    )
    
    input("Está vendo os registros DNS? Pressione ENTER...")
    
    # Passo 5
    print_step(
        "5️⃣",
        "ADICIONAR REGISTRO A",
        [
            "Clique em: '+ Adicionar Registro' ou 'Add Record'",
            "",
            "📝 Preencha EXATAMENTE assim:",
            "",
            "┌─────────────────────────────────────┐",
            "│ Tipo/Type:        A                 │",
            "│ Nome/Name:        @                 │",
            "│                   (ou deixe vazio)  │",
            "│ Valor/Value:      76.76.21.21       │",
            "│ TTL:              3600              │",
            "│                   (ou 1 Hour)       │",
            "└─────────────────────────────────────┘",
            "",
            "👉 Clique em: 'Adicionar' ou 'Save'"
        ]
    )
    
    input("Adicionou o registro A? Pressione ENTER...")
    
    # Passo 6
    print_step(
        "6️⃣",
        "ADICIONAR REGISTRO CNAME",
        [
            "Clique novamente em: '+ Adicionar Registro'",
            "",
            "📝 Preencha EXATAMENTE assim:",
            "",
            "┌─────────────────────────────────────┐",
            "│ Tipo/Type:        CNAME             │",
            "│ Nome/Name:        www               │",
            "│ Valor/Value:      cname.vercel-dns.com │",
            "│ TTL:              3600              │",
            "└─────────────────────────────────────┘",
            "",
            "👉 Clique em: 'Adicionar' ou 'Save'"
        ]
    )
    
    input("Adicionou o registro CNAME? Pressione ENTER...")
    
    # Passo 7
    print_step(
        "7️⃣",
        "VERIFICAR REGISTROS",
        [
            "✅ Verifique se ambos os registros foram salvos:",
            "",
            "┌──────────┬────────┬──────────────────────┬──────┐",
            "│ Tipo     │ Nome   │ Valor                │ TTL  │",
            "├──────────┼────────┼──────────────────────┼──────┤",
            "│ A        │ @      │ 76.76.21.21          │ 3600 │",
            "│ CNAME    │ www    │ cname.vercel-dns.com │ 3600 │",
            "└──────────┴────────┴──────────────────────┴──────┘",
            "",
            "⚠️ Não delete outros registros (MX, TXT, etc)!"
        ]
    )
    
    input("Tudo correto? Pressione ENTER...")
    
    # Passo 8
    print_step(
        "8️⃣",
        "VERIFICAR PROPAGAÇÃO DNS",
        [
            "Agora vamos verificar se o DNS está propagando...",
            "",
            "🔍 Abrindo DNS Checker...",
            "https://dnschecker.org",
            "",
            "⏰ Aguarde 10-60 minutos",
            "✅ Quando a maioria dos países mostrar: 76.76.21.21",
            "   → DNS propagado!"
        ]
    )
    
    input("Pressione ENTER para abrir DNS Checker...")
    webbrowser.open("https://dnschecker.org/?domain=marquesdesignstudio.com&type=A")
    
    # Passo 9
    print_step(
        "9️⃣",
        "CONFIGURAR NO VERCEL",
        [
            "Enquanto o DNS propaga, vamos configurar no Vercel...",
            "",
            "🚀 Abrindo Vercel Dashboard...",
            "https://vercel.com/dashboard",
            "",
            "📋 No Vercel:",
            "   1. Clique no projeto: marques-design-studio",
            "   2. Settings → Domains",
            "   3. Digite: marquesdesignstudio.com",
            "   4. Clique: Add",
            "   5. Adicione também: www.marquesdesignstudio.com",
            "",
            "✅ Vercel validará automaticamente!"
        ]
    )
    
    input("Pressione ENTER para abrir Vercel Dashboard...")
    webbrowser.open("https://vercel.com/dashboard")
    
    # Conclusão
    print("\n" + "="*70)
    print("  🎉 PARABÉNS! CONFIGURAÇÃO CONCLUÍDA!")
    print("="*70)
    print()
    print("✅ O que você fez:")
    print("   1. ✅ Adicionou registro A no DNS da Hostinger")
    print("   2. ✅ Adicionou registro CNAME para www")
    print("   3. ✅ Configurou domínio no Vercel")
    print()
    print("⏰ Próximos passos:")
    print("   • Aguardar 10-60 minutos para DNS propagar")
    print("   • Verificar em: https://dnschecker.org")
    print("   • Quando propagar: SSL ativa automaticamente")
    print()
    print("🌐 Seu site estará em:")
    print("   https://marquesdesignstudio.com")
    print()
    print("💰 Custo total: R$ 0,00/mês (só paga o domínio)")
    print("="*70)
    print()
    
    # Salvar checklist
    with open("checklist_concluido.txt", "w", encoding="utf-8") as f:
        f.write("CONFIGURAÇÃO DNS CONCLUÍDA\n")
        f.write("="*50 + "\n\n")
        f.write("Data: 4 de dezembro de 2025\n")
        f.write("Domínio: marquesdesignstudio.com\n\n")
        f.write("REGISTROS ADICIONADOS:\n")
        f.write("✅ A: @ → 76.76.21.21\n")
        f.write("✅ CNAME: www → cname.vercel-dns.com\n\n")
        f.write("PRÓXIMOS PASSOS:\n")
        f.write("[ ] Aguardar propagação DNS (10-60 min)\n")
        f.write("[ ] Verificar em dnschecker.org\n")
        f.write("[ ] Confirmar domínio no Vercel\n")
        f.write("[ ] Aguardar SSL ativar automaticamente\n")
        f.write("[ ] Testar site em https://marquesdesignstudio.com\n")
    
    print("📝 Checklist salvo em: checklist_concluido.txt")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Guia interrompido")
    except Exception as e:
        print(f"\n\n❌ Erro: {e}")
