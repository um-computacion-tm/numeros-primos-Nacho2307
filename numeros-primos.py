import unittest

def es_primo(numero):
    x = 1 
    c = 0
    while x <= numero:
        if numero % x == 0:
            c = c + 1
        x = x + 1
    if c == 2:
        return True 
    else:
        return False


class TestPrimos(unittest.TestCase):
    def testp_1(self):
        result = es_primo(1)
        self.assertEqual(result, False)
    
    def testp_2(self):
        result = es_primo(2)
        self.assertEqual(result, True)

    def testp_3(self):
        result = es_primo(3)
        self.assertEqual(result, True)

    def testp_4(self):
        result = es_primo(4)
        self.assertEqual(result, False)

    def testp_5(self):
        result = es_primo(5)
        self.assertEqual(result, True)

    def testp_6(self):
        result = es_primo(6)
        self.assertEqual(result, False)
    
    def testp_7(self):
        result = es_primo(7)
        self.assertEqual(result, True)
    
    def testp_8(self):
        result = es_primo(8)
        self.assertEqual(result, False)

    def testp_9(self):
        result = es_primo(19)
        self.assertEqual(result, True)

unittest.main()