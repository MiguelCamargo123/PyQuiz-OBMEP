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
                    self.acertos += 1
                    break
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

        print()
        print(
            'Antes de começarmos, você deve digitar a dificuldade do teste, após essa mensagem, aparecerá uma pergunta para você escolher a dificuldade das questões'
        )

        print()
        try:
            dificuldade = int(
                input(
                    'Digite a dificuldade das perguntas que você quer receber (digite 1 ou 2) '
                )
            )
            filtradas = perguntas._dificuldade_questoes(dificuldade)
        except ValueError:
            print()
            print('Por favor, digite um número dos falados a cima, não um texto')

        print()
        questao = perguntas._mostrar_questoes(filtradas)

        print()
        resposta = input('Digite a resposta da pergunta acima: ')

        print()
        perguntas.verificar_acerto(questao, resposta)

        print()
        deseja_sair = input(
            'Você deseja sair do sistema? Se sim, digite S, caso contrario, digite N '
        ).upper()

        print()
        if deseja_sair == 'S':
            perguntas._criar_historico()
            print('Obrigado por entrar e usar meu sistema!!')
            break


if __name__ == '__main__':
    main()
