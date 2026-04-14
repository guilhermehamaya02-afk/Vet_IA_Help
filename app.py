Mensagem_Inicial = print("Olá, eu sou a IA helpvet, estou aqui para auxliar em diagnósticos, responda as perguntas para começarmos.")
Mensagem_Inicial = print("Ps: Não fui criada para definir diagnóstico e sim para auxiliar.Fica a critério do clínoco o diagnóstico")

Nome = input("Nome do paciente - ")
Idade = int( input("Idade - ") )
Peso = float( input("Peso - ") )
Dor = input("Paciente sente dor? - ")
Comendo = input("Paciente está se alimentando? - ")
Sintomas = input("Sintomas do paciente - ")

print(Nome)
print(type(Idade))
print(type(Peso))
print(Dor)
print(Comendo)
print(Sintomas)

Realizar_Diagnóstico = print("Paciente apresentando sangue em vômito (Hematêmese) e fraqueza, fortes indícios de Hemorragia interna/Intoxicação; Gastrite ou Úlcera GRAVE; Parvoviróse. Paciente se encontra com mais algum sintoma?")

Duvida = input("Quais?")

print(Duvida)

Conclusão = print("Fortes indícios de Gastríte/Úlcera hemorrágica. Recomenda-se investigar se: Gengíva estiver pálida; Vômitos em repetição. Deixar paciente em observação com reposição de soro fisiológico, realizar exames de sangue e fezes + ultrassom ")

Dúvida_Vet= input("Algo mais?")

print(Dúvida_Vet)

Conclusão_final = print("Não posso recomendar remédios e conclusões. Lembrando que conclusão de diagnóstico fica a críterio do clínico.")
Conclusão_final = print("Ajudo em algo mais?")
