def analisar(texto):

    texto = texto.lower()

    # 🔍 NORMALIZAÇÃO SIMPLES
    if "vomitando" in texto:
        texto += " vomito"
    if "não come" in texto or "sem comer" in texto:
        texto += " anorexia"
    if "fraco" in texto:
        texto += " fraqueza"

    # 🔴 EMERGÊNCIAS (PRIORIDADE MÁXIMA)

    if "sangue" in texto and "vomito" in texto:
        return {
            "diagnostico": ["Hemorragia digestiva", "Úlcera grave", "Intoxicação"],
            "nivel": "grave",
            "explicacao": "Sangue no vômito indica possível lesão grave no trato gastrointestinal.",
            "recomendacao": "🚨 Procurar atendimento veterinário imediatamente."
        }

    if "dificuldade para urinar" in texto or ("urinar" in texto and "não consegue" in texto):
        return {
            "diagnostico": ["Obstrução urinária"],
            "nivel": "grave",
            "explicacao": "A dificuldade para urinar pode indicar obstrução, especialmente perigosa em gatos.",
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

    # 🟠 MODERADOS

    if "vomito" in texto and "diarreia" in texto:
        return {
            "diagnostico": ["Gastroenterite", "Infecção intestinal"],
            "nivel": "moderado",
            "explicacao": "Vômito associado à diarreia indica inflamação gastrointestinal.",
            "recomendacao": "Manter hidratação e observar evolução."
        }

    if "vomito" in texto:
        return {
            "diagnostico": ["Gastrite", "Irritação gastrointestinal"],
            "nivel": "moderado",
            "explicacao": "O vômito pode estar relacionado a inflamação do estômago.",
            "recomendacao": "Observar frequência e manter hidratação."
        }

    if "diarreia" in texto:
        return {
            "diagnostico": ["Enterite", "Infecção intestinal leve"],
            "nivel": "moderado",
            "explicacao": "Diarreia indica alteração intestinal.",
            "recomendacao": "Monitorar evolução e hidratação."
        }

    if "tosse" in texto or "espirro" in texto:
        return {
            "diagnostico": ["Doença respiratória"],
            "nivel": "moderado",
            "explicacao": "Sintomas respiratórios indicam possível infecção ou irritação.",
            "recomendacao": "Monitorar e procurar avaliação se piorar."
        }

    # 🟢 LEVES

    if "coceira" in texto or "pele" in texto:
        return {
            "diagnostico": ["Alergia", "Dermatite"],
            "nivel": "leve",
            "explicacao": "Sintomas compatíveis com alteração dermatológica.",
            "recomendacao": "Observar evolução e evitar automedicação."
        }

    # ⚪ GERAL

    if "fraqueza" in texto or "apatia" in texto or "anorexia" in texto:
        return {
            "diagnostico": ["Doença sistêmica"],
            "nivel": "moderado",
            "explicacao": "Os sinais indicam comprometimento geral do organismo.",
            "recomendacao": "Recomenda-se avaliação clínica."
        }

    # 🔘 FALLBACK FINAL

    return {
        "diagnostico": ["Quadro inespecífico"],
        "nivel": "leve",
        "explicacao": "Os sintomas não permitem uma hipótese clara.",
        "recomendacao": "Recomenda-se avaliação veterinária."
    }
