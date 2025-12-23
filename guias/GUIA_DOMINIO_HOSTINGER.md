# 🌐 Configurar marquesdesignstudio.com (Hostinger) com Hospedagem Gratuita

Você tem o domínio **marquesdesignstudio.com** na Hostinger e quer hospedar seu site **GRATUITAMENTE** no Vercel, Netlify ou GitHub Pages com SSL/HTTPS automático.

## 🎯 Escolha Rápida de Plataforma

| Plataforma | Dificuldade | Tempo Setup | Melhor Para |
|------------|-------------|-------------|-------------|
| **Vercel** | Fácil | 5 min | Sites modernos, Next.js |
| **Netlify** | Muito Fácil | 5 min | Sites estáticos (HTML/CSS/JS) |
| **GitHub Pages** | Médio | 10 min | Sites simples, open source |

**Recomendação**: Use **Netlify** (mais fácil) ou **Vercel** (mais rápido).

---

## 🚀 Opção 1: Vercel (Recomendado)

### Passo 1: Criar e fazer deploy do site

```bash
# 1. Criar site via API
POST http://localhost:8000/webbuilder/create/landing
{
  "project_name": "marques-design",
  "title": "Marques Design Studio",
  "description": "Soluções criativas e inovadoras",
  "primary_color": "#667eea",
  "cta_text": "Ver Portfolio"
}

# 2. Instalar Vercel CLI
npm install -g vercel

# 3. Fazer deploy
cd "G:\Projeto de IA\generated_sites\marques-design"
vercel

# Siga as instruções:
# - Login com GitHub/Google
# - Confirme o deploy
# - Anote a URL: https://[seu-projeto].vercel.app
```

### Passo 2: Configurar DNS na Hostinger

1. **Login na Hostinger**: https://hpanel.hostinger.com
2. **Acesse Domínios** → Clique em `marquesdesignstudio.com`
3. **Vá em DNS / Name Servers** → Gerenciar
4. **Adicione estes registros**:

#### Registro A (raiz do domínio)
```
Tipo: A
Nome: @ (ou deixe em branco)
Valor: 76.76.21.21
TTL: 3600 (ou 1 hora)
```

#### Registro CNAME (www)
```
Tipo: CNAME
Nome: www
Valor: cname.vercel-dns.com
TTL: 3600
```

**Screenshot do painel Hostinger**:
- Clique em "+ Adicionar Registro"
- Selecione tipo "A" ou "CNAME"
- Preencha os campos
- Clique em "Adicionar"

### Passo 3: Adicionar domínio no Vercel

1. **Login no Vercel**: https://vercel.com
2. **Selecione seu projeto** na dashboard
3. **Settings** → **Domains**
4. Digite: `marquesdesignstudio.com`
5. Clique em **Add**
6. Adicione também: `www.marquesdesignstudio.com`
7. Vercel validará automaticamente os registros DNS

### Passo 4: Aguardar propagação

- **Tempo estimado**: 10 minutos a 2 horas
- **Verifique propagação**: https://dnschecker.org
- **SSL automático**: Ativa em ~10 minutos após DNS propagar

### Passo 5: Testar

```bash
# Verificar se está online
curl https://marquesdesignstudio.com

# Deve redirecionar para HTTPS automaticamente
# ✅ Site disponível em https://marquesdesignstudio.com
# ✅ SSL/HTTPS ativo (Let's Encrypt)
```

---

## 🎨 Opção 2: Netlify (Mais Fácil)

### Passo 1: Deploy no Netlify

**Método A: Drag & Drop (Super Fácil)**
1. Vá em https://app.netlify.com
2. Faça login/cadastro (GitHub, Google ou email)
3. Clique em **Add new site** → **Deploy manually**
4. Arraste a pasta `generated_sites/marques-design`
5. Aguarde upload (~30 segundos)
6. ✅ Site online em `https://[nome-aleatorio].netlify.app`

