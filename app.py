import streamlist as st

st.title("VetHelp IA - Assitente Veterinário")

st.markdown("""
Olá
Sou a *VetHelp*, uma assintente inteligente de triagem veterinária.

def analisar(texto):

    texto = texto.lower()

    diagnostico = []
    explicacao = ""
    recomendacao = ""

    # 🔴 CASOS PRIORITÁRIOS

    if "sangue" in texto and "vomito" in texto:
        diagnostico = ["Hemorragia digestiva", "Úlcera grave", "Intoxicação"]
        explicacao = "Presença de sangue no vômito indica possível lesão grave no trato gastrointestinal."
        recomendacao = "🚨 Procurar atendimento imediato."

    elif "vomito" in texto and "diarreia" in texto:
        diagnostico = ["Gastroenterite", "Infecção intestinal"]
        explicacao = "Os sinais indicam inflamação gastrointestinal, comum em infecções."
        recomendacao = "Manter hidratação e observar evolução."

    elif "dificuldade para urinar" in texto:
        diagnostico = ["Obstrução urinária"]
        explicacao = "A dificuldade para urinar pode indicar obstrução, especialmente grave em felinos."
        recomendacao = "🚨 Atendimento imediato."

    elif "convuls" in texto:
        diagnostico = ["Distúrbio neurológico"]
        explicacao = "Convulsões indicam alteração neurológica importante."
        recomendacao = "🚨 Emergência veterinária."

    elif "tosse" in texto:
        diagnostico = ["Doença respiratória"]
        explicacao = "Os sinais indicam possível comprometimento respiratório."
        recomendacao = "Monitorar evolução e procurar avaliação."

    elif "coceira" in texto:
        diagnostico = ["Alergia / dermatite"]
        explicacao = "Sintomas compatíveis com problema dermatológico."
        recomendacao = "Observar e evitar automedicação."

    else:
        diagnostico = ["Quadro inespecífico"]
        explicacao = "Os sinais não permitem uma hipótese clara."
        recomendacao = "Recomenda-se avaliação clínica."

    return diagnostico, explicacao, recomendacao
