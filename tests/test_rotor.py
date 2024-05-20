from Enigma.rotor import Rotor
import unittest

"""
Goal is to test the rotor class to see if the wiring, ring, notch and position settings work
Check if forward and backward maps are created (can I do this without the reflector?)
"""


class TestRotor(unittest.TestCase):
    def setUp(self):
        """
        Set up a rotor for testing
        """
        self.wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        self.notch = 'Q'
        self.initial_position = 0
        self.ring_setting =0
        self.rotor = Rotor(self.wiring, self.notch, self.initial_position, self.ring_setting)
    
    def test_step(self):
        #test the rotor's initialization
        self.assertEqual(self.rotor.wiring, self.wiring)
        self.assertEqual(self.rotor.notch, self.notch)
        self.assertEqual(self.rotor.position, self.initial_position)
        self.assertEqual(self.rotor.ring_setting, self.ring_setting)
        self.assertEqual(self.rotor.forward_map['A'], 'E')
        self.assertEqual(self.rotor.backward_map['E'], 'A')