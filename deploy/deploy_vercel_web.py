#!/usr/bin/env python3
"""
Instruções para Deploy via Vercel Web Interface
"""

print("""
╔══════════════════════════════════════════════════════════════════════╗
║          DEPLOY NO VERCEL - MARQUES DESIGN STUDIO                    ║
╔══════════════════════════════════════════════════════════════════════╗

Você está em: https://vercel.com/new

📦 OPÇÕES DE DEPLOY:

┌─────────────────────────────────────────────────────────────────────┐
│ OPÇÃO 1: VIA GIT (Recomendado para projetos)                       │
└─────────────────────────────────────────────────────────────────────┘

Se você tem GitHub, GitLab ou Bitbucket:

1. Criar repositório no GitHub:
   → Vá em: https://github.com/new
   → Nome: marques-design-studio
   → Público
   → Create repository

2. No PowerShell:
   cd "G:\\Projeto de IA\\generated_sites\\marques-design-studio"
   git init
   git add .
   git commit -m "Initial commit - Marques Design Studio"
   git branch -M main
   git remote add origin https://github.com/SEU-USUARIO/marques-design-studio.git
   git push -u origin main

3. No Vercel (https://vercel.com/new):
   → Import Git Repository
   → Conecte GitHub
   → Selecione: marques-design-studio
   → Deploy

┌─────────────────────────────────────────────────────────────────────┐
│ OPÇÃO 2: VIA VERCEL CLI (Mais Rápido)                              │
└─────────────────────────────────────────────────────────────────────┘

No PowerShell:

   # Instalar Vercel CLI (se ainda não tem)
   npm install -g vercel
   
   # Navegar até o site
   cd "G:\\Projeto de IA\\generated_sites\\marques-design-studio"
   
   # Deploy
   vercel --prod
   
   # Siga as instruções interativas
   # Login → Yes → Deploy

┌─────────────────────────────────────────────────────────────────────┐
│ OPÇÃO 3: VIA DRAG & DROP (Mais Fácil)                              │
└─────────────────────────────────────────────────────────────────────┘

INFELIZMENTE, Vercel não tem drag & drop igual Netlify.
Use Netlify se quiser arrastar pasta:
   
   https://app.netlify.com/drop

═════════════════════════════════════════════════════════════════════

🎯 RECOMENDAÇÃO: Use OPÇÃO 2 (CLI)

É mais rápido e você já tem a pasta pronta!

═════════════════════════════════════════════════════════════════════

Quer que eu prepare os comandos prontos para você?
""")
