import unittest
from src.Methods import methods
from src.Constructor import Average
class MethodsTest(unittest.TestCase):

#test add
    def test_add(self):
        inst = methods()
        result = inst.add(5, 2)
        self.assertEqual(7, result)
#test val_age
    def test_age_negative(self):
        inst = methods()
        result = inst.val_age(-232)
        self.assertFalse(result)

    def test_age_up100(self):
        inst = methods()
        result = inst.val_age(162)
        self.assertFalse(result)
#test max
    def test_max_maxValue(self):
        inst = methods()
        result = inst.max(12,2,5)
        self.assertEqual((12,True), result)

    def test_max_0Values(self):
        inst = methods()
        result = inst.max(0,0,0)
        self.assertFalse(result)

#test isVocal
    def test_isVocal_vocalTrue(self):
        inst = methods()
        result = inst.isVocal('a')
        self.assertEqual('Es vocal', result)

    def test_isVocal_numberTrue(self):
        inst = methods()
        result = inst.isVocal(234)
        self.assertEqual('Es numero', result)

    def test_isVocal_cadenaTrue(self):
        inst = methods()
        result = inst.isVocal('albert')
        self.assertEqual('Es cadena', result)

    def test_isVocal_consonantTrue(self):
        inst = methods()
        result = inst.isVocal('l')
        self.assertEqual('Es consonante', result)

#test palindromo
    def test_palindromo_True(self):
        inst = methods()
        result = inst.palindromo('oruro')
        self.assertTrue(result)

    def test_palindromo_False(self):
        inst = methods()
        result = inst.palindromo('jorge')
        self.assertFalse(result)
#test higherLesser

    def test_higherLesser_ClassGetters(self):
        inst = methods()
        result = inst.higherLesser([40,35,15])
        self.assertEqual((40,15,30),(result.get_higher(),result.get_lesser(),result.get_average()))

#test countries

    def test_countries_HighLength(self):
        inst = methods()
        result = inst.countries(['PANAMA', 'VENEZUELA', 'RUSIA'])
        self.assertEqual('VENEZUELA', result)

#test binary

    def test_binary_TrueValue(self):
        inst = methods()
        result = inst.binary(200)
        self.assertEqual('11001000', result)

#test CantChar

    def test_CantChar_TrueValue(self):
        inst = methods()
        result = inst.CantChar('WALTER')
        self.assertEqual(6, result)