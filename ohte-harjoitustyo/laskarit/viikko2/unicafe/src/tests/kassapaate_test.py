import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(400)
        self.vajaakortti = Maksukortti(100)

    def test_kassan_saldo_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_edullisesti_lounaat_oikein_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_kassan_maukkaasti_lounaat_oikein_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateismaksu_onnistuu_edullisesti(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateismaksu_onnistuu_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateismaksu_vaihtoraha_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)

    def test_kateismaksu_vaihtoraha_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)

    def test_kateismaksu_onnistuu_edullisesti_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateismaksu_onnistuu_maukkaasti_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateismaksu_ei_riittava_edullisesti(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateismaksu_ei_riittava_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateismaksu_ei_riittava_vaihtoraha_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_kateismaksu_ei_riittava_vaihtoraha_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_kateismaksu_ei_riittava_edullisesti_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateismaksu_ei_riittava_maukkaasti_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttimaksu_onnistuu_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)

    def test_korttimaksu_onnistuu_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)

    def test_korttismaksu_onnistuu_edullisesti_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttismaksu_onnistuu_maukkaasti_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttimaksu_ei_onnistu_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.vajaakortti), False)

    def test_korttimaksu_ei_onnistu_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.vajaakortti), False)

    def test_korttismaksu_ei_onnistu_edullisesti_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.vajaakortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttismaksu_ei_onnistu_maukkaasti_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.vajaakortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttimaksu_edullisesti_ei_muuta_kassassa_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_korttimaksu_maukkaasti_ei_muuta_kassassa_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 200)
        self.assertEqual(self.kortti.saldo, 600)

    def test_lataa_rahaa_kortille_kassan_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

    def test_lataa_negatiivinen_rahaa_kortille_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -200)
        self.assertEqual(self.kortti.saldo, 400)