
#3: O que são marcas no Pytest?

#   Marks é um auxiliar com o qual você pode facilmente definir metadados em suas funções de teste, alguns marcadores embutidos, por exemplo:

#   skip - sempre pule uma função de teste
#   xfail - produzir um resultado de “falha esperada” se uma determinada condição for atendida
#   Exemplo de marcas usadas:

import pytest



@pytest.mark.xfail
def test_some_magic_test():
    pass


@pytest.mark.skip
def test_old_functional():
    pass

#   Markscomo criar marcas personalizadas para Pytest?

#   Marks A única maneira é registrar suas marcas no pytest.iniarquivo:

# [pytest]
# markers =
#    slow: marks tests as slow
#    serial




# Q6: O que é Parametrizar no Pytest?

# `Parametrize` é uma marca embutida e um dos recursos matadores do pytest. Com esta marca, você pode realizar várias chamadas para a mesma função de teste.

# Exemplo de simples parametrizeem teste:

@pytest.mark.parametrize(
   'text_input, result', [('5+5', 10), ('1+4', 5)]
)
def test_sum(text_input, result):
   assert eval(text_input) == result