**Método B: Via Git (Recomendado para projetos)**
```bash
# 1. Criar repositório no GitHub
cd "G:\Projeto de IA\generated_sites\marques-design"
git init
git add .
git commit -m "Initial commit - Marques Design Studio"
git branch -M main
git remote add origin https://github.com/[seu-usuario]/marques-design.git
git push -u origin main

# 2. No Netlify: New site from Git → GitHub → Selecionar repo
# 3. Deploy automático!
```

### Passo 2: Configurar DNS na Hostinger

1. **Login na Hostinger**: https://hpanel.hostinger.com
2. **Domínios** → `marquesdesignstudio.com` → **DNS/Name Servers**
3. **Adicione estes registros**:

#### Registro A (raiz)
```
Tipo: A
Nome: @
Valor: 75.2.60.5
TTL: 3600
```

#### Registro CNAME (www)
```
Tipo: CNAME
Nome: www
Valor: [seu-site].netlify.app
TTL: 3600
```

**Exemplo**: Se seu site é `marques-design-abc123.netlify.app`, use:
- Valor: `marques-design-abc123.netlify.app`

### Passo 3: Adicionar domínio no Netlify

1. **No Netlify**, selecione seu site
2. **Domain settings** → **Add custom domain**
3. Digite: `marquesdesignstudio.com`
4. Clique em **Verify**
5. Netlify confirmará que é seu domínio
6. Adicione também: `www.marquesdesignstudio.com`

### Passo 4: Ativar SSL

1. **Domain settings** → **HTTPS**
2. **Verify DNS configuration**
3. **Provision certificate** (aguarde ~1 minuto)
4. ✅ SSL ativo automaticamente!

### Passo 5: Configurar redirects (opcional)

Criar arquivo `_redirects` na raiz do site:
```
# Redirecionar www para não-www
https://www.marquesdesignstudio.com/* https://marquesdesignstudio.com/:splat 301!

# Forçar HTTPS
http://marquesdesignstudio.com/* https://marquesdesignstudio.com/:splat 301!
```

---

## 📱 Opção 3: GitHub Pages (Gratuito Ilimitado)

### Passo 1: Criar repositório no GitHub

```bash
# 1. Criar repo público no GitHub: marquesdesignstudio.com
# 2. Fazer push do código
cd "G:\Projeto de IA\generated_sites\marques-design"
git init
git add .
git commit -m "Site Marques Design Studio"
git branch -M main
git remote add origin https://github.com/[seu-usuario]/marquesdesignstudio.com.git
git push -u origin main
```

### Passo 2: Ativar GitHub Pages

1. **No GitHub**, vá no repositório
2. **Settings** → **Pages**
3. **Source**: Deploy from a branch
4. **Branch**: main → /(root) → Save
5. Aguarde ~2 minutos
6. Site disponível em: `https://[seu-usuario].github.io/marquesdesignstudio.com`

### Passo 3: Configurar domínio customizado

1. **Ainda em Settings → Pages**
2. **Custom domain**: `marquesdesignstudio.com`
3. Clique em **Save**
4. Marque **Enforce HTTPS** (após DNS propagar)

### Passo 4: Configurar DNS na Hostinger

1. **Login na Hostinger**: https://hpanel.hostinger.com
2. **Domínios** → `marquesdesignstudio.com` → **DNS**
3. **Adicione 4 registros A**:

```
Tipo: A | Nome: @ | Valor: 185.199.108.153 | TTL: 3600
Tipo: A | Nome: @ | Valor: 185.199.109.153 | TTL: 3600
Tipo: A | Nome: @ | Valor: 185.199.110.153 | TTL: 3600
Tipo: A | Nome: @ | Valor: 185.199.111.153 | TTL: 3600
```

#### Registro CNAME (www)
```
Tipo: CNAME
Nome: www
Valor: [seu-usuario].github.io
TTL: 3600
```

### Passo 5: Criar arquivo CNAME no repositório

Criar arquivo `CNAME` na raiz do projeto:
```
marquesdesignstudio.com
```

Fazer commit e push:
```bash
echo "marquesdesignstudio.com" > CNAME
git add CNAME
git commit -m "Add custom domain"
git push
```

