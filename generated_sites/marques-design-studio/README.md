# DM Negócios IA - Site Ultra Clean

## 📋 Sobre

Site profissional com layout minimalista para DM Negócios IA.

## 🎨 Características

- ✅ Design ultra clean, sem distrações
- ✅ Fundo escuro profissional (#0a0a0a)
- ✅ Foto de perfil com ícone (substituível por foto real)
- ✅ CTA direto para WhatsApp
- ✅ Totalmente responsivo
- ✅ Animações suaves
- ✅ Zero elementos técnicos

## 🚀 Como Publicar

### Opção 1: Netlify Drop (RECOMENDADO)

1. Acesse: https://app.netlify.com/drop
2. Arraste a pasta `dm-negocios-ia/` completa
3. Aguarde o upload
4. Configure o domínio personalizado

### Opção 2: GitHub + Netlify

1. Suba os arquivos para um repositório GitHub
2. Conecte no Netlify
3. Deploy automático em cada commit

## 📝 Personalização

### Atualizar Número do WhatsApp

No arquivo `index.html`, linha do botão:

```html
<a href="https://wa.me/5511999999999" class="cta-button">
```

Substitua `5511999999999` pelo seu número completo:
- Formato: 55 (Brasil) + DDD + número (sem espaços)
- Exemplo: `5521987654321`

### Adicionar Foto Real

1. Adicione sua foto na pasta como `profile.jpg`
2. No arquivo `index.html`, substitua:

```html
<!-- ANTES -->
<div class="profile-photo">
    🧠
</div>

<!-- DEPOIS -->
<div class="profile-photo" style="background-image: url('profile.jpg'); background-size: cover; background-position: center; font-size: 0;">
</div>
```

### Mudar Cores

No arquivo `style.css`, modifique as variáveis no `:root`:

```css
:root {
    --dark-bg: #0a0a0a;        /* Fundo */
    --text-primary: #ffffff;   /* Texto principal */
    --text-secondary: #a0a0a0; /* Texto secundário */
    --accent: #4a9eff;         /* Cor de destaque */
    --accent-hover: #3d8ae0;   /* Hover do botão */
}
```

## 📁 Estrutura

```
dm-negocios-ia/
├── index.html       # Página principal
├── style.css        # Estilos
├── dashboard.html   # (Opcional) Página técnica
└── README.md        # Este arquivo
```

## 🌐 Links Úteis

- Netlify Drop: https://app.netlify.com/drop
- WhatsApp Link Generator: https://wa.me/
- Otimizador de Imagens: https://tinypng.com/

## 📞 Suporte

Para modificações ou suporte, entre em contato.

---

© 2025 DM Negócios IA
