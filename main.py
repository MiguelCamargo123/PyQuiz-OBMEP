import json
import random


class Quiz:
    def __init__(self):
        self.questoes = []
        self.historico = []
        self.acertos = 0
        self.erros = 0
        self.perguntas_feitas = 0
        self._carregar_questoes()
        self._carregar_historico()

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
        questao = random.sample(lista_filtrada)
        print(f'A pergunta é a seguinte: {questao["pergunta"]}')
        return questao

    def verificar_acerto(self, questao, resposta_pessoa):
        with open('answers.json', 'r', encoding='utf-8') as re:
            resposta = json.load(re)

        for r in resposta:
            if r['id'] == questao['id']:
                if resposta_pessoa == r['resposta']:
                    print('Parabens, você acertou a questão!')
                    self.acertos += 1
                else:
                    print('Infelizmente, você errou a questão')
                    self.erros += 1
                break
            self.perguntas_feitas += 1

    def _carregar_historico(self):
        try:
            with open('historico.json', 'r', encoding='utf=8') as his:
                self.historico = json.load(his)
        except FileNotFoundError:
            self.historico = []

    def _criar_historico(self):
        self.historico.append(
            {
                'Acertos': self.acertos,
                'Erros': self.erros,
                'Questões feitas': self.perguntas_feitas,
            }
        )

        with open('historico.json', 'w', encoding='utf-8') as his:
            json.dump(self.historico, his, ensure_ascii=False, indent=4)


def main():
    perguntas = Quiz()
    while True:
        print(
            'Seja bem vindo ao treinamento da OBMEP, criado por Miguel Camargo, feito para estudantes que querem ir bem na OBMEP'
        )

        print(
            'Antes de começarmos, você deve digitar a dificuldade do teste, após essa mensagem, aparecerá uma pergunta para você escolher a dificuldade das questões'
        )

        try:
            dificuldade = int(
                input(
                    'Digite a dificuldade das perguntas que você quer receber (digite 1, 2) '
                )
            )
            filtradas = perguntas._dificuldade_questoes(dificuldade)
        except ValueError:
            print('Por favor, digite um número dos falados a cima, não um texto')

        questao = perguntas._mostrar_questoes(filtradas)

        resposta = int(input('Digite a resposta da pergunta acima: '))

        perguntas.verificar_acerto(questao, resposta)