### Passo 6: Aguardar e testar

- **Propagação DNS**: 30 min a 48h (geralmente 1-2h)
- **Verificar**: https://dnschecker.org
- **SSL**: Ativa automaticamente em ~1h após DNS propagar

---

## 🔧 Testando via API do Projeto

```python
import requests

# Obter guia completo para Vercel
response = requests.post("http://localhost:8000/webbuilder/domain/guide", json={
    "domain_name": "marquesdesignstudio.com",
    "hosting_platform": "vercel"
})

print("📋 PASSOS PARA CONFIGURAR:")
for step in response.json()['steps']:
    print(f"  {step}")

print("\n📊 REGISTROS DNS:")
for record in response.json()['dns_records']:
    print(f"  {record['type']} → {record['name']} → {record['value']}")
```

---

## 📊 Comparação Rápida

| Recurso | Vercel | Netlify | GitHub Pages |
|---------|--------|---------|--------------|
| **Deploy** | CLI ou Git | Drag&Drop ou Git | Git apenas |
| **SSL Grátis** | ✅ Sim | ✅ Sim | ✅ Sim |
| **Propagação DNS** | ~10 min | ~30 min | ~1-2h |
| **Ativação SSL** | ~10 min | ~1 min | ~1h |
| **Bandwidth** | 100GB/mês | 100GB/mês | 100GB/mês |
| **Custom Domain** | ✅ Ilimitado | ✅ Ilimitado | ✅ 1 por repo |
| **Dificuldade** | Fácil | Muito Fácil | Médio |

**Recomendação para marquesdesignstudio.com**:
- **Profissional/Portfolio**: Use **Vercel** (deploy rápido, ótima performance)
- **Site institucional**: Use **Netlify** (mais fácil, forms inclusos)
- **Projeto pessoal**: Use **GitHub Pages** (100% gratuito, sem limites)

---

## 🐛 Troubleshooting Hostinger

### Problema: "Não encontro onde adicionar registros DNS"

**Solução**:
1. Login em https://hpanel.hostinger.com
2. Menu lateral → **Domínios**
3. Clique no domínio `marquesdesignstudio.com`
4. Procure por:
   - **DNS Zone Editor** (na aba superior)
   - Ou **Gerenciar** → **DNS/Name Servers**
   - Ou **Advanced** → **DNS Records**

### Problema: "DNS não está propagando"

**Solução**:
1. Verifique se salvou os registros na Hostinger
2. Aguarde pelo menos 30 minutos
3. Teste em: https://dnschecker.org
4. Limpe cache DNS local:
   ```powershell
   ipconfig /flushdns
   ```
5. Teste em navegador anônimo (Ctrl+Shift+N)

### Problema: "SSL não ativa"

**Solução**:
1. **Vercel**: Aguarde DNS propagar completamente (use dnschecker.org)
2. **Netlify**: Domain Settings → HTTPS → Renew certificate
3. **GitHub Pages**: Desmarque e remarque "Enforce HTTPS" após 1h

### Problema: "Site mostra erro 404"

**Solução**:
1. Verifique se `index.html` está na raiz do projeto
2. Confirme que o deploy foi bem-sucedido
3. Teste a URL temporária primeiro (*.vercel.app ou *.netlify.app)
4. Depois configure o domínio

---

## ✅ Checklist Completo

### Antes de começar:
- [ ] Domínio registrado na Hostinger (✅ marquesdesignstudio.com)
- [ ] Site criado localmente (`POST /webbuilder/create/landing`)
- [ ] Escolhida plataforma (Vercel, Netlify ou GitHub Pages)

### Deploy:
- [ ] Deploy realizado com sucesso
- [ ] Site acessível via URL temporária (*.vercel.app, *.netlify.app, etc)
- [ ] Testado no navegador (funciona sem erros)

### Configuração DNS Hostinger:
- [ ] Login na Hostinger realizado
- [ ] Localizado painel DNS do domínio
- [ ] Registros A adicionados (IP da plataforma)
- [ ] Registro CNAME adicionado (www)
- [ ] Salvos todos os registros

