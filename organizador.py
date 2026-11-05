MINUTOS_POR_HORA = 60
LARGURA_SEPARADOR = 30

materia = input("Matéria: ")
minutos_estudados = int(input("Minutos estudados: "))
questoes_feitas = int(input("Questões feitas: "))
questoes_acertadas = int(input("Questões acertadas: "))

horas = minutos_estudados // MINUTOS_POR_HORA
minutos_restantes = minutos_estudados % MINUTOS_POR_HORA

taxa_de_acerto = (questoes_acertadas / questoes_feitas) * 100

separador = "=" * LARGURA_SEPARADOR

print(separador)
print("Resumo da sessão")
print(separador)
print(f"Matéria: {materia}")
print(f"Tempo: {horas}h{minutos_restantes:02d}")  # Sem o zero, 125 minutos apareceria como 2h 5, que parece um erro.
print(f"Acertos: {questoes_acertadas} de {questoes_feitas} ({taxa_de_acerto:.1f}%)")