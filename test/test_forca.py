import unittest
from unittest.mock import patch
import forca

class TestForca(unittest.TestCase):


    # ----------Testes Escolher Dificuldade -----------------

    # simula o input '1' do usuario
    @patch('builtins.input', side_effect=['1'])
    def test_escolherDificuldade_facil(self, mock_input):
        self.assertEqual(forca.escolherDificuldade(), 120)

    # simula o input '2' do usuario
    @patch('builtins.input', side_effect=['2'])
    def test_escolherDificuldade_medio(self, mock_input):
        self.assertEqual(forca.escolherDificuldade(), 60)

    # simula o input '3' do usuario
    @patch('builtins.input', side_effect=['3'])
    def test_escolherDificuldade_dificil(self, mock_input):
        self.assertEqual(forca.escolherDificuldade(), 40)

    # simula o input '4' do usuario
    @patch('builtins.input', side_effect=['4'])
    def test_escolherDificuldade_invalido(self, mock_input):
        self.assertEqual(forca.escolherDificuldade(), 60)

    # ------------------------------------------------------

    def test_verificacao_acerto(self):
        # Simular as variáveis globais usadas na função
        forca.sorteada = "teste"
        forca.partesSorteada = list(forca.sorteada)
        forca.partesUpper = [letra.upper() for letra in forca.partesSorteada]
        forca.partesAtual = list('_' * len(forca.sorteada))
        
        forca.verificacao_acerto('T')
        self.assertEqual(forca.partesAtual[0] and forca.partesAtual[3], 'T')

        forca.verificacao_acerto('E')
        self.assertEqual(forca.partesAtual[1], 'E')


    def test_verificacao_erro(self):

        forca.sorteada = "abacaxi"
        forca.partesSorteada = list(forca.sorteada)
        forca.partesUpper = [letra.upper() for letra in forca.partesSorteada]
        
        self.assertTrue(forca.verificacao_erro('z'))
        self.assertFalse(forca.verificacao_erro('a'))


    def test_verificacao_vitoria(self):

        forca.partesUpper = ['T','E','S','T','E']
        forca.partesAtual = ['T','E','S','T','E']
        self.assertTrue(forca.verificacao_vitoria())
        forca.partesAtual = ['E','R','R','O']
        self.assertFalse(forca.verificacao_vitoria())

if __name__ == '__main__':
    unittest.main()