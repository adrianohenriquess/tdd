from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        #given
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        #when
        resultado = funcionario_teste.idade()
        #then
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Adriano_Henrique_deve_retornar_Henrique(self):
        entrada = ' Adriano Henrique '
        esperado = 'Henrique'
        funcionario_teste = Funcionario(entrada, '20/06/1988', 1111)
        resultado = funcionario_teste.sobre_nome()
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
        funcionario_teste = Funcionario(entrada_nome, '20/06/1988', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100
        funcionario_teste = Funcionario('teste', '20/06/1988', entrada)
        resultado = funcionario_teste.calcular_bonus()
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000
            funcionario_teste = Funcionario('teste', '20/06/1988', entrada)
            resultado = funcionario_teste.calcular_bonus()
            assert resultado