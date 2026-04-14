from openai import OpenAI
client = OpenAI(api_key="SUA_CHAVE_AQUI")

st.title("🐶 IA HelpVet")

st.write("Olá, eu sou a IA HelpVet.")
st.warning("⚠️ Não substituo o veterinário.")

# Estado inicial
if "analisado" not in st.session_state:
    st.session_state.analisado = False

# Inputs principais
nome = st.text_input("Nome do paciente")
idade = st.number_input("Idade", min_value=0)
peso = st.number_input("Peso (kg)", min_value=0.0)
dor = st.selectbox("Paciente sente dor?", ["Sim", "Não"])
comendo = st.selectbox("Paciente está se alimentando?", ["Sim", "Não"])
sintomas = st.text_area("Descreva os sintomas")

# Botão principal
if st.button("Analisar"):
    st.session_state.analisado = True
    st.session_state.sintomas = sintomas
    st.session_state.comendo = comendo

# 🔍 MOSTRAR RESULTADO (sem resetar)
if st.session_state.analisado:

    st.subheader("📊 Análise inicial")

    sintomas_lower = st.session_state.sintomas.lower()
    possiveis = []

    if "sangue" in sintomas_lower or "vômito" in sintomas_lower:
        possiveis += [
            "Hemorragia interna / intoxicação",
            "Gastrite ou úlcera grave",
            "Parvovirose"
        ]

    if "diarreia" in sintomas_lower:
        possiveis += [
            "Infecção intestinal",
            "Parasitose"
        ]

    if "fraqueza" in sintomas_lower:
        possiveis += [
            "Anemia",
            "Doença sistêmica"
        ]

    if st.session_state.comendo == "Não":
        possiveis.append("Quadro preocupante (anorexia)")

    if not possiveis:
        possiveis.append("Quadro inespecífico — საჭირ avaliação clínica")

    st.write("### 🧠 Possíveis diagnósticos:")
    for p in possiveis:
        st.write(f"- {p}")

    # 👇 AGORA NÃO SOME MAIS
    mais = st.text_input("Paciente apresenta mais algum sintoma?", key="mais")

    if mais:
        if "diarreia" in mais.lower():
            st.write("➡️ Pode reforçar suspeita de infecção intestinal ou parasitose")

        if "febre" in mais.lower():
            st.write("➡️ Pode indicar processo infeccioso")

    st.write("### 🔎 Avaliação clínica:")
    st.write("- Monitorar estado geral")
    st.write("- Verificar gengiva")
    st.write("- Considerar exames")

    # 👇 PERGUNTA CORRETA SOBRE REMÉDIO
    remedio = st.text_input("Deseja saber qual medicamento usar?", key="remedio")

    if remedio:
        st.error("❌ Não posso recomendar medicamentos.")
        st.write("💡 O tratamento deve ser definido por um médico veterinário.")

    st.success("Análise concluída.")
