[22:06, 14/04/2026] Gui Amoreco: import streamlit as st

st.title("🐶 VetHelp IA - Assistente Clínica")

st.markdown("""
Olá 👋  
Sou a *VetHelp*, uma assistente inteligente de triagem veterinária.

Descreva os sinais clínicos do paciente para iniciarmos a análise 🐾
""")

st.info("⚠️ Esta ferramenta auxilia na triagem e não substitui o médico veterinário.")

# 🔒 Estado
if "analisado" not in st.session_state:
    st.session_state.analisado = False

if "sintomas_total" not in st.session_state:
    st.session_state.sintomas_total = ""

# 📥 Inputs
nome = st.text_input("Nome do paciente", key="nome")
especie = st.selectbox("Espécie", ["Cachorro", "Gato"], key="especie")
idade = st.number_input("Idade", min_value=0, key="idade")
peso = st.number_input("Peso (kg)", min_value=0.0, key="peso")

t…
[22:12, 14/04/2026] Gui Amoreco: def analisar(texto):

    texto = texto.lower()

    diagnostico = []
    explicacao = ""
    recomendacao = ""

    # 🔴 CASOS PRIORITÁRIOS

    if "sangue" in texto and "vomito" in texto:
        diagnostico = ["Hemorragia digestiva", "Úlcera grave", "Intoxicação"]
        explicacao = "Presença de sangue no vômito indica possível lesão grave no trato gastrointestinal."
        recomendacao = "🚨 Procurar atendimento imediato."

    elif "vomito" in texto and "diarreia" in texto:
        diagnostico = ["Gastroenterite", "Infecção intestinal"]
        explicacao = "Os sinais indicam inflamação gastrointestinal, comum em infecções."
        recomendacao = "Manter hidratação e observar evolução."

    elif "dificuldade para urinar" in texto:
        diagnostico = ["Obstrução urinária"]
        explicacao = "A dificuldade para urinar pode indicar obstrução, especialmente grave em felinos."
        recomendacao = "🚨 Atendimento imediato."

    elif "convuls" in texto:
        diagnostico = ["Distúrbio neurológico"]
        explicacao = "Convulsões indicam alteração neurológica importante."
        recomendacao = "🚨 Emergência veterinária."

    elif "tosse" in texto:
        diagnostico = ["Doença respiratória"]
        explicacao = "Os sinais indicam possível comprometimento respiratório."
        recomendacao = "Monitorar evolução e procurar avaliação."

    elif "coceira" in texto:
        diagnostico = ["Alergia / dermatite"]
        explicacao = "Sintomas compatíveis com problema dermatológico."
        recomendacao = "Observar e evitar automedicação."

    else:
        diagnostico = ["Quadro inespecífico"]
        explicacao = "Os sinais não permitem uma hipótese clara."
        recomendacao = "Recomenda-se avaliação clínica."

    return diagnostico, explicacao, recomendacao
