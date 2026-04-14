import streamlit as st

st.title("🐶 VetHelp IA")

st.markdown("""
Olá 👋  
Sou a **VetHelp**, uma assistente virtual de triagem veterinária.

Estou aqui para te ajudar na avaliação inicial do paciente 🐾  
Descreva os sinais clínicos para começarmos.
""")

st.info("⚠️ Esta ferramenta auxilia na triagem e não substitui o médico veterinário.")

# 🔒 Estado
if "analisado" not in st.session_state:
    st.session_state.analisado = False
if "sintomas_total" not in st.session_state:
    st.session_state.sintomas_total = ""

# 📥 Dados
nome = st.text_input("Nome do paciente")
especie = st.selectbox("Espécie", ["Cachorro", "Gato"])
idade = st.number_input("Idade", min_value=0)
peso = st.number_input("Peso (kg)", min_value=0.0)

tempo = st.selectbox("Tempo dos sinais", ["Hoje", "1-2 dias", "3+ dias"])
intensidade = st.selectbox("Intensidade percebida", ["Leve", "Moderado", "Intenso"])

dor = st.selectbox("Paciente apresenta dor?", ["Sim", "Não"])
comendo = st.selectbox("Está se alimentando normalmente?", ["Sim", "Não"])

sintomas = st.text_area("Descreva os sinais observados")

# ▶️ Botão
if st.button("Iniciar análise"):
    st.session_state.analisado = True
    st.session_state.sintomas_total = sintomas

# 🔍 Função
def analisar(texto):

    texto = texto.lower()
    possiveis = set()
    score = 0

    # Combinações
    if "vomito" in texto and "diarreia" in texto:
        possiveis.add("Gastroenterite")
        score += 3

    if "sangue" in texto and "fraqueza" in texto:
        possiveis.add("Hemorragia interna")
        score += 4

    if "tosse" in texto and "cansaço" in texto:
        possiveis.add("Alteração cardíaca ou respiratória")
        score += 3

    # Graves
    if "convuls" in texto:
        possiveis.add("Distúrbio neurológico")
        score += 4

    if "sangue" in texto:
        possiveis.add("Úlcera ou intoxicação")
        score += 3

    # Moderados
    if "vomito" in texto or "vômito" in texto:
        possiveis.add("Gastrite")
        score += 2

    if "diarreia" in texto:
        possiveis.add("Infecção intestinal ou parasitose")
        score += 2

    if "febre" in texto:
        possiveis.add("Processo infeccioso")
        score += 2

    if "tosse" in texto:
        possiveis.add("Doença respiratória")
        score += 2

    # Leves
    if "coceira" in texto:
        possiveis.add("Dermatite ou alergia")
        score += 1

    if "queda de pelo" in texto:
        possiveis.add("Alteração dermatológica")
        score += 1

    return possiveis, score

# 🔍 Execução
if st.session_state.analisado:

    st.write("🔎 Analisando os dados informados...")

    texto_total = st.session_state.sintomas_total

    possiveis, score = analisar(texto_total)

    # Ajustes clínicos
    if comendo == "Não":
        possiveis.add("Anorexia (sinal clínico relevante)")
        score += 2

    if dor == "Sim":
        possiveis.add("Possível processo inflamatório")
        score += 1

    if especie == "Gato" and "vomito" in texto_total.lower():
        possiveis.add("Em felinos, vômitos podem ocorrer com maior frequência — avaliar padrão")

    if idade < 1:
        possiveis.add("Paciente jovem — maior risco de doenças infecciosas")
        score += 1

    if idade > 8:
        possiveis.add("Paciente idoso — considerar doenças crônicas")
        score += 1

    if tempo == "3+ dias":
        score += 2

    if intensidade == "Intenso":
        score += 3
    elif intensidade == "Moderado":
        score += 2

    if not possiveis:
        possiveis.add("Quadro inespecífico — recomenda-se avaliação clínica detalhada")

    # Gravidade
    if score >= 7:
        nivel = "grave"
    elif score >= 4:
        nivel = "moderado"
    else:
        nivel = "leve"

    # Resultado
    st.subheader("🧠 Análise inicial")

    st.write("Com base nas informações fornecidas, identifiquei algumas possibilidades clínicas:")

    for p in possiveis:
        st.write(f"- {p}")

    st.subheader("⚠️ Avaliação de gravidade")

    if nivel == "grave":
        st.error("🚨 O quadro apresenta sinais de maior gravidade. Recomenda-se atendimento veterinário imediato.")
    elif nivel == "moderado":
        st.warning("⚠️ O quadro requer atenção e avaliação clínica.")
    else:
        st.success("🟢 No momento, os sinais indicam um quadro mais leve, porém deve ser monitorado.")

    # Frase inteligente
    st.subheader("📊 Interpretação geral")

    st.write(f"O conjunto dos sinais sugere um quadro clínico **{nivel}**, considerando a associação dos sintomas apresentados.")

    # Recomendações
    st.subheader("📋 Recomendações iniciais")

    st.write("- Monitorar a evolução do paciente")
    st.write("- Observar alterações no comportamento")
    st.write("- Avaliar ingestão de água e alimentação")
    st.write("- Considerar exames laboratoriais, se necessário")

    # Atualização
    st.subheader("🔄 Atualizar com novos sinais")

    mais = st.text_input("Deseja acrescentar mais algum sintoma?")

    if mais:
        st.write("🔄 Atualizando análise com as novas informações...")
        st.session_state.sintomas_total += " " + mais

        novos, _ = analisar(st.session_state.sintomas_total)

        st.write("🧠 Nova análise considerando todos os sinais:")
        for n in novos:
            st.write(f"- {n}")

    # Pergunta
    st.subheader("💬 Conversar com a VetHelp")

    pergunta = st.text_input("Digite sua pergunta:")

    if pergunta:
        if any(p in pergunta.lower() for p in ["remedio", "remédio", "medicamento", "dose"]):
            st.error("❌ Como assistente de triagem, não posso recomendar medicamentos.")
            st.write("💡 A conduta terapêutica deve ser definida por um médico veterinário.")
        else:
            st.write("🧠 Essa é uma pergunta relevante para a avaliação clínica.")
            st.write("Recomenda-se considerar o contexto completo do paciente.")

    st.info("Para um diagnóstico definitivo, procure um médico veterinário.")