import unittest

from main import get_em_labels, get_length_units

class TestLabels(unittest.TestCase):
    length_units = get_length_units()
    em_labels = get_em_labels()

    def test_length_units_km(self):
        self.assertEqual(self.length_units.km, 10**3)

    def test_length_units_pc(self):
        self.assertEqual(self.length_units.pc, 3.08567758149137e16)

    def test_length_units_mm(self):
        self.assertEqual(self.length_units.mm, 10**-3)

    def test_length_units_um(self):
        self.assertNotEqual(self.length_units.um, 10**-7)

    def test_em_labels_voltage(self):
        self.assertEqual(self.em_labels.V, 'voltage')
        
    def test_em_labels_resistance(self):
        self.assertEqual(self.em_labels.O, 'resistance')
    
    def test_em_labels_power(self):
         self.assertNotEqual(self.em_labels.W, 'Power')
        