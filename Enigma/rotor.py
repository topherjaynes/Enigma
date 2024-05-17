"""
https://en.wikipedia.org/wiki/Enigma_rotor_details
"""
class Rotor:

    def __init__(self, wiring, notch, initial_position=0, ring_setting =0):
        """

        Attributes:
            Wiring: a string of the internal wiring of the rotor that allows the substitution for example: 'JGDQOXUSCAMIFRVTPNEWKBLZYH'
            Notch: (str) a single turn over notch positioned on the left side that triggers the stepping motion: example Q if rotor steps from Q to R the next rotor advances
            position: (int) current position of the rotor
            ring_setting: (int) offset applied to the rotors wiring

        Should I do a list instead of a string? Slicing just as easy str in list. Any memory or speed tradeoffs? [] research


        """

        self.wiring = wiring
        self.notch = notch
        self.position = initial_position
        self.ring_setting = ring_setting
        self._create_wiriing_map()


    def _create_wiring_map(self):
        """
        Create a wiring map based on the settings

        Adjusts the wiring for the ring setting and creates the back and forth mapping.
        https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Enigma-action.svg/400px-Enigma-action.svg.png


    
        """
        # Adjust wiring for ring setting
        adjusted_wiring = self._adjust_wiring_for_ring_setting(self.wiring, self.ring_setting)

        # Create forward and backward mappings
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for i in range(26):
            forward_letter = adjusted_wiring[i]
            self.forward_map[alphabet[i]] = forward_letter
            self.backward_map[forward_letter] = alphabet[i]
    
    def _adjust_wiring_for_ring_setting(self, wiring, ring_setting):
        """
        Adjust the rotors wiring based on the ring setting

        Args: 
        wiring: str the original wiring of the rotor
        ring setting (int) the ring settting to adjust to

        returns:

            str of adjusted wire

        example: 
        Input:
            wiring: "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
            ring_setting: 2
            Output:
            Adjusted wiring: "MFLGDQVZNTOWYHXUSPAIBRCJEK"
        """
        return wiring[ring_setting:] + wiring[:ring_setting]


    def encode_forward(self,char):
        """
        Encode a character through the machone from right to left

        Args:
            char (str): the character that was "pressed"on the keyboard
        """
        #adjusted the character index by the current position
        #converting to ascii char to 
        char_index = (ord(char)) - ord('A') + self.position) %26
        adjusted_char = chr(char_index + ord('A'))

        # Map the character using the forward map
        encoded_char = self.forward_map[adjusted_char]

        #adjust back by the current position
        endoded_index = (ord(encoded_char) - ord('A') - self.position)%26
        return chr(encoded_index + ord('A'))

    def encode_backward(self, char):
        """
        Encode back after the reflector from left to right
        Arg:
            char (str): character to encode
        Returns:
            str: encoded char
        """
        char_index = (ord(char) - ord('A')+ self.position) % 26
        adjusted_char = chr(char_index + ord('A'))

        #map to the backwards map
        encoded_char = self.backward_map[adjusted_char]

        #adjust back by the current position
        encoded_index = (ord(encoded_char) - ord('A') - self.position) % 26
        return chr(encoded_index + ord('A'))

    def step(self):
        """
        Step the rotor to the next position after each "key" press

        returns:
            bool: trie if the rotor hits the notch position, spins the next rotor
        """
        #wrap back around at 25th position
        self.position = (self.position +1) % 26
        return self.position == ord(self.notch) - ord('A')
    