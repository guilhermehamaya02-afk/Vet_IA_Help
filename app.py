import streamlit as st

st.title("🐶 IA HelpVet - Triagem Veterinária")
st.warning("⚠️ Não substitui o médico veterinário")

# 🔒 Estado
if "analisado" not in st.session_state:
    st.session_state.analisado = False
if "sintomas_total" not in st.session_state:
    st.session_state.sintomas_total = ""

# 📥 Inputs
nome = st.text_input("Nome do paciente")
idade = st.number_input("Idade", min_value=0)
peso = st.number_input("Peso (kg)", min_value=0.0)
dor = st.selectbox("Paciente sente dor?", ["Sim", "Não"])
comendo = st.selectbox("Paciente está se alimentando?", ["Sim", "Não"])
sintomas = st.text_area("Descreva os sintomas iniciais")

# ▶️ Botão
if st.button("Analisar"):
    st.session_state.analisado = True
    st.session_state.sintomas_total = sintomas

# 🔍 FUNÇÃO DE ANÁLISE
def analisar(sintomas_texto, dor, comendo):
    sintomas_lower = sintomas_texto.lower()
    possiveis = set()

    if "sangue" in sintomas_lower:
        possiveis.update([
            "Hemorragia interna",
            "Úlcera hemorrágica",
            "Intoxicação",
            "Parvovirose"
        ])

    if "vomito" in sintomas_lower or "vômito" in sintomas_lower:
        possiveis.update([
            "Gastrite",
            "Infecção gastrointestinal"
        ])

    if "diarreia" in sintomas_lower:
        possiveis.update([
            "Parasitose",
            "Infecção intestinal"
        ])

    if "fraqueza" in sintomas_lower:
        possiveis.update([
            "Anemia",
            "Doença sistêmica"
        ])

    if "febre" in sintomas_lower:
        possiveis.update([
            "Infecção"
        ])

    if comendo == "Não":
        possiveis.add("Anorexia (quadro preocupante)")

    if dor == "Sim":
        possiveis.add("Processo inflamatório")

    if not possiveis:
        possiveis.add("Quadro inespecífico - necessita avaliação clínica")

    return possiveis

# 🔍 ANÁLISE PRINCIPAL
if st.session_state.analisado:

    possiveis = analisar(
        st.session_state.sintomas_total,
        dor,
        comendo
    )

    st.subheader("🧠 Possíveis causas:")
    for p in possiveis:
        st.write(f"- {p}")

    st.subheader("📋 Recomendações:")
    st.write("- Manter em observação")
    st.write("- Avaliar hidratação")
    st.write("- Considerar exames laboratoriais")

    # 🔄 MAIS SINTOMAS (AGORA SOMA)
    st.subheader("🔄 O paciente apresenta mais algum sintoma?")
    mais = st.text_input("Se sim, descreva:")

    if mais:
        st.session_state.sintomas_total += " " + mais

        novos_resultados = analisar(
            st.session_state.sintomas_total,
            dor,
            comendo
        )

        st.subheader("🧠 Atualização da análise:")
        for n in novos_resultados:
            st.write(f"- {n}")

    # 💬 Pergunta livre
    st.subheader("💬 Pergunta ao sistema")
    pergunta = st.text_input("Digite sua pergunta:")

    if pergunta:
        pergunta_lower = pergunta.lower()

        if any(p in pergunta_lower for p in [
            "remedio", "remédio", "medicamento", "dose", "tratamento"
        ]):
            st.error("❌ Não posso recomendar medicamentos.")
            st.write("💡 Fui criada apenas para auxiliar no diagnóstico.")
            st.write("⚠️ A decisão final é do médico veterinário.")

        else:
            st.write("🧠 Pergunta relevante para avaliação clínica.")
            st.write("Considere o quadro completo do paciente.")

    st.info("Procure um veterinário para avaliação completa.")
