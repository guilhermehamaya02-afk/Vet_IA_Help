import streamlit as st

# Título
st.title("🐶 IA HelpVet")

# Mensagem inicial
st.write("Olá, eu sou a IA HelpVet, estou aqui para auxiliar em diagnósticos.")
st.warning("⚠️ Não fui criada para definir diagnóstico, apenas auxiliar. A decisão final é do médico veterinário.")

# Inputs
nome = st.text_input("Nome do paciente")
idade = st.number_input("Idade", min_value=0)
peso = st.number_input("Peso (kg)", min_value=0.0)
dor = st.selectbox("Paciente sente dor?", ["Sim", "Não"])
comendo = st.selectbox("Paciente está se alimentando?", ["Sim", "Não"])
sintomas = st.text_area("Descreva os sintomas")

# Botão
if st.button("Analisar"):

    st.subheader("📋 Dados do paciente")
    st.write(f"Nome: {nome}")
    st.write(f"Idade: {idade}")
    st.write(f"Peso: {peso} kg")
    st.write(f"Dor: {dor}")
    st.write(f"Alimentação: {comendo}")
    st.write(f"Sintomas: {sintomas}")

    # Lógica simples
    if "sangue" in sintomas.lower() or "vômito" in sintomas.lower():
        st.error("🚨 Possível caso grave!")
        st.write("Possíveis causas:")
        st.write("- Hemorragia interna / intoxicação")
        st.write("- Gastrite ou úlcera grave")
        st.write("- Parvovirose")

        duvida = st.text_input("Paciente apresenta mais algum sintoma? Quais?")
        
        if duvida:
            st.write(f"Sintomas adicionais: {duvida}")

        st.warning("Recomenda-se investigar:")
        st.write("- Gengiva pálida")
        st.write("- Vômitos frequentes")
        st.write("- Exames de sangue, fezes e ultrassom")

    else:
        st.success("Caso aparentemente não crítico, mas requer avaliação clínica.")

    # Final
    duvida_vet = st.text_input("Algo mais que deseja informar?")

    if duvida_vet:
        st.write(f"Informação adicional: {duvida_vet}")

    st.info("Não posso recomendar medicamentos. O diagnóstico final é do veterinário.")
