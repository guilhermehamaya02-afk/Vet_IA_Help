import streamlit as st

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

tempo = st.selectbox("Tempo dos sinais", ["Hoje", "1-2 dias", "3+ dias"], key="tempo")
intensidade = st.selectbox("Intensidade", ["Leve", "Moderado", "Intenso"], key="intensidade")

dor = st.selectbox("Sente dor?", ["Sim", "Não"], key="dor")
comendo = st.selectbox("Está se alimentando?", ["Sim", "Não"], key="comendo")

sintomas = st.text_area("Descreva os sintomas", key="sintomas")

# ▶️ Botão análise
if st.button("Analisar", key="btn_analise"):
    if sintomas.strip() == "":
        st.warning("⚠️ Descreva os sintomas antes de analisar.")
    else:
        st.session_state.analisado = True
        st.session_state.sintomas_total = sintomas


# 🔍 Normalização
def normalizar(texto):
    texto = texto.lower()

    substituicoes = {
        "vômito": "vomito",
        "vomitando": "vomito",
        "diarréia": "diarreia",
        "falta de ar": "dispneia",
        "não come": "anorexia",
        "sem comer": "anorexia",
        "muito fraco": "fraqueza",
        "mole": "apatia",
        "triste": "apatia"
    }

    for k, v in substituicoes.items():
        if k in texto:
            texto = texto.replace(k, v)

    return texto


# 🔍 Análise clínica
def analisar(texto, especie, idade, comendo, dor, tempo, intensidade):

    texto = normalizar(texto)

    sistemas = {
        "Gastrointestinal": {"lista": set(), "score": 0},
        "Respiratório": {"lista": set(), "score": 0},
        "Neurológico": {"lista": set(), "score": 0},
        "Urinário": {"lista": set(), "score": 0},
        "Dermatológico": {"lista": set(), "score": 0},
        "Sistêmico": {"lista": set(), "score": 0}
    }

    # Gastro
    if "vomito" in texto:
        sistemas["Gastrointestinal"]["lista"].add("Gastrite")
        sistemas["Gastrointestinal"]["score"] += 2

    if "diarreia" in texto:
        sistemas["Gastrointestinal"]["lista"].add("Enterite")
        sistemas["Gastrointestinal"]["score"] += 2

    if "vomito" in texto and "diarreia" in texto:
        sistemas["Gastrointestinal"]["lista"].add("Gastroenterite")
        sistemas["Gastrointestinal"]["score"] += 3

    # Respiratório
    if "tosse" in texto:
        sistemas["Respiratório"]["lista"].add("Doença respiratória")
        sistemas["Respiratório"]["score"] += 2

    if "dispneia" in texto:
        sistemas["Respiratório"]["lista"].add("Emergência respiratória")
        sistemas["Respiratório"]["score"] += 4

    # Neurológico
    if "convuls" in texto:
        sistemas["Neurológico"]["lista"].add("Distúrbio neurológico")
        sistemas["Neurológico"]["score"] += 4

    # Urinário
    if "urinar" in texto and "dificuldade" in texto:
        sistemas["Urinário"]["lista"].add("Obstrução urinária")
        sistemas["Urinário"]["score"] += 4

    # Sistêmico
    if "fraqueza" in texto or "apatia" in texto:
        sistemas["Sistêmico"]["lista"].add("Doença sistêmica")
        sistemas["Sistêmico"]["score"] += 2

    if comendo == "Não":
        sistemas["Sistêmico"]["lista"].add("Anorexia")
        sistemas["Sistêmico"]["score"] += 2

    if dor == "Sim":
        sistemas["Sistêmico"]["score"] += 1

    # Intensidade
    if intensidade == "Intenso":
        for s in sistemas:
            sistemas[s]["score"] += 2

    return sistemas


# 🔍 EXECUÇÃO
if st.session_state.analisado:

    st.write("🔎 Analisando dados clínicos...")

    sistemas = analisar(
        st.session_state.sintomas_total,
        especie,
        idade,
        comendo,
        dor,
        tempo,
        intensidade
    )

    maior_score = 0
    sistema_principal = None

    for nome_sistema, dados in sistemas.items():
        if dados["lista"]:
            st.subheader(f"🔎 {nome_sistema}")
            for d in dados["lista"]:
                st.write(f"- {d}")

            if dados["score"] >= maior_score:
                maior_score = dados["score"]
                sistema_principal = nome_sistema

    # 🧠 Interpretação
    if sistema_principal:
        st.subheader("🧠 Interpretação clínica")

        if sistema_principal == "Gastrointestinal":
            st.write("Os sinais indicam comprometimento gastrointestinal, podendo envolver inflamação ou infecção.")

        elif sistema_principal == "Respiratório":
            st.write("Os sintomas sugerem envolvimento respiratório, podendo indicar infecção ou dificuldade respiratória.")

        elif sistema_principal == "Urinário":
            st.write("Há sinais compatíveis com problema urinário, podendo ser grave.")

        elif sistema_principal == "Neurológico":
            st.write("Os sinais indicam possível alteração neurológica, requerendo atenção.")

        elif sistema_principal == "Sistêmico":
            st.write("O quadro indica comprometimento geral do organismo.")

    # 📋 Recomendações
    st.subheader("📋 Recomendações iniciais")

    if sistema_principal == "Gastrointestinal":
        st.write("- Manter hidratação")
        st.write("- Observar vômitos e diarreia")

    elif sistema_principal == "Respiratório":
        st.write("- Evitar esforço")
        st.write("- Monitorar respiração")

    elif sistema_principal == "Urinário":
        st.write("- Procurar atendimento imediato se não urinar")

    elif sistema_principal == "Neurológico":
        st.write("- Procurar emergência veterinária")

    elif sistema_principal == "Sistêmico":
        st.write("- Monitorar estado geral")
        st.write("- Buscar avaliação clínica")

    # 🔄 Adicionar sintoma
    novo = st.text_input("Adicionar novo sintoma", key="novo")

    if st.button("Adicionar sintoma", key="btn_add"):
        if novo.strip() != "":
            st.session_state.sintomas_total += " " + novo
            st.success("Sintoma adicionado! Reanalisando...")
            st.session_state.analisado = True

    # 💬 Pergunta
    pergunta = st.text_input("Pergunta ao sistema", key="pergunta")

    if pergunta:
        if any(p in pergunta.lower() for p in ["remedio", "remédio", "medicamento"]):
            st.error("❌ Não posso recomendar medicamentos.")
            st.write("💡 A decisão deve ser do veterinário.")
        else:
            st.write("🧠 Pergunta válida para avaliação clínica.")

    st.info("Consulte um veterinário para diagnóstico definitivo.")
