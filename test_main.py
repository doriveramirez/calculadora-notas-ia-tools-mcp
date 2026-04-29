import unittest

from main import determine_result, parse_grade
from tools_notas import calcular_media, calcular_mediana, validar_notas


class TestToolsNotas(unittest.TestCase):
    def test_calcular_media(self):
        self.assertAlmostEqual(calcular_media([5, 5, 5]), 5.0)
        self.assertAlmostEqual(calcular_media([10, 8, 9]), 9.0)

    def test_calcular_mediana(self):
        self.assertEqual(calcular_mediana([2, 10, 4]), 4)
        self.assertEqual(calcular_mediana([9, 3, 7]), 7)

    def test_validar_notas_requires_list(self):
        with self.assertRaises(ValueError):
            validar_notas((5, 5, 5))

    def test_validar_notas_requires_three_values(self):
        with self.assertRaises(ValueError):
            validar_notas([5, 5])

    def test_parse_grade_valid(self):
        self.assertEqual(parse_grade("0"), 0.0)
        self.assertEqual(parse_grade("10"), 10.0)
        self.assertAlmostEqual(parse_grade("7.5"), 7.5)

    def test_parse_grade_invalid(self):
        with self.assertRaises(ValueError):
            parse_grade("abc")
        with self.assertRaises(ValueError):
            parse_grade("-1")
        with self.assertRaises(ValueError):
            parse_grade("11")

    def test_determine_result(self):
        self.assertEqual(determine_result(5.0), "Aprobado")
        self.assertEqual(determine_result(4.99), "Suspenso")


if __name__ == "__main__":
    unittest.main()
