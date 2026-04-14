import streamlit as st

st.title("🐶 IA HelpVet")

st.write("Olá, eu sou a IA HelpVet, estou aqui para auxiliar em diagnósticos.")
st.warning("⚠️ Não substituo o veterinário. O diagnóstico final é do clínico.")

# Inputs
nome = st.text_input("Nome do paciente")
idade = st.number_input("Idade", min_value=0)
peso = st.number_input("Peso (kg)", min_value=0.0)
dor = st.selectbox("Paciente sente dor?", ["Sim", "Não"])
comendo = st.selectbox("Paciente está se alimentando?", ["Sim", "Não"])
sintomas = st.text_area("Descreva os sintomas")

if st.button("Analisar"):

    st.subheader("📊 Análise inicial")

    sintomas_lower = sintomas.lower()

    # Diagnóstico base
    possiveis = []

    if "sangue" in sintomas_lower or "vômito" in sintomas_lower:
        possiveis.append("Hemorragia interna / intoxicação")
        possiveis.append("Gastrite ou úlcera grave")
        possiveis.append("Parvovirose")

    if "diarreia" in sintomas_lower:
        possiveis.append("Infecção intestinal")
        possiveis.append("Parasitose")

    if "fraqueza" in sintomas_lower:
        possiveis.append("Anemia")
        possiveis.append("Doença sistêmica")

    if comendo == "Não":
        possiveis.append("Quadro clínico preocupante (anorexia)")

    # Se não detectou nada específico
    if not possiveis:
        possiveis.append("Quadro inespecífico — საჭირ análise clínica detalhada")

    # Mostrar hipóteses
    st.write("### 🧠 Possíveis diagnósticos:")
    for p in possiveis:
        st.write(f"- {p}")

    # Pergunta adicional
    mais = st.text_input("Paciente apresenta mais sintomas?")

    if mais:
        st.write("📌 Informação adicional registrada.")

    # Simulação de raciocínio clínico
    st.write("### 🔎 Avaliação:")
    st.write("Paciente deve ser monitorado e avaliado com exames complementares.")
    st.write("Verificar:")
    st.write("- Gengiva (cor)")
    st.write("- Frequência de vômitos/diarreia")
    st.write("- Estado de hidratação")

    # Pergunta sobre medicamento
    remedio = st.text_input("Deseja saber sobre medicação?")

    if remedio:
        st.error("❌ Não posso recomendar medicamentos.")
        st.write("💡 O tratamento deve ser definido por um médico veterinário.")

    st.success("Análise concluída.")
