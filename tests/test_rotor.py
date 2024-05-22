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
    
    def test_step(self):
        """
        Test stepping the rotor.
        """
        # Step the rotor 1 position
        self.rotor.step()
        self.assertEqual(self.rotor.position, 1)
        
        # Step the rotor 25 more positions (total 26)
        for _ in range(25):
            self.rotor.step()
        self.assertEqual(self.rotor.position, 0)

    def test_encode_forward(self):
        """
        Test encoding a character forward through the rotor.
        """
        self.assertEqual(self.rotor.encode_forward('A'), 'E')
        self.assertEqual(self.rotor.encode_forward('B'), 'K')
        self.assertEqual(self.rotor.encode_forward('C'), 'M')
    
    def test_encode_backward(self):
        """
        Test encoding a character backward through the rotor.
        """
        self.assertEqual(self.rotor.encode_backward('E'), 'A')
        self.assertEqual(self.rotor.encode_backward('K'), 'B')
        self.assertEqual(self.rotor.encode_backward('M'), 'C')