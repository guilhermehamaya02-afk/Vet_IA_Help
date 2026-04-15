import streamlit as st

# 🧠 Título
st.title("🐶 VetHelp IA - Triagem Veterinária")

st.write("Descreva os sintomas do paciente para análise.")

# 🔍 Função de análise
def analisar(texto):

    texto = texto.lower()

    # 🔍 NORMALIZAÇÃO
    if "vomitando" in texto:
        texto += " vomito"
    if "não come" in texto or "sem comer" in texto:
        texto += " anorexia"
    if "fraco" in texto:
        texto += " fraqueza"

    # 🔴 EMERGÊNCIAS
    if "sangue" in texto and "vomito" in texto:
        return {
            "diagnostico": ["Hemorragia digestiva", "Úlcera grave", "Intoxicação"],
            "nivel": "grave",
            "explicacao": "Sangue no vômito indica possível lesão grave no trato gastrointestinal.",
            "recomendacao": "🚨 Procurar atendimento veterinário imediatamente."
        }

    if "dificuldade para urinar" in texto:
        return {
            "diagnostico": ["Obstrução urinária"],
            "nivel": "grave",
            "explicacao": "Dificuldade para urinar pode indicar obstrução, especialmente perigosa em gatos.",
            "recomendacao": "🚨 Emergência veterinária imediata."
        }

    if "convuls" in texto or "tremor" in texto:
        return {
            "diagnostico": ["Distúrbio neurológico", "Possível intoxicação"],
            "nivel": "grave",
            "explicacao": "Convulsões ou tremores indicam alteração neurológica importante.",
            "recomendacao": "🚨 Atendimento veterinário urgente."
        }

    if "falta de ar" in texto or "dispneia" in texto:
        return {
            "diagnostico": ["Emergência respiratória"],
            "nivel": "grave",
            "explicacao": "Dificuldade respiratória pode indicar condição grave.",
            "recomendacao": "🚨 Atendimento imediato."
        }

    # 🟠 MODERADO
    if "vomito" in texto and "diarreia" in texto:
        return {
            "diagnostico": ["Gastroenterite", "Infecção intestinal"],
            "nivel": "moderado",
            "explicacao": "Vômito + diarreia indicam inflamação gastrointestinal.",
            "recomendacao": "Manter hidratação e observar evolução."
        }

    if "vomito" in texto:
        return {
            "diagnostico": ["Gastrite"],
            "nivel": "moderado",
            "explicacao": "O vômito pode estar ligado a inflamação do estômago.",
            "recomendacao": "Observar frequência e hidratação."
        }

    if "diarreia" in texto:
        return {
            "diagnostico": ["Enterite"],
            "nivel": "moderado",
            "explicacao": "Diarreia indica alteração intestinal.",
            "recomendacao": "Monitorar evolução."
        }

    if "tosse" in texto or "espirro" in texto:
        return {
            "diagnostico": ["Doença respiratória"],
            "nivel": "moderado",
            "explicacao": "Sintomas respiratórios indicam possível infecção.",
            "recomendacao": "Observar e procurar avaliação se piorar."
        }

    # 🟢 LEVE
    if "coceira" in texto:
        return {
            "diagnostico": ["Alergia / Dermatite"],
            "nivel": "leve",
            "explicacao": "Sintomas de pele geralmente indicam alergia.",
            "recomendacao": "Observar evolução."
        }

    # ⚪ GERAL
    if "fraqueza" in texto or "apatia" in texto or "anorexia" in texto:
        return {
            "diagnostico": ["Doença sistêmica"],
            "nivel": "moderado",
            "explicacao": "Indica comprometimento geral do organismo.",
            "recomendacao": "Recomenda-se avaliação clínica."
        }

    return {
        "diagnostico": ["Quadro inespecífico"],
        "nivel": "leve",
        "explicacao": "Os sintomas não permitem diagnóstico claro.",
        "recomendacao": "Procure um veterinário."
    }


# 📥 Input
sintomas = st.text_input("Digite os sintomas")

# ▶️ Botão
if st.button("Analisar"):

    if sintomas.strip() == "":
        st.warning("Digite os sintomas primeiro.")
    else:
        resultado = analisar(sintomas)

        st.subheader("🧠 Diagnóstico sugerido")
        for d in resultado["diagnostico"]:
            st.write(f"- {d}")

        st.subheader("📊 Nível")
        st.write(resultado["nivel"])

        st.subheader("🧠 Explicação")
        st.write(resultado["explicacao"])

        st.subheader("📋 Recomendação")
        st.write(resultado["recomendacao"])

        st.info("⚠️ Esta é uma triagem, não substitui o veterinário.")
