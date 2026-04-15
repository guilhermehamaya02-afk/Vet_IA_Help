import streamlit as st

# 🧠 Interface
st.title("🐶 VetHelp IA - Triagem Clínica")

st.markdown("""
Olá 👋  
Sou a *VetHelp*, assistente de triagem veterinária.

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
        "cansaço": "cansaco",
        "falta de ar": "dispneia",
        "urina com sangue": "hematúria",
        "urina sangue": "hematúria",
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

    # 🟠 Gastro
    if "vomito" in texto:
        sistemas["Gastrointestinal"]["lista"].add("Gastrite")
        sistemas["Gastrointestinal"]["score"] += 2

    if "diarreia" in texto:
        sistemas["Gastrointestinal"]["lista"].add("Enterite / infecção intestinal")
        sistemas["Gastrointestinal"]["score"] += 2

    if "vomito" in texto and "diarreia" in texto:
        sistemas["Gastrointestinal"]["lista"].add("Gastroenterite")
        sistemas["Gastrointestinal"]["score"] += 3

    # 🔵 Respiratório
    if "tosse" in texto:
        sistemas["Respiratório"]["lista"].add("Doença respiratória")
        sistemas["Respiratório"]["score"] += 2

    if "dispneia" in texto:
        sistemas["Respiratório"]["lista"].add("Dispneia - possível emergência")
        sistemas["Respiratório"]["score"] += 4

    # 🟣 Neurológico
    if "convuls" in texto:
        sistemas["Neurológico"]["lista"].add("Distúrbio neurológico")
        sistemas["Neurológico"]["score"] += 4

    if "tremor" in texto:
        sistemas["Neurológico"]["lista"].add("Alteração neurológica ou intoxicação")
        sistemas["Neurológico"]["score"] += 2

    # 💧 Urinário
    if "hematúria" in texto:
        sistemas["Urinário"]["lista"].add("Cistite / cálculo urinário")
        sistemas["Urinário"]["score"] += 3

    if "dificuldade para urinar" in texto:
        sistemas["Urinário"]["lista"].add("Obstrução urinária (emergência)")
        sistemas["Urinário"]["score"] += 4

    # 🧴 Dermato
    if "coceira" in texto:
        sistemas["Dermatológico"]["lista"].add("Alergia / dermatite")
        sistemas["Dermatológico"]["score"] += 1

    # 🔴 Sistêmico
    if "fraqueza" in texto or "apatia" in texto:
        sistemas["Sistêmico"]["lista"].add("Doença sistêmica")
        sistemas["Sistêmico"]["score"] += 2

    if comendo == "Não":
        sistemas["Sistêmico"]["lista"].add("Anorexia")
        sistemas["Sistêmico"]["score"] += 2

    if dor == "Sim":
        sistemas["Sistêmico"]["lista"].add("Processo inflamatório")
        sistemas["Sistêmico"]["score"] += 1

    # 🐱 Felino crítico
    if especie == "Gato" and "dificuldade para urinar" in texto:
        sistemas["Urinário"]["lista"].add("Emergência felina (obstrução uretral)")
        sistemas["Urinário"]["score"] += 5

    # 👶 Idade
    if idade < 1:
        sistemas["Sistêmico"]["score"] += 1

    if idade > 8:
        sistemas["Sistêmico"]["score"] += 1

    # ⏱️ Tempo
    if tempo == "3+ dias":
        for s in sistemas:
            sistemas[s]["score"] += 1

    # 🔥 Intensidade
    if intensidade == "Intenso":
        for s in sistemas:
            sistemas[s]["score"] += 2
    elif intensidade == "Moderado":
        for s in sistemas:
            sistemas[s]["score"] += 1

    return sistemas

# 🔍 Execução
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

    if sistema_principal:
        st.subheader("🧠 Principal suspeita clínica")
        st.success(f"Sistema mais afetado: {sistema_principal}")

    # 🔄 Adicionar sintoma
    novo = st.text_input("Adicionar novo sintoma", key="novo_sintoma")

    if st.button("Adicionar sintoma", key="btn_add"):
        if novo.strip() != "":
            st.session_state.sintomas_total += " " + novo
            st.success("Sintoma adicionado!")

    # 💬 Pergunta
    pergunta = st.text_input("Pergunta ao sistema", key="pergunta")

    if pergunta:
        if any(p in pergunta.lower() for p in ["remedio", "remédio", "medicamento", "dose"]):
            st.error("❌ Não posso recomendar medicamentos.")
            st.write("💡 A conduta deve ser definida por um médico veterinário.")
        else:
            st.write("🧠 Pergunta relevante para avaliação clínica.")

    st.info("Procure um veterinário para diagnóstico definitivo.")
