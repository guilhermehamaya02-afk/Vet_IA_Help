import streamlit as st

st.title("🐶 VetHelp IA")

st.markdown("""
Olá 👋  
Sou a *VetHelp*, uma assistente virtual de triagem veterinária.

Estou aqui para te ajudar na avaliação inicial do paciente 🐾  
Descreva os sinais clínicos para começarmos.
""")

st.info("⚠️ Esta ferramenta auxilia na triagem e não substitui o médico veterinário.")

# 🔒 Estado
if "analisado" not in st.session_state:
    st.session_state.analisado = False

if "sintomas_total" not in st.session_state:
    st.session_state.sintomas_total = ""

if "ultima_atualizacao" not in st.session_state:
    st.session_state.ultima_atualizacao = ""

# 📥 Inputs
nome = st.text_input("Nome do paciente")
especie = st.selectbox("Espécie", ["Cachorro", "Gato"])
idade = st.number_input("Idade", min_value=0)
peso = st.number_input("Peso (kg)", min_value=0.0)

tempo = st.selectbox("Tempo dos sinais", ["Hoje", "1-2 dias", "3+ dias"])
intensidade = st.selectbox("Intensidade", ["Leve", "Moderado", "Intenso"])

dor = st.selectbox("Paciente apresenta dor?", ["Sim", "Não"])
comendo = st.selectbox("Está se alimentando?", ["Sim", "Não"])

sintomas = st.text_area("Descreva os sintomas")

# ▶️ Iniciar análise
if st.button("Iniciar análise"):
    st.session_state.analisado = True
    st.session_state.sintomas_total = sintomas

# 🔍 FUNÇÃO PRINCIPAL (AGORA COMPLETA)
def analisar(texto, especie, idade, comendo, dor, tempo, intensidade):

    texto = texto.lower()
    possiveis = set()
    score = 0

    # 🔴 Combinações fortes
    if "vomito" in texto and "diarreia" in texto:
        possiveis.add("Gastroenterite")
        score += 3

    if "sangue" in texto and "fraqueza" in texto:
        possiveis.add("Hemorragia interna")
        score += 4

    # 🔴 Graves
    if "convuls" in texto:
        possiveis.add("Distúrbio neurológico")
        score += 4

    if "sangue" in texto:
        possiveis.add("Úlcera ou intoxicação")
        score += 3

    # 🟠 Moderados
    if "vomito" in texto or "vômito" in texto:
        possiveis.add("Gastrite")
        score += 2

    if "diarreia" in texto:
        possiveis.add("Infecção intestinal")
        score += 2

    if "febre" in texto:
        possiveis.add("Infecção")
        score += 2

    if "tosse" in texto:
        possiveis.add("Doença respiratória")
        score += 2

    # 🟡 Leves
    if "coceira" in texto:
        possiveis.add("Alergia ou dermatite")
        score += 1

    # 📊 Estado geral
    if comendo == "Não":
        possiveis.add("Anorexia")
        score += 2

    if dor == "Sim":
        possiveis.add("Processo inflamatório")
        score += 1

    # 🐱 Espécie
    if especie == "Gato" and "vomito" in texto:
        possiveis.add("Vômito frequente em felinos — avaliar padrão")

    # 👶 Idade
    if idade < 1:
        possiveis.add("Paciente jovem — maior risco infeccioso")
        score += 1

    if idade > 8:
        possiveis.add("Paciente idoso — atenção para doenças crônicas")
        score += 1

    # ⏱️ Tempo
    if tempo == "3+ dias":
        score += 2

    # 🔥 Intensidade
    if intensidade == "Intenso":
        score += 3
    elif intensidade == "Moderado":
        score += 2

    # fallback
    if not possiveis:
        possiveis.add("Quadro inespecífico — avaliação clínica necessária")

    return possiveis, score

# 🔍 EXECUÇÃO
if st.session_state.analisado:

    st.write("🔎 Analisando...")

    possiveis, score = analisar(
        st.session_state.sintomas_total,
        especie,
        idade,
        comendo,
        dor,
        tempo,
        intensidade
    )

    # Gravidade
    if score >= 7:
        nivel = "grave"
    elif score >= 4:
        nivel = "moderado"
    else:
        nivel = "leve"

    # Resultado
    st.subheader("🧠 Possíveis causas:")
    for p in possiveis:
        st.write(f"- {p}")

    st.subheader("⚠️ Gravidade:")
    if nivel == "grave":
        st.error("🚨 Caso grave — procurar atendimento imediato")
    elif nivel == "moderado":
        st.warning("⚠️ Caso moderado — avaliação recomendada")
    else:
        st.success("🟢 Caso leve — observar evolução")

    # Atualização controlada
    st.subheader("🔄 Adicionar novo sintoma")
    mais = st.text_input("Digite outro sintoma:")

    if mais and mais != st.session_state.ultima_atualizacao:
        st.session_state.sintomas_total += " " + mais
        st.session_state.ultima_atualizacao = mais
        st.rerun()

    # Pergunta
    st.subheader("💬 Pergunta ao sistema")
    pergunta = st.text_input("Digite sua pergunta:")

    if pergunta:
        if any(p in pergunta.lower() for p in ["remedio", "remédio", "medicamento", "dose"]):
            st.error("❌ Não posso recomendar medicamentos.")
            st.write("💡 Sou uma ferramenta de triagem.")
        else:
            st.write("🧠 Pergunta válida para avaliação clínica.")

    st.info("Consulte um veterinário para diagnóstico definitivo.")
    
