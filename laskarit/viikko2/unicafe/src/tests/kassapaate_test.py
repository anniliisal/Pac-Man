import unittest
from kassapaate import Kassapaate 
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti1 = Maksukortti(10)
        self.maksukortti2 = Maksukortti(400)
        
    
    def test_kontsruktori_asettaa_rahan_oikein(self):
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")

    def test_konstruktori_asettaa_edulliset_oikein(self):
        self.assertEqual(str(self.kassa.edulliset), "0")

    def test_konstruktori_asettaa_maukkaat_oikein(self):
        self.assertEqual(str(self.kassa.maukkaat), "0")

    def test_syo_edullisesti_kateisella(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassa.edulliset), "1")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100240")

    def test_syo_edullisesti_kateisella_eiriita(self):
        self.kassa.syo_edullisesti_kateisella(20)
        self.assertEqual(str(self.kassa.edulliset), "0")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")


    def test_syo_maukkaasti_kateisella(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassa.maukkaat), "1")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100400")

    def test_syo_maukkaasti_kateisella_eiriita(self):
        self.kassa.syo_maukkaasti_kateisella(4)
        self.assertEqual(str(self.kassa.maukkaat), "0")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")

    
    def test_syo_maukkaasti_kortilla(self):
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti2)
        self.assertEqual(str(self.maksukortti2), f"saldo: 0.0")
        self.assertEqual(str(self.kassa.maukkaat), "1")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")


    def test_syo_maukkaasti_kortilla_eiriita(self):
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti1)
        self.assertEqual(str(self.maksukortti1), f"saldo: 0.1")
        self.assertEqual(str(self.kassa.maukkaat), "0")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")



    def test_syo_edullisesti_kortilla_(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti2)
        self.assertEqual(str(self.maksukortti2), f"saldo: 1.6")
        self.assertEqual(str(self.kassa.edulliset), "1")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")

    def test_syo_edullisesti_kortilla_eiriita(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti1)
        self.assertEqual(str(self.maksukortti1), f"saldo: 0.1")
        self.assertEqual(str(self.kassa.edulliset), "0")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")

    

    def test_lataa_rahaa_kortille(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti1, 10)
        self.assertEqual(str(self.maksukortti1), f"saldo: 0.2")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100010")


    def test_lataa_rahaa_kortille_negatiivinen(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti1, -1)
        self.assertEqual(str(self.maksukortti1), f"saldo: 0.1")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")





