import unittest
import mates.mates as mates
class TestMates(unittest.TestCase):
    def test_parell(self):
        self.assertTrue(mates.parell(4))
        self.assertTrue(mates.parell(2))
        self.assertFalse(mates.parell(3))
        self.assertFalse(mates.parell(-3))
        self.assertTrue(mates.parell(0))
        self.assertTrue(mates.parell(-4))
        self.assertEqual(mates.parell("AAAA"),"Entrada no vàlida")

    def test_quadrat(self):
        self.assertTrue(mates.quadrat(2))
        self.assertFalse(mates.quadrat(-2))
        self.assertTrue(mates.quadrat(0))
        self.assertEqual(mates.parell("AAAA"), "Entrada no vàlida")

    def test_cubic(self):
        self.assertTrue(mates.cubic(2))
        self.assertFalse(mates.cubic(-2))
        self.assertTrue(mates.cubic(0))
        self.assertEqual(mates.cubic("AAAA"), "Entrada no vàlida")

    def test_saluda(self):
        self.assertTrue(mates.saluda(str))
        self.assertFalse(mates.saluda(self != str))

    def test_aleatori(self):
        self.assertGreaterEqual(mates.aleatori(),1)
        self.assertLessEqual(mates.aleatori(),11)