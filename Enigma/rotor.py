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
        pass
    
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
