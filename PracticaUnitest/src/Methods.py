import unittest
from src.Constructor import Average
class methods:


    def add(self, val1, val2):
        result = val1 + val2
        return result

    def val_age(self, val):
        if val > 0 and val < 100:
            return True
        else:
            return False

    def max(self, val1, val2, val3):
        List_num = [val1, val2, val3]
        if not(val1 == 0 and val2 == 0 and val3 == 0):
            return(max(List_num),True)
        else:
            return False


    def isVocal(self, val):
        List_vocal = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if str(val).isnumeric() == True:
            return 'Es numero'
        elif len(str(val)) > 1:
            return 'Es cadena'
        elif str(val) in List_vocal:
            return 'Es vocal'
        elif not(str(val) in List_vocal):
            return 'Es consonante'

    def inversa(self, val):
        list_inverse = list()
        for i in str(val):
            list_inverse.append(i)
        list_inverse.reverse()
        str_inverse = " ".join(list_inverse)
        return str_inverse

    def palindromo(self, val):
        val.replace(" ","")
        list_val = list()
        list_val_inverse = list()
        for i in str(val):
            list_val.append(i)
            list_val_inverse.append(i)
        list_val_inverse.reverse()
        #str_inverse = " ".join(list_val_inverse)
        if list_val == list_val_inverse:
            return True
        else:
            return False

    def higherLesser(self, val):
        higher = val[0]
        lesser = val[0]
        add = 0
        for value in val:
            if value > higher:
                higher = value
            if value < lesser:
                lesser = value
            add = add + value
        average = add/len(val)
        ResultObject = Average(higher, lesser, average)
        return ResultObject

    def countries(self, val):
        result = val[0]
        for country in val:
            if len(country) > len(result):
                result = country
        return result

    def binary(self, val):
        Convert = format(val, "b")
        return Convert

    def CantChar(self, val):
        valor = len(str(val))
        return valor




