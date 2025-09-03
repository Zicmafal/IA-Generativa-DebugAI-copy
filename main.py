# 1. Imports essenciais
import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 2. Configuração da Página (Aba do Navegador)
st.set_page_config(
    page_title="DebugAI – Diagnóstico de Erros DevOps",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 3. Carregar API Key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("🔑 API Key não encontrada. Verifique o arquivo .env.")
    st.stop()

# 4. Configuração da API do Gemini
genai.configure(api_key=GEMINI_API_KEY)

def init_gemini():
    generation_config = {
        "temperature": 0.3,   # mais técnico, menos criativo
        "top_p": 0.8,
        "top_k": 40,
        "max_output_tokens": 1024,
    }
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )
    return model

# Função para gerar resposta com histórico das últimas 5 mensagens
def generate_response(model, user_input):
    try:
        conversation_history = ""
        for msg in st.session_state.messages[-5:]:  # últimas 5 mensagens
            role = "Usuário" if msg["role"] == "user" else "Assistente"
            conversation_history += f"{role}: {msg['content']}\n"

        prompt = f"""
        Você é um assistente especializado em DevOps, Docker, Kubernetes, Prometheus, AWS e Linux.
        O usuário fornecerá mensagens, incluindo erros, logs e contexto adicional.

        Histórico da conversa até agora:
        {conversation_history}

        Nova mensagem do usuário:
        {user_input}

        Regras:
        1. Sempre responda em português.
        2. Mantenha coerência com o histórico (não reinicie a conversa).
        3. Se o usuário apenas adicionar detalhes (ex.: "no Linux"), use o contexto anterior.
        4. Explique de forma clara e sugira soluções práticas.
        5. Se não souber, peça mais detalhes, mas sem perder o contexto.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

# Inicializar modelo
if 'model' not in st.session_state:
    with st.spinner("🔄 Inicializando modelo Gemini..."):
        st.session_state.model = init_gemini()

# 5. Sidebar – Configurações + Estatísticas
with st.sidebar:
    st.header("⚙️ Configurações")
    if st.button("🗑️ Limpar Conversa"):
        if 'messages' in st.session_state:
            st.session_state.messages = []
            st.rerun()
    
    st.divider()
    st.subheader("📊 Estatísticas")
    if 'messages' in st.session_state:
        st.metric("Mensagens trocadas", len(st.session_state.messages))
    else:
        st.metric("Mensagens trocadas", 0)

    st.divider()
    st.subheader("🔧 Links úteis")
    st.markdown("[🐳 Docker Docs](https://docs.docker.com/)")
    st.markdown("[☸️ Kubernetes Docs](https://kubernetes.io/docs/)")
    st.markdown("[📊 Prometheus Docs](https://prometheus.io/docs/)")
    st.markdown("[☁️ AWS CLI Docs](https://docs.aws.amazon.com/cli/)")

# 6. CSS customizado – tema escuro estilo hacker
st.markdown("""
<style>
    body {
        background-color: #0d1117;
        color: #f8f8f2;
        font-family: "Fira Code", monospace;
    }

    [data-testid="stSidebar"] {
        background-color: #0d1117;
        color: #f8f8f2;
    }
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] li {
        color: #f8f8f2 !important;
    }

    .stButton button {
        background-color: #21262d;
        color: #f8f8f2;
        border: 1px solid #30363d;
        border-radius: 6px;
        transition: all 0.2s ease;
    }
    .stButton button:hover {
        background-color: #30363d;
        border-color: #58a6ff;
        color: #58a6ff;
    }

    /* Mensagens estilo terminal */
    .stChatMessage {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 12px;
        color: #f8f8f2 !important;
        font-family: "Fira Code", monospace;
        font-size: 15px;
        line-height: 1.6;
    }

    .stChatMessage p, 
    .stChatMessage li,
    .stChatMessage span {
        color: #f8f8f2 !important;
    }

    h1, h2, h3 {
        color: #58a6ff;
        font-family: "Fira Code", monospace;
    }

    /* Inline code */
    code {
        background-color: #0d1117;
        color: #3fb950;
        padding: 2px 5px;
        border-radius: 4px;
        font-family: "Fira Code", monospace;
        font-size: 13px;
    }

    /* Blocos de código */
    pre, pre code {
        background-color: #0d1117 !important;
        color: #f8f8f2 !important;
        border-radius: 6px;
        padding: 10px;
        font-family: "Fira Code", monospace;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# 7. Interface principal – estilo console
st.markdown("""
<pre style="background:#0d1117; color:#58a6ff; padding:15px; border-radius:10px; font-family:'Fira Code', monospace; font-size:14px;">
👾 DebugAI v1.0
------------------------------------
Assistente de Diagnóstico DevOps
Digite um erro ou log para iniciar análise
</pre>
""", unsafe_allow_html=True)

# Histórico de mensagens
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": """👋 Bem-vindo ao **DebugAI**!
Sou seu assistente de diagnóstico DevOps.

Posso ajudar com erros de:
- 🐍 Python  
- 🐳 Docker  
- ☸️ Kubernetes  
- 📊 Prometheus  
- ☁️ AWS CLI  

Digite abaixo o erro ou log que você quer analisar.
"""
    })

# Exibir mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
if prompt := st.chat_input("💬 Digite o erro ou log aqui..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("🤔 Analisando o erro..."):
            response = generate_response(st.session_state.model, prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
