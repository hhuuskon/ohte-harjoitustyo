import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldo_kasvaa_lataamalla(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_saldo_vahenee_ottamalla(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_saldo_ei_muutu_jos_ei_katetta(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10), True)

    def test_rahat_eivat_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(11), False)