### Configuração na Plataforma:
- [ ] Domínio adicionado na plataforma (Settings → Domains)
- [ ] Domínio www também adicionado
- [ ] Plataforma validou os registros DNS

### Aguardar:
- [ ] Propagação DNS iniciada (verificar dnschecker.org)
- [ ] DNS propagado globalmente (pode levar 1-48h)
- [ ] SSL/HTTPS ativado automaticamente
- [ ] Site acessível em https://marquesdesignstudio.com ✅

### Testes finais:
- [ ] Site carrega sem erros
- [ ] HTTPS funciona (cadeado verde no navegador)
- [ ] www redireciona para não-www (ou vice-versa)
- [ ] Site responsivo no mobile

---

## 🎯 Próximos Passos

Depois que seu site estiver online:

1. **Google Search Console**
   - Adicione seu site
   - Envie sitemap.xml
   - Monitore indexação

2. **Google Analytics**
   - Adicione código de tracking
   - Monitore visitantes

3. **Performance**
   - Teste em https://pagespeed.web.dev
   - Otimize imagens
   - Minimize CSS/JS

4. **SEO**
   - Configure meta tags
   - Adicione Open Graph
   - Crie robots.txt

5. **Backup**
   - Mantenha código no GitHub
   - Faça commits regulares
   - Use Git para controle de versão

---

## 📞 Suporte Rápido

**Links Úteis**:
- Hostinger Support: https://www.hostinger.com.br/tutoriais/
- Vercel Docs: https://vercel.com/docs/custom-domains
- Netlify Docs: https://docs.netlify.com/domains-https/custom-domains/
- GitHub Pages: https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site

**Ferramentas de Teste**:
- DNS Checker: https://dnschecker.org
- SSL Test: https://www.ssllabs.com/ssltest/
- PageSpeed: https://pagespeed.web.dev

---

## 🚀 Script Automatizado

```powershell
# Script completo para deploy (Windows PowerShell)

# 1. Criar site
$response = Invoke-RestMethod -Uri "http://localhost:8000/webbuilder/create/landing" -Method POST -ContentType "application/json" -Body (@{
    project_name = "marques-design"
    title = "Marques Design Studio"
    description = "Soluções criativas e inovadoras"
    primary_color = "#667eea"
    cta_text = "Ver Portfolio"
} | ConvertTo-Json)

Write-Host "✅ Site criado em: $($response.path)"

# 2. Obter guia DNS
$dnsGuide = Invoke-RestMethod -Uri "http://localhost:8000/webbuilder/domain/guide" -Method POST -ContentType "application/json" -Body (@{
    domain_name = "marquesdesignstudio.com"
    hosting_platform = "vercel"
} | ConvertTo-Json)

Write-Host "`n📋 PASSOS PARA CONFIGURAR DNS:"
$dnsGuide.steps | ForEach-Object { Write-Host "  $_" }

Write-Host "`n📊 REGISTROS DNS PARA HOSTINGER:"
$dnsGuide.dns_records | ForEach-Object { 
    Write-Host "  $($_.type) → $($_.name) → $($_.value)"
}

# 3. Abrir site localmente
Start-Process "G:\Projeto de IA\generated_sites\marques-design\index.html"

Write-Host "`n✅ Próximos passos:"
Write-Host "  1. Verificar site no navegador"
Write-Host "  2. Deploy no Vercel: cd generated_sites\marques-design && vercel"
Write-Host "  3. Configurar DNS na Hostinger (registros acima)"
Write-Host "  4. Aguardar propagação (1-2h)"
Write-Host "  5. ✅ Site online em https://marquesdesignstudio.com"
```

---

**Última atualização**: 2 de dezembro de 2025  
**Domínio**: marquesdesignstudio.com  
**Registrador**: Hostinger  
**Hospedagem**: Vercel/Netlify/GitHub Pages (GRATUITO)

🎉 **Boa sorte com seu site!**
