import streamlit as st
import unicodedata

st.title("🐶 VetHelp IA v2")

st.markdown("""
Assistente inteligente de triagem veterinária 🧠🐾  
Sistema de análise por sintomas + gravidade.
""")

st.info("⚠️ Ferramenta de triagem — não substitui veterinário.")

# =========================
# NORMALIZAÇÃO
# =========================
def normalizar(texto):
    texto = texto.lower()
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

# =========================
# BANCO DE SINTOMAS
# =========================
SINTOMAS = {
    "vomito": {"Gastroenterite / distúrbio GI": 2},
    "diarreia": {"Infecção intestinal / parasitose": 2},
    "sangue": {"Sinais hemorrágicos / úlcera": 4},
    "fraqueza": {"Anemia / doença sistêmica": 3},
    "febre": {"Processo infeccioso": 2},
    "tosse": {"Doença respiratória": 2},
    "convuls": {"Distúrbio neurológico grave": 5},
    "coceira": {"Dermatite / alergia": 1},
    "queda de pelo": {"Alteração dermatológica": 1},
    "cansaco": {"Doença sistêmica": 3},
    "desmaio": {"Colapso sistêmico grave": 5}
}

# =========================
# ESTADO
# =========================
if "texto_total" not in st.session_state:
    st.session_state.texto_total = ""

if "analisado" not in st.session_state:
    st.session_state.analisado = False

def reset():
    st.session_state.analisado = False
    st.session_state.texto_total = ""

# =========================
# INPUTS
# =========================
nome = st.text_input("Nome do paciente")
especie = st.selectbox("Espécie", ["Cachorro", "Gato"])
idade = st.number_input("Idade (anos)", min_value=0.1)
peso = st.number_input("Peso (kg)", min_value=0.1)

dor = st.selectbox("Paciente com dor?", ["Sim", "Não"])
comendo = st.selectbox("Está comendo normalmente?", ["Sim", "Não"])

sintomas = st.text_area("Descreva os sinais clínicos")

# =========================
# BOTÃO
# =========================
if st.button("Iniciar análise"):
    st.session_state.analisado = True
    st.session_state.texto_total = sintomas

# =========================
# IA
# =========================
def analisar(texto):
    texto = normalizar(texto)

    possiveis = {}
    score = 0
    red_flag = False

    RED_FLAGS = ["convuls", "desmaio", "inconsciente", "paralis"]

    if any(flag in texto for flag in RED_FLAGS):
        red_flag = True
        score += 5  # 🔴 agora influencia gravidade

    for sintoma, diagn in SINTOMAS.items():
        if sintoma in texto:
            for d, peso in diagn.items():
                possiveis[d] = possiveis.get(d, 0) + peso
                score += peso

    return possiveis, score, red_flag

# =========================
# EXECUÇÃO
# =========================
if st.session_state.analisado:

    st.subheader("🔎 Análise clínica")

    texto = st.session_state.texto_total
    possiveis, score, red_flag = analisar(texto)

    # ajustes clínicos (AGORA COM PESO CORRETO)
    if comendo == "Não":
        score += 2
        possiveis["Anorexia / inapetência"] = possiveis.get("Anorexia / inapetência", 0) + 2

    if dor == "Sim":
        score += 1

    if idade < 1:
        score += 2
        possiveis["Paciente jovem (alto risco infeccioso)"] = possiveis.get("Paciente jovem (alto risco infeccioso)", 0) + 2

    if idade > 8:
        score += 2
        possiveis["Paciente idoso (risco crônico)"] = possiveis.get("Paciente idoso (risco crônico)", 0) + 2

    # =========================
    # CLASSIFICAÇÃO
    # =========================
    if red_flag or score >= 10:
        nivel = "grave"
    elif score >= 5:
        nivel = "moderado"
    else:
        nivel = "leve"

    # =========================
    # RESULTADO
    # =========================
    st.write("### 🧠 Possibilidades clínicas:")

    if possiveis:
        for d in sorted(possiveis, key=possiveis.get, reverse=True):
            st.write(f"- {d}")
    else:
        st.write("- Quadro inespecífico")

    st.write("---")

    st.write("### ⚠️ Gravidade")

    if red_flag:
        st.error("🚨 ALERTA: Sinais neurológicos ou críticos detectados!")

    if nivel == "grave":
        st.error("🚨 EMERGÊNCIA VETERINÁRIA — atendimento imediato recomendado.")
    elif nivel == "moderado":
        st.warning("⚠️ Avaliação veterinária recomendada em breve.")
    else:
        st.success("🟢 Quadro leve — monitorar evolução.")

    st.metric("Score clínico", score)

    # =========================
    # RECOMENDAÇÕES
    # =========================
    st.write("### 📋 Recomendações")
    st.write("- Monitorar evolução")
    st.write("- Observar alimentação e água")
    st.write("- Procurar veterinário se piorar")
    st.write("- Considerar exames clínicos se persistir")

    # =========================
    # RESET
    =========================
    st.button("Resetar caso", on_click=reset)
