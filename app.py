import streamlit as st
import base64

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="Kuhn & Fedrigo | Advocacia de Trânsito",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. CARREGAMENTO DE IMAGENS
# ==============================================================================
def get_base64_image(image_filename):
    try:
        with open(image_filename, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode().replace("\n", "")
    except FileNotFoundError:
        return None

IMG_FUNDO = get_base64_image("fundo_transito.jpg")
IMG_LOGO = get_base64_image("logo_kf.png")
# Foto do Douglas carregada via st.image para estabilidade

# Links
WHATSAPP = "5549999589724"
LINK_ZAP = f"https://wa.me/{WHATSAPP}?text=Ol%C3%A1%2C%20gostaria%20de%20uma%20an%C3%A1lise%20jur%C3%ADdica%20do%20meu%20caso."

# ==============================================================================
# 3. CSS (DESIGN V15 - AJUSTE FINO DE MARGEM)
# ==============================================================================
st.markdown("""
<style>
    /* RESET */
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header, footer, #MainMenu { display: none !important; }
    
    /* FONTE */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap');
    * { box-sizing: border-box; }
    body { font-family: 'Montserrat', sans-serif; line-height: 1.6; margin: 0; }
    
    /* UTILITÁRIOS */
    .container-limit { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
    .gold-text { color: #C5A059 !important; }
    
    /* HERO */
    .hero-logo { width: 700px; max-width: 90%; margin-bottom: 3rem; filter: drop-shadow(0 0 20px rgba(0,0,0,0.8)); }
    .hero-title { 
        font-family: 'Playfair Display', serif; font-weight: 700;
        color: white !important; font-size: clamp(3.5rem, 6vw, 5.5rem); 
        line-height: 1.1; margin-bottom: 1.5rem; text-shadow: 0 4px 10px rgba(0,0,0,1); 
    }
    .hero-subtitle { color: #EEE !important; font-size: 1.5rem; font-weight: 400; max-width: 900px; margin-bottom: 4rem; text-shadow: 0 2px 5px rgba(0,0,0,0.8); }

    /* BOTÃO */
    .btn { display: inline-block; padding: 25px 60px; font-size: 1.2rem; font-weight: 700; text-transform: uppercase; text-decoration: none; border-radius: 4px; transition: 0.3s; border: none; cursor: pointer; letter-spacing: 1px; }
    .btn-gold { background: linear-gradient(45deg, #C5A059, #E5C158); color: #000 !important; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
    .btn-gold:hover { transform: scale(1.05); box-shadow: 0 15px 40px rgba(197, 160, 89, 0.6); background: linear-gradient(45deg, #E5C158, #FFF); }

    /* CARDS */
    .section-white { background-color: #FFFFFF; padding: 8rem 0; color: #000; }
    .grid-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 40px; margin-top: 5rem; }
    .card { background: #FDFDFD; padding: 4rem 3rem; border: 1px solid #EEE; border-top: 6px solid #C5A059; border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: 0.3s; }
    .card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
    
    /* ALINHAMENTO PERFEITO DOS TÍTULOS */
    .card h3 { 
        text-align: center; 
        color: #000000 !important; 
        font-size: 1.8rem; 
        margin-bottom: 1rem; 
        font-weight: 700;
        min-height: 5.5rem; 
        display: flex; 
        align-items: center; 
        justify-content: center;
    }
    .card p { text-align: justify; color: #000000 !important; }
    .card-icon { font-size: 4rem; color: #C5A059; margin-bottom: 2rem; display: block; text-align: center; }

    /* CHECKLIST */
    .check-list li { 
        font-size: 1.3rem; color: #E5E5E5 !important; 
        margin-bottom: 1.5rem; list-style: none; 
        display: flex; align-items: center; 
        justify-content: flex-start; 
    }
    .check-list li::before { content: "✓"; color: #C5A059; font-weight: bold; font-size: 1.5rem; margin-right: 15px; flex-shrink: 0; }

    /* RODAPÉ */
    .footer { background: #050505; color: #888; padding: 6rem 0 3rem 0; border-top: 5px solid #C5A059; }
    .footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 4rem; }
    .footer h4 { color: white !important; font-size: 1.4rem; margin-bottom: 2rem; text-transform: uppercase; letter-spacing: 2px; text-align: center; font-weight: 700; }
    .footer-link { color: #AAA; font-size: 1.1rem; text-decoration: none; display: block; margin-bottom: 1rem; text-align: center; }
    .footer-link:hover { color: #C5A059; }

    @media (max-width: 900px) { 
        .hero-title { font-size: 3rem; } 
        .section-white { padding: 4rem 0; }
        .btn { width: 100%; } 
        .card h3 { min-height: auto; } 
    }
</style>
""", unsafe_allow_html=True)

# BACKGROUND HERO
hero_bg_style = f"""
<style>
    .hero {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url("data:image/jpg;base64,{IMG_FUNDO}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        min-height: 95vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 4rem 2rem;
    }}
</style>
"""
st.markdown(hero_bg_style, unsafe_allow_html=True)

# ==============================================================================
# 4. CONTEÚDO
# ==============================================================================

# --- HERO ---
logo_html = f'<img src="data:image/png;base64,{IMG_LOGO}" class="hero-logo">' if IMG_LOGO else '<h1 class="gold-text">KUHN & FEDRIGO</h1>'

st.markdown(f"""
<div class="hero">
    {logo_html}
    <h1 class="hero-title">
        <span style="color: #FFFFFF;">Mantenha seu Direito de Ir e Vir.</span><br>
        <span class="gold-text" style="font-style: italic;">Proteja sua CNH com Estratégia Jurídica.</span>
    </h1>
    <p class="hero-subtitle">
        Atuação especializada na defesa administrativa e judicial de condutores. Protegendo seu direito de dirigir através de uma análise minuciosa de nulidades processuais em Santa Catarina.
    </p>
    <a href="{LINK_ZAP}" target="_blank" class="btn btn-gold">
        SOLICITAR ANÁLISE JURÍDICA
    </a>
</div>
""", unsafe_allow_html=True)

# --- CARDS ---
st.markdown("""
<div class="section-white">
    <div class="container-limit">
        <h2 style="font-family: 'Playfair Display', serif; font-weight: 700; color: #000 !important; font-size: 3.5rem; margin-bottom: 1.5rem; text-align: center;">O Risco de Não se Defender</h2>
        <p style="max-width: 800px; margin: 0 auto; text-align: center; color: #000000 !important;">
            A ausência de defesa técnica dentro do prazo legal autoriza a aplicação imediata das penalidades, impedindo a análise de erros formais que poderiam anular o processo.
        </p>
        <div class="grid-cards">
            <div class="card">
                <span class="card-icon">🚫</span>
                <h3>Suspensão de Até 12 Meses</h3>
                <p>Impedimento legal de conduzir qualquer veículo automotor. O bloqueio no prontuário impede a renovação da CNH até o cumprimento da pena.</p>
            </div>
            <div class="card">
                <span class="card-icon">⚖️</span>
                <h3>Cassação da CNH</h3>
                <p>Dirigir suspenso gera a Cassação. O condutor perde a habilitação definitivamente e deve esperar 2 anos para iniciar o processo do zero.</p>
            </div>
            <div class="card">
                <span class="card-icon">⚠️</span>
                <h3>Agravamento por Reincidência</h3>
                <p>A manutenção de uma infração crítica no prontuário serve como base para o agravamento de sanções futuras. Caso ocorra uma nova infração em 12 meses, as penalidades são duplicadas e o risco de cassação direta torna-se iminente, dificultando defesas posteriores.</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- SOBRE ---
st.markdown('<div style="background-color: #FFFFFF !important; padding: 6rem 0; width: 100%; color: #E5E5E5 !important;">', unsafe_allow_html=True)
st.markdown('<div class="container-limit">', unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    # AJUSTE DE MARGEM DO TEXTO
    # padding-left: 4rem (Move para direita)
    # padding-right: 2rem (Mantém longe da foto)
    
    # 1. TÍTULO
    st.markdown("""
    <div style="padding-left: 4rem; padding-right: 2rem;">
        <div style="text-align: center;">
            <h4 class="gold-text" style="margin-bottom: 2rem; font-weight: 700;">ADVOCACIA ESPECIALIZADA</h4>
            <h2 style="color: #000000 !important; font-size: 3.5rem; margin-bottom: 2rem; font-family: 'Playfair Display', serif;">A Inteligência Jurídica contra a Burocracia.</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. TEXTO (Ajustado)
    st.markdown("""
    <div style="padding-left: 4rem; padding-right: 2rem;">
        <p style="color: #E5E5E5; margin-bottom: 2rem; text-align: justify; font-size: 1.15rem;">
            A <strong>Kuhn & Fedrigo</strong> fundamenta sua atuação na análise técnica individualizada de cada demanda. Rejeitamos soluções padronizadas para priorizar uma investigação minuciosa de falhas procedimentais e nulidades administrativas que possam reverter a penalidade.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 3. CHECKLIST
    st.markdown("""
    <div style="padding-left: 4rem; padding-right: 2rem; display: flex; justify-content: center;">
        <ul class="check-list" style="padding: 0; margin: 0 0 30px 0; display: inline-block;">
            <li>Identificação de nulidades e vícios procedimentais.</li>
            <li>Monitoramento estratégico de prazos e prescrições.</li>
            <li>Medidas judiciais de urgência e Mandados de Segurança.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # 4. BOTÃO
    st.markdown(f"""
    <div style="padding-left: 4rem; padding-right: 2rem; text-align: center;">
        <a href="{LINK_ZAP}" target="_blank" class="btn btn-gold">
            FALAR COM ESPECIALISTA
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    try:
        st.image("foto_douglas.png", use_container_width=True)
    except:
        st.write("")

st.markdown('</div></div>', unsafe_allow_html=True)


# --- RODAPÉ ---
st.markdown(f"""
<div class="footer">
    <div class="container-limit">
        <div class="footer-grid">
            <div style="text-align: center;">
                <h4>KUHN & FEDRIGO</h4>
                <div class="footer-link" style="font-weight: bold; color: #AAA;">Douglas Kuhn (OAB/SC 76.144)</div>
                <div class="footer-link" style="font-weight: bold; color: #AAA;">Gabrieli Fedrigo (OAB/SC 45.099)</div>
                <div class="footer-link" style="margin-top: 2rem; opacity: 0.8;">CNPJ: 33.398.431/0001-07</div>
            </div>
            <div style="text-align: center;">
                <h4>CONTATO</h4>
                <a href="{LINK_ZAP}" class="footer-link" style="color: #C5A059; font-weight: bold; font-size: 1.3rem;">📞 (49) 99995-89724</a>
                <div class="footer-link">✉️ contato@advogadoskf.com.br</div>
                <div class="footer-link">🕒 Seg. a Sex. das 08h às 18h</div>
            </div>
            <div style="text-align: center;">
                <h4>ENDEREÇO</h4>
                <div class="footer-link">Rua Norino Rótulo, nº 130</div>
                <div class="footer-link">Centro, Joaçaba/SC</div>
                <div class="footer-link">CEP: 89.600-000</div>
            </div>
        </div>
        <div style="text-align: center; margin-top: 6rem; padding-top: 2rem; border-top: 1px solid #222; opacity: 0.5; font-size: 0.9rem;">
            © 2026 Kuhn & Fedrigo Advogados. Todos os direitos reservados.<br>
            Site informativo. A contratação de advogado é indispensável.
        </div>
    </div>
</div>

""", unsafe_allow_html=True)

# ==============================================================================
# 5. CORREÇÃO DE CONTRASTE POR DISPOSITIVO (ADICIONAR AO FINAL)
# ==============================================================================
st.markdown("""
<style>
    /* --- CONFIGURAÇÃO PARA COMPUTADOR (Telas Grandes) --- */
    @media (min-width: 901px) {
        /* Força fundo branco na seção 'Sobre' e Cards no PC */
        .section-white, div[style*="background-color: #080808"] {
            background-color: #FFFFFF !important;
        }
        /* Força letras pretas para leitura perfeita no PC */
        .section-white h2, .section-white p,
        div[style*="background-color: #080808"] h2, 
        div[style*="background-color: #080808"] p,
        div[style*="background-color: #080808"] li {
            color: #1A1A1A !important;
        }
    }

    /* --- CONFIGURAÇÃO PARA CELULAR (Telas Pequenas) --- */
    @media (max-width: 900px) {
        /* Mantém o visual que você já aprovou no celular (Fundo Escuro) */
        div[style*="background-color: #080808"] {
            background-color: #080808 !important;
        }
        div[style*="background-color: #080808"] h2, 
        div[style*="background-color: #080808"] p,
        div[style*="background-color: #080808"] li {
            color: #FFFFFF !important;
        }
    }
</style>
""", unsafe_allow_html=True)








