import json

with open('questions.json', 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

with open('answers.json', 'r', encoding='utf-8') as f:
    respostas = json.load(f)


while True:
    enunciado = input('Digite o enunciado: ')
    dificuldade = int(input('Digite a dificuldade (1 = 6/7, 2 = 8/9, 3 = em) '))

    id_perguntas = len(perguntas) + 1

    respostas_das_perguntas = input('Digite a resposta das perguntas: ')
    id_respostas = len(respostas) + 1

    perguntas.append(
        {'id': id_perguntas, 'pergunta': enunciado, 'dificuldade': dificuldade}
    )

    respostas.append({'id': id_respostas, 'resposta': respostas_das_perguntas})

    with open('questions.json', 'w', encoding='utf-8') as q:
        json.dump(perguntas, q, ensure_ascii=False, indent=4)

    with open('answers.json', 'w', encoding='utf-8') as a:
        json.dump(respostas, a, ensure_ascii=False, indent=4)

    termino = input('Voce quer continuar adicionando coisas? (s/n) ').upper()

    if termino != 'S':
        break
