from django.test import TestCase

class Programa:

    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme('Vingadores', 2023, 160)
print(vingadores.nome)

