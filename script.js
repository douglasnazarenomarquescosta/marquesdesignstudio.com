// Modal de Orçamento
const modal = document.getElementById('modal-orcamento');
const btnOrcamento = document.getElementById('btn-orcamento');
const spanClose = document.querySelector('.modal-close');
const form = document.getElementById('form-orcamento');

// Abrir modal
if (btnOrcamento) {
    btnOrcamento.addEventListener('click', () => {
        modal.classList.add('active');
    });
}

// Fechar modal ao clicar no X
if (spanClose) {
    spanClose.addEventListener('click', () => {
        modal.classList.remove('active');
    });
}

// Fechar modal ao clicar fora
window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.classList.remove('active');
    }
});

// Enviar formulário
if (form) {
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const email = document.getElementById('email').value;
        const whatsapp = document.getElementById('whatsapp').value;
        const assunto = document.getElementById('assunto').value;
        const descricao = document.getElementById('descricao').value;
        
        // Criar corpo do email
        const corpoEmail = `Olá Douglas,

Segue minha solicitação de orçamento:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📧 Email: ${email}
📱 WhatsApp: ${whatsapp}

Como posso te ajudar:
${assunto}

Descrição detalhada:
${descricao}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Aguardo seu retorno.

Atenciosamente.`;
        
        // Criar link mailto
        const mailtoLink = `mailto:dmnegocios79@gmail.com?subject=${encodeURIComponent('Solicitação de Orçamento - ' + assunto)}&body=${encodeURIComponent(corpoEmail)}`;
        
        // Abrir cliente de email
        window.location.href = mailtoLink;
        
        // Fechar modal e limpar formulário após pequeno delay
        setTimeout(() => {
            modal.classList.remove('active');
            form.reset();
        }, 500);
    });
}

// Smooth scroll para links de navegação
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Adicionar classe 'scrolled' ao header quando rolar a página
window.addEventListener('scroll', () => {
    const header = document.querySelector('header');
    if (window.scrollY > 50) {
        header.style.boxShadow = '0 5px 20px rgba(0,0,0,0.15)';
    } else {
        header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
    }
});

// Handler para botões CTA (exceto o botão de orçamento)
document.querySelectorAll('.cta-button:not(#btn-orcamento)').forEach(button => {
    button.addEventListener('click', () => {
        const whatsappNumber = '5564996105742';
        const message = encodeURIComponent('Olá! Gostaria de saber mais sobre os serviços de empreendedorismo.');
        window.open(`https://wa.me/${whatsappNumber}?text=${message}`, '_blank');
    });
});

// Controle do slider
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function showSlide(index) {
    slides.forEach(slide => slide.classList.remove('active'));
    
    if (index >= slides.length) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = slides.length - 1;
    } else {
        currentSlide = index;
    }
    
    slides[currentSlide].classList.add('active');
}

function changeSlide(direction) {
    showSlide(currentSlide + direction);
}

// Auto-play do slider (muda a cada 5 segundos)
setInterval(() => {
    changeSlide(1);
}, 5000);

console.log('Site carregado com sucesso! 🚀');