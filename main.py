import json
import random


class Quiz:
    def __init__(self):
        self.questoes = []
        self.acertos = 0
        self.erros = 0
        self._carregar_questoes()

    def _carregar_questoes(self):
        with open('questions.json', 'r', encoding='utf-8') as f:
            pergunta = json.load(f)
            self.questoes.extend(pergunta)

    def _dificuldade_questoes(self, dificuldade):
        filtradas = []
        for q in self.questoes:
            if q['dificuldade'] == dificuldade:
                filtradas.append(q)
        return filtradas

    def _mostrar_questoes(self, lista_filtrada):
        questao = random.choice(lista_filtrada)
        print(f'A pergunta é a seguinte: {questao["pergunta"]}')
        return questao

    def verificar_acerto(self, questao, resposta_pessoa):
        with open('answers.json', 'r', encoding='utf-8') as re:
            resposta = json.load(re)

        for r in resposta:
            if r['id'] == questao['id']:
                if resposta_pessoa == r['resposta']:
                    print('Parabens, você acertou a questão!')
                else:
                    print('Infelizmente, você errou a questão')
                break
