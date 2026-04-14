import streamlit as st

st.title("🐶 IA HelpVet - Triagem Veterinária")
st.warning("⚠️ Não substitui o médico veterinário")

# 🔒 Estado
if "analisado" not in st.session_state:
    st.session_state.analisado = False

# 📥 Inputs
nome = st.text_input("Nome do paciente")
idade = st.number_input("Idade", min_value=0)
peso = st.number_input("Peso (kg)", min_value=0.0)
dor = st.selectbox("Paciente sente dor?", ["Sim", "Não"])
comendo = st.selectbox("Paciente está se alimentando?", ["Sim", "Não"])
sintomas = st.text_area("Descreva os sintomas")

# ▶️ Botão
if st.button("Analisar"):
    st.session_state.analisado = True
    st.session_state.sintomas = sintomas
    st.session_state.comendo = comendo
    st.session_state.dor = dor

# 🔍 ANÁLISE
if st.session_state.analisado:

    sintomas_lower = st.session_state.sintomas.lower()

    possiveis = set()
    gravidade_score = 0

    # 🔴 GRAVES
    if "sangue" in sintomas_lower:
        possiveis.update([
            "Hemorragia interna",
            "Úlcera hemorrágica",
            "Intoxicação",
            "Parvovirose"
        ])
        gravidade_score += 3

    if "convuls" in sintomas_lower:
        possiveis.update([
            "Distúrbio neurológico",
            "Intoxicação",
            "Epilepsia"
        ])
        gravidade_score += 3

    if "prostra" in sintomas_lower or "não levanta" in sintomas_lower:
        possiveis.update([
            "Choque",
            "Doença sistêmica grave"
        ])
        gravidade_score += 3

    # 🟠 MODERADOS
    if "vomito" in sintomas_lower or "vômito" in sintomas_lower:
        possiveis.update([
            "Gastrite",
            "Corpo estranho",
            "Infecção gastrointestinal"
        ])
        gravidade_score += 2

    if "diarreia" in sintomas_lower:
        possiveis.update([
            "Parasitose",
            "Infecção intestinal",
            "Giardíase"
        ])
        gravidade_score += 2

    if "febre" in sintomas_lower:
        possiveis.update([
            "Infecção bacteriana",
            "Doença viral"
        ])
        gravidade_score += 2

    if "tosse" in sintomas_lower:
        possiveis.update([
            "Tosse dos canis",
            "Doença respiratória",
            "Problema cardíaco"
        ])
        gravidade_score += 2

    # 🟡 LEVES
    if "coceira" in sintomas_lower:
        possiveis.update([
            "Dermatite",
            "Alergia",
            "Pulgas ou carrapatos"
        ])
        gravidade_score += 1

    if "queda de pelo" in sintomas_lower:
        possiveis.update([
            "Dermatite",
            "Doença hormonal"
        ])
        gravidade_score += 1

    if "fraqueza" in sintomas_lower:
        possiveis.update([
            "Anemia",
            "Doença sistêmica"
        ])
        gravidade_score += 2

    # 📊 Estado geral
    if st.session_state.comendo == "Não":
        possiveis.add("Anorexia (sinal clínico importante)")
        gravidade_score += 2

    if st.session_state.dor == "Sim":
        possiveis.add("Processo inflamatório ou dor interna")
        gravidade_score += 1

    # 🧠 fallback
    if not possiveis:
        possiveis.add("Quadro inespecífico - necessita avaliação clínica")
        gravidade_score += 1

    # 📊 Classificação
    if gravidade_score >= 6:
        gravidade = "GRAVE"
    elif gravidade_score >= 3:
        gravidade = "MODERADO"
    else:
        gravidade = "LEVE"

    # 📤 RESULTADO
    st.subheader("🧠 Possíveis causas:")
    for p in possiveis:
        st.write(f"- {p}")

    st.subheader("⚠️ Nível de gravidade:")
    if gravidade == "GRAVE":
        st.error("GRAVE - procurar veterinário imediatamente")
    elif gravidade == "MODERADO":
        st.warning("MODERADO - atenção e avaliação recomendada")
    else:
        st.success("LEVE - observar evolução")

    # ❓ Perguntas clínicas
    st.subheader("❓ Perguntas adicionais:")
    st.write("- Há quanto tempo começaram os sintomas?")
    st.write("- O animal está letárgico?")
    st.write("- A gengiva está pálida?")
    st.write("- Há presença de sangue nas fezes ou vômito?")
    st.write("- Está bebendo água normalmente?")

    # 📋 Recomendações
    st.subheader("📋 Recomendações:")
    st.write("- Manter em observação")
    st.write("- Avaliar hidratação")
    st.write("- Considerar exames laboratoriais (sangue, fezes)")
    st.write("- Em casos graves, buscar atendimento imediato")

    # 💬 PERGUNTA DO VETERIN
    
