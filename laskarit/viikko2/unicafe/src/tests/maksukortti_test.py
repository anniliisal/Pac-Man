import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)


    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), f"saldo: 0.1")


    def test_lataa_rahaa(self):
        self.maksukortti.lataa_rahaa(10)
        

        self.assertEqual(str(self.maksukortti), f"saldo: 0.2")

    def test_ota_rahaa_negatiivinen(self):
        self.maksukortti.ota_rahaa(50)
        self.assertEqual(str(self.maksukortti), f"saldo: 0.1")
        


    def test_ota_rahaa_positiivinen(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), f"saldo: 0.05")

    
        




