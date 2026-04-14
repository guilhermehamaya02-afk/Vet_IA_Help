import streamlit as st

st.title("🐶 IA HelpVet")

st.write("Assistente de triagem veterinária")
st.warning("⚠️ Não substitui o médico veterinário")

nome = st.text_input("Nome do paciente")
idade = st.number_input("Idade", min_value=0)
peso = st.number_input("Peso (kg)", min_value=0.0)
dor = st.selectbox("Paciente sente dor?", ["Sim", "Não"])
comendo = st.selectbox("Paciente está se alimentando?", ["Sim", "Não"])
sintomas = st.text_area("Descreva os sintomas")

if st.button("Analisar"):

    sintomas_lower = sintomas.lower()
    possiveis = []
    gravidade = "Leve"

    if "sangue" in sintomas_lower:
        possiveis += ["Hemorragia interna", "Úlcera grave", "Intoxicação"]
        gravidade = "Grave"

    elif comendo == "Não":
        possiveis += ["Anorexia (sinal clínico importante)"]
        gravidade = "Moderado"

    if "vomito" in sintomas_lower or "vômito" in sintomas_lower:
        possiveis += ["Gastrite", "Infecção gastrointestinal"]

    if "diarreia" in sintomas_lower:
        possiveis += ["Infecção intestinal", "Parasitose"]

    if "fraqueza" in sintomas_lower:
        possiveis += ["Anemia", "Doença sistêmica"]

    if "febre" in sintomas_lower:
        possiveis += ["Processo infeccioso"]

    if dor == "Sim":
        possiveis += ["Processo inflamatório ou dor interna"]

    if not possiveis:
        possiveis = ["Quadro inespecífico - necessita avaliação clínica"]
        gravidade = "Moderado"

    possiveis = list(set(possiveis))

    st.subheader("🧠 Possíveis causas:")
    for p in possiveis:
        st.write(f"- {p}")

    st.subheader("⚠️ Nível de gravidade:")
    if gravidade == "Grave":
        st.error("GRAVE - procurar veterinário imediatamente")
    elif gravidade == "Moderado":
        st.warning("MODERADO - atenção e avaliação recomendada")
    else:
        st.success("LEVE - observar evolução")

    st.subheader("❓ Perguntas adicionais:")
    if "sangue" in sintomas_lower:
        st.write("- A gengiva está pálida?")
    if "diarreia" in sintomas_lower:
        st.write("- Há presença de muco ou sangue?")
    if "febre" in sintomas_lower:
        st.write("- Temperatura foi medida?")
    st.write("- O animal está letárgico?")
    st.write("- Há quanto tempo começaram os sintomas?")

    st.subheader("📋 Recomendações:")
    st.write("- Manter paciente em observação")
    st.write("- Avaliar hidratação")
    st.write("- Considerar exames laboratoriais")

    remedio = st.text_input("Deseja saber qual medicamento usar?")

    if remedio.lower() in ["sim", "quero", "medicamento"]:
        st.error("❌ Não posso recomendar medicamentos.")
        st.write("💡 O tratamento deve ser definido por um médico veterinário.")

    st.info("Procure um veterinário para avaliação completa.